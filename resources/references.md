# 《驾驭AI编程》参考资源汇总

> All references cited in the book, organized by category. Entries appearing in multiple chapters list all chapters where cited.

---

## 1. 学术论文 (Academic Papers)

- **Liu et al., "Lost in the Middle: How Language Models Use Long Contexts"**, Stanford/TACL, 2023-2024. 实验证明LLM对长上下文中间部分的信息利用率显著低于首尾部分。https://arxiv.org/abs/2307.03172
  - 引用章节: 第1章, 第4章

- **Arditi et al., "Refusal in Language Models Is Mediated by a Single Direction"**, arXiv:2406.11717, 2024. 模型拒答行为可用一个线性方向表征，移除后安全对齐即失效。https://arxiv.org/abs/2406.11717
  - 引用章节: 第1章

- **Siegel et al., "CORE-Bench: Fostering Credibility of Published Research Through a Computational Reproducibility Agent Benchmark"**, Princeton University, arXiv:2409.11363, 2024. Claude Opus + 通用scaffold = 51%, Claude Opus + 专用harness = 78%. HAL排行榜: hal.cs.princeton.edu/corebench_hard https://arxiv.org/abs/2409.11363
  - 引用章节: 第2章

- **Anthropic, "How AI Assistance Affects Skill Formation"**, arXiv:2601.20245, 2026. 52名程序员实验，6种用户画像。委托式使用<40%理解度, 探究式>65%. AI组报错平均1次 vs 手动组3次，考试分数低17%. https://arxiv.org/abs/2601.20245
  - 引用章节: 第2章, 第5章, 第7章, 第8章

- **Cheng, Lee, Khadpe, "Sycophantic AI Can Undermine Human Judgment"**, Science, 2026. DOI: 10.1126/science.aec8352. 11个LLM比人类共识多49%肯定率，2405人实验。
  - 引用章节: 第1章

- **Nghi D. Q. Bui, "Terminal-Native AI Coding Agent Architecture"**, arXiv:2603.05344, 2026. 四层架构模型、扩展ReAct六阶段、Scaffolding vs Harness学术定义。https://arxiv.org/abs/2603.05344
  - 引用章节: 第2章, 附录B

- **Xin Xia et al., "Measuring Program Comprehension: A Large-Scale Field Study with Professionals"**, IEEE Transactions on Software Engineering, Vol. 44, No. 10, 2018. 78名专业开发者、3148工作小时实地研究。
  - 引用章节: 第7章

- **Prithvi Rajasekaran, "Harness Design for Long-Running Application Development"**, Anthropic Labs, 2026年3月24日. 三Agent架构、Self-Evaluation Bias、Context Anxiety、V1->V2简化方法论。
  - 引用章节: 第1章, 第2章, 第5章

- **Harvard Business School, "Who is AI Displacing?"**, 覆盖6200万劳动者的研究, 2025 (NBER Working Paper, 2026).
  - 引用章节: 第0章, 第8章

---

## 2. 官方文档与博客 (Official Docs & Blogs)

### Anthropic

- **Anthropic, Claude Research多Agent生产复盘**, 2025-2026. 5个生产级坑、上下文截断时计划消失、原型1周生产3月、token消耗15倍、36.9%状态不一致。
  - 引用章节: 第1章, 第4章, 第7章

- **Anthropic, "Claude Code: Best practices for agentic coding"**, 2025. Rules + Skills双轨制、工具数量建议、上下文管理原则。https://docs.anthropic.com/en/docs/claude-code/best-practices
  - 引用章节: 第4章

- **Anthropic, "Prompt Caching"**, docs.anthropic.com. Claude Sonnet缓存价$0.30 vs 正常价$3.00/百万token.
  - 引用章节: 第4章

- **Anthropic, Claude Code开源代码及技术博客**. 子agent设计、/compact压缩流程、100:1输入输出比、ripgrep检索实现。
  - 引用章节: 第1章, 第4章

- **Anthropic用户调研**, 2026. 80508名用户, 33%认为AI帮助学习, 16%学生注意到认知能力萎缩, 19%反映AI反而增加工作量。
  - 引用章节: 第5章, 第8章

- **Anthropic Engineering Blog, C编译器项目实录**, 2026. 2000次Claude Code会话、10万行C代码。
  - 引用章节: 第5章

### OpenAI / Kiro / AWS

- **Kiro生产事故报告 (AWS Cost Explorer)**, CNBC/FT/The Register, 2025-2026. Kiro在自主模式下删除AWS Cost Explorer生产环境，13小时宕机。
  - 引用章节: 第3章

### Stripe

