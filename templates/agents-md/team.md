<!--
  来源：《驾驭AI编程》第7章（7.4 场景三：团队AI规则不统一 + AGENTS.md）
  用法：复制到项目根目录，重命名为 AGENTS.md
        所有 AI 工具（Claude Code / Cursor / Copilot / TRAE / Windsurf）启动时读取此文件
        工具特定的配置文件（CLAUDE.md / .cursorrules）从本文件生成或引用，不再单独维护
  更新：团队统一维护，修改需 code review。规则由人编写，AI 不得自行修改本文件

  核心原则（第 7 章）：
  - 约束只有一份，且存储在 Git 中
  - 一个文件一个负责人
  - 提交即负责
-->

# AGENTS.md — Team AI Development Rules

> This file is the single source of truth for all AI coding tools in this project.
> All team members' AI assistants read this same file.
> Tool-specific configs (CLAUDE.md, .cursorrules) should reference or generate from this file.

## Project Identity

Project: [项目名称]
Stack: [语言] / [框架版本] / [数据库] / [关键依赖]
Team size: [人数]
Repo: [仓库地址]

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

<!-- 给代码画安全地图，所有人的 AI 看到同一张图 -->

| Module | Permission | Owner | Reason |
|--------|-----------|-------|--------|
| `src/payment/` | **AI 不可修改** | [负责人] | 支付核心，修改需负责人审查 |
| `src/auth/` | **AI 不可修改** | [负责人] | 认证模块，安全敏感 |
| `src/features/` | AI 可自由修改 | — | 业务功能 |
| `migrations/` | **AI 禁止创建/修改** | [DBA/负责人] | 迁移必须人工操作 |
| `config/` | **只读** | [负责人] | 配置手动维护 |
| `.env*` | **禁止访问** | — | 敏感信息 |

### File Ownership

<!-- 第 7 章铁律二：一个文件一个负责人 -->
<!-- 同一时间，一个文件只由一个人（或一个 Agent）修改 -->

- Public modules (utils, common) changes go through **separate PRs**, not mixed with feature PRs
- If you need to modify a file owned by someone else, coordinate first

## Verification Rules

<!-- 第 5 章验证纪律，全团队统一执行 -->

1. 禁止删除或修改已有测试用例，除非需求本身变更了测试预期
2. 测试失败时，修代码，不许改测试
3. 新增功能必须附带测试
4. 所有代码必须能编译/运行，所有已有测试必须通过
5. 不得声称"已完成"而未提供运行验证的输出
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
- CI failure 2x on same PR → escalate to human review
- Reviewer checks: scope creep (C), hidden assumptions (I), happy-path-only tests (V)

## AI Crash Log

<!-- 第 6 章 6.8：从个人踩坑到团队知识 -->
<!-- 维护在 docs/ai-lessons.md，每条 3-5 行 -->
<!-- 格式：发生了什么 / 根因 / 新规则 -->

See `docs/ai-lessons.md` for team AI crash log.
When AI makes an error that a rule should have prevented, the reviewer adds a new entry.

## Maintenance

- Owner: [团队负责人 / Tech Lead]
- Review cycle: 每两周审查一次，删除过期规则
- Change process: 修改本文件需提 PR，至少一人 approve
- Last reviewed: [日期]
