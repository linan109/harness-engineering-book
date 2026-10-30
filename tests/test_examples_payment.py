"""按已写明的教学契约验证签名、幂等、状态边界与数据库失败。"""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "payment_example", ROOT / "examples/code/payment-callback/payment_callback.py"
)
payment = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(payment)
SECRET = b"test-only-secret"


class PaymentCallbackTests(unittest.TestCase):
    def setUp(self):
        self.store = payment.create_store()
        self.addCleanup(self.store.close)
        self.store.execute("INSERT INTO orders VALUES ('order-1', 'pending')")

    def body(self, **changes):
        payload = {"event_id": "evt-1", "order_id": "order-1", "status": "paid"}
        payload.update(changes)
        return json.dumps(payload).encode()

    def call(self, body=None, **kwargs):
        body = self.body() if body is None else body
        return payment.handle_callback(
            self.store, body, payment.sign(body, SECRET), SECRET, **kwargs
        )

    def assert_state(self, status, events=0, memberships=0):
        self.assertEqual(self.store.execute("SELECT status FROM orders").fetchone()[0], status)
        self.assertEqual(self.store.execute("SELECT COUNT(*) FROM callbacks").fetchone()[0], events)
        self.assertEqual(self.store.execute("SELECT COUNT(*) FROM memberships").fetchone()[0], memberships)

    def test_success_and_duplicate_only_grant_once(self):
        self.assertEqual(self.call(), (200, {"ok": True, "duplicate": False}))
        self.assertEqual(self.call(), (200, {"ok": True, "duplicate": True}))
        self.assert_state("paid", 1, 1)

    def test_bad_or_tampered_signature_cannot_change_state(self):
        body = self.body()
        for signature in ("forged", "签名", None, payment.sign(body, b"wrong-secret")):
            with self.subTest(signature=signature):
                self.assertEqual(payment.handle_callback(self.store, body, signature, SECRET)[0], 403)
        changed = self.body(order_id="other")
        self.assertEqual(payment.handle_callback(
            self.store, changed, payment.sign(body, SECRET), SECRET
        )[0], 403)
        self.assert_state("pending")

    def test_signed_malformed_payload_is_rejected_without_writes(self):
        for body in (b"{", b"[]", b"null", b"{}", self.body(event_id=""),
                     self.body(order_id=7), self.body(status=None), b"\xff"):
            with self.subTest(body=body):
                self.assertEqual(self.call(body)[0], 400)
                self.assert_state("pending")

    def test_unknown_order_does_not_create_order_or_mark_event(self):
        self.assertEqual(self.call(self.body(order_id="missing"))[0], 404)
        self.assertEqual(self.store.execute("SELECT COUNT(*) FROM orders").fetchone()[0], 1)
        self.assert_state("pending")

    def test_signed_utf16_and_utf32_bodies_are_rejected_before_transaction(self):
        text = self.body().decode("utf-8")
        for encoding in ("utf-16", "utf-16-le", "utf-16-be", "utf-32"):
            with self.subTest(encoding=encoding):
                self.assertEqual(self.call(text.encode(encoding))[0], 400)
                self.assert_state("pending")
                self.assertFalse(self.store.in_transaction)
        self.assertEqual(self.call()[0], 200)
        self.assert_state("paid", 1, 1)

    def test_escaped_surrogates_are_rejected_before_transaction(self):
        for key in ("event_id", "order_id", "status"):
            for surrogate in ("\ud800", "\udfff"):
                with self.subTest(key=key, surrogate=repr(surrogate)):
                    # ensure_ascii=True产生合法ASCII JSON，解码后仍可能有孤立代理项。
                    self.assertEqual(self.call(self.body(**{key: surrogate}))[0], 400)
                    self.assert_state("pending")
                    self.assertFalse(self.store.in_transaction)
        self.assertEqual(self.call()[0], 200)
        self.assert_state("paid", 1, 1)

    def test_terminal_order_states_cannot_return_to_paid(self):
        for status in ("paid", "refunded", "closed"):
            with self.subTest(status=status):
                self.store.execute("UPDATE orders SET status = ?", (status,))
                self.assertEqual(self.call()[0], 409)
                self.assert_state(status)

    def test_unsupported_events_do_not_prevent_later_valid_payment(self):
        for status in ("failed", "refunded", "pending"):
            with self.subTest(status=status):
                self.assertEqual(self.call(self.body(status=status))[0], 409)
                self.assert_state("pending")
        self.assertEqual(self.call()[0], 200)
        self.assert_state("paid", 1, 1)

    def test_new_event_for_paid_order_cannot_grant_again(self):
        self.call()
        self.assertEqual(self.call(self.body(event_id="evt-2"))[0], 409)
        self.assert_state("paid", 1, 1)

    def test_same_event_id_with_changed_body_is_conflict(self):
        self.call()
        self.assertEqual(self.call(self.body(order_id="other")),
                         (409, {"error": "event_id_conflict"}))
        self.assert_state("paid", 1, 1)

    def test_actual_commit_failure_rolls_back_and_allows_retry(self):
        # 延迟外键约束在COMMIT时失败，覆盖真实SQLite提交失败而非只mock返回值。
        self.store.execute("PRAGMA foreign_keys = ON")
        self.store.executescript("""
            CREATE TABLE parent (id INTEGER PRIMARY KEY);
            CREATE TABLE fault (parent_id INTEGER REFERENCES parent(id)
                                DEFERRABLE INITIALLY DEFERRED);
        """)
        result = self.call(before_commit=lambda store: store.execute("INSERT INTO fault VALUES (99)"))
        self.assertEqual(result, (503, {"error": "transaction_failed"}))
        self.assert_state("pending")
        self.assertEqual(self.store.execute("SELECT COUNT(*) FROM fault").fetchone()[0], 0)
        self.assertEqual(self.call()[0], 200)
        self.assert_state("paid", 1, 1)

    def test_failed_membership_write_does_not_leave_paid_order(self):
        self.store.execute("""CREATE TRIGGER reject_membership BEFORE INSERT ON memberships
                              BEGIN SELECT RAISE(ABORT, 'injected storage failure'); END""")
        self.assertEqual(self.call()[0], 503)
        self.assert_state("pending")
        self.store.execute("DROP TRIGGER reject_membership")
        self.assertEqual(self.call()[0], 200)
        self.assert_state("paid", 1, 1)


if __name__ == "__main__":
    unittest.main()
