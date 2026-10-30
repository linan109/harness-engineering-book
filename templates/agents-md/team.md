<!--
  来源：《驾驭AI编程》第7章（7.4 场景三：团队AI规则不统一 + AGENTS.md）
  用法：复制到项目根目录，重命名为 AGENTS.md
        作为团队规则的单一来源，按各工具支持的方式加载、导入或生成适配文件
        不假设所有工具启动时自动读取；逐项验证加载范围与更新方式
  更新：团队统一维护，修改需 code review。AI可按授权整理修改，不得自行改变团队约定

  核心原则（第 7 章）：
  - 约束只有一份，且存储在 Git 中
  - 一个文件一个负责人
  - 提交即负责
-->

# AGENTS.md — Team AI Development Rules

> This file is the single source of truth for all AI coding tools in this project.
> Configure each tool to load these rules, then verify that it does so.
> Tool-specific configs should import or generate from this file using supported mechanisms.
> A plain-text link does not necessarily load its target. These rules are not a security sandbox.

## Project Identity

Project: [项目名称]
Stack: [语言] / [框架版本] / [数据库] / [关键依赖]
Team size: [人数]
Repo: [仓库地址]

Authoritative sources: [当前需求、架构和任务状态入口；注明已失效的旧决定]

## System Architecture

<!-- 心智模型：所有 AI 工具共享同一张全局图 -->

```
[数据流简图]
```

Key design decisions (and why):
- [决策 1]：[原因]
- [决策 2]：[原因]
- Rejected alternatives: [已否决的方案及原因，防止 AI 反复建议]

## Build & Test Commands

<!-- 统一命令，不管用什么 AI 工具都一样 -->

```bash
install:    [命令]
dev:        [命令]
test:       [命令]
lint:       [命令]
build:      [命令]
typecheck:  [命令]
```

## Code Conventions

<!-- 统一风格，解决"你的 AI 用 snake_case，同事的 AI 用 camelCase"的问题 -->

### Naming

- Variables/functions: [camelCase / snake_case]
- Classes/Components: [PascalCase]
- Constants: [UPPER_SNAKE_CASE]
- Files: [kebab-case / camelCase / PascalCase]
- Database tables/columns: [lower_snake_case]

### Error Handling

- Pattern: [统一模式，如"只抛自定义异常" / "Result 类型"]
- Logging: [格式要求]
- No empty catch blocks

### Code Structure

- Max function length: [行数]
- Max file length: [行数]
- [其他团队约定]

## Architecture Boundaries

### Module Permissions

<!-- 默认边界示例。明确任务授权后按范围执行；读取敏感数据也需要相应授权。 -->

| Module | Permission | Owner | Reason |
|--------|-----------|-------|--------|
| `src/payment/` | **默认只读** | [负责人] | 获准修改后需支付状态及失败路径验证 |
| `src/auth/` | **默认只读** | [负责人] | 获准修改后需安全审查与权限验证 |
| `src/features/` | 任务范围内可读写 | [负责人] | 业务功能 |
| `migrations/` | **默认只读** | [DBA/负责人] | 编写、演练、执行分别明确范围 |
| `config/` | **只读** | [负责人] | 配置手动维护 |
| `.env*` | **禁止访问** | — | 敏感信息 |

### File Ownership

<!-- 第 7 章铁律二：一个文件一个负责人 -->
<!-- 同一时间，一个文件只由一个人（或一个 Agent）修改 -->

- Shared-module changes identify an owner and all dependent callers; review shared wiring together with the feature that needs it
- If you need to modify a file owned by someone else, coordinate first

## Verification Rules

<!-- 第 5 章验证纪律，全团队统一执行 -->

1. 测试失败时默认修代码，不得为了变绿而删测试、降低断言或跳过失败
2. 确需改测试，先说明需求变化或测试本身的错误，按已有授权或经确认后修改
3. 按风险验证关键行为、边界和失败路径，不以测试数量代替覆盖质量
4. 完成项目要求的构建与测试，区分已有失败、本次引入的问题和未验证范围
5. 提供实际验证证据，区分分支完成、主干接收和实际用户流程可用
6. 每个 PR 只做一件事（一个功能或一个 bug fix，不混在一起）

## Security Rules

- 参数化查询，禁止字符串拼接 SQL
- 禁止 `innerHTML` 赋值用户输入
- 禁止硬编码密钥、token、密码
- 禁止 `verify=False` / `shell=True` + 用户输入
- 认证检查覆盖所有非公开 API 路由
- 日志中禁止打印密码、token 等敏感信息

## Forbidden Patterns

<!-- 不管你用什么 AI 工具，这些规则不能破 -->

- [禁用的库/框架]（原因：[说明]）
- [禁用的代码模式]
- Do not modify this file (AGENTS.md) without team review
- Do not install new dependencies without confirmation

## PR & Review Standards

<!-- 第 7 章团队协作规则 -->

- Every AI-generated PR must be reviewed by a human before merge
- PR scope: one feature or one fix per PR, no mixed changes
- AI "incidental" refactors (renaming, reformatting unrelated code) must be in separate PRs
- Repeated CI failures without new evidence → stop patching and review the diagnosis
- Reviewer checks: scope creep (C), hidden assumptions (I), happy-path-only tests (V)

## AI Crash Log

<!-- 第 6 章 6.8：从个人踩坑到团队知识 -->
<!-- 维护在 docs/ai-lessons.md，长证据用链接 -->
<!-- 格式：发生了什么 / 证据 / 已确认原因与假设 / 恢复结果 / 后续措施 -->

See `docs/ai-lessons.md` for team AI crash log.
Record reusable lessons with evidence. Decide whether a test, permission control or rule is needed; do not add a rule for every error.

## Maintenance

- Owner: [团队负责人 / Tech Lead]
- Review cycle: 每两周审查一次，删除过期规则
- Change process: 修改本文件需提 PR，至少一人 approve
- Loading check: 核实各工具的规则入口、作用范围和更新是否生效，不假设在用会话自动刷新
- Last reviewed: [日期]
