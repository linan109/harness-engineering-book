"""
来源：《驾驭AI编程》第5章 5.5节
说明：有Spec驱动时AI生成的登录代码（关键片段）
      同样的AI、同样的模型，区别仅在于你提供了8行Spec还是一句话需求
"""

from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException
from sqlalchemy import func

from auth import create_jwt, verify_hash  # Spec要求: 密码哈希验证
from rate_limit import rate_limit  # Spec要求: 请求频率限制
from session import count_active_sessions, revoke_oldest_session

app = FastAPI()


@app.post("/login")
@rate_limit(max_calls=20, period=60)  # Spec: 防暴力破解
def login(email: str, password: str):
    # Spec: 不接受空邮箱或空密码
    if not email or not password:
        raise HTTPException(401, "Invalid credentials")

    # Spec: 邮箱不区分大小写
    user = db.query(User).filter(
        func.lower(User.email) == email.lower()
    ).first()

    # Spec: 错误密码返回401，不泄露"用户是否存在"（统一错误消息）
    if not user or not verify_hash(password, user.password_hash):
        check_and_lock(user)  # Spec: 连续5次失败锁定账户15分钟
        raise HTTPException(401, "Invalid credentials")

    # Spec: 账户锁定检查
    if user.is_locked and user.locked_until > datetime.utcnow():
        raise HTTPException(423, "Account temporarily locked")

    # Spec: 同一账户最多3个活跃session
    active = count_active_sessions(user.id)
    if active >= 3:
        revoke_oldest_session(user.id)

    # Spec: JWT有效期24小时，包含用户ID和角色信息
    token = create_jwt(user, expires_in=timedelta(hours=24))
    return {"token": token}