- **Stripe Engineering Blog, Minions系统**, 2026. 每周1300+AI PR全人类review, 2次CI重试上限, 300万+自动化测试, Blueprints混合编排, 500 MCP.
  - 引用章节: 第3章, 第5章, 第7章

### Vercel

- **Vercel, "How We Built d0"**, 2026. 15工具->2工具、成功率80%->100%、token消耗降37%.
  - 引用章节: 第3章

### Google

- **Google DORA Report 2025**, dora.dev. AI使PR大小+154%, review时间+91%, bug率+9%.
  - 引用章节: 第0章, 第7章

### Shopify

- **Shopify CEO Tobi Lutke全员备忘录**, 2025年4月. 3000+ Cursor许可、不设token预算上限、1000实习生扩招计划。Business Insider/The Verge/Shopify Engineering Blog.
  - 引用章节: 第0章

### Airbnb

- **Airbnb Engineering Blog, Charles Covey-Brandt**, 2025年3月; Szczepan Faber, DPE Summit, 2025年9月. 3500测试文件6周迁移, Sample-Tune-Sweep方法论, 重试循环。
  - 引用章节: 第5章, 第8章

### Apple

- **9to5Mac, "Apple pushing back on vibe coding iPhone apps"**, 2026年3月. 苹果引用App Store Guideline 2.5.2限制Replit/Vibecode等Vibe Coding应用上架。
  - 引用章节: 第2章

### Stanford

- **Stanford HAI AI Index 2025报告**, Technical Performance章节. SWE-bench解决率2023年4.4%->2024年71.7%.
  - 引用章节: 第1章

### METR

- **METR, "Task-Completion Time Horizons"**, metr.org/time-horizons, 2026年1月TH1.1版. 228个任务, GPT-4~4小时, Claude Opus 4.6~719小时, 每7个月翻倍.
  - 引用章节: 第1章

### Stack Overflow

- **Stack Overflow 2025 Developer Survey** (48945名开发者). GitHub Copilot 67.9%, Claude Code 40.8%. AI采用率84%, 信任度从43%降至29%.
  - 引用章节: 第0章, 第1章, 第5章

### LangChain

- **LangChain Blog, "The Anatomy of an Agent's Harness"**, 2026. "Agent = Model + Harness". Terminal Bench 2.0: 同模型只改Harness, 排名Top 30->Top 5.
  - 引用章节: 第2章

### Monday.com

- **Monday.com联合CEO Eran Zinman**, 20VC播客访谈, 2026年3月.
  - 引用章节: 第8章

### Manus

- **Manus, "Context Engineering for AI Agents: Lessons from Building Manus"**, manus.im.
  - 引用章节: 第4章

### DX

- **DX (getdx.com), 400家公司纵向追踪**, 2024.11-2026.02. AI工具使用量+65%, PR交付量仅+9.97%.
  - 引用章节: 第7章

---

## 3. 行业报告与数据 (Industry Reports & Data)

- **Faros AI, "The AI Productivity Paradox Research Report"**, 2025. 基于10,000+开发者遥测: PR审查时间+91%, PR体积+154%, bug率+9%. (注: Faros AI遥测数据, 非DORA原始报告)
  - 引用章节: 第0章, 第5章, 第7章

- **Apiiro, "4x Velocity, 10x Vulnerabilities: AI Coding Assistants Are Shipping More Risks"**, Itay Nussbaum, 2025年9月. 语法错误减76%, 特权提升+322%, 架构缺陷+153%.
  - 引用章节: 第1章

- **CodeRabbit, "State of AI vs Human Code Generation Report"**, David Loker, 2025年12月. 470个开源PR, 安全漏洞2.74倍、逻辑错误+75%.
  - 引用章节: 第0章

- **Harness, "State of Software Delivery 2025"**. 67%的开发者报告debug AI代码的时间超过自己写.
  - 引用章节: 第0章

- **Forbes/Workday研究**, 2026年3月. 近40%预期生产力增益被修复AI低质量输出消耗.
  - 引用章节: 第5章

- **Oasis Security, ClawHub安全扫描报告**, 2026年初. 近4000个Skill, 恶意Skill案例. ClawJacked漏洞: 恶意网页通过WebSocket连接本机Agent.
  - 引用章节: 第0章

- **IEEE Spectrum / SignalFire / LeadDev / Stanford 就业数据综合**. 美国程序员就业降27.5%, 初级招聘降25%, 54%管理者计划因AI减少初级招聘.
  - 引用章节: 第0章

- **DryRun Security, "AI coding agents keep repeating decade-old security mistakes"**, Help Net Security, 2026年3月. 30个PR/143个安全问题/87%含漏洞.
  - 引用章节: 第0章

- **Aikido Security / Veracode**, 2025-2026. AI代码安全性研究.
  - 引用章节: 第5章

