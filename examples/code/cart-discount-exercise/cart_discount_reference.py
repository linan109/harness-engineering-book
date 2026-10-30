"""纯本地购物车练习参考答案；原cart-discount-bug.py保留教学错误。"""


def calculate_total(items, member_discount_percent=0):
    """items为(单价分, 数量)序列；返回优惠二选一后的应付分数。"""
    if type(member_discount_percent) is not int:
        raise TypeError("discount must be an integer percent")
    if not 0 <= member_discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    subtotal = 0
    for price_cents, quantity in items:
        if type(price_cents) is not int or type(quantity) is not int:
            raise TypeError("price and quantity must be integers")
        if price_cents < 0 or quantity < 1:
            raise ValueError("price must be nonnegative and quantity positive")
        subtotal += price_cents * quantity

    full_reduction = subtotal - 3000 if subtotal >= 20000 else subtotal
    # 正数金额四舍五入到分，避免二进制浮点误差。
    member_price = (subtotal * (100 - member_discount_percent) + 50) // 100
    return min(full_reduction, member_price)


if __name__ == "__main__":
    print(calculate_total([(30000, 1)], 10))  # 27000分，不叠加成为24000分
