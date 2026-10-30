# Claude Code 配置模板

来源：《驾驭AI编程》第3章约束、第5章验证。核对官方文档：2026-10-30。

这些文件是可裁剪的示例。`hooks.json`、`permissions.json` 都是标准 JSON；说明放在本文件中。不要用任意一份覆盖项目已有的 `.claude/settings.json`。

## 合并与启动

1. 查看现有项目、个人和组织配置，备份项目的 `.claude/settings.json`。按项目实际需求选择规则。
2. 将 `permissions.json` 中的 `permissions` 合并进去。已有 `allow`、`ask`、`deny` 数组分别追加并去重；检查原有宽权限是否仍然适用。不要把两份 JSON 直接拼接，也不要让后一次复制覆盖前一次配置。
3. 如需文件 Hook，把 `hook_paths.py`、`file_policy.py`、`check_python.py` 复制到目标项目的 `.claude/hooks/`，再按事件把 `hooks.json` 的处理器追加到现有 `hooks` 中。不要复制本目录 README 到 hooks 目录作为脚本。
4. 确认有 Python 3.10+。`command: "python"` 必须指向真正的 Python 可执行文件；Linux/macOS 可能需改为 `python3`，Windows 可改为 Python 的绝对 `.exe` 路径。不要在 `command` 后拼接参数，参数已放在 `args` 中。
5. 此配置要求 **Claude Code ≥2.1.295**，其中 `onFailure: "block"` 从该版本起受支持。用 `claude --version` 核对版本。旧版不可依靠这个字段防止启动失败放行。
6. 在目标项目根目录启动新会话，通过 `/hooks`、`/permissions` 查看加载项，并按下面的场景验证。配置还受组织策略、其他配置源和权限模式影响；不得仅凭 JSON 能解析就判定已生效。

示例使用 `args` 的 exec 形式，Python 脚本和带空格的路径都作为独立参数传递，不依赖 Bash、PowerShell 管道或 `head`/`tail`。

## 权限边界

默认模式为 `default`；只预先放行两个明确的 Git 只读命令。未列入 `allow` 不等于一律拒绝，仍按 Claude Code 的默认权限流程处理。不要为了减少提示改成 `bypassPermissions`。

`Read`/`Edit` 拒绝规则覆盖任意层级的 `.env*`、`.pem`、`.key`，也会排除 `.env.example`；这是有意保守的示例，需要公开样例时改用无敏感值、不同名称的文档。文件写入权限使用 `Edit(path)`，不能写成无效的 `Write(path)` 路径规则。迁移和 CI 配置示例设置为 `ask`，受控任务可以明确审批，并非永远禁止实现。

没有预先放行 `npx *`、`mvn *`、`find *`、任意解释器或任意项目脚本。构建、测试、依赖脚本都可能执行项目代码；审查项目与脚本后，再添加具体命令。数据库只读由数据库账号权限保证，不能靠 `Bash(DROP *)` 模拟。

权限匹配和这个 Hook 都不是完整安全沙箱。文件规则不能覆盖任意 Python/Node 子进程或所有间接读写；本例 Hook 只覆盖列出的文件工具，不拦截 Bash、PowerShell、MCP 等其他入口。需要跨进程保护时使用操作系统/容器隔离、Claude Code 沙箱、最小权限账号和网络限制，并独立验收。

## 两个 Hook 的行为

| 事件 | 匹配的工具 | 脚本与结果 |
|---|---|---|
| `PreToolUse` | `Read`、`Edit`、`Write`、`NotebookEdit` | 解析 stdin JSON；检查项目范围、解析后的符号链接目标以及敏感路径。正常退出0不主动授予额外权限；拒绝退出2。脚本无法启动/超时则由处理器层的 `onFailure: "block"` 拒绝。 |
| `PostToolUse` | `Edit`、`Write` | 仅对改动后的 `.py` 做 Python 语法检查，不执行目标代码、不生成 `.pyc`。失败退出2并向 Claude 反馈；文件已经修改，不能撤回，也不保证后续所有操作被禁止。 |

matcher 只写工具名。路径从 `tool_input.file_path`（NotebookEdit 使用 `notebook_path`）读取；敏感路径不读取内容。只检查项目内的相对路径组件，项目目录或祖先目录叫 `.env-project`、`archive.key` 不会误拦普通文件；项目入口为符号链接时，原路径与解析后路径分别使用对应项目根作为基准。Hook 依赖 `CLAUDE_PROJECT_DIR`，相对路径按输入 `cwd` 解析。若会话内进入另一 worktree，变量仍可能指向原项目；本例会拒绝原项目外路径，请在目标 worktree 重新启动并验收，不把范围检查直接删掉。

语法通过不等于测试或业务验证通过。这是无需额外依赖的最小示范；真实项目应补自己的 lint、类型检查、相关测试和人工审查。若替换成外部检查命令，必须保留检查的非零退出码；不要用默认取最后一段退出码的 `check | head` 掩盖失败。

## 本地触发测试与会话验收

在本配套仓库根目录运行，不调用模型、不安装依赖：

```sh
python -m unittest discover -s tests -p "test_settings*.py" -v
```

测试读取模板的真实处理器，替换可执行文件为当前 Python，并在带空格的临时项目中以 stdin 触发子进程：正常读写退出0；嵌套 `.env`、项目外路径及畸形输入退出2；Python 语法错误退出2，且原修改仍保留。测试进程不会模拟 Claude 的权限引擎。

在满足版本条件的 Claude Code 中，还需使用无敏感数据的临时项目逐项验收：

1. 普通 `.py` 编辑成功；故意制造语法错误后能看到事后检查反馈，文件仍有错误。
2. 尝试读写内容为 `DUMMY_ONLY` 的 `.env.hook-check` 被拒绝。敏感路径也配置了 permissions deny，可能先被权限规则拒绝；要单独验收 Hook，在隔离项目中只保留 Hook 配置再测，查看 debug 日志确认处理器实际触发。
3. 在隔离项目中临时把 `file_policy.py` 指向不存在的脚本，再做普通文件操作。应显示 `onFailure` 导致的阻断；恢复路径再测正常场景。这个步骤验证脚本故障时的行为，不能用直接运行 Python 代替。

本轮实际覆盖：Windows、本地 Python 子进程测试，14项中12项通过，2项符号链接用例因主机无创建权限跳过。读到的 Claude Code 为2.1.282，低于上述字段最低版本；尚未做新版 Claude 会话加载/权限引擎验收，也未做 Linux/macOS 运行验收。

官方依据：[Hooks reference](https://code.claude.com/docs/en/hooks)、[Configure permissions](https://code.claude.com/docs/en/permissions)。工具升级后需重新核对并运行上述场景。
