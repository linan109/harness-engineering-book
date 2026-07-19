# AI时代的TDD循环 (Chapter 5, Section 5.8)

本图展示AI编程时代TDD循环的人机分工变化：RED-GREEN-REFACTOR三个阶段中，人类和AI各自承担不同角色。核心洞察：测试是人类定义"什么算对"的合同，AI负责让合同履行。

![AI时代的TDD循环](tdd-cycle.svg)

## Mermaid 源码

```mermaid
graph LR
    RED["🔴 RED<br/>写测试 / 定义失败<br/>━━━━━━━━━━<br/>👤 人类主导<br/>• 定义什么算对<br/>• 定义什么算失败<br/>• 覆盖边界条件<br/>• 此时无实现代码<br/>• 测试应该是红的"]
    
    GREEN["🟢 GREEN<br/>写实现 / 让测试通过<br/>━━━━━━━━━━<br/>🤖 AI主导<br/>• 写实现代码<br/>• 让测试从红变绿<br/>• 快速产出可运行代码"]
    
    REFACTOR["🔵 REFACTOR<br/>重构 + 审查<br/>━━━━━━━━━━<br/>🤖 AI重构<br/>• 清理代码结构<br/>• 提取公共逻辑<br/>👤 人类审查<br/>• 跑测试确认无回归<br/>• 审查架构合理性"]

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
    Start(("开始新功能")) --> WriteSpec["👤 人类：写Spec<br/>自然语言定义需求"]
    WriteSpec --> WriteTest["👤 人类：写测试<br/>（或独立AI会话写 + 人审）"]
    WriteTest --> RunTest1{"运行测试"}
    RunTest1 -->|"红色 ✓"| AskAI["🤖 AI：写实现代码<br/>让测试从红变绿"]
    RunTest1 -->|"绿色 ✗<br/>测试写错了"| WriteTest
    
    AskAI --> RunTest2{"运行测试"}
    RunTest2 -->|"绿色 ✓"| Refactor["🤖 AI：重构代码<br/>清理结构"]
    RunTest2 -->|"红色"| FixImpl["🤖 AI：修实现<br/>不许改测试！"]
    FixImpl --> RunTest2
    
    Refactor --> RunTest3{"运行测试"}
    RunTest3 -->|"绿色 ✓"| Review["👤 人类：审查<br/>架构合理？逻辑对？"]
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
| RED | 人类 | 测试和代码出自不同的脑子，偏差不会同步 |
| GREEN | AI | AI负责实现，测试失败时修代码而非改测试 |
| REFACTOR | AI + 人类 | AI擅长重构，人类确认无回归 |

## 保证测试质量的两种做法

1. **你自己写测试** -- 测试和代码出自不同脑子，偏差不会同步
2. **用独立会话或另一个AI写** -- 写测试的AI只看需求，不看实现代码（裁判和运动员不能是同一个人）

## CLAUDE.md验证规则（直接粘贴可用）

```
# 验证规则
- 禁止删除或修改已有测试用例，除非需求本身变更了测试预期
- 测试失败时，修代码，不许改测试
- 新增功能必须附带测试
- 代码必须能编译/运行，所有已有测试必须通过
```
