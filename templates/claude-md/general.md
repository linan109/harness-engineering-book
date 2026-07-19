<!--
  来源：《驾驭AI编程》第3章（约束）、第4章（上下文工程）、第5章（验证）
  用法：复制到项目根目录，重命名为 CLAUDE.md，根据项目实际情况修改
  更新：根据项目需求修改，删除不适用的部分
  原则：保持在 200 行以内。每条规则都应该是"删掉它 AI 会做错的事"
-->

# Project Overview

<!-- 30 秒心智模型：告诉 AI 系统如何运转，比写 10 条具体规则更有效（第 4 章） -->

[项目名称] — [一句话描述]

Tech stack: [语言] / [框架] / [数据库] / [关键依赖及版本]

```
用户请求 → [入口] → [核心服务] → [数据库]
                                  ↓
                          [消息队列] → [Worker] → [外部服务]
```

<!-- 负面上下文：告诉 AI "为什么不"，压缩它的搜索空间（第 4 章） -->
Design decisions:
- 我们评估过 [备选方案]，因 [原因] 选择了 [当前方案]，请勿建议迁移
- [其他已否决的技术选型及原因]

## Build & Test Commands

<!-- AI 需要知道如何构建和验证代码 -->

```bash
# Install dependencies
[包管理器] install

# Run dev server
[命令]

# Run tests (AI 每次改完代码后必须运行)
[测试命令]

# Lint
[lint 命令]

# Build
[构建命令]
```

## Architecture Boundaries

<!-- 模块权限：给代码画安全地图（第 3 章） -->

| Path | Permission | Reason |
|------|-----------|--------|
| `src/core/` | AI 可读写 | 核心业务逻辑 |
| `src/payment/` | **只读** | 支付模块，修改需人工审查 |
| `src/auth/` | **只读** | 认证模块，安全敏感 |
| `config/` | **只读** | 配置文件，手动维护 |
| `migrations/` | **禁止创建/修改** | 数据库迁移必须人工操作 |
| `.env` | **禁止访问** | 环境变量含敏感信息 |

## Code Conventions

<!-- 软约束：给理由，AI 遇到边界场景时能自己判断（第 3 章） -->

- [语言/框架] version: [版本号]（[为什么锁定此版本]）
- Naming: [命名风格，如 snake_case / camelCase]
- Error handling: [统一的错误处理模式，如 "只抛自定义 BusinessException"]
- Logging: [日志格式要求]
- Config format: [如 YAML/JSON/TOML]

Forbidden patterns:
- 不要使用 [被禁用的库/模式]（原因：[简要说明]）
- 不要硬编码 URL、端口、密钥等配置值
- 不要使用 `any` 类型 / 裸抛 RuntimeException / [其他]

## Verification Rules

<!-- 直接粘贴到 CLAUDE.md 的验证纪律（第 5 章 5.9 实操卡片） -->

- 禁止删除或修改已有测试用例，除非需求本身变更了测试预期
- 测试失败时，修代码，不许改测试
- 新增功能必须附带测试
- 代码必须能编译/运行，所有已有测试必须通过
- 执行结果截图或日志必须附在 PR 描述中
- 不得声称"已完成"而未提供运行验证的输出

## Forbidden Zones

<!-- 不可逆操作约束：问自己"AI 做什么是我按不了 Ctrl+Z 的？"（第 3 章） -->

Database operations:
- SELECT: 随意
- INSERT/UPDATE: 需要确认
- DELETE 和 DROP: **禁止**

File system:
- `src/` 下自由读写
- `config/` 下只读
- `.env` 禁止访问

External services:
- 读取类 API 调用: 允许
- 写入类 API 调用（发邮件、创建订单、修改用户数据）: **需要确认**
- 生产环境 API: **禁止直接调用**

## Context Maintenance

<!--
  每周花 15 分钟审查本文件（第 4 章）：
  - 对每条规则问"删掉这条，AI 会做错什么？"答不上来就删
  - 能用 Hook/CI 替代的移出去，不占用上下文预算
  - AI 犯了一个"你不会犯的错"→ 补一条隐性知识进来
-->

Last reviewed: [日期]
