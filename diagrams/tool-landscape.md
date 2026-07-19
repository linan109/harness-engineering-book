# AI编程工具全景图 (Appendix D)

本图展示AI编程工具按自主程度分类的全景坐标系，核心洞察：工具越自主，所需的Harness就越强。

![AI编程工具全景坐标系](tool-landscape.svg)

## Mermaid 源码

```mermaid
graph LR
    subgraph legend["核心规律：自主程度 ↑ = Harness需求 ↑"]
        direction LR
        L1["低自主<br/>低Harness"] -.-> L2["中自主<br/>中Harness"] -.-> L3["高自主<br/>高Harness"] -.-> L4["很高自主<br/>很高Harness"]
    end

    style legend fill:#f8f9fa,color:#333
```

```mermaid
graph TB
    subgraph T1["第一类：代码补全"]
        direction TB
        T1H["自主程度：低（你打字，它预测）<br/>Harness需求：低（天然受限）"]
        T1A["GitHub Copilot<br/>2000万用户，市场份额42%"]
        T1B["通义灵码<br/>1300万下载，国内企业领先"]
        T1C["文心快码<br/>百度生态"]
    end

    subgraph T2["第二类：IDE Agent"]
        direction TB
        T2H["自主程度：中（对话+多文件编辑）<br/>Harness需求：中（需规则文件）"]
        T2A["Cursor<br/>ARR 20亿美元，增长最快SaaS"]
        T2B["Trae（字节跳动）<br/>600万用户，国内份额41.2%"]
        T2C["Windsurf（Codeium）<br/>已被Devin收购"]
    end

    subgraph T3["第三类：CLI Agent"]
        direction TB
        T3H["自主程度：高（终端自主执行）<br/>Harness需求：高（完整CIVR体系）"]
        T3A["Claude Code<br/>ARR约25亿美元"]
        T3B["Codex CLI（OpenAI）<br/>开源，160万周活"]
        T3C["Aider<br/>开源，repo map架构"]
    end

    subgraph T4["第四类：云端Agent"]
        direction TB
        T4H["自主程度：很高（云端全自主）<br/>Harness需求：很高（任务设计即Harness）"]
        T4A["Devin<br/>估值102亿美元"]
        T4B["Codex Cloud（OpenAI）<br/>单次最长6小时"]
        T4C["Copilot Coding Agent<br/>GitHub Actions集成"]
    end

    subgraph T5["第五类：平台类"]
        direction TB
        T5H["自主程度：中（生成即部署）<br/>Harness需求：中（面向产品验证）"]
        T5A["Bolt.new"]
        T5B["Replit Agent"]
        T5C["Lovable"]
    end

    T1 --> T2 --> T3 --> T4
    T5 -.-> T2

    style T1 fill:#69db7c,color:#333
    style T2 fill:#ffd43b,color:#333
    style T3 fill:#ffa94d,color:#333
    style T4 fill:#ff6b6b,color:#fff
    style T5 fill:#a9e34b,color:#333
```

## 工具全景对照表

| 工具类别 | 代表产品 | 自主程度 | Harness需求度 | 典型场景 | 上下文获取方式 |
|----------|----------|----------|--------------|---------|---------------|
| 代码补全 | Copilot、通义灵码、Tabnine | 低（你打字，它预测） | 低（天然受限） | 日常敲代码加速 | 当前文件 + 打开的Tab |
| IDE Agent | Cursor、Trae、Windsurf | 中（对话+多文件编辑） | 中（需规则文件） | 深度参与项目开发 | Embedding + 向量检索（预索引） |
| CLI Agent | Claude Code、Codex CLI、Aider | 高（终端自主执行） | 高（完整CIVR体系） | 复杂多步骤任务 | 按需搜索（ripgrep/glob/repo map） |
| 云端Agent | Devin、Codex Cloud、Copilot Agent | 很高（云端全自主） | 很高（任务设计即Harness） | 长时间自主作业 | 云端沙盒克隆仓库 |
| 平台类 | Bolt.new、Replit Agent、Lovable | 中（生成即部署） | 中（面向产品验证） | 快速原型、非工程师 | 平台内置环境 |

## 选择决策树

- 加速日常编码 --> Copilot / 通义灵码
- AI深度参与项目 --> Cursor / Trae
- 多步骤自主任务 --> Claude Code / Codex CLI
- 长时间自主执行 --> Devin / Codex Cloud（需确认：任务是否真的不需要中间干预？）
- 国内企业采购 --> 通义灵码（企业）/ Trae CN（个人）
