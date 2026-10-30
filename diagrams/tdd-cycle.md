# AI时代的TDD循环 (Chapter 5, Section 5.8)

本图展示AI编程时代TDD循环的人机分工变化：RED-GREEN-REFACTOR三个阶段中，人类和AI各自承担不同角色。测试把需求的一部分转成可执行检查，由人审定预期，AI辅助实现。测试通过只证明已覆盖的检查通过。

![AI时代的TDD循环](tdd-cycle.svg)

## Mermaid 源码

```mermaid
graph LR
    RED["RED<br/>写测试 / 定义失败<br/>━━━━━━━━━━<br/>人类主导<br/>• 定义什么算对<br/>• 定义什么算失败<br/>• 覆盖边界条件<br/>• 目标行为尚未实现<br/>• 测试应该是红的"]
    
    GREEN["GREEN<br/>写实现 / 让测试通过<br/>━━━━━━━━━━<br/>AI主导<br/>• 写实现代码<br/>• 让测试从红变绿<br/>• 快速产出可运行代码"]
    
    REFACTOR["REFACTOR<br/>重构 + 审查<br/>━━━━━━━━━━<br/>AI重构<br/>• 清理代码结构<br/>• 提取公共逻辑<br/>人类审查<br/>• 跑测试检查已覆盖行为<br/>• 审查架构合理性"]

    RED -->|"人类交棒给AI"| GREEN
    GREEN -->|"AI交棒给人+AI"| REFACTOR
    REFACTOR -->|"下一个功能"| RED

    style RED fill:#ff6b6b,color:#fff
    style GREEN fill:#51cf66,color:#333
    style REFACTOR fill:#339af0,color:#fff
```

## 详细流程图

```mermaid
flowchart TB
    Start(("开始新功能")) --> WriteSpec["人类：写Spec<br/>自然语言定义需求"]
    WriteSpec --> WriteTest["人类：写测试<br/>（或独立AI会话写 + 人审）"]
    WriteTest --> RunTest1{"运行测试"}
    RunTest1 -->|"预期的失败"| AskAI["AI：写实现代码<br/>让测试从红变绿"]
    RunTest1 -->|"绿色<br/>检查测试是否有效"| WriteTest
    
    AskAI --> RunTest2{"运行测试"}
    RunTest2 -->|"绿色 ✓"| Refactor["AI：重构代码<br/>清理结构"]
    RunTest2 -->|"红色"| FixImpl["AI：修实现<br/>默认先修实现"]
    FixImpl --> RunTest2
    
    Refactor --> RunTest3{"运行测试"}
    RunTest3 -->|"绿色 ✓"| Review["人类：审查<br/>架构合理？逻辑对？"]
    RunTest3 -->|"红色"| Refactor
    
    Review -->|"通过"| Next(("下一个功能"))
    Review -->|"需修改"| AskAI
    
    Next --> WriteSpec

    style WriteSpec fill:#ff6b6b,color:#fff
    style WriteTest fill:#ff6b6b,color:#fff
    style AskAI fill:#51cf66,color:#333
    style Refactor fill:#339af0,color:#fff
    style Review fill:#ffa94d,color:#333
    style FixImpl fill:#51cf66,color:#333
```

## 关键规则

| 阶段 | 谁主导 | 核心原则 |
|------|--------|---------|
| RED | 人类 | 从需求独立设计测试，由人核对预期，降低共享盲区 |
| GREEN | AI | 默认修实现；若测试错误或需求变化，说明依据并确认后改测试 |
| REFACTOR | AI + 人类 | AI辅助重构，人类审查结构与未覆盖风险 |

## 提高测试独立性的两种做法

1. **你自己写测试** -- 对照需求审定断言，减少照着实现验证自身的风险
2. **用独立会话或另一个AI写** -- 测试会话读取需求、接口契约、输入输出结构与函数签名，避免先看实现；缺失预期先列待确认项，不能编造。会话独立仍需人审，不保证没有共享盲区

## AGENTS.md验证规则示例（按项目调整）

```
# 验证规则
- 测试失败默认先修实现；确需修改测试时，说明需求变化或测试错误并确认
- 不通过删除断言、放宽预期或跳过用例掩盖问题
- 为重要行为提供与风险相称的验证，覆盖关键边界和异常路径
- 报告实际运行的检查、结果及未覆盖范围，不把测试全绿等同于行为完全正确
```
