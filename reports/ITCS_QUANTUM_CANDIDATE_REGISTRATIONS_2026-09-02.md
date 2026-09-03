# ITCS 2027：四个量子算法候选方向与已注册摘要

本文件保留 9 月 2 日注册时的摘要、判断和外部状态。9 月 3 日整合时未重新操作会议系统；后续理论进展及方向排序见 [当前研究总档案](../research/pro_collaboration_2026-09-02/README.md)。公开归档省略了登录账号标识。

## 注册结果与准确状态

- 日期：2026-09-02（America/Los_Angeles）。
- 四项均在当天摘要注册截止前保存成功，随后重新打开各自页面确认。
- 作者：Cheng Xin；单位：California State University, Fresno。
- 状态：**Registered draft；尚未上传 Submission PDF；Not ready for review。**
- 这四个摘要描述拟研究的问题和技术路线，不声称已经证明新的量子优势，也不是四篇已完成论文。
- 网站显示的完整论文截止时间：2026-09-04 16:59:59 PDT。不完整的草稿不会进入评审。
- 原有 Ramsey #193 与 Navigable Graph #90 未在这次操作中修改。
- AI 使用项已填写 Formatting & language、Literature、Substantial role；AI-assisted reviews 选择 Allow。未把尚未开展的数学证明工作填成已完成。
- 本次没有启动实验，没有请求新的 ChatGPT Pro 审查，也没有把文稿公开到 GitHub。

| 编号 | 标题 | 注册页面 |
| --- | --- | --- |
| #622 | Quantum Algorithms for Generalized Persistence Rank Queries | [编辑草稿](https://itcs2027.hotcrp.com/u/0/paper/622/edit) |
| #627 | Quantum Algorithms for Dynamic Zigzag Persistence Queries | [编辑草稿](https://itcs2027.hotcrp.com/u/0/paper/627/edit) |
| #628 | Quantum Sampling of Persistence Diagrams: Accuracy and Query Complexity | [编辑草稿](https://itcs2027.hotcrp.com/u/0/paper/628/edit) |
| #629 | Quantum Navigation of Proximity Graphs for Approximate Nearest-Neighbor Search | [编辑草稿](https://itcs2027.hotcrp.com/u/0/paper/629/edit) |

## 快速筛选结论

三个 TDA 方向的暂定优先级是：广义秩查询、动态 zigzag、持久图采样。导航图作为另一个研究分支保留。该排序综合了与既有工作的连接、数学问题是否具体、经典基线的强弱和可能产生新机制的空间，不代表已通过完整 novelty 审查。

本轮做了快速主文献检索与独立选题复核，没有把通用 Grover/量子线性代数的已知加速直接记作新贡献。对前三个方向，应优先与 QuantumTDA 任务已有的推导和障碍衔接；对第四个方向，应首先逐项对照已有 quantum HNSW 文献。

以下英文标题与摘要是已保存到 HotCRP 的原文。其后中文内容是后续研究说明，不属于已经填写的摘要。

## 1. 广义持久性：只回答一个秩查询 — #622

### Title

Quantum Algorithms for Generalized Persistence Rank Queries

### Abstract

Generalized persistence describes topological information indexed by a partially ordered set, but computing an entire module decomposition can be substantially more expensive than answering a single rank query. We investigate quantum algorithms for estimating the generalized rank of a specified connected subposet under explicit sparse-matrix and coherent-access models. The proposed approach expresses the limit-to-colimit map through compatibility constraints and subspace projections, linking generalized-rank computation to quantum singular-value estimation. A central question is whether topology-specific structure or preconditioning can control the global subspace angles that arise when local constraints are combined. The investigation distinguishes exact rank from normalized additive estimation and accounts separately for state preparation, matrix access, conditioning, and classical output. Comparisons with zigzag-unfolding algorithms and randomized classical estimators are part of the same access model. The aim is to identify natural families admitting a provable quantum advantage, or precise obstructions showing why local spectral-gap assumptions alone are insufficient. This study targets individual generalized-rank queries rather than claiming an efficient quantum algorithm for unrestricted multiparameter decomposition.

### Topics

Quantum Algorithms; Quantum Complexity; Discrete and Computational Geometry; TCS + Math.

### 为什么优先考虑

