# AI时代的能力冰山模型 (Chapter 8, Section 8.1)

冰山图展示AI时代的能力分层：水面之上是AI较容易辅助的执行任务，水面之下是需要持续培养的判断力、领域知识、系统思维、错误识别与跨领域组织能力。这是能力结构的比喻，不代表人机能力的固定边界或比例。

![能力冰山图](capability-iceberg.svg)

## Mermaid 源码

```mermaid
block-beta
    columns 1
    
    block:above:1
        columns 1
        space
        A1["执行 Execution<br/>代码生成、样板代码、CRUD、重构"]
        A2["模式匹配 Pattern Matching<br/>识别常见模式、套用设计模式、语法转换"]
        A3["信息检索 Information Retrieval<br/>API用法查询、文档摘要、知识问答"]
    end
    
    WL["~~~~ 水面线 ════════════════════ AI辅助执行 ↑ ｜ ↓ 持续培养的能力 ~~~~"]
    
    block:below:1
        columns 1
        B1["判断力 Judgment<br/>什么时候该信AI、什么时候该拦<br/>验证悖论：AI最能帮你的地方，恰好是你最没法验证的地方"]
        B2["领域知识 Domain Knowledge<br/>隐性知识、业务上下文、历史包袱<br/>你公司上周改的Schema、昨天变的需求、今早调的阈值"]
        B3["系统思维 System Thinking<br/>架构决策、模块边界、长期权衡<br/>向下懂两层，向上懂一层"]
        B4["错误识别 Error Recognition<br/>识别Almost Right、发现缺失而非错误<br/>审查边界条件、遗漏与隐含假设"]
        B5["跨领域组织能力 Cross-domain Orchestration<br/>把测序→生信分析→mRNA设计→合作→审批整条链路串起来<br/>借助AI获取知识，由你组织资源并承担决策责任"]
    end

    style above fill:#74c0fc,color:#333
    style WL fill:#339af0,color:#fff
    style below fill:#1864ab,color:#fff
    style A1 fill:#a5d8ff,color:#333
    style A2 fill:#a5d8ff,color:#333
    style A3 fill:#a5d8ff,color:#333
    style B1 fill:#1971c2,color:#fff
    style B2 fill:#1864ab,color:#fff
    style B3 fill:#155d9e,color:#fff
    style B4 fill:#134f87,color:#fff
    style B5 fill:#0f4170,color:#fff
```

## 替代方案：纵向流程图

```mermaid
graph TB
    subgraph water_above["水面之上 —— AI较容易辅助的任务"]
        direction TB
        E["执行<br/>代码生成、CRUD、样板代码"]
        PM["模式匹配<br/>设计模式套用、语法转换"]
        IR["信息检索<br/>API查询、文档摘要"]
    end
    
    WL["════════ 水面线 ════════"]
    
    subgraph water_below["水面之下 —— 需要持续培养的能力"]
        direction TB
        J["判断力<br/>什么时候该信，什么时候该拦"]
        DK["领域知识<br/>隐性知识、业务上下文、历史包袱"]
        ST["系统思维<br/>架构决策、模块边界、长期权衡"]
        ER["错误识别<br/>识别Almost Right、发现缺失"]
        CO["跨领域组织能力<br/>串联多领域资源与流程"]
    end
    
    E --> PM --> IR --> WL
    WL --> J --> DK --> ST --> ER --> CO

    style water_above fill:#a5d8ff,color:#333
    style WL fill:#339af0,color:#fff,stroke:#339af0
    style water_below fill:#1864ab,color:#fff
    style E fill:#74c0fc,color:#333
    style PM fill:#74c0fc,color:#333
    style IR fill:#74c0fc,color:#333
    style J fill:#1971c2,color:#fff
    style DK fill:#1864ab,color:#fff
    style ST fill:#155d9e,color:#fff
    style ER fill:#134f87,color:#fff
    style CO fill:#0f4170,color:#fff
```

## 关键洞察

- **水上部分**占冰山的一小部分，代表AI较容易辅助的执行任务，仍需按风险验证
- **水下部分**远大于水上，代表需要持续培养的深层能力，AI也可以辅助
- **瓶颈视角**：执行加速后，判断、架构与领域决策可能成为瓶颈；图形面积不表示能力占比或价值倍数
- **自检规则**：向下懂两层，向上懂一层
