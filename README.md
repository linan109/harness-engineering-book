# 《驾驭AI编程：从古法手作到工业化生产》配套资源

这里提供书中的实践手册、配置模板、检查清单、代码练习、图表与阅读资料。围绕四个动作组织：**C 约束、I 告知、V 验证、R 校准**。

本次资源核对：2026-10-30。[配套实践手册](manuals/实践手册.md)已按作者提供的出版社排版PDF整理为Markdown，覆盖非研发岗位职场人、工程师、学生和研发团队四类读者。现有资源的变更见[更新记录](CHANGELOG.md)。

## 从你正在遇到的问题开始

| 你想做什么 | 从这里开始 |
|---|---|
| 按自己的身份完成一组实践 | [配套实践手册](manuals/实践手册.md)：办公提效、编程入门、学生练习、团队协作 |
| 在自己的项目里用起来 | [CIVR十问](checklists/civr-quickcheck.md) → [通用项目规则](templates/claude-md/general.md) |
| 配置工具的权限与检查 | [Claude Code配置说明](templates/settings/README.md)、[Cursor规则说明](templates/cursorrules/README.md) |
| 让团队使用同一套约定 | [团队AGENTS.md模板](templates/agents-md/team.md) |
| 长任务换会话、交接不丢状态 | [上下文自检](checklists/context-health.md)、[HANDOFF模板](templates/handoff/HANDOFF.md) |
| 判断结果是否做对、走偏后怎样处理 | [验证规则](checklists/verify-rules.md)、[校准清单](checklists/redirect.md) |
| 跑一个完整的小练习 | [支付回调](examples/code/payment-callback/README.md)、[购物车优惠](examples/code/cart-discount-exercise/README.md) |
| 理解AI的能力与局限 | [九个能力陷阱](diagrams/pitfall-map.md)、[附录C学习路径](resources/reading-paths.md) |
| 查找书中引用的资料 | [参考资料索引](resources/references.md) |

## 使用模板

先填写项目事实、删除不适用条目，再合并到现有文件。不要直接覆盖已有规则或配置。

- **Claude Code：** 选择[通用](templates/claude-md/general.md)、[前端](templates/claude-md/frontend.md)或[Spring Boot](templates/claude-md/spring-boot.md)模板，按项目调整后放入`CLAUDE.md`。权限与Hook另按[配置说明](templates/settings/README.md)合并。
- **Cursor：** 使用[general.mdc](templates/cursorrules/general.mdc)，按[说明](templates/cursorrules/README.md)放入`.cursor/rules/`并核对加载状态。
- **团队：** 将[team.md](templates/agents-md/team.md)作为`AGENTS.md`的起点。按各工具支持的方式导入或生成适配文件，实际检查是否读取；不能假设所有工具都会自动加载同一个文件。

文字约定、工具权限和运行环境隔离各有作用。模板里的路径、命令和技术选型都是需要裁剪的示例，不是安全保证。

## 运行练习

在本仓库根目录使用Python 3.10及以上版本，仅需标准库：

```sh
python -B examples/code/payment-callback/payment_callback.py
python -B examples/code/cart-discount-exercise/cart_discount_reference.py
python -B -m unittest discover -s tests -v
```

支付示例演示验签、幂等、状态变更和事务失败；购物车练习演示怎样发现优惠叠加错误。两者均为本地教学示例，详细契约和边界见各自README。

[登录对比](examples/code/login-comparison/spec-template.md)仍是关键代码片段，依赖未提供的业务模块，不能直接当作完整登录服务运行。`without-spec.py`和`cart-discount-bug.py`保留了有意设计的错误，供对比练习。

## 资料与书的对应关系

| 资源 | 对应内容 |
|---|---|
| [能力陷阱总图](diagrams/pitfall-map.md) | 第1章：AI能力与边界 |
| [CIVR全景图](diagrams/civr-panorama.md)、[十问](checklists/civr-quickcheck.md) | 第2章：框架总览 |
| 项目规则、权限配置、[告知清单](checklists/inform.md) | 第3—4章：约束与上下文 |
| [支付回调](examples/code/payment-callback/README.md) | 第5章5.5节：规格与验证 |
| [代码反述](examples/prompts/code-restatement.md)、[购物车练习](examples/code/cart-discount-exercise/README.md) | 第5章：双翻译；代码反述后与需求比较 |
| [独立QA](examples/prompts/qa-independent-test.md)、[TDD图](diagrams/tdd-cycle.md)、[信任矩阵](diagrams/trust-matrix.md) | 第5章：独立测试与验证策略 |
| [校准清单](checklists/redirect.md)、[交接](templates/handoff/HANDOFF.md)、[翻车记录](checklists/crash-log.md) | 第6章：校准与经验沉淀 |
| [代码考古](examples/prompts/code-archaeology.md)、[特征化测试](examples/prompts/characterization-test.md)、团队规则 | 第7章：已有系统与团队协作 |
| [能力冰山](diagrams/capability-iceberg.md) | 第8章：你的护城河 |
| [学习路径](resources/reading-paths.md)、[推荐书单](diagrams/reading-lists.md) | 附录C：深入理解AI的推荐阅读 |
| [工具分类示意](diagrams/tool-landscape.md) | 延伸阅读：工具形态，不是实时产品排行 |

图表提供Markdown说明、Mermaid源码与SVG展示图。九陷阱名称、顺序和主要CIVR映射已按终校图示同步；不表示仓库已与出版社最终排版稿逐字核对。

## 验证与维护

- Python示例及Hook脚本有本地自动化测试；测试通过只说明被覆盖的行为，未包含真实支付、完整登录系统或生产部署。
- Hook模板要求Claude Code **≥2.1.295**；本轮本机版本为2.1.282，尚未完成新版Claude会话内的加载与权限引擎验收。脚本子进程测试不能替代这一层验证。
- Cursor规则已检查格式与使用说明，尚未做实际Cursor会话加载验收。
- 7张SVG已解析、渲染并检查；Mermaid源码做了文本核对，未单独渲染验收。

工具变化后应重新核对官方文档与实际行为。发现错误可提[Issue](https://github.com/linan109/harness-engineering-book/issues)，尽量附上工具版本、复现步骤、期望与实际结果；也欢迎补充实际使用中的经验。

## 作者与许可

作者：李楠。公众号：**CIVR笔记**，分享AI开发实践，也欢迎读者留言交流。

本仓库自有代码、模板、清单和图表按[MIT License](LICENSE)提供。书籍正文与[配套实践手册](manuals/实践手册.md)不适用本仓库的MIT许可；外链资料和第三方引用仍按各自权利人的许可使用。
