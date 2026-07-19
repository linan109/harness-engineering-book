"""
来源：《驾驭AI编程》第5章 5.5节
说明：无Spec时AI生成的登录代码（问题版本）
      演示AI在没有明确规格时生成的"看起来对"但存在多个生产级问题的代码
"""

from fastapi import FastAPI, HTTPException
import jwt

app = FastAPI()
SECRET = "my-secret-key"  # 问题1: 密钥硬编码在源码中


@app.post("/login")
def login(email: str, password: str):
    # 问题2: 没有输入验证（空字符串、格式检查等）
    user = db.query(User).filter(User.email == email).first()
    # 问题3: 没有处理邮箱大小写（User@Example.com != user@example.com）

    if not user:
        raise HTTPException(404, "User not found")
        # 问题4: 错误消息泄露用户是否存在（攻击者可枚举有效邮箱）

    if password != user.password:
        # 问题5: 明文比较密码（说明密码也是明文存储的）
        raise HTTPException(401, "Wrong password")
        # 问题6: 不同的错误消息泄露"用户存在但密码错"

    # 问题7: 没有rate limiting（攻击者可无限次尝试）
    # 问题8: 没有失败计数和账户锁定机制
    # 问题9: 没有任何日志记录（安全审计无从追溯）

    token = jwt.encode({"user_id": user.id}, SECRET)
    # 问题10: token没有过期时间
    # 问题11: token payload没有包含角色信息
    # 问题12: 没有限制并发session数量

    return {"token": token}
