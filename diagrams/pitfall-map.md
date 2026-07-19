# AI能力陷阱总图 (Chapter 1, Section 1.8)

本图展示8个AI结构性能力陷阱，按AI原理特征分组，映射到对应的CIVR动作、典型症状和检测信号。

![AI能力陷阱总图](pitfall-map.svg)

## Mermaid 源码

```mermaid
mindmap
  root((8个能力陷阱))
    下一token预测
      ① Almost Right<br/>看起来对，其实不对
        ::icon(fa fa-check-circle)
        CIVR: 验证(V)
        症状: 代码通过测试但逻辑错误
        信号: 输出95%正确，边界条件失败
    训练数据驱动
      ② The Unsaid<br/>隐性知识不可达
        ::icon(fa fa-eye-slash)
        CIVR: 告知(I)
        症状: 缺少业务上下文的关键假设
        信号: AI不问就动手，遗漏领域规则
      ③ Frozen in Time<br/>知识会过期
        ::icon(fa fa-snowflake)
        CIVR: 告知(I)
        症状: 使用已废弃的API或过时方案
        信号: 推荐的库版本与当前不符
    RLHF讨好本能
      ④ The Yes-Man<br/>无法诚实说不确定
        ::icon(fa fa-thumbs-up)
        CIVR: 验证(V)
        症状: 自信地给出错误答案
        信号: 从不说"我不确定"，事实性错误
    有限上下文窗口
      ⑤ Context Rot<br/>注意力衰减
        ::icon(fa fa-hourglass)
        CIVR: 告知(I) + 校准(R)
        症状: 长对话后遗忘早期指令
        信号: 输出与最初约束矛盾
      ⑥ Goldfish Memory<br/>跨会话失忆
        ::icon(fa fa-fish)
        CIVR: 告知(I)
        症状: 新会话不记得之前的决策
        信号: 重复问已回答过的问题
    Agent多步执行
      ⑦ Error Snowball<br/>误差累积
        ::icon(fa fa-snowflake)
        CIVR: 验证(V) + 校准(R)
        症状: 多步任务中错误逐步放大
        信号: 后续步骤基于前面的错误结果
      ⑧ Toolbox Paradox<br/>工具箱悖论
        ::icon(fa fa-tools)
        CIVR: 约束(C)
        症状: 调用过多不必要的工具
        信号: 工具数量增加但准确率下降
```

## 陷阱-CIVR对照表

| 陷阱 | AI原理特征 | 典型症状 | 检测信号 | 对应CIVR |
|------|-----------|---------|---------|----------|
| ① Almost Right | 下一token预测 | 代码通过编译但逻辑有细微错误 | 边界条件失败、性能异常、安全漏洞 | **V** 验证 |
| ② The Unsaid | 训练数据驱动 | 缺少你没说的业务规则和隐性知识 | AI不问就动手，遗漏领域特有约束 | **I** 告知 |
| ③ Frozen in Time | 训练数据驱动 | 使用已废弃的API或过时的最佳实践 | 推荐的版本/方法与当前文档不符 | **I** 告知 |
| ④ The Yes-Man | RLHF讨好本能 | 自信地给出错误答案，不表达不确定 | 事实性陈述未经验证、从不质疑你 | **V** 验证 |
| ⑤ Context Rot | 有限上下文窗口 | 长对话后遗忘或扭曲早期指令 | 输出与最初约束矛盾、重复已有内容 | **I** 告知 + **R** 校准 |
| ⑥ Goldfish Memory | 有限上下文窗口 | 新会话完全不记得之前的架构决策 | 重复问已回答的问题、方案前后不一致 | **I** 告知 |
| ⑦ Error Snowball | Agent多步执行 | 前一步的小错误在后续步骤中放大 | 多步任务后结果与预期偏差越来越大 | **V** 验证 + **R** 校准 |
| ⑧ Toolbox Paradox | Agent多步执行 | 工具越多，选对的概率越低 | 工具数量多但完成率低、调用链过长 | **C** 约束 |
