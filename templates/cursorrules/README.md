# Cursor 项目规则

当前入口为 `general.mdc`。填写项目与命令占位后，复制到目标项目 `.cursor/rules/general.mdc`，保留开头的 frontmatter。`alwaysApply: true` 表示每次会话都应用；本例不按文件类型筛选。若要拆分规则，应按实际使用场景设置 `description`、`globs`、`alwaysApply`。

`general.rules` 仅保留旧链接指引，不能直接复制到 `.cursor/rules/` 期待自动加载。旧根目录 `.cursorrules` 属兼容入口，不要同时维护两份相同规则；新项目优先使用 `.mdc`。若已有统一的 `AGENTS.md`，根据当前 Cursor 支持方式选择一个事实正本，避免复制后各自漂移。

加载验收：在目标项目打开 Cursor 的 Rules 设置，确认项目规则出现且类型为 Always Apply；再开新 Agent 对话，检查该规则是否出现在已附加规则/上下文中。可临时加入只用于加载检查的唯一标记，要求 Agent 引用它，随后删除标记并重开会话。模型复述标记只是辅助证据，还应核对界面中的规则附加状态；文件存在不等于规则已加载。

本轮核对了文件扩展名与 frontmatter，尚未在 Cursor 界面验证加载。规则是提供给模型的指令，不能代替工具权限、沙箱或数据库账号授权。

官方依据：[Cursor Rules](https://cursor.com/docs/rules)（2026-10-30核对）。
