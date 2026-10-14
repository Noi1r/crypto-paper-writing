# 密码学论文写作指南

统一入口：`skills/cpw-write/SKILL.md`；各章节写作指南位于 `skills/cpw-write/references/sections/`，
协作润色、领域语言表达、从素材起草与参考论文分析指南位于 `skills/cpw-write/references/`，按当前任务按需读取。
仓库内示例均为合成材料；真实论文的草稿、实验日志和风格记录保存在各自的论文项目中。

## 核心原则

1. **先立论据主线，再定行文结构。** 动笔前先厘清四个支点：具体研究问题与设定、前人方案在此遇到的核心技术阻碍（Obstacle）、破局的关键观察或机制（Mechanism），以及在明确假设下成立的结果（Result）。段落数、贡献条数与图表数量完全由内容决定，不套用机械模板。
2. **先调结构与逻辑链，再磨字句。** 修改已有稿件时，按“段落职责与位置 $\to$ 缺失前提与推理衔接 $\to$ 句内信息流 $\to$ 用词与记号”的顺序推进。只有当删减保留了必要的动机、适用条件与因果链条时，变短才是改进。
3. **写清“怎么做到（How）”，而不止于“做到了（That）”。** 无论是引言贡献、技术概览还是实验分析，都要交代清楚背后的结构机制、代数性质或协议改动，避免用“novel / efficient / tight”等空泛形容词代替技术解释。
4. **润色绝不暗中放大技术主张。** 定理假设、量词顺序、敌手能力、概率空间、安全模型、比较基准和证据状态必须严丝合缝。语言修饰不能修补缺失的归约步骤，模型运算量计数也不能直接等同于实测运行时间。

## 全文参考结构

| 部分 | 读者需要获得什么 | 组织与位置弹性 |
|---|---|---|
| Abstract | 问题设定、核心机制、主要结果及成立条件 | 按内容与会场要求分为一段或两段 |
| Introduction | 研究动机、前人瓶颈、本文破局思路与核心贡献 | 贡献可写成列表或自然段；始终交代最直接的竞争工作 |
| Technical Overview | 核心困难、直觉观察及各技术模块的咬合关系 | 可作为引言子节，也可独立成节或置于必要定义之后 |
| Preliminaries | 后文实际用到的记号、安全模型、定义与已有工具 | 较长的新问题定义或安全模型可独立成节 |
| Main Technical Content | 协议、构造、算法或核心理论推导 | 按逻辑依赖拆分排序；明确区分继承自前人的步骤与本文改动 |
| Correctness / Security / Analysis | 性质陈述、证明思路、具体安全估计与代价分析 | 可紧随对应构造，也可独立成节 |
| Evaluation | 参数对比、理论代价或实测数据如何回答研究问题 | 以核心观察（Observation）领起段落，交代开销与劣势区间 |
| Related Work | 按技术维度梳理相关工作及与本文的精确边界 | 可前置建立背景，也可后置利用正文记号做精细对比 |
| Conclusion | 结果意义、核心取舍（Trade-off）或开放问题 | 若会场允许且无额外综合价值，可省略 |
| References / Appendix | 经核实的参考文献与详细证明、补充数据 | 严格遵循目标会场对附录页数与审稿义务的规定 |

## 领域语言与清晰表达（初稿与润色通用）

详见 `skills/cpw-write/references/field-language-and-clarity.md` 与 `skills/cpw-write/references/collaborative-polishing.md`：

- **技术名词锁定定义，普通叙述使用具象动词。**
  - 对形式化对象（如 `witness`、`commitment`、`random oracle`、`simulator`、`evaluation key`），全篇保持唯一名称；切忌为了“避免重复”而在相邻句子里把 `witness` 换成 `secret evidence` 或 `credential`——在数学与密码学写作中，换词意味着换了对象。
  - 普通叙述优先用直接动作词（`computes`、`samples`、`sends`、`checks`、`aborts`、`bounds`、`reduces`、`interpolates`），清理抽象名词堆叠（把 *"performs the computation of"* 改为 *"computes"*）和模糊粘合动词（如用 *"allows public verification"* 代替空泛的 *"retains public verifiability"* 或 *"leverages ... to facilitate"*）。
