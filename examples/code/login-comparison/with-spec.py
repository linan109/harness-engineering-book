"""
来源：《驾驭AI编程》第5章的额外Spec练习（5.5节主例已改为支付回调）
说明：有Spec驱动时AI生成的登录代码（关键片段）
      不是完整登录服务；auth、db、账户锁定等依赖须由实际项目提供。
      可运行的标准库练习见 ../payment-callback/。
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
    # Spec: 不接受空邮箱，密码长度为8—128个字符
    if not email or not 8 <= len(password) <= 128:
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
