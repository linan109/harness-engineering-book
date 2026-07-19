# 《驾驭AI编程：从古法手作到工业化生产》配套资源

> Companion resources for *Harness AI Programming: From Artisan Craft to Industrial Production*

本仓库是《驾驭AI编程》一书的配套资源库，提供书中提到的配置模板、检查清单、代码示例和提示词模板。

**书的核心方法论：CIVR框架**
- **C**onstrain（约束）：给AI画安全边界
- **I**nform（告知）：把你知道的告诉AI
- **V**erify（验证）：确认AI做的是对的
- **R**edirect（校准）：当AI走偏了怎么办

## 仓库结构

```
├── templates/              配置模板（开箱即用）
│   ├── claude-md/          CLAUDE.md 模板（通用/Spring Boot/前端）
│   ├── settings/           .claude/settings.json 示例（权限/Hook）
│   ├── cursorrules/        .cursorrules 模板（Cursor用户）
│   ├── agents-md/          AGENTS.md 跨工具统一模板（团队用）
│   └── handoff/            HANDOFF.md 多session交接模板
├── checklists/             检查清单（可打印）
│   ├── civr-quickcheck.md  CIVR 10个问题速查
│   ├── inform.md           告知 Checklist
│   ├── context-health.md   上下文健康度自检
│   ├── verify-rules.md     验证规则（可直接粘贴到CLAUDE.md）
│   ├── redirect.md         校准流程 Checklist
│   └── crash-log.md        翻车记录模板
├── examples/               示例
│   ├── code/               代码示例（登录对比、Spec模板等）
│   └── prompts/            提示词模板（代码考古、特征化测试等）
├── diagrams/               参考图表（Mermaid格式）
└── resources/              推荐阅读链接聚合
```

## 快速开始

### 个人使用

1. 把 `templates/claude-md/general.md` 复制到你的项目根目录，重命名为 `CLAUDE.md`
2. 根据项目实际情况修改内容（删除不适用的部分）
3. 把 `templates/settings/permissions.json` 复制到 `.claude/settings.json`

### 团队使用

1. 把 `templates/agents-md/team.md` 复制到仓库根目录，重命名为 `AGENTS.md`
2. 团队成员的工具配置（CLAUDE.md、.cursorrules）从 AGENTS.md 引用，不单独维护
3. 用 `checklists/crash-log.md` 的格式维护团队的 AI 翻车记录

### 校准与交接

1. 用 `checklists/redirect.md` 判断校准是否走偏
2. 多session任务用 `templates/handoff/HANDOFF.md` 做交接

## 使用原则

这些模板是**起点，不是终点**。书中反复强调：

- **约束不是越多越好。** 模板提供的是框架，你需要根据项目和团队裁剪
- **工具适配层是消耗品。** AI工具迭代很快，模板会过时，原则不会
- **用模板的过程本身就是CIVR的实践。** 你在决定保留哪些规则、删除哪些规则时，就是在做约束（C）和告知（I）

## 与书的对应关系

| 资源 | 对应章节 | CIVR维度 |
|------|---------|---------|
| CLAUDE.md 模板 | 第3章（约束）、第4章（告知） | C + I |
| 权限配置 | 第3章（硬约束） | C |
| Hook配置 | 第5章（验证纪律） | V |
| 验证规则 | 第5章（验证纪律） | V |
| 校准Checklist | 第6章（校准） | R |
| HANDOFF.md | 第6章（开新对话） | R |
| 代码考古提示词 | 第7章（已有系统） | I |
| AGENTS.md | 第7章（团队协作） | C（团队层） |
| 翻车记录 | 第6章（团队知识） | R（团队层） |

## 贡献

欢迎通过 PR 贡献：
- 其他工具的配置模板（Windsurf、Copilot、TRAE等）
- 其他语言/框架的 CLAUDE.md 模板
- 实际使用中发现的改进

## 许可

MIT License

---

**作者**：李楠 · 北大CS 2008

**书籍**：《驾驭AI编程：从古法手作到工业化生产》（2026年出版）
