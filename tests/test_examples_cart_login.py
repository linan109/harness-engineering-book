"""登录片段仅验证长度边界；购物车验证业务契约并保留故意错误反例。"""

import ast
from datetime import datetime, timedelta
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock


ROOT = Path(__file__).resolve().parents[1]


def load_example(name, relative_path):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cart = load_example("cart_reference", "examples/code/cart-discount-exercise/cart_discount_reference.py")
bad_cart = load_example("cart_bug", "examples/code/cart-discount-bug.py")


class CartTests(unittest.TestCase):
    def test_discount_threshold_in_cents(self):
        for subtotal, expected in ((0, 0), (19999, 19999), (20000, 17000), (20001, 17001)):
            with self.subTest(subtotal=subtotal):
                self.assertEqual(cart.calculate_total([(subtotal, 1)]), expected)
        self.assertEqual(cart.calculate_total([]), 0)

    def test_choose_more_favorable_discount_without_stacking(self):
        self.assertEqual(cart.calculate_total([(30000, 1)], 10), 27000)
        self.assertEqual(cart.calculate_total([(30000, 1)], 20), 24000)
        self.assertEqual(cart.calculate_total([(10000, 2)], 10), 17000)
        self.assertEqual(cart.calculate_total([(19999, 1)], 10), 17999)
        self.assertEqual(cart.calculate_total([(10000, 1), (5000, 2)], 0), 17000)

    def test_original_example_still_exposes_stacking_bug(self):
        source_cart = SimpleNamespace(
            items=[SimpleNamespace(price=300, quantity=1)], member_discount=0.1
        )
        self.assertEqual(bad_cart.apply_discount(source_cart), 240)
        # 参考实现按明确的“不叠加、取更优惠者”契约，应付270元。
        self.assertEqual(cart.calculate_total([(30000, 1)], 10), 27000)

    def test_fractional_cent_rounding_and_full_member_discount(self):
        self.assertEqual(cart.calculate_total([(101, 1)], 5), 96)
        self.assertEqual(cart.calculate_total([(1, 1)], 50), 1)
        self.assertEqual(cart.calculate_total([(30000, 1)], 100), 0)

    def test_invalid_prices_quantities_and_discount_rates(self):
        for items, rate, error in (
            ([(True, 1)], 0, TypeError), ([(100, False)], 0, TypeError),
            ([(1.5, 1)], 0, TypeError), ([(100, 1)], True, TypeError),
            ([(100, 1)], "10", TypeError), ([(-1, 1)], 0, ValueError),
            ([(100, 0)], 0, ValueError), ([(100, -1)], 0, ValueError),
            ([(100, 1)], -1, ValueError), ([(100, 1)], 101, ValueError),
        ):
            with self.subTest(items=items, rate=rate):
                with self.assertRaises(error):
                    cart.calculate_total(items, rate)


class TeachingHTTPException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


class LoginLengthBoundaryTests(unittest.TestCase):
    def setUp(self):
        # 正例明确为关键片段。隔离原函数并替换外部依赖，无需安装FastAPI等库；
        # 仅验证长度条件，不声称验证真实认证、锁定、会话或JWT安全。
        path = ROOT / "examples/code/login-comparison/with-spec.py"
        tree = ast.parse(path.read_text(encoding="utf-8"))
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "login")
        function.decorator_list = []
        self.db = Mock()
        self.db.query.return_value.filter.return_value.first.return_value = SimpleNamespace(
            id=1, password_hash="external-hash", is_locked=False
        )
        self.create_token = Mock(return_value="teaching-token")
        namespace = {
            "HTTPException": TeachingHTTPException, "db": self.db,
            "User": SimpleNamespace(email="email-column"),
            "func": SimpleNamespace(lower=lambda value: value),
            "verify_hash": Mock(return_value=True), "check_and_lock": Mock(),
            "count_active_sessions": Mock(return_value=0), "revoke_oldest_session": Mock(),
            "create_jwt": self.create_token, "datetime": datetime, "timedelta": timedelta,
        }
        exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), "exec"), namespace)
        self.login = namespace["login"]

    def test_out_of_range_password_cannot_reach_database_or_token_issuer(self):
        for length in (0, 1, 7, 129):
            with self.subTest(length=length):
                with self.assertRaises(TeachingHTTPException) as caught:
                    self.login("reader@example.com", "x" * length)
                self.assertEqual(caught.exception.status_code, 401)
                self.assertEqual(caught.exception.detail, "Invalid credentials")
        self.db.query.assert_not_called()
        self.create_token.assert_not_called()

    def test_both_password_length_endpoints_are_accepted(self):
        for length in (8, 128):
            with self.subTest(length=length):
                self.assertEqual(self.login("reader@example.com", "x" * length),
                                 {"token": "teaching-token"})
        self.assertEqual(self.create_token.call_count, 2)

    def test_empty_email_rejected_before_authentication(self):
        with self.assertRaises(TeachingHTTPException) as caught:
            self.login("", "12345678")
        self.assertEqual(caught.exception.status_code, 401)
        self.db.query.assert_not_called()


if __name__ == "__main__":
    unittest.main()
