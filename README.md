# crypto-paper-writing

面向 Codex 的密码学与安全论文写作工具箱，帮助作者把已有研究结果组织成清楚、准确的论文。
包含文献与引用核对、全文规划、章节写作、语言润色、图表、模拟审稿、rebuttal 和投稿准备。

文章写作统一使用 `$cpw-write`。它按当前任务读取内部指南，处理全文规划、摘要、
逐段润色、技术概览、评估和相关工作。文献、图表、审稿和投稿准备保留独立入口。

新论文的写作路径：

**梳理已有结果 → 阅读合适的相关论文 → 拟定结构与表达方案 → 撰写关键部分 → 逐节完善 → 按需审稿与投稿准备**

工具箱提供 Codex 技能和辅助脚本。论文的技术主张由作者决定，证明、实验和原始数据来自论文项目。
具体边界见 [SPEC.md](SPEC.md)。

## 快速开始

### 安装到本机

在工具箱仓库中运行：

```bash
./install.sh --user
```

这会在 `~/.agents/skills/` 中注册当前版本的入口和工具技能，链接到此检出目录，并保留用户自建的同名技能。
本机安装会随这个检出目录中的内容更新；请保留该目录。下一轮 Codex 对话即可尝试调用，
若尚未显示则重开会话。新论文可这样初始化：

```text
$cpw-init 请在 /path/to/my-paper 初始化论文项目。
```

### 安装到论文项目

在工具箱仓库中运行，目标目录应位于工具箱之外：

```bash
./install.sh /path/to/my-paper
cd /path/to/my-paper
```

安装器会准备项目记录和 LNCS 稿件骨架，将工具资源复制到 `.paper-writing/`，
并在 `.agents/skills/` 下建立技能目录链接。7 个 `$cpw-*` 入口覆盖不同工作流程，
其中文章写作统一由 `$cpw-write` 处理。默认稿件是 `paper/main.tex`，参考文献是 `paper/refs.bib`。