- **Chroma Research, "Context Rot"**, 2026. 上下文腐烂研究.
  - 引用章节: 第4章

- **Gartner 2026年2月预测**: 50%因AI裁减客服的公司将在2027年前重新招聘.
  - 引用章节: 第8章

- **Klarna AI客服数据**, 官方新闻稿2024年2月 + Fast Company 2025年5月 (CEO承认"走太远了").
  - 引用章节: 第8章

---

## 4. 技术博客与文章 (Tech Blogs & Articles)

### 个人技术博客

- **Mitchell Hashimoto, "My AI Adoption Journey"**, mitchellh.com, 2026年2月. HashiCorp联创/Terraform创造者. 首次命名"Harness Engineering", 六阶段AI采纳旅程. https://mitchellh.com/writing/my-ai-adoption-journey
  - 引用章节: 第2章

- **Birgitta Bockeler, "Exploring Generative AI: Harness Engineering"**, martinfowler.com, 2026. "学徒缺口"概念. https://martinfowler.com/articles/exploring-gen-ai.html
  - 引用章节: 第8章

- **Addy Osmani, "Comprehension Debt"**, addyosmani.com, 2026年3月. 理解债务定义、逻辑漂移机制、"绿灯不代表正确，只代表一致".
  - 引用章节: 第5章, 第7章

- **Cassie Kozyrkov, "Harness Engineering: How to Supervise Code You Can't Read"**, decision.substack.com, 2026年3月. 信任债务概念、AI自信程度与准确度脱钩.
  - 引用章节: 第5章

- **Phil Schmid, "Context Engineering Part 2"**, philschmid.de. 47000 token schema vs 400 token CLI封装.
  - 引用章节: 第4章

- **Martin Fowler, "Strangler Fig Application"**, martinfowler.com. 遗留系统改造模式.
  - 引用章节: 第7章

- **Paul Duvall, "Sharing AI Development Rules Across Your Organization"**, paulmduvall.com, 2026.
  - 引用章节: 第7章

- **Vitthal Mirji, "Build the Harness, Not the Code"**, 2026. Glean Skill准确度案例、8周实施蓝图.
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

- **Tw93, "你不知道的Claude Code"**, 知乎, 2026年3月. 200K上下文实际可用空间, MCP隐形开销12.5%, HANDOFF.md会话交接.
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

- **零一猴子**, 知乎"如何看待现阶段坚持不用AI的古法编程", 2025年. DDD+README工作流, 60%代码AI生成.
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

- **BaiFu (中国科大学生)**, MiroFish项目. 10天登顶GitHub Trending, 5.7k Star, 陈天桥注资3000万.
  - 引用章节: 第0章

### 中文媒体

- **Jensen Huang, GTC 2026 Keynote + All-In Podcast**, 2026年3月. "$500K工程师+$250K token=10倍放大". Yahoo Finance/CNBC/Fortune报道.
  - 引用章节: 第0章

- **Dario Amodei (Anthropic CEO)**, "People by WTF"播客 (Nikhil Kamath), 2026年2月. 5%判断+95% AI执行=20倍效率; 放射科医生悖论.
  - 引用章节: 第8章

- **陶哲轩**, YouTube + Dwarkesh Patel播客, 2026年3月. Claude Code在Lean中形式化"单例定律"; AI把理念生成成本降到接近零, 瓶颈转向验证.
  - 引用章节: 第0章, 第1章, 第5章, 第8章

- **爱范儿**, "大厂裁员裁到大动脉", 2026年3月. 亚马逊2023-2026累计裁员57,000+人.
  - 引用章节: 第0章

- **Fortune, "AI coding risks"**, Beatrice Nolan, 2026年3月18日. Claude Code删库案例、Amazon宕机6小时.
  - 引用章节: 第0章, 第2章

- **TechCrunch, "Meta is having trouble with rogue AI agents"**, Amanda Silberling, 2026年3月. Meta内部AI Agent未授权发帖, Sev 1事故.
  - 引用章节: 第0章

- **极客公园**, "Vibe Coding是怎么'玩废'程序员的？", 2026年3月.
  - 引用章节: 第2章

- **阮一峰《科技爱好者周刊》第388期**, 读者留言, 2026年3月.
  - 引用章节: 第0章

- **孤独大脑 (公众号)**, "在'龙虾'和'草台班子'横行的日子里", 2026年3月. "AI是你自己的n次方"类比.
  - 引用章节: 第8章

- **得物技术, "AI编程能力边界探索: 基于Claude Code的Spec Coding项目实战"**, 阳凯, 2026年3月. 10天/217指令/25546行代码/提效36%.
  - 引用章节: 第2章, 第5章

