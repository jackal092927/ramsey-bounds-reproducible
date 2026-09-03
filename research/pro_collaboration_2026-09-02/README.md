# 研究成果、方向与 Pro 协作总档案

启动日期：2026-09-02（PDT）；整合更新：2026-09-03。这是项目级成果总览和补充审计档案。TDA 当前 Pro 请求及持续回收的主档案是 [同日协作目录](../quantum_direction_selection/collaboration/2026-09-02/README.md)，两处记录共用同一研究分支和原 Pro 会话。

当前值得重点推进的是 **exact-kernel 转移到真实归一化持久性**。现有文稿给出了抽象转移、加权 history、阈值和部分谱估计的推导；完整结论仍依赖明确的局部 gadget 定理，以及受限精确电路承诺的复杂度地位。它还不是一个已经完成的无限制 SDQC1-hardness 结果。

旧 Pro 回复已收回：TDA、广义秩/zigzag、双曲导航、exact-seven。它们的原文完整保存在 `responses/`，本轮补充研究判断在本目录的 disposition 中处理。旧回复只审查了当时收到的版本，不能覆盖后来的证明。新一轮已由并行协作线程沿原 TDA 会话提交，使用 GitHub 固定快照 a46f4087693edc088663e0cbf4f6aa9961494325，要求先审查最新证明，再尽可能发展出有高水平 TCS 投稿价值的强定理。已设置一个每小时回收的跟进；本目录不重复提交请求或另设自动任务。

阅读顺序：

1. [成果与方向总报告](RESEARCH_BRIEF.md)：已有结果、证据范围、候选方向和具体推进问题。
2. [结论台账](CLAIM_LEDGER.md)：正面结果、反例、失败机制和未决问题。
3. [Pro 意见处置](REVIEW_DISPOSITION.md)：原文观点与本地验证的区别。
4. [里程碑](MILESTONES.md)：历史成果、已完成核查和下一步。
5. [来源与依赖](SOURCE_MAP.md)：当前引用版本与尚未独立重证的来源事实。
6. [协作状态](SESSION_STATE.md)：发送、取回、验证、GitHub 同步分别记录。
7. [并行工作整合说明](INTEGRATION.md)：两个档案的分工、主请求及本轮新增的来源纠正。
8. [验证与复现记录](VERIFICATION.md)：39 个 persistent-domain 检查、现有探针、稿件源文件及 PDF 哈希核对。

新的谱转移候选见 [PERSISTENT_SPECTRAL_TRANSFER.md](PERSISTENT_SPECTRAL_TRANSFER.md)。它来自 Pro 的建议，经本地重构后作为结构性推论推进；persistent Laplacian 的单调性本身已有文献，不能列作新发现。

原始研究材料在 [quantum_direction_selection](../quantum_direction_selection/README.md)。Ramsey 上界、下界、有限证书和量子查询论文的项目入口仍是 [根 README](../../README.md) 与 [STATUS](../../STATUS.md)。这些工作并非一篇论文的四个相互依赖结论。

有限计算用于核对实现和反例，不替代无限族证明。超时保留为 `UNKNOWN`；来源依赖、待验证建议、已证明局部结论和已投稿记录使用不同状态。新颖性评价是有限来源核查后的研究判断，不是优先权证明。
