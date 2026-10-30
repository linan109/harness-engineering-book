"""第5章5.5节配套：仅用标准库演示本地支付回调规格，无网络或真实支付。"""

import hashlib
import hmac
import json
import sqlite3


def create_store():
    """每次创建独立内存数据库；权益也用本地表表示。"""
    connection = sqlite3.connect(":memory:", isolation_level=None)
    connection.executescript("""
        CREATE TABLE orders (id TEXT PRIMARY KEY, status TEXT NOT NULL);
        CREATE TABLE callbacks (event_id TEXT PRIMARY KEY, body_hash TEXT NOT NULL);
        CREATE TABLE memberships (order_id TEXT PRIMARY KEY);
    """)
    return connection


def sign(body: bytes, secret: bytes) -> str:
    """教学协议：对收到的原始字节计算HMAC-SHA256，返回十六进制字符串。"""
    return hmac.new(secret, body, hashlib.sha256).hexdigest()


class CallbackRejected(Exception):
    def __init__(self, status, error):
        self.status = status
        self.error = error


def handle_callback(connection, body: bytes, signature: str, secret: bytes, *,
                    before_commit=None):
    """返回(教学HTTP状态码, 响应字典)。before_commit仅用于注入提交前故障。"""
    if not isinstance(signature, str) or not signature.isascii():
        return 403, {"error": "invalid_signature"}
    if not hmac.compare_digest(sign(body, secret), signature):
        return 403, {"error": "invalid_signature"}

    try:
        payload = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return 400, {"error": "invalid_payload"}
    if not isinstance(payload, dict) or any(
        not isinstance(payload.get(key), str) or not payload[key].strip()
        for key in ("event_id", "order_id", "status")
    ):
        return 400, {"error": "invalid_payload"}
    try:
        # JSON转义可表示孤立代理项；进入事务前拒绝SQLite无法UTF-8编码的标识。
        for key in ("event_id", "order_id", "status"):
            payload[key].encode("utf-8")
    except UnicodeEncodeError:
        return 400, {"error": "invalid_payload"}

    event_id, order_id = payload["event_id"], payload["order_id"]
    body_hash = hashlib.sha256(body).hexdigest()
    try:
        # 验重、状态检查、状态更新与本地权益写入共享同一事务。
        connection.execute("BEGIN IMMEDIATE")
        previous = connection.execute(
            "SELECT body_hash FROM callbacks WHERE event_id = ?", (event_id,)
        ).fetchone()
        if previous:
            if previous[0] != body_hash:
                raise CallbackRejected(409, "event_id_conflict")
            connection.rollback()
            return 200, {"ok": True, "duplicate": True}

        order = connection.execute(
            "SELECT status FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        if order is None:
            raise CallbackRejected(404, "order_not_found")
        if order[0] != "pending" or payload["status"] != "paid":
            raise CallbackRejected(409, "invalid_transition")

        connection.execute("UPDATE orders SET status = 'paid' WHERE id = ?", (order_id,))
        connection.execute("INSERT INTO memberships VALUES (?)", (order_id,))
        connection.execute("INSERT INTO callbacks VALUES (?, ?)", (event_id, body_hash))
        if before_commit is not None:
            before_commit(connection)
        connection.commit()
    except CallbackRejected as rejected:
        connection.rollback()
        return rejected.status, {"error": rejected.error}
    except sqlite3.Error:
        connection.rollback()
        return 503, {"error": "transaction_failed"}
    return 200, {"ok": True, "duplicate": False}


if __name__ == "__main__":
    secret = b"local-teaching-secret"
    body = b'{"event_id":"evt-1","order_id":"order-1","status":"paid"}'
    with create_store() as store:
        store.execute("INSERT INTO orders VALUES ('order-1', 'pending')")
        print(handle_callback(store, body, sign(body, secret), secret))
        print(handle_callback(store, body, sign(body, secret), secret))
        print("memberships:", store.execute("SELECT COUNT(*) FROM memberships").fetchone()[0])
