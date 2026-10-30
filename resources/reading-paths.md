# 附录C学习路径与直达链接

对应《驾驭AI编程》附录C。先建立原理认知，再按问题补读；无需一次读完。章节号表示本书中的相关主题，不是对出版社最终排版稿的逐页核验。

链接核对日期：2026-10-30。优先列原作者、论文预印本和官方文档；经典书不附购买链接。完整历史资料索引见[参考资料](references.md)。

## 先看这三个

1. [Andrej Karpathy：Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)：建立LLM训练、推理与局限的整体认识，对应第1章。
2. [3Blue1Brown：Attention in Transformers](https://www.3blue1brown.com/lessons/attention/)：以图解理解注意力；作者网站含文字版和视频入口，对应第1章、第4章。
3. [Andrej Karpathy：Let's Build GPT from Scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY)：动手实现一个小型GPT，对应第1章。配套代码见作者的[Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)。

## 从零系统学习的顺序

| 阶段 | 原作者或官方入口 | 学习目标 | 对应章节 |
|------|------------------|----------|----------|
| 破除魔法感 | [3Blue1Brown神经网络系列](https://www.3blue1brown.com/topics/neural-networks) | 从神经网络、梯度下降走向Transformer | 第1章 |
| 概览LLM | [Karpathy：Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 区分训练、推理、生成与事实可靠性 | 第1章 |
| 理解注意力 | [Attention in Transformers](https://www.3blue1brown.com/lessons/attention/)；[Attention Is All You Need](https://arxiv.org/abs/1706.03762)，Vaswani等，2017 | 先读图解，再看论文Figure 1和Section 3 | 第1章、第4章 |
| 动手实现 | [Let's Build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)；[Let's Build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)；[作者课程与代码](https://github.com/karpathy/nn-zero-to-hero) | 理解next-token预测与字符串到token的转换 | 第1章 |
| 中文系统教材 | [《动手学深度学习》中文版](https://zh.d2l.ai/)，阿斯顿·张、李沐、扎卡里·C.立顿、亚历山大·J.斯莫拉 | 按需要补齐数学、训练和深度学习基础；站内有代码与课程入口 | 第1章、附录C |
| Agent范式 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)，Yao等，2022 | 理解推理与环境行动交替的Agent模式 | 第1章、第7章 |
| 从模型到产品 | [Anthropic：Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)；[LangChain RAG教程](https://docs.langchain.com/oss/python/deepagents/rag) | 区分工作流、Agent与检索；观察如何组织外部知识 | 第4章、第7章 |
| 持续跟踪 | [Anthropic Research](https://www.anthropic.com/research)；[OpenAI Research](https://openai.com/research/)；[Google DeepMind博客](https://deepmind.google/blog/) | 优先读研究方法与适用边界，再看产品结论 | 全书 |

LangChain旧教程地址已重定向到Deep Agents RAG教程；当前页面是更新后的实现路线，不应把旧版代码与新版API混用。实践前先核对页面列出的运行环境和依赖版本。

## 带着具体问题补读

| 问题 | 直达材料 | 怎么读 |
|------|----------|--------|
| 为什么长上下文里会漏信息？ | [Lost in the Middle](https://arxiv.org/abs/2307.03172)；[Chroma：Context Rot](https://www.trychroma.com/research/context-rot) | 比较位置效应与输入长度效应；放入窗口不等于稳定使用 |
| 为什么同一问题回答不同？ | [Hugging Face：How to Generate Text](https://huggingface.co/blog/how-to-generate)；[nanoGPT的sample.py](https://github.com/karpathy/nanoGPT/blob/master/sample.py) | 观察temperature、top-k、top-p等采样控制；不要把整个sample.py误认成只有几行 |
| 为什么AI不认识私有项目？ | [LangChain检索说明](https://docs.langchain.com/oss/python/deepagents/retrieval)；[RAG教程](https://docs.langchain.com/oss/python/deepagents/rag)；[OpenAI Embeddings指南](https://developers.openai.com/api/docs/guides/embeddings) | 区分模型参数中的知识与推理时提供的外部资料；检索召回仍需验证 |
| 为什么回答流畅却会错？ | [Karpathy：Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)；[Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)；[迎合行为研究预印本](https://arxiv.org/abs/2510.01395) | 区分生成机制、对齐方法与迎合的实证研究。Constitutional AI讨论对齐方法，不能单独证明所有幻觉或迎合的成因 |
| 为什么Agent会用错工具？ | [Anthropic Tool Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)；[OpenAI Function Calling](https://developers.openai.com/api/docs/guides/function-calling)；[Phil Schmid：Context Engineering Part 2](https://www.philschmid.de/context-engineering-part-2) | 分开检查描述、schema、可用工具集和执行权限；协议说明不等于调用一定正确 |

## Harness Engineering一手资料

| 材料 | 来源性质与用途 | 对应章节 |
|------|----------------|----------|
| [Harness Engineering: Leveraging Codex in an Agent-First World](https://openai.com/index/harness-engineering/) | OpenAI官方工程复盘：代码库、环境、架构约束与反馈环路 | 第2—7章 |
| [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | Anthropic官方复盘：跨上下文窗口的任务连续性 | 第4章、第6章、第7章 |
| [Harness Engineering for Coding Agent Users](https://martinfowler.com/articles/harness-engineering.html) | Birgitta Böckeler发表于Martin Fowler网站的分析；这是对早期memo扩写的文章 | 第2章、第7章、第8章 |
| [Harness Engineering: How to Supervise Code You Can't Read](https://kozyrkov.medium.com/harness-engineering-how-to-supervise-code-you-cant-read-71ebd05bfde7) | Cassie Kozyrkov作者文章；可核对标题与作者，全文可能需Medium会员 | 第5章 |
| [Build the Harness, Not the Code](https://vitthalmirji.com/2026/02/build-the-harness-not-the-code-a-staff/principal-engineers-guide-to-ai-agent-systems/) | Vitthal Mirji作者文章：工程负责人的实践视角 | 第4章、第7章 |
| [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) | Dex Horthy / HumanLayer开源项目：Agent工程原则 | 第2章、第7章 |
| [Claude Code官方文档](https://code.claude.com/docs/)；[系统提示词社区整理](https://github.com/Piebald-AI/claude-code-system-prompts) | 前者为产品说明，后者为非官方观察材料；公开提示词不代表完整产品开源，也不保证与当前版本完全一致 | 第3章、第4章、第6章 |

## 经典书与延伸阅读

| 书名 | 作者 | 阅读方向 |
|------|------|----------|
| 《人月神话》 | Frederick P. Brooks Jr. | 团队沟通与软件工程约束 |
| 《设计模式》 | Erich Gamma、Richard Helm、Ralph Johnson、John Vlissides | 设计选择与结构权衡 |
| 《重构》 | Martin Fowler | 识别坏味道和小步改善结构 |
| 《持续交付》 | Jez Humble、David Farley | 交付流水线与可重复验证 |
| 《凤凰项目》 | Gene Kim、Kevin Behr、George Spafford | 系统瓶颈、协作与运维 |
| 《思考，快与慢》 | Daniel Kahneman | 判断与复核；类比不能代替AI机制解释 |
| 《反脆弱》 | Nassim Nicholas Taleb | 怎样从偏差和失败中改善系统 |
| 《清单革命》 | Atul Gawande | 用检查清单减少可预防的遗漏 |

## 链接核验范围

本轮逐个打开了本文的外部地址，核对页面标题、来源及可读取内容；重定向采用已核对的落地地址。YouTube只确认了视频页与标题，未验证地区可播放性、字幕或完整视频；作者课程仓库提供交叉入口。Medium文章可见会员墙，未声称全文免费。

链接可访问只证明入口存在，不代表已重做论文实验、跑通教程或审查社区仓库全部代码。文档、默认分支代码和产品机制仍会变化；需要复现实验时记录具体版本。完整历史索引中尚未核实的条目不在本页链接核验承诺内。