- **句内信息流遵循“由已知到未知（Given-before-New）”。**
  - 句子开头优先放置读者已熟悉的上下文、前文刚引入的对象或当前步骤的前提条件，把新的技术洞察、复杂度界或关键改动放在句末重心位置；避免用长达二十多个词的抽象名词短语充当主语。
  - 消除句首悬空的指代词（把裸露的 `This shows...`、`It ensures...` 明确为 `This degree bound shows...`、`The MAC check ensures...`）。
- **数学符号与英文语法自然嵌合。**
  - 绝不用裸露的数学符号或数字作为句首第一个词（用 `"The polynomial $f(X)$ has degree..."` 代替 `"$f(X)$ has degree..."`）。
  - 首次引入符号时配上类别名词（如 `"Let $d$ be the ring dimension and $\mathbf{c} \in \mathbb{Z}_q^n$ the challenge vector"`），减少读者回翻查记号的负担。
  - 独立成行的公式（Displayed equations）仍是句子的语法成分，需用完整的引导分句（加冒号）或谓语动词自然衔接，并标明句末标点；紧随公式解释其物理或代数含义。
- **中译英与中式学术句式调优。**
  - **化“话题链流水句”为主谓分明的英文句式：** 将 *"Regarding the bootstrapping step, by introducing sparse packing, it makes the key-switching cost significantly reduced"* 改写为主语明确、动作直接的句子：*"Our sparse packing method reduces the key-switching cost during bootstrapping from $O(N)$ to $O(\sqrt{N})$ automorphisms."*
  - **消除垂悬分词与无主语被动句：** 将 *"Utilizing the LWE assumption, the security is proved"* 改为明确主体的 *"Under the LWE assumption, Theorem 3 establishes IND-CPA security"*。
  - **校准跨语言主张强度：** 中文草稿常见的“极大地提升了”“彻底解决了”，在英文中应转化为具体的渐近界、实测倍数或形式化性质，切勿直译为空洞的最高级。

## 新论文规划与从研究材料起草

1. **研读少量高价值参考论文（`writing-from-related-work.md`）：**
   - 区分两类参考对象：**技术最接近的前作**（决定必须交代哪些背景、定义与对比基准）和**贡献形态相近、写法清晰的范文**（帮助设计技术概览的拆解节奏与符号密度）。
   - 阅读对应正文小节而非只看摘要，记录哪些结构选择适合当前论文、哪些因问题或篇幅不同需要调整。
2. **从研究材料尽早写出完整正文（`drafting-from-materials.md`）：**
   - 先用简短几句话串起“具体问题 $\to$ 前人阻碍 $\to$ 核心观察/机制 $\to$ 条件化结论”的主线。
   - 对解释次序尚不确定的难点小节，先列出读者进入本节时已知什么、离开时需理解什么，以及中间按依赖排序的桥梁步骤。
   - 尽早交付核心小节（如 Technical Overview、Introduction 或核心构造）的完整段落，用真实正文校准语气、深度与记号；缺失的实验数据或待查引文明白标出，绝不编造占位数字。

## 协作润色与逐段对照册

- **局部润色直接上手：** 修改单段或单节时，直接读取当前稿件与上下文即可开展，无需为此初始化全套项目台账（`STATE.md` / `EVIDENCE.md`）或建立个人风格档案（`STYLE.md` 仅在作者明确要求提炼个人风格时使用）。
- **逐段对照册（`review-comparison.md`）：** 当审阅产生多处候选改写、适合作者异步集中批阅时，可询问是否生成逐段对照册（以稳定的 `C1, C2, ...` 编号展示灰色原文、红色改写方案、位置及取舍理由）。对照册使用独立预览副本，不直接覆盖原稿。

## 审阅与核验边界

`cpw-review` 根据自然语言请求自动匹配审阅深度（表达与可读性、章节结构、技术主张与证据一致性、投稿合规准备），各关注点可自由组合：

- 每条审阅意见明确指出具体位置、造成理解困难或技术漏洞的原因、证据支撑以及相称的改写建议；严格区分**已确认错误**、**待核实疑点**、**结构取舍选项**与**纯风格偏好**。
- 涉及数值修改时核对原始日志或表格；若项目启用了 `EVIDENCE.md`，同步维护 `\ev{E1}` 链接并运行 `make -C paper audit`（详见 `docs/evidence-audit.md`）。
