"""
来源：《驾驭AI编程》第5章 5.7节
说明：AI生成的购物车折扣代码（含隐藏bug）
      用于演示"双翻译"方法——让AI反述代码功能，通过比对发现需求偏差
      需求："满200减30，不能和其他优惠叠加"
"""


def apply_discount(cart):
    total = sum(item.price * item.quantity for item in cart.items)
    discount = 30 if total >= 200 else 0

    if cart.member_discount:
        total *= (1 - cart.member_discount)  # 会员折扣照常生效

    return total - discount
    # BUG: 需求明确要求"不能和其他优惠叠加"
    # 但代码允许会员折扣和满减同时生效
    # 正确实现应在两种优惠中选一个（取对用户更优惠的那个，或按业务规则二选一）
    #
    # 双翻译怎么抓到这个bug：
    # AI反述: "如果用户有会员折扣，会先按会员折扣比例打折，再减去满减金额。两种优惠可以同时生效。"
    # 你的需求: "不能和其他优惠叠加"
    # 差异一目了然。
