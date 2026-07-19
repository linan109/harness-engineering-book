# CIVR框架全景图 (Chapter 8, Section 8.4)

全书核心CIVR框架的思维导图，中心为"Harness Engineering"，四个分支为约束、告知、验证、校准，每个分支展示关键子概念。作为读者合上书本前最后的记忆定格。

![CIVR框架全景图](civr-panorama.svg)

## Mermaid 源码

```mermaid
mindmap
  root((Harness<br/>Engineering<br/>驾驭工程))
    C 约束 Constrain
      权限分级
        文件级读写控制
        命令执行白名单
        危险操作需确认
      工具裁剪
        砍掉不必要的工具
        工具越少准确率越高
        Vercel砍80%工具案例
      范围锁定
        限定可修改的文件/目录
        约束改动范围
        AutoResearch单文件夹约束
      对抗陷阱
        ⑧ Toolbox Paradox
    I 告知 Inform
      上下文工程
        CLAUDE.md/Rules文件
        渐进式加载
        Push vs Pull两种机制
      项目地图
        架构决策记录
        模块依赖关系
        历史包袱说明
      知识注入
        隐性知识显性化
        负面上下文（不要做什么）
        版本时效标注
      对抗陷阱
        ② The Unsaid
        ③ Frozen in Time
        ⑤ Context Rot
        ⑥ Goldfish Memory
    V 验证 Verify
      四层验证
        能跑（编译通过）
        做对（逻辑正确）
        性能（不是灾难）
        安全（无隐蔽漏洞）
      双翻译
        AI代码→人类解释
        交叉比对发现偏差
      Spec驱动
        自然语言定义"什么算对"
        验证前置于实现
      TDD循环
        RED：人写测试
        GREEN：AI写实现
        REFACTOR：AI重构+人审查
      对抗陷阱
        ① Almost Right
        ④ The Yes-Man
        ⑦ Error Snowball
    R 校准 Redirect
      诊断三层次
        需求层（方向错了）
        实现层（做法错了）
        表达层（没说清楚）
      信号识别
        三次相同反馈无改善
        复杂度持续上升
        AI开始编造解释
      破解策略
        开新对话（重置上下文）
        换模型（不同视角）
        自己动手（人工接管）
      对抗陷阱
        ⑤ Context Rot
        ⑦ Error Snowball
```

## CIVR与能力成长的飞轮

```mermaid
graph LR
    C["C 约束<br/>练系统思维"] --> I["I 告知<br/>练领域知识"]
    I --> V["V 验证<br/>练工程判断力"]
    V --> R["R 校准<br/>三种能力综合"]
    R --> C
    
    C -.->|"画边界 → 理解模块依赖"| 成长["能力<br/>提升"]
    I -.->|"写上下文 → 暴露知识盲区"| 成长
    V -.->|"审AI代码 → 高密度Review"| 成长
    R -.->|"定位偏差 → 综合判断训练"| 成长
    
    成长 -->|"下一轮约束更精确"| C

    style 成长 fill:#69db7c,color:#333
```

## 核心公式

**结果 = LLM x Agent架构 x 你的驾驭方式**

CIVR循环同时产出两样东西：**代码**交付给项目，**能力**留在你身上。
