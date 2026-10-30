# 购物车本地练习

沿用第5章“双翻译”的[故意错误代码](../cart-discount-bug.py)，保留其“会员折扣与满减叠加”的教学bug。本练习额外约定两种优惠取应付金额较低者；原始需求只说不叠加，并没有决定怎样二选一。

## 输入输出契约

实现`calculate_total(items, member_discount_percent=0) -> int`：

- `items`为`(price_cents, quantity)`对的序列。单价为非负整数分，数量为正整数；空购物车返回0。
- 会员折扣率是0—100的整数百分数，10表示九折；默认0表示没有会员优惠。
- 先按原价总额判断是否满20000分，满则减3000分；另算会员优惠后的金额。两者取更低应付金额，禁止叠加。
- 会员应付金额四舍五入到分，例如101分打九五折得96分。
- 布尔值及非整数价格/数量/折扣率抛`TypeError`，值越界抛`ValueError`。输入对数及容器形状由调用方保证。

## 练习顺序

1. 将原反例交给[代码反述Prompt](../../prompts/code-restatement.md)，对照“不叠加”的需求找偏差。
2. 按上述完整契约写自己的实现。不要修改反例来伪装成正例。
3. 从仓库根目录运行下列命令，再对照`cart_discount_reference.py`。

```sh
python examples/code/cart-discount-exercise/cart_discount_reference.py
python -m unittest discover -s tests -p "test_examples*.py" -v
```

演示输出27000。测试用固定金额验证满减阈值、两种优惠各自更优、不叠加、分币舍入和非法输入，同时明确验证反例仍能暴露叠加问题。只有标准库，无服务、账号或网络前置条件。
