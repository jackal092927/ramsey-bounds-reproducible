# 量子 TDA：结果归档与 Pro 协作

本目录把现有推导、调研、正反结论和外部 review 串联成可继续推进的研究记录。主线是 **真实归一化 persistence**：
\[
\beta_d(X_1\to X_2)/\beta_d(X_1).
\]

- [研究总文档](RESEARCH_DOSSIER.md)：当前结论、完整条件、潜在方向及停止条件。
- [审稿勘误](AUDIT_CORRECTIONS.md)：明确撤回 spectator、interface、误差阈值等错误异议。
- [来源与依赖表](SOURCE_LEDGER.md)：区分此前报告的来源检查与本次实际核查。
- [阶段进展](MILESTONES.md)：保留正结果、负结果、未完成项和实际同步状态。
- [Pro 任务书](PRO_REQUEST.md)：先审查，再直接推进证明与理论结果。
- [9 月 3 日 Pro 完整答复](PRO_REVIEW_2026-09-03.md)与[独立处理意见](PRO_REVIEW_DISPOSITION_2026-09-03.md)：保留采纳、纠正与尚未核验的结论。
- [当前最强条件性证明](FINITE_CERTIFICATE_CONCENTRATION.md)：有限零权重证书推出全几何链 concentration，逻辑 gap 依赖降为线性；[先得到的谱分区证明](EXACT_FILLING_COERCIVITY.md)作为中间里程碑保留。
- [实际三项 gadget 的精确证书](REPRESENTATIVE_GADGET_CERTIFICATE.md)：包含原始图、整数填充链、模素数秩证明及[可复现检查器](certify_representative_bulk.py)；完整 guard 家族仍待覆盖。
- [新一轮聚焦请求与发送回执](PRO_FOLLOWUP_DISPATCH_RECEIPT_2026-09-03.md)：固定快照、实际正文、附件哈希和运行证据。
- [聚焦请求的运行失败记录](PRO_FAILED_ATTEMPT_2026-09-03.md)：没有最终数学答复；保留可见活动与具体复现错误。
- [有界证明审查完整答复](PRO_BOUNDED_PROOF_REVIEW_2026-09-03.md)与[独立处理意见](PRO_BOUNDED_PROOF_DISPOSITION_2026-09-03.md)：已完成并收集，138 个公式完整保留；显式假设下的全链定理经本地核查后采纳。
- [selected-cycle guard 闭包证明](SELECTED_CYCLE_GUARD_CLOSURE.md)与[精确检查结果](SELECTED_CYCLE_GUARD_CHECKS.json)：新构造的局部推导和整数检查已完成，一般证明待下一轮独立审查。
- [guard 审查发送回执](PRO_SELECTED_GUARD_DISPATCH_RECEIPT_2026-09-03.md)：第五条请求已在原 Pro 5/5 会话运行，固定 source commit **9f2e088** 与 13966 字节附件。
- [guard 完整答复](PRO_SELECTED_GUARD_REVIEW_2026-09-03.md)与[独立处理意见](PRO_SELECTED_GUARD_DISPOSITION_2026-09-03.md)：条件性闭包已采纳，124 个公式及三项表述修正完整归档。
- [剩余活跃态精确证书](REMAINING_ACTIVE_ATOM_CERTIFICATES.md)：单比特差态和两类双比特两项态均通过源码固定的整数证书与离线重算；显式固定 palette 的本地证书链已闭合。
- [最小受限 reduction 定理](CLEAN_RESTRICTED_REDUCTION_THEOREM.md)：将精确实门电路 promise 转成真实归一化 persistence；标准复杂性来源与新颖性仍是开放关卡。
- [受限定理整合审查回执](PRO_RESTRICTED_THEOREM_DISPATCH_RECEIPT_2026-09-03.md)：第六条有界请求已在原 Pro 5/5 会话运行，固定 source commit **23f83cf**。
- [受限定理完整审查](PRO_RESTRICTED_THEOREM_REVIEW_2026-09-03.md)与[独立处理意见](PRO_RESTRICTED_THEOREM_DISPOSITION_2026-09-03.md)：端到端整合在修正 source interface 后通过；137 个公式完整归档。
- [源复杂度关卡](SOURCE_COMPLEXITY_GATE.md)：标准常数给出 \(1/6\) 的 fixed-space fraction gap；任意 trace gap 与 exact-rank gap 不等价，restricted real-gate source 与 unrestricted SDQC1 必须分开。
- [源复杂度 Pro 请求与发送回执](PRO_SOURCE_COMPLEXITY_DISPATCH_RECEIPT_2026-09-03.md)：第七条有界请求已在同一 Pro 5/5 会话运行；固定 source commit **b78da7a** 与 28196 字节附件。
- [四个 Hadamard 活跃态的精确重标号证明](ACTIVE_HADAMARD_ORBIT.md)：同一个证书覆盖四个无 guard 三项约束，四条整数填充式全部核验。
- [离线复现结果](OFFLINE_REPRESENTATIVE_CHECKS.json)：无需 gh 或网络重算归档图的全部证书条件。
- [上一轮 TDA Pro 完整答复](PRO_PREVIOUS_TDA_RESPONSE.md)：已收集的模型建议，未经采纳不算已证明。
- [persistent Laplacian 条件性扩展](PERSISTENT_LAPLACIAN_EXTENSION.md)：对 Pro 提案的独立推导与边界。
- [复现实验原始输出](REPRODUCTION_RESULTS.json)：7 个已有小型检查的本次重跑结果。
- [执行状态](COLLABORATION_STATE.json)：发送、运行、收集、核查、同步分别记录。
- [本轮发送回执](PRO_DISPATCH_RECEIPT.md)：固定 Git 快照、实际任务消息、附件哈希和 Pro 运行证据。
- [发送后的来源纠正](POST_DISPATCH_SOURCE_UPDATE.md)：persistent Laplacian 单调性已有来源，列入下一轮评估。
- [后续工作流程](FOLLOW_UP_WORKFLOW.md)：每小时回收、独立核查、继续推进和同步。
- [此前 hyperbolic 备选讨论](PRO_PREVIOUS_HYPERBOLIC_RESPONSE.md)：保留完整建议及停止理由。
- [项目级补充档案](../../../pro_collaboration_2026-09-02/README.md)：47 份来源快照、四份历史 Pro 回复、39 个 persistent-domain 检查及 Ramsey 成果总览；补充任务书未发送，当前请求仍以本目录的固定附件为准。

目前最实质的候选是由有限零权重证书推出任意低能几何链的全局 concentration，得到对逻辑 gap 的线性依赖；后面的维数与商空间推理属于标准推论。固定实门 palette 及端到端受限 transfer theorem 已通过分阶段证书和有界审查。当前首要关卡转为 exact source complexity：标准常数的 separated promise 有效，但 unrestricted SDQC1 与优先权仍未建立。备选方向包括 persistent Laplacian 低谱的共同复制转换、量子几何采样及自然的 evaluated-Hom-width 受限类。

研究快照 a46f408 的 Pro 请求已完成并完整收集，界面记录处理用时 155 分 30 秒。后续快照 **789f87f** 的请求以“Thinking failed”终止，没有最终答复。快照 **f4ec1b7** 的全链审查、**9f2e088** 的 guard 审查及 **23f83cf** 的受限定理整合审查均已完成、收集并独立处理。source commit **b78da7a** 的第七条请求正在审查 separated real-gate source 能支持的精确复杂度表述。每小时回收仍有效。本目录不是投稿或 unrestricted 标准复杂性硬度认证。