这是与 Cheng Xin 既有研究最直接衔接的方向：Dey–Xin 的工作已经给出了通过 zigzag 展开计算 generalized rank 的经典路径。新的研究目标是改变计算任务的粒度：不输出整个分解，只回答指定区域的一次广义秩查询。[Dey–Xin 原文](https://arxiv.org/abs/2403.08110)

### 技术切入点与最小目标

尝试把 limit-to-colimit 映射的秩表达成兼容约束下的子空间投影问题，用量子谱估计回答归一化、加性误差的秩查询。首先必须明确系数域、矩阵输入方式、归一化分母、精度及相关谱间隙；量子复向量空间上的数值秩不能不加说明地替代有限域同调秩。

最小的有意义结果：找出一个自然的 persistence module 家族，证明全局条件数或相关子空间夹角可控，并把这些参数全部代入总查询复杂度，与同样访问模型的经典算法比较。仅给定一个“好条件数”假设再套用通用量子线性代数，还不足以形成强贡献。

### 首先要解决什么

另一个 QuantumTDA 任务的当前记录提出了局部谱间隙不能保证全局子空间夹角良好的障碍。这次筛选未重新证明该结论；它是优先检查的风险，而不是已有正向加速定理。先找能避免该障碍的拓扑结构或预条件化，而非直接宣称一般情形加速。

**当前判断：TDA 中优先级最高；有研究连续性，但新的量子优势尚待证明。**

## 2. 动态 zigzag：更新后快速回答拓扑查询 — #627

### Title

Quantum Algorithms for Dynamic Zigzag Persistence Queries

### Abstract

Zigzag persistence tracks topological features through both insertions and deletions, making it a natural model for changing data. We investigate whether quantum computation can accelerate interval queries on a simplex-wise zigzag filtration without constructing its entire barcode after every update. The computational target is a specified interval-rank or persistence-threshold query, with preprocessing, update processing, query cost, and output size charged separately. The proposed route combines low-rank changes in boundary operators with reusable subspace representations and quantum estimation. Its main challenges are the accumulation of approximation error and the possibility that a local update causes a large change in a global homological subspace. We seek structural conditions under which amortized quantum query improvements survive these effects, using fast classical zigzag and dynamic-graph algorithms as baselines. The study includes explicit access and precision assumptions and separates higher-dimensional instances from graph cases with near-linear classical algorithms. The goal is an output-sensitive theory of quantum dynamic topology, not an assumption that generic quantum linear algebra automatically accelerates barcode computation.

### Topics

Quantum Algorithms; Quantum Complexity; Discrete and Computational Geometry; Graph Algorithms; TCS + Math.

### 为什么考虑

插入和删除都存在时，zigzag 是自然对象。新的问题不是一次性输出整个 barcode，而是在更新流中处理指定区间的查询，研究预处理、单次更新和查询之间的权衡。

### 技术切入点与最小目标

利用边界矩阵的低秩变化，探索可重用的子空间表示和量子估计。先选一个清楚的模型：固定长度的 zigzag 区间查询，或在线追加插入/删除操作后的查询；不能把两种更新模型混写成同一个定理。

最小目标是在一个结构明确的高维复形家族上，证明总更新成本与查询成本的摊还界；同时控制误差累积、谱变化与表示维护的开销。

### 首先要解决什么

一处局部更新可能显著改变全局同调子空间。如果每次都要重建数据访问结构，所谓“快速更新”可能没有优势。经典基线也已经很强：FastZigzag 能转化为普通持久性计算，图上的 zigzag 已有近线性算法。[FastZigzag](https://arxiv.org/abs/2204.11080)，[图上的近线性算法](https://arxiv.org/abs/2103.07353)

**当前判断：TDA 第二优先级；成败取决于能否真正复用计算，而非每次重算。**

## 3. 持久图采样：不求完整条形码，只求有用统计 — #628

### Title

Quantum Sampling of Persistence Diagrams: Accuracy and Query Complexity

### Abstract

Many applications of persistent homology use a summary of a persistence diagram rather than every birth-death pair. We investigate quantum algorithms for sampling barcode features and estimating bounded statistics of persistence diagrams under explicit rank-query and boundary-access models. The target output is a specified distribution over persistence pairs or an additive approximation to a selected diagram statistic, rather than a full classical barcode. The proposed framework explores adaptive subdivision of the birth-death plane using persistent-rank estimates, with quantum estimation used only where the required accuracy and feature mass justify its cost. A key difficulty is cancellation: small errors in several rank estimates can overwhelm the multiplicity of a rare feature. We seek a precision-aware allocation rule and matching limitations that account for this effect, state preparation, and output size. Comparisons with classical rank-query sampling and existing quantum persistent-Betti estimators will determine when a quantum improvement is possible. The intended contribution is a principled connection between approximate topological summaries and quantum query complexity, with explicit guarantees needed before any speedup claim.

### Topics

Quantum Algorithms; Quantum Complexity; Discrete and Computational Geometry; Sublinear Algorithms; TCS + Math.

### 为什么考虑

实际使用中，有时需要的是长期存活特征占比、某类 barcode 统计量，或少量代表性 birth–death 对，而不是所有条形码。这为避开完整输出成本提供了明确的问题设定。

### 技术切入点与最小目标

先限定在普通一参数、有限且可区间分解的 persistence module。必须写明抽样分布，例如按条形码重数均匀抽样，或按寿命加权抽样，并处理无穷长条形码和零质量情形；不能将普通条形码中的非负重数直接推广成多参数 signed diagram 的概率。

探索通过 birth–death 平面的自适应划分与 rank queries，定位目标特征，再利用量子估计减少查询次数。最小目标是证明一个有明确误差保证的采样或统计估计算法，并在同一个 rank-query 或边界访问模型中比较经典成本。

### 首先要解决什么

条形码重数可以来自若干秩值相减。稀有特征的质量很小，秩估计的误差却可能把它完全淹没。需要一个精度随区域质量变化的分配规则；不能把常数精度的 normalized Betti 估计当作免费精确 rank oracle。

归一化 persistence 已有非常近的量子复杂性文献，因此新的内容必须体现在采样任务、精度依赖或算法机制上，而非再次提出“估计持久特征比例”。[Lowe 等，2026](https://arxiv.org/abs/2607.03278)

**当前判断：TDA 第三优先级；任务比较清楚，但与近期文献重合的风险较高。**

## 4. 导航图近邻检索：证明完整查询的量子优势 — #629

### Title

Quantum Navigation of Proximity Graphs for Approximate Nearest-Neighbor Search

### Abstract

Graph-based approximate nearest-neighbor search underlies many large-scale retrieval systems, including hierarchical navigable small-world indices. We investigate quantum query algorithms for navigating a preprocessed proximity graph given coherent access to neighbor lists and query-to-point distances. The central question is when quantum search among outgoing neighbors improves total retrieval cost once navigation length, graph degree, approximation quality, and the fraction of improving neighbors are all accounted for. The proposed analysis separates exact local minimum finding from sampling sufficiently improving moves and studies how these choices change the progress of a navigation trajectory. Classical and quantum algorithms are compared using the same graph and access model, with preprocessing, coherent data access, and repeated-query amortization treated explicitly. We seek geometric or graph-theoretic conditions supporting a provable end-to-end query improvement, together with limitations for bounded-degree graphs and long dependent paths. Hierarchical graph retrieval motivates the model, but acceleration of a local neighbor search is not assumed to imply a speedup of an entire HNSW implementation or retrieval-augmented generation pipeline.

### Topics

Quantum Algorithms; Quantum Complexity; Graph Algorithms; Sublinear Algorithms; Discrete and Computational Geometry.

### 和 Navigable Graph / HNSW / RAG 的关系

HNSW 是图式近邻检索方法。这里研究的是检索图上如何根据一个查询导航；它可以服务于 RAG 的检索阶段，但不是对 LLM 生成阶段或整个 RAG 系统的加速结论。[HNSW 原文](https://arxiv.org/abs/1603.09320)

这也是一个独立于现有 ITCS #90 的量子查询问题；没有复制或修改 #90，也不把其中尚未核实的定理当作这里已经成立的假设。

### 技术切入点与最小目标

在一个节点有 d 个候选邻居时，量子最小值查找提供约平方根级的候选查询成本，这是已知原语，不是我们的新结果。[Dürr–Høyer](https://arxiv.org/abs/quant-ph/9607014)

真正值得做的是把“局部候选选择”与“全程导航进展”联系起来：是否一定要选最优邻居，还是找到一个足够好的邻居即可？如果好邻居比例变化，经典随机抽样与量子搜索的成本分别是多少？量子化后导航步数、近似率和成功率能否同时控制？

最小目标是在明确的几何图族上，证明把局部量子选择代入后仍有可控的导航步数和近似保证，并给出包括数据访问、误差放大在内的总查询界。比较对象不能只是暴力扫描整个数据库，还必须包括同一张图上的经典随机导航算法。

### 直接相关前人工作：必须比较

IJCAI 2025 已有 Xia、Tian、Yuan、Deng 的 *Efficient Quantum Approximate kNN Algorithm via Granular-Ball Computing*，明确结合 quantum kNN 与 HNSW。因此“首次量子 HNSW”不是可用的新意。[IJCAI 正式论文页](https://www.ijcai.org/proceedings/2025/739)

此次核实了其正式发表信息与所研究方向；尚未对其完整证明进行对抗性审查，也没有断言它的复杂度分析错误。我们的候选区别是：把图度数、导航长度、近似保证与同等访问模型下的经典成本显式纳入一个可证明的端到端查询结论。这是研究目标，不是已经建立的优越性。

### 首先要解决什么

若每个节点只有常数个邻居，局部平方根加速一般不会改变对数据库规模的渐近依赖；自适应导航路径也不一定能被整体量子并行化。若最后只剩“在已知导航算法里调用一次量子最小值查找”，还不足以支撑有力度的独立理论论文。

**当前判断：值得保留的独立探索方向；需要新的导航进展定理，不能只做 HNSW 的量子包装。**

## 本轮核实与尚未核实

已核实：四个注册编号、已保存的标题和摘要、Fresno 作者信息、草稿未准备好评审的状态；Dey–Xin generalized-rank 经典路线；FastZigzag 和图上近线性经典基线；2026 normalized-persistence 近邻文献；已有 IJCAI 2025 quantum HNSW 工作。

尚未建立：四个方向中的任何新量子加速定理、匹配下界、完整去量子化比较、新的实验结果、ITCS 录用级 novelty。没有以“暂未搜索到完全相同题名”作为原创性证明。

后续推进应围绕一个具体可证的最小结论展开。若多个候选最后只是同一条定理的不同表述，应合并而不是为了保留注册数量拆成多篇；若没有实质性结果，则不把草稿标记为 ready for review。