`.agents/skills/` 和技能目录链接遵循 [Codex 的官方技能发现约定](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。
这些技能属于当前论文项目，不会写入个人全局配置。
如果本机与项目中同时存在同名技能，可按技能路径选择项目版本。

已有文件会保留：

- 非空的 `paper/` 不会被替换；已有稿件可以继续使用自己的目录和模板。
- 已有 `AGENTS.md` 不会被覆盖，可参考 `.paper-writing/templates/project/AGENTS.md` 整合指导。
- 项目已有的 `scripts/`、`skills/` 等目录不影响工具路径。
- 已有同名 Codex 技能会保留，安装器会提示冲突。
- 重复安装会补充缺少的资源，但不会覆盖已有文件内容；更新已有技能时需保留并合并本地修改。
- 旧安装器创建的入口链接会被清理，用户自己的配置和文件会保留。

旧的 `paper-playbook`、`polish-writing`、`abstract-craft`、`technique-overview`、
`related-work-writing` 和 `experiments-writing` 已合并为 `cpw-write` 的内部指南。
重新安装会移除本安装器创建的这些旧入口链接，保留旧项目中的指南内容和自定义技能。
已有项目的入口文件也会保留；更新项目副本时，应将其本地修改与新版 `cpw-write` 合并。

先在 `STATE.md` 中记录论文问题、已有贡献、目标会场、稿件与数据位置。
使用已有项目时，同时记录实际参考文献路径和构建命令。

### 怎样开始一次写作任务

在 Codex 中打开论文项目，用 `$cpw-write` 发起文章写作，也可以用自然语言说明需求。
Codex CLI / IDE 中可用 `$` 指定技能或通过 `/skills` 查找。技能以当前 Codex
会话的工具和模型执行；这些入口不是终端命令，也不会自动创建多个助手进程。
调用方式见 [官方技能说明](https://learn.chatgpt.com/docs/build-skills#how-codex-uses-skills)。

新论文可以这样发起：

```text
$cpw-write 请读取 STATE.md。
根据项目已有结果，选择并阅读合适的相关论文，分析内容覆盖、章节组织和表达方式。
先给出本论文的目录、每节职责和写作方案，并记录在 STATE.md 中。
```

已有稿件的局部修改可以直接说明范围：

```text
$cpw-write 请润色 paper/sections/intro.tex。
沿用当前写作方案，保持技术主张和引用不变，重点检查领域用词和解释是否清楚。
```

局部修改复用已有参考分析和稿件习惯。没有 `STATE.md`、证据台账或项目安装时，
可以直接提供段落、稿件路径和已有支撑材料，不需要先初始化项目。

`cpw-write` 的章节指南保存在 `skills/cpw-write/references/`，作为内部文档按需读取。
你只需说明要写什么，助手会选择当前需要的指南；无需分别调用摘要、润色或评估技能。

审阅后有多处修改适合集中讨论时，`cpw-review` 或 `cpw-write` 会询问是否需要
[逐段对照册](skills/cpw-write/references/review-comparison.md)：按 C1、C2 等编号，
列出灰色原文、红色候选改写、位置和理由，便于之后逐项讨论、接受或拒绝。
已经明确要求对照册时直接制作；对照册使用独立副本，采纳哪些修改由作者决定。
它是可选协作方式，页数和建议数量由内容决定。

如果刚安装的技能尚未出现，重开 Codex 会话后检查；也可直接要求读取
`.paper-writing/skills/cpw-write/SKILL.md`。在非 Git 项目中，建议从论文项目根目录开始会话。

## 新论文的写作流程

### 1. 明确已有结果和当前任务

梳理论文的问题、主要结果、适用条件和现有支撑材料。确认当前任务是全文规划、章节撰写、
局部润色还是投稿准备。需要澄清的主张应当保留为明确的问题，避免在润色中增强结论。

从 `STATE.md` 开始，按任务读取相关主张、实验记录、证明来源和文献笔记。

### 2. 阅读适合的参考论文

选择少量能帮助当前写作决策的论文，不规定数量：

- 最接近的技术工作：帮助判断哪些背景、定义、比较和实验问题需要交代。
- 贡献类型相近、表达清楚的论文：帮助选择组织方式、解释深度和语言风格。

两者可以是同一篇论文。阅读相关正文和必要上下文，记录有用的章节位置及其写法为什么适合当前工作。
参考论文中的技术结果、假设和贡献不能自动成为本文内容。

IACR ePrint 使用其规范页面核对身份、版本和引用信息；全文阅读遵循用户配置的来源，
优先使用可用的 Markdown 镜像，涉及公式、表格或版面细节时核对对应 PDF。

### 3. 形成当前论文的写作方案

给出目录、每节职责、支撑材料和前后依赖。说明参考论文中哪些组织与表达方式适用，哪些需要调整。
把方案简要记录在 `STATE.md`，或从中链接已有项目笔记。

默认不要求建立个人风格档案。`STYLE.md` 只在作者明确需要时使用。

### 4. 撰写关键部分并逐节完善

开始撰写时，可以先写引言、技术概览等关键部分，在写作过程中结合作者反馈调整方案。
之后按材料成熟度和章节依赖推进；这不要求每篇论文采用相同的写作顺序。

章节内容应来自实际工作。摘要讲清问题、方法和主要结果；技术概览解释真正的困难与关键观察。
段落数、贡献数、insight 数量和图表数量由内容决定。

### 5. 核对文字、数字和图表

文字检查同时关注领域用词、解释顺序和技术含义。图表从项目数据生成，明确单位、范围、来源和图注。
对修改涉及的引用、公式、数值和依赖做相应检查，并报告实际执行了哪些检查。

### 6. 按当前阶段进行审稿和投稿准备

需要整体反馈时进行模拟审稿，区分已确认的问题、待核实的疑点和表达建议。
收到审稿意见后准备 rebuttal；提交前核对当前会场要求、匿名性、引用、源文件和 PDF。
上传、投稿、发送回复或公开发布需要作者明确批准。

完整方法见 [参考论文阅读与写作规划](skills/cpw-write/references/writing-from-related-work.md)。

## 全文结构怎样安排

以下是可调整的阅读顺序：

| 部分 | 主要职责与调整方式 |
|---|---|
| Abstract | 问题、方法和主要结果；按内容安排段落 |
| Introduction | 动机、问题、最相关前作和主要贡献 |
| Technical Overview | 困难与关键观察；可并入引言，或放在必要定义之后 |
| Preliminaries | 后文使用的记号、定义、模型和已有工具 |
| Main Technical Content | 协议、构造、算法或理论结果；按依赖拆分与排序 |
| Correctness / Security / Analysis | 所声明性质及其支持；可随构造展开，也可独立成节 |
| Evaluation | 现有参数计算、成本分析或测量如何回答研究问题 |
| Related Work | 与相关成果的关系；可以前置，也可以放在主要内容之后 |
| Conclusion | 有用的总结、取舍或剩余问题；按需要和会场要求设置 |
| References / Appendix | 引用及详细支撑材料；遵循会场规定 |

章节可以合并、拆分、移动或省略。Related Work 无论放在哪里，引言都应交代最直接的相关工作。
不固定各节篇幅比例，也不在模板中预填研究结论。详见 [整体结构指南](skills/cpw-write/references/sections/00_overall_structure.md)。

## 语言风格：领域用词自然，解释容易理解

这些要求同时用于初稿和润色：

- 使用相关子领域惯用、与定义一致的术语；同一个技术对象保持同一个名称。
- 普通叙述优先使用常用词和具体动作，清理空泛强调、生造标签和抽象名词堆叠。
- 默认让相邻子领域的密码学研究者能读懂引言和概览；必要时解释定义或公式的作用。
- 把对象、动作、条件和推理连接讲清楚，避免让读者补出省略的关键环节。
- 保留假设、量词、安全模型、比较口径和证据状态；不采用机械禁用词表或固定句长。

具体示例见 [语言与清晰表达指南](skills/cpw-write/references/field-language-and-clarity.md)；
局部改写参考[协作润色指南](skills/cpw-write/references/collaborative-polishing.md)，
结构和归因的例子见[合成修改示例](skills/cpw-write/examples/revision-decisions.md)。

## 常用入口

在安装后的论文项目中使用：

| Codex 技能 | 用途 | 主要输出 |
|---|---|---|
| `$cpw-init` | 初始化记录，确认材料和下一步任务 | `STATE.md` 与项目路径记录 |
| `$cpw-lit` | 整理相关工作、阅读笔记和核实过的引用 | `LITERATURE.md`、笔记和参考文献 |
| `$cpw-write` | 撰写、规划或修改稿件 | 写作方案与指定章节 |
| `$cpw-figure` | 从项目数据生成或修改图表 | 图表、生成脚本与来源记录 |
| `$cpw-review` | 模拟审稿并形成可定位的修改建议 | `REVIEWS.md` |
| `$cpw-rebuttal` | 按实际篇幅限制准备作者回复 | 内部详版和提交长度的回复 |
| `$cpw-submit` | 准备供作者核对的提交材料 | 投稿材料和 `SUBMISSION.md` |

在技能名之后直接描述主题、章节、数据来源或字数限制等要求。文章写作只需
`$cpw-write`；文献检索、图表和投稿等工具按相应任务使用。

## 论文项目中的记录

| 文件 | 保存什么 |
|---|---|
| `STATE.md` | 论文问题、状态、材料位置、写作参考、方案和待办 |
| `CLAIMS.md` | 主张的准确表述、适用范围和支撑 |
| `EVIDENCE.md` | 报告的数值、来源命令、日志、配置和统计信息 |
| `LITERATURE.md`、`paper/refs.bib` | 相关工作、比较依据和已核实的引用 |
| `THEORY.md` | 可选的定理、证明状态及来源指针 |
| `REVIEWS.md`、`DECISIONS.md` | 审稿意见、修改行动和作者决定 |
| `SUBMISSION.md` | 当前会场规则、实际检查结果和待处理项 |

记录服务于写作与核对，按当前任务维护相关部分。局部修改可以沿用项目已有的记录方式。
草稿、真实日志、审稿意见和私人资料留在论文项目中。

## 构建、检查与边界

以下命令从论文项目根目录运行，适用于默认 LNCS 骨架：

```bash
make -C paper                 # 匿名稿
make -C paper audit           # 数值与证据链接检查
make -C paper check LIMIT=30  # PDF 辅助检查；30 仅为示例，按当前 CFP 修改
make -C paper anon            # 匿名性辅助检查
make -C paper camera          # camera-ready 版本
make -C paper full            # full version
```

- 数值审计需要 Python 3.10+，只使用标准库。
- LaTeX 构建需要可用的 TeX 环境和 `latexmk`；LNCS 类优先从本机 TeX 环境取得，缺失时由辅助脚本获取。
- PDF 检查使用 Poppler 工具；图表使用 NumPy、Matplotlib，图像提取另外需要 PyMuPDF。
- 其他会场应使用其当前模板；已有稿件按 `STATE.md` 中记录的路径和命令操作。

数值审计支持 `1.23 s\ev{E1}` 或同一源代码行上的 `% EV:E1` 注释，检查链接的值、可见单位、
日志路径和可达的 LaTeX 输入文件。它不验证日志内容、推导算术、任意宏展开、图片内数字或技术主张。
详见 [审计范围与示例](docs/evidence-audit.md)。

当前 PDF 和匿名检查对缺失输入的错误处理还不完整，应先确认目标文件存在并核对实际输出。
文献台账初始模板与 `lit-matrix` 检查器的格式也尚未完全统一，使用该检查器前需对齐其列与检索记录格式。
编译成功或辅助检查通过都不代表证明、实验或整篇论文已经正确。

## 仓库内容与维护

| 路径 | 内容 |
|---|---|
| `skills/cpw-*/` | 七个 Codex 工作流入口，包含原先角色指导的职责 |
| `skills/` 中其余目录 | 文献、章节写作、润色、图表和检查的配套技能 |
| `templates/` | 稿件骨架、项目记录、回复和交接模板 |
| `figures/` | 使用合成数据的绘图、TikZ 模板及本地图像提取工具 |
| `references/reading-lists/` | 公开文献检索起点 |
| `papercheck/`、`scripts/` | 数值审计及仓库辅助脚本 |
| `docs/zh/writing-playbook.md` | [中文写作指南](docs/zh/writing-playbook.md) |

维护工具箱时只使用合成示例和公开资料。在工具箱仓库中运行针对安装与审计的检查：

```bash
python3 scripts/audit_tex.py --selftest
python3 -m unittest discover -s tests
```

推送改动前，按 [AGENTS.md](AGENTS.md) 使用本地、被 Git 忽略的 `.privacy-denylist` 运行
`scripts/privacy_scan.sh`。真实论文内容和提取出的他人论文图片不应加入工具箱。

## 来源与许可

本项目提取自 [crypto-research-agents](https://github.com/acprk/crypto-research-agents)，
来源和提取范围见 [SOURCE.md](SOURCE.md)。采用 [MIT License](LICENSE)，保留原有署名。
