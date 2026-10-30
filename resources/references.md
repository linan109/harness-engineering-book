# 《驾驭AI编程》参考资源汇总

按类别保留写作时的资料索引，章节号用于定位讨论主题，不代表与出版社最终排版稿逐项一致。附录C的学习顺序与直达链接见[学习路径](reading-paths.md)。

本轮核对：2026-10-30。优先修正已确认的事实和归因，并补充主要原始来源。旧条目中尚无直达链接的材料仍是查找线索，不能视为已经完成来源核验；个人复盘、媒体报道、厂商自测与学术研究应分别判断。历史实验不能直接代表当前模型、产品或行业整体表现，本文不提供实时价格、市场份额或固定效率倍数。

---

## 1. 学术论文 (Academic Papers)

- **Liu et al., "Lost in the Middle: How Language Models Use Long Contexts"**, TACL, 2024（预印本2023）。研究长上下文中的位置信息使用差异。[论文](https://arxiv.org/abs/2307.03172)。
  - 引用章节: 第1章, 第4章

- **Arditi et al., "Refusal in Language Models Is Mediated by a Single Direction"**, 2024。研究特定模型及实验设置中的拒答表征，不等于所有安全机制都可被同一种方法移除。[论文](https://arxiv.org/abs/2406.11717)。
  - 引用章节: 第1章

- **Siegel et al., "CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark"**, 2024。用于理解模型与harness共同影响评测结果；比较分数前需核对同一榜单版本和实验条件。[论文](https://arxiv.org/abs/2409.11363)。
  - 引用章节: 第2章

- **Judy Hanwen Shen、Alex Tamkin, "How AI Impacts Skill Formation"**, 2026。程序员学习实验；理解测验与编码速度需分别解读，不把实验结果当作所有AI使用者的固定效果。[论文](https://arxiv.org/abs/2601.20245)。
  - 引用章节: 第2章, 第5章, 第7章, 第8章

- **Cheng, Lee, Khadpe等, "Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence"**, Science, 2026。研究AI迎合及其对人类判断的影响。[DOI](https://doi.org/10.1126/science.aec8352)（本轮返回403，未读到期刊全文）；[预印本](https://arxiv.org/abs/2510.01395)。预印本与期刊版统计口径可能不同。
  - 引用章节: 第1章

- **Nghi D. Q. Bui, "Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned"**, 2026。终端Agent架构与概念区分。[论文](https://arxiv.org/abs/2603.05344)。
  - 引用章节: 第2章, 附录B

- **Xin Xia et al., "Measuring Program Comprehension: A Large-Scale Field Study with Professionals"**, IEEE Transactions on Software Engineering, Vol. 44, No. 10, 2018. 78名专业开发者、3148工作小时实地研究。
  - 引用章节: 第7章

- **Prithvi Rajasekaran, "Harness Design for Long-Running Application Development"**, Anthropic, 2026-03-24。开发与评估角色分离、长任务上下文管理的工程复盘。[原文](https://www.anthropic.com/engineering/harness-design-long-running-apps)。
  - 引用章节: 第1章, 第2章, 第5章

- **Harvard Business School, "Who is AI Displacing?"**, 覆盖6200万劳动者的研究, 2025 (NBER Working Paper, 2026).
  - 引用章节: 第0章, 第8章

---

## 2. 官方文档与博客 (Official Docs & Blogs)

### Anthropic

- **Anthropic, "How We Built Our Multi-Agent Research System"**, 2025。研究型多Agent系统的角色分工、上下文与协调成本复盘；其中成本比较只适用于文中场景。[原文](https://www.anthropic.com/engineering/multi-agent-research-system)。
  - 引用章节: 第1章, 第4章, 第7章

- **Anthropic, "Best Practices for Claude Code"**。规则、上下文与验证的官方使用建议；以当前版本文档为准。[官方文档](https://code.claude.com/docs/en/best-practices)。
  - 引用章节: 第4章

- **Anthropic, "Prompt Caching"**。理解缓存的机制与约束；费率和适用模型以当前官方说明为准，不保留旧价格。[官方文档](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)。
  - 引用章节: 第4章

- **Anthropic, Claude Code官方文档及工程博客**。用于了解子agent、上下文压缩和工具集成。公开文档与社区逆向材料不等于完整产品开源，内部实现推断需标明来源。[官方文档](https://code.claude.com/docs/)。
  - 引用章节: 第1章, 第4章

- **Anthropic, "What 81,000 People Want from AI"**, 2026。面向Claude用户的80,508份开放式访谈，分析愿望、收益与担忧。引用比例时需核对类别与样本，不能混淆全体受访者、学生子样本、期望与亲历的分母。[原始报告](https://www.anthropic.com/features/81k-interviews)。
  - 引用章节: 第5章, 第8章

- **Nicholas Carlini, "Building a C Compiler with a Team of Parallel Claudes"**, Anthropic, 2026-02-05。多Agent构建的是约10万行Rust实现的C编译器原型，编译器实现语言与其编译的语言不同。[原文](https://www.anthropic.com/engineering/building-c-compiler)。
  - 引用章节: 第5章

### OpenAI / Kiro / AWS

- **Kiro / AWS Cost Explorer事件报道与Amazon回应**, 2026-02。媒体报道2025年12月的一次服务中断涉及Kiro执行环境变更；Amazon认为根因是用户错误及访问控制配置，并否认AI自主失控这一归因。应同时阅读双方材料，不称作AWS发布的官方AI事故报告。[FT报道](https://www.ft.com/content/00c282de-ed14-4acd-a948-bc8d6bdb339d)（会员墙，已核对标题）；[Amazon回应](https://www.aboutamazon.com/news/aws/aws-service-outage-ai-bot-kiro)。
  - 引用章节: 第3章

### Stripe

- **Stripe, "Minions: Stripe's One-Shot, End-to-End Coding Agents"**, 2026。官方开发流水线复盘，讨论确定性步骤、Agent执行与人工审查的组合；PR量与测试规模为当时案例背景。[原文](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)。
  - 引用章节: 第3章, 第5章, 第7章

### Vercel

- **Vercel, "We Removed 80% of Our Agent's Tools"**, 2025-12-22。d0工具裁剪与任务完成质量的产品实验；具体提升仅适用于其测试设置，不外推为工具越少越好。[原文](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)。
  - 引用章节: 第3章

### Google

- **Google DORA Report 2025**。软件交付与组织绩效研究。[官方入口](https://dora.dev/research/2025/dora-report/)。旧索引误归于此的PR体积、审查时间和bug变化来自Faros遥测，见第3部分；DORA报告与DORA指标不是同一概念。
  - 引用章节: 第0章, 第7章

### Shopify

- **Shopify CEO Tobi Lutke全员备忘录**, 2025年4月. 团队采用AI的管理备忘录，具体采购与招聘数字待原始材料核对。Business Insider/The Verge/Shopify Engineering Blog.
  - 引用章节: 第0章

### Airbnb

- **Airbnb Engineering Blog, Charles Covey-Brandt**, 2025年3月; Szczepan Faber, DPE Summit, 2025年9月. 测试迁移、Sample-Tune-Sweep方法与重试循环的企业案例。
  - 引用章节: 第5章, 第8章

### Apple

- **9to5Mac, "Apple pushing back on vibe coding iPhone apps"**, 2026年3月. 苹果引用App Store Guideline 2.5.2限制Replit/Vibecode等Vibe Coding应用上架。
  - 引用章节: 第2章

### Stanford

- **Stanford HAI AI Index 2025报告**, Technical Performance章节. 讨论技术能力基准的历史演进；跨年份比较需核对模型、题集和脚手架是否一致。
  - 引用章节: 第1章

### METR

- **METR, "Time Horizon 1.1"**, 2026-01-29。以给定成功率阈值估计任务的人类等价完成时长；不是模型实际连续运行时长，也不是任意真实项目的可自主工作时长。阅读时需看任务分布、成功率阈值与置信区间；此处不列未经核验的单模型小时数。[原始说明](https://metr.org/blog/2026-01-29-time-horizon-1-1/)。
  - 引用章节: 第1章

### Stack Overflow

- **Stack Overflow 2025 Developer Survey**。AI采用与信任的历史调查，题目和分母各异，不能把某工具的受访者使用率等同市场份额。[AI专题](https://survey.stackoverflow.co/2025/ai/)。
  - 引用章节: 第0章, 第1章, 第5章

### LangChain

- **LangChain, "The Anatomy of an Agent Harness"**, 2026。模型与harness的职责分界。[原文](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)；[Improving Deep Agents with Harness Engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)。评测提升以具体模型、基准与实验版本为限。
  - 引用章节: 第2章

### Monday.com

- **Monday.com联合CEO Eran Zinman**, 20VC播客访谈, 2026年3月.
  - 引用章节: 第8章

### Manus

- **Manus, "Context Engineering for AI Agents: Lessons from Building Manus"**, manus.im.
  - 引用章节: 第4章

### DX

- **DX (getdx.com), 400家公司纵向追踪**, 2024.11-2026.02. AI工具使用与工程交付变化的纵向观察，均值与中位数应分别解释。
  - 引用章节: 第7章

---

## 3. 行业报告与数据 (Industry Reports & Data)

- **Faros AI, "The AI Productivity Paradox Research Report"**, 2025。开发者遥测中观察到PR体积增加154%、审查时间增加91%、bug增加9%的关联；这不是Google DORA报告的数据，也不能据此认定AI造成同幅度的因果变化。开发者层面变化不等于组织交付绩效改善。[原报告页面](https://www.faros.ai/blog/ai-software-engineering)。
  - 引用章节: 第0章, 第5章, 第7章

- **Apiiro, "4x Velocity, 10x Vulnerabilities: AI Coding Assistants Are Shipping More Risks"**, Itay Nussbaum, 2025年9月. AI代码风险的厂商研究，需结合样本及检测方法解释。
  - 引用章节: 第1章

- **CodeRabbit, "State of AI vs Human Code Generation Report"**, David Loker, 2025年12月. AI与人类代码PR比较的厂商研究，不能直接外推为所有项目的风险倍数。
  - 引用章节: 第0章

- **Harness, "State of Software Delivery 2025"**. 开发者对AI代码调试负担的调查，原始题目与分母待补核。
  - 引用章节: 第0章

- **Workday, "New Workday Research: Companies Are Leaving AI Gains on the Table"**, 2026-01-14。研究AI节省时间与返工消耗的关系；这是Workday研究的口径，不与Anthropic开放式访谈混用。[官方新闻稿](https://newsroom.workday.com/2026-01-14-New-Workday-Research-Companies-Are-Leaving-AI-Gains-on-the-Table)。
  - 引用章节: 第5章

- **Oasis Security, ClawHub安全扫描报告**, 2026年初. 恶意Skill案例与安全扫描背景。 ClawJacked漏洞: 恶意网页通过WebSocket连接本机Agent.
  - 引用章节: 第0章

- **IEEE Spectrum / SignalFire / LeadDev / Stanford 就业数据综合**. 就业、招聘与管理者意向的不同数据口径，应分别回到原报告，不拼成统一统计结论。
  - 引用章节: 第0章

- **DryRun Security, "The Agentic Coding Security Report"**, 2026-03。让Claude Code、OpenAI Codex、Google Gemini开发两个真实应用，针对30个PR进行了38次扫描，发现143个安全问题；4个PR未发现漏洞。未发现不等于证明无漏洞，扫描次数、PR数量与应用数量是不同口径。[Help Net Security报道](https://www.helpnetsecurity.com/2026/03/13/claude-code-openai-codex-google-gemini-ai-coding-agent-security/)；[厂商资料入口](https://www.dryrun.security/resources)。
  - 引用章节: 第0章

- **Aikido Security / Veracode**, 2025-2026. AI代码安全性研究.
  - 引用章节: 第5章

- **Chroma Research, "Context Rot: How Increasing Input Tokens Impacts LLM Performance"**, 2025-07。研究增加上下文长度时的性能变化，不能用固定轮次直接诊断所有工具的上下文退化。[原文](https://www.trychroma.com/research/context-rot)。
  - 引用章节: 第4章

- **Gartner 2026年2月预测**: 关于客服岗位调整的预测，属于未来判断而非已经发生的事实；原始公告直达链接待补核。
  - 引用章节: 第8章

- **Klarna AI客服数据**, 官方新闻稿2024年2月 + Fast Company 2025年5月 (CEO承认"走太远了").
  - 引用章节: 第8章

---

## 4. 技术博客与文章 (Tech Blogs & Articles)

### 个人技术博客

- **Mitchell Hashimoto, "My AI Adoption Journey"**, 2026-02-05。AI采纳过程中的个人经验，讨论为Agent构建harness；不声称作者首次命名或独创Harness Engineering。[原文](https://mitchellh.com/writing/my-ai-adoption-journey)。
  - 引用章节: 第2章

- **Birgitta Böckeler, "Harness Engineering for Coding Agent Users"**, martinfowler.com, 2026-04-02。作者在早期memo基础上扩写的harness工程分析。[作者原文](https://martinfowler.com/articles/harness-engineering.html)。
  - 引用章节: 第8章

- **Addy Osmani, "Comprehension Debt"**, addyosmani.com, 2026年3月. 理解债务定义、逻辑漂移机制、"绿灯不代表正确，只代表一致".
  - 引用章节: 第5章, 第7章

- **Cassie Kozyrkov, "Harness Engineering: How to Supervise Code You Can't Read"**, 2026-03-05。监督AI代码、信任债务与代码反述思路。[作者Medium原文](https://kozyrkov.medium.com/harness-engineering-how-to-supervise-code-you-cant-read-71ebd05bfde7)（会员文章，已核对标题与作者，全文可能需订阅）。
  - 引用章节: 第5章

- **Phil Schmid, "Context Engineering for AI Agents: Part 2"**, 2025-12-04。上下文卸载、压缩、检索与隔离，以及工具空间管理；个案token规模不能当作所有工具的固定开销。[原文](https://www.philschmid.de/context-engineering-part-2)。
  - 引用章节: 第4章

- **Martin Fowler, "Strangler Fig Application"**, martinfowler.com. 遗留系统改造模式.
  - 引用章节: 第7章

- **Paul Duvall, "Sharing AI Development Rules Across Your Organization"**, paulmduvall.com, 2026.
  - 引用章节: 第7章

- **Vitthal Mirji, "Build the Harness, Not the Code"**, 2026。面向工程负责人的harness实践文章。[作者原文](https://vitthalmirji.com/2026/02/build-the-harness-not-the-code-a-staff/principal-engineers-guide-to-ai-agent-systems/)。
  - 引用章节: 第4章

- **Richard Porter, "Claude Code for Legacy Codebases: A Practitioner's Guide"**, 2026年1月.
  - 引用章节: 第7章

- **Agmis, "What We've Learned Refactoring Legacy Code with AI"**, 2026年2月.
  - 引用章节: 第7章

### 知乎

- **Andrej Karpathy, No Priors播客专访**, 2026年3月. "Jagged Intelligence"概念: AI能力在不同任务上呈锯齿状分布.
  - 引用章节: 第1章

- **Devymex Wang**, 知乎"如何评价王垠对AI编程的看法", 223赞, 2026年3月. 30年编程经验, 驾驭AI四个门槛.
  - 引用章节: 第0章

- **酱紫君**, 知乎同题回答, 1228赞+1628赞, 2026年. 信道论与贝叶斯分析框架, "双信源"模型.
  - 引用章节: 第8章

- **旷野**, 知乎同题回答, 381赞, 2026年. "向下懂两层向上懂一层"规则, Joel Spolsky抽象泄漏定律.
  - 引用章节: 第8章

- **Weyne Chen, "AI工程范式三次演化: Prompt Engineering -> Context Engineering -> Harness Engineering"**, 知乎, 2026年3月. Debug Agent三层递进踩坑记.
  - 引用章节: 第2章

- **Tw93, "你不知道的Claude Code"**, 知乎, 2026年3月. 上下文预算、MCP开销与会话交接的个人经验，具体占比随配置变化。
  - 引用章节: 第4章, 第6章

- **Li鱼鱼, "Claude Code最佳实践"**, 知乎, 2026年3月. 六层控制面架构、团队落地七步法、"常驻上下文更像缓存预算".
  - 引用章节: 第3章, 第4章

- **Grivn (浙大计算机硕士), "为什么你复刻不了Claude Code的体验"**, 知乎专栏, 2026年3月. 内生秩序密度、三圈层约束模型.
  - 引用章节: 第3章

- **程引 (快手工程师), "Claude Harness Engineering操作手册"**, 2026. 四大支柱SOP, 5条硬规则, "不怕AI犯错, 怕犯错后没有反馈".
  - 引用章节: 第3章, 第5章

- **夏凯文**, 知乎AI编程案例分享, 2026年3月. 推荐系统排序逻辑/客服流转系统排错案例.
  - 引用章节: 第0章, 第5章

- **唐英俊**, 知乎 (598赞), 2025年7月. 24000字需求文档让Cursor做项目, 49测试全绿但部署翻车, AI不修代码去改测试.
  - 引用章节: 第5章

- **孟健AI编程 (前腾讯T11/前字节3-1)**, 知乎, 2026年3月. 得物前端部门整建制解散事件分析.
  - 引用章节: 第0章

- **花宝宝**, 知乎"如何解决Agent编码屎山问题", 2026年3月. 1379关注/458099浏览. Agent局部最优全局随机.
  - 引用章节: 第2章

- **飞天红猪侠**, 知乎"如何看待坚持不用AI的'古法编程'？", 5644赞, 2026年3月.
  - 引用章节: 第6章

- **零一猴子**, 知乎"如何看待现阶段坚持不用AI的古法编程", 2025年. DDD与README工作流的个人实践，自报AI代码占比不作一般效率指标。
  - 引用章节: 第4章

- **Soulflare**, 知乎"AI时代程序员为什么不会消失", 2026年3月.
  - 引用章节: 第0章

- **绅士喵 (Linux优秀答主)**, 知乎Vibe Coding讨论, 153赞, 2026年3月.
  - 引用章节: 第0章

- **dbsx / "咋又要取名"**, 知乎, 2026年3月. "零熵悖论"讨论: 指令精确到零熵就等于自己编程.
  - 引用章节: 第2章

- **Kajian**, 知乎"OPC实践——上班族5个月4款产品盈利", 2026年3月.
  - 引用章节: 第8章

- **神笔工坊**, 知乎"你为什么恨AI？", 2026年. 编辑12年故事、"AI是一面镜子".
  - 引用章节: 第8章

- **zha zha / apple jobs**, 知乎, 2026年3月. 一线开发者对"从底层积累经验"路径断裂的讨论.
  - 引用章节: 第8章

- **匿名 (游戏行业项目主程)**, 知乎"如何理性解读Anthropic失业报告", 361赞, 2026年3月. 游戏行业AI替代链条.
  - 引用章节: 第0章

- **王勃**, 知乎专栏, 2026年3月. Vibe Coding到9步Planned工作流, Dijkstra EWD667理论框架.
  - 引用章节: 第0章

- **BaiFu (中国科大学生)**, MiroFish项目. 项目传播与融资的历史线索，实时Star及金额不在本轮核验范围。
  - 引用章节: 第0章

### 中文媒体

- **Jensen Huang, GTC 2026 Keynote + All-In Podcast**, 2026年3月. 工程师与AI投入关系的公开访谈类比，不当作实测效率或预算建议。 Yahoo Finance/CNBC/Fortune报道.
  - 引用章节: 第0章

- **Dario Amodei (Anthropic CEO)**, "People by WTF"播客 (Nikhil Kamath), 2026年2月. 执行加速后判断可能成为瓶颈的类比； 放射科医生悖论.
  - 引用章节: 第8章

- **陶哲轩**, YouTube + Dwarkesh Patel播客, 2026年3月. Claude Code在Lean中形式化"单例定律"; AI把理念生成成本降到接近零, 瓶颈转向验证.
  - 引用章节: 第0章, 第1章, 第5章, 第8章

- **爱范儿**, "大厂裁员裁到大动脉", 2026年3月. 亚马逊2023-2026累计裁员57,000+人.
  - 引用章节: 第0章

- **Fortune, "AI coding risks"**, Beatrice Nolan, 2026年3月18日. AI编码事故的媒体报道；具体事件、影响范围及当事方回应应分别核对。
  - 引用章节: 第0章, 第2章

- **TechCrunch, "Meta is having trouble with rogue AI agents"**, Amanda Silberling, 2026年3月. Meta内部AI Agent未授权发帖, Sev 1事故.
  - 引用章节: 第0章

- **极客公园**, "Vibe Coding是怎么'玩废'程序员的？", 2026年3月.
  - 引用章节: 第2章

- **阮一峰《科技爱好者周刊》第388期**, 读者留言, 2026年3月.
  - 引用章节: 第0章

- **孤独大脑 (公众号)**, "在'龙虾'和'草台班子'横行的日子里", 2026年3月. "AI是你自己的n次方"类比.
  - 引用章节: 第8章

- **得物技术, "AI编程能力边界探索: 基于Claude Code的Spec Coding项目实战"**, 阳凯, 2026年3月. Spec Coding的单项目实践，工时、代码量与提效自报数据不作行业均值。
  - 引用章节: 第2章, 第5章

- **得物技术SmartCode团队, "Claude Code使用感受"**, 2026年3月. 三窗口架构师/开发者工作流.
  - 引用章节: 第7章

- **OpenClaw安全风险事件与相关通告**, 2026。恶意Skill、凭证泄露与异常Token账单需分别核对具体事件，不能直接把它们串成未经证实的单一因果链。原始通告直达链接待补核。
  - 引用章节: 第3章

- **Summer Yue (@summerlyue)**, X/Twitter, 2026年2月. OpenClaw邮件Agent删除200封邮件. TechCrunch报道.
  - 引用章节: 第3章

- **Paul Conyngham mRNA癌症疫苗案例**, The Australian/NY Post/YouTube, 2026年3月.
  - 引用章节: 第8章

- **范冰,《价值百万的AI创业血泪史》**, 2025年Q3-Q4.
  - 引用章节: 第8章

- **北京语言大学2025年停招翻译专业**, 36氪; 蒙特雷国际研究院(MIIS)关停, 第一财经2025年8月.
  - 引用章节: 第8章

- **律师AI虚假判例**, Cronkite News, 2025年10月. 486起案件, 128名律师.
  - 引用章节: 第8章

### 英文技术社区

- **KatanaLarp, "Your LLM Doesn't Write Correct Code. It Writes Plausible Code"**, blog.katanaquant.com, 2026年3月. AI生成SQLite实现的性能个案；具体差距受查询类型、硬件、版本和基线实现影响，不直接代表AI代码的一般性能。
  - 引用章节: 第1章, 第5章

- **Stack Overflow, "AI can 10x developers...in creating tech debt"**, 官方博客.
  - 引用章节: 第0章

- **Cory Doctorow, "Maximally Codelike Bugs"**, Pluralistic, 2025.
  - 引用章节: 第1章

- **DEV Community, "I Ran 23 AI Agents Simultaneously on One Codebase Overnight"**, 2026.
  - 引用章节: 第7章

- **Dev Genius, "I Let AI Refactor Our Legacy Codebase. It Created 127 New Bugs"**, 2026。个人复盘，不是经过独立验证的对照实验，标题数字不应推广为AI重构的一般规律。
  - 引用章节: 第7章

- **Vitalii Petrenko**, DEV Community, 2026. 安全审查清单.
  - 引用章节: 第5章

- **Sanity Engineering Blog, "First attempt will be 95% garbage"**, 2026.
  - 引用章节: 第7章

- **incident.io, "Shipping faster with Claude Code and Git Worktrees"**, 2026.
  - 引用章节: 第7章

- **DolbyUUU, "关于Tool Use的Agent工程师面试题目"**, 知乎, 2026年3月. 四层12题完整技术栈.
  - 引用章节: 附录B

- **Zgicc, "CLAUDE.md安全约束对AI代码质量的影响"**, 2026。规则约束实验的历史查找线索；实验设置与原始来源未完成核验，暂不列提升比例。
  - 引用章节: 第3章

- **艾姆安格瑞, "软件工程将死于银弹"**, 知乎专栏, 2026年2月. "显式复杂度->黑箱复杂度"概念.
  - 引用章节: 第5章, 附录A

- **Todd Saunders (Broadlume)**, 管道工程师零代码用Claude Code做TakeOff Trak产品, 2026. 跨领域开发产品的个案，成效需按原始报道的场景解释。
  - 引用章节: 第8章

### 行业访谈与作者一手材料

- **作者面试访谈**, 2026年3月. 某AI公司CTO (不具名); 某AI公司CEO (不具名, "共识知识vs规范性知识"分类框架).
  - 引用章节: 第0章, 第1章

- **作者与量化投资从业者交流**, 2026年初. AI将沪深指数数据套用1997年亚洲金融危机数据.
  - 引用章节: 第1章

- **开发者使用Opus 4.6 + AutoResearch模式写CUDA GPU算子**, 实践报告, 2026年3月. GPU算子优化及评测约束的个案线索；性能优越性须以可复现实验为准。
  - 引用章节: 第1章, 第5章, 第7章

- **S053 头部AI编程工具自动校准机制调研**, 2026年3月. 校准机制的历史调研；工具实际机制须以对应版本的官方说明和运行证据为准。
  - 引用章节: 第6章

- **ML工程师6个生产项目迁移经验**, "自主!=自动".
  - 引用章节: 第5章

---

## 5. 开源项目 (Open Source)

- **RIPER-5**, GitHub: NeekChaw/RIPER-5 及 johnpeterman72/CursorRIPER. 社区的分阶段AI协作规则示例，具体模式和使用方式以项目版本为准。 https://github.com/NeekChaw/RIPER-5
  - 引用章节: 第2章, 第7章

- **BMAD Method**, GitHub。基于角色与工作流的开发方法；角色数量和具体格式随版本变化。[项目](https://github.com/bmad-code-org/BMAD-METHOD)。
  - 引用章节: 第2章

- **Garry Tan, "gstack"**, 2026。角色隔离、验证自动化和失败升级的个人实践项目；自报代码量不等于质量或行业生产率。[项目](https://github.com/garrytan/gstack)。
  - 引用章节: 第7章

---

## 6. 书籍 (Books)

- **Kent Beck,《Test-Driven Development: By Example》**, 2003. TDD方法论系统化.
  - 引用章节: 第5章

- **Jim Collins,《Good to Great》(中文版《从优秀到卓越》)**, 2001. "技术本身不是推动力，只有服务于清晰概念和目标时才是".
  - 引用章节: 第6章

- **范冰,《价值百万的AI创业血泪史》**, 2025年Q3-Q4.
  - 引用章节: 第8章

---

## 7. 其他 (Other)

- **阿姆达尔定律 (Amdahl's Law)**. 系统整体提速受限于无法加速的部分. 即使95%加速到无穷快, 整体最多快20倍.
  - 引用章节: 第8章

- **Dan North**, BDD (Behavior-Driven Development) 概念提出者, 2006. Given/When/Then格式.
  - 引用章节: 第5章

- **Token定义**: 模型处理文本最小单位. 英文约4字符=1 token, 中文约1.5-2字符=1 token.
  - 引用章节: 第1章

- **Agent输入输出比、KV Cache与上下文退化**。实际比例、缓存收益与触发条件取决于模型、工具和任务，不保留固定成本倍数。
  - 引用章节: 第1章

- **失败后的Git恢复工作流**。先保留可恢复状态，再按失败原因决定修复、回滚或重新规划，不把固定失败次数视为通用规则。
  - 引用章节: 第5章

- **代码熵管理概念**.
  - 引用章节: 第5章

- **附录D工具资料说明**。工具能力、名称、权限机制和费用会随版本变化；使用前核对官方文档。本配套不把写作时的用户数、份额或报价作为当前选型依据。
  - 引用章节: 附录D

---

*索引建立于2026-04；本轮核对于2026-10-30。未逐条重新核实全部历史来源，未获得直达链接的条目保留为查找线索。*