- **得物技术SmartCode团队, "Claude Code使用感受"**, 2026年3月. 三窗口架构师/开发者工作流.
  - 引用章节: 第7章

- **深圳程序员OpenClaw安全事件**, 2026年3月. 恶意Skill窃取API密钥, 1.2万元Token账单. CNCERT安全风险通告.
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

- **KatanaLarp, "Your LLM Doesn't Write Correct Code. It Writes Plausible Code"**, blog.katanaquant.com, 2026年3月. 58万行AI生成Rust代码SQLite, 主键查询慢20171倍.
  - 引用章节: 第1章, 第5章

- **Stack Overflow, "AI can 10x developers...in creating tech debt"**, 官方博客.
  - 引用章节: 第0章

- **Cory Doctorow, "Maximally Codelike Bugs"**, Pluralistic, 2025.
  - 引用章节: 第1章

- **DEV Community, "I Ran 23 AI Agents Simultaneously on One Codebase Overnight"**, 2026.
  - 引用章节: 第7章

- **Dev Genius, "I Let AI Refactor Our Legacy Codebase. It Created 127 New Bugs"**, 2026年2月. 4小时AI重构->3周回滚修复, 损失$76K.
  - 引用章节: 第7章

- **Vitalii Petrenko**, DEV Community, 2026. 安全审查清单.
  - 引用章节: 第5章

- **Sanity Engineering Blog, "First attempt will be 95% garbage"**, 2026.
  - 引用章节: 第7章

- **incident.io, "Shipping faster with Claude Code and Git Worktrees"**, 2026.
  - 引用章节: 第7章

- **DolbyUUU, "关于Tool Use的Agent工程师面试题目"**, 知乎, 2026年3月. 四层12题完整技术栈.
  - 引用章节: 附录B

- **Zgicc, "CLAUDE.md安全约束对AI代码质量的影响"**, 2026. 30行约束Pass@1提升188%.
  - 引用章节: 第3章

- **艾姆安格瑞, "软件工程将死于银弹"**, 知乎专栏, 2026年2月. "显式复杂度->黑箱复杂度"概念.
  - 引用章节: 第5章, 附录A

- **Todd Saunders (Broadlume)**, 管道工程师零代码用Claude Code做TakeOff Trak产品, 2026. 8周完成, 核心流程10分钟->60秒.
  - 引用章节: 第8章

### 行业访谈与作者一手材料

- **作者面试访谈**, 2026年3月. 某AI公司CTO (不具名); 某AI公司CEO (不具名, "共识知识vs规范性知识"分类框架).
  - 引用章节: 第0章, 第1章

- **作者与量化投资从业者交流**, 2026年初. AI将沪深指数数据套用1997年亚洲金融危机数据.
  - 引用章节: 第1章

- **开发者使用Opus 4.6 + AutoResearch模式写CUDA GPU算子**, 实践报告, 2026年3月. 性能超越开源社区, AI偷改评测case.
  - 引用章节: 第1章, 第5章, 第7章

- **S053 头部AI编程工具自动校准机制调研**, 2026年3月. Codex RL训练循环、Cursor 3次即停、Devin双Agent对抗、Claude Code三阶段循环.
  - 引用章节: 第6章

- **ML工程师6个生产项目迁移经验**, "自主!=自动".
  - 引用章节: 第5章

---

## 5. 开源项目 (Open Source)

- **RIPER-5**, GitHub: NeekChaw/RIPER-5 及 johnpeterman72/CursorRIPER. Cursor社区最流行的AI约束规则框架, 5模式协议. https://github.com/NeekChaw/RIPER-5
  - 引用章节: 第2章, 第7章

- **BMAD Method (Build Modular AI-Driven)**, GitHub. 12个专家角色, 每个角色有对应的Skill文件和工作流.
  - 引用章节: 第2章

- **Garry Tan, "gstack"**, GitHub, 2026年3月. 15个专精Skill + 6个Power Tool, 60天600K行代码. https://github.com/garrytan/gstack
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

- **Agent平均输入输出比100:1; KV Cache命中vs未命中成本差10倍; Context Rot在远低于最大长度时出现**.
  - 引用章节: 第1章

- **"3次失败即回滚"和"存档两连"Git工作流**, Claude Code社区实践总结.
  - 引用章节: 第5章

- **代码熵管理概念**.
  - 引用章节: 第5章

- **附录D数据说明**: 产品数据来自各公司官方披露、GitHub Octoverse、Stack Overflow Developer Survey 2025及行业分析报告, 截至2026年3月.
  - 引用章节: 附录D

---

*Generated: 2026-04-04. Total unique references: ~100+. Covers chapters 0-8 and appendices A-E.*
