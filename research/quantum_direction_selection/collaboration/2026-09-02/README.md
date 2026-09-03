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
- [最小受限 reduction 定理](CLEAN_RESTRICTED_REDUCTION_THEOREM.md)：将 separated 精确实门电路 promise 转成真实归一化 persistence；显式 promise corollary 已成立，标准类等价与新颖性仍是开放关卡。
- [受限定理整合审查回执](PRO_RESTRICTED_THEOREM_DISPATCH_RECEIPT_2026-09-03.md)：第六条有界请求已在原 Pro 5/5 会话运行，固定 source commit **23f83cf**。
- [受限定理完整审查](PRO_RESTRICTED_THEOREM_REVIEW_2026-09-03.md)与[独立处理意见](PRO_RESTRICTED_THEOREM_DISPOSITION_2026-09-03.md)：端到端整合在修正 source interface 后通过；137 个公式完整归档。
- [源复杂度关卡](SOURCE_COMPLEXITY_GATE.md)：标准常数给出 \(1/6\) 的 fixed-space fraction gap；任意 trace gap 与 exact-rank gap 不等价，restricted real-gate source 与 unrestricted SDQC1 必须分开。
- [源复杂度 Pro 请求与发送回执](PRO_SOURCE_COMPLEXITY_DISPATCH_RECEIPT_2026-09-03.md)：第七条有界请求已在同一 Pro 5/5 会话运行；固定 source commit **b78da7a** 与 28196 字节附件。
- [源复杂度完整审查](PRO_SOURCE_COMPLEXITY_REVIEW_2026-09-03.md)与[独立处理意见](PRO_SOURCE_COMPLEXITY_DISPOSITION_2026-09-03.md)：第七条答复已完成并收集，113 个公式完整归档；接受 separated exact-real-gate promise corollary，停止 unrestricted SDQC1 硬度表述。
- [八标签 BQP1 source lemma](NORMALIZED_BQP1_SOURCE_GATE.md)与[独立接口审查](NORMALIZED_BQP1_SOURCE_GATE_INDEPENDENT_REVIEW.md)：在第七条答复之后得到的本地构造，把 exact \(G_2\) 的 perfect-completeness verifier 变为 perfect fraction \(3/4\) 对 \(1/8\)；代数、clean/mixed interface、dummy denominator、exact gates 与 Rudolph 原始定义均已本地核查，后续有界 Pro 复核也已完成。
- [八标签 BQP1 有界审查包](PRO_BQP1_SOURCE_PACKET_2026-09-03.md)与[发送回执](PRO_BQP1_SOURCE_DISPATCH_RECEIPT_2026-09-03.md)：第八条请求已在原 Pro 5/5 会话运行；仅核对 acceptance operator、clean/mixed interface、\(G_2\) 精确实现、denominator 与 gate-dependent hardness composition，不做 gadget 或 novelty 审查。
- [八标签 BQP1 完整审查](PRO_BQP1_SOURCE_REVIEW_2026-09-03.md)与[独立处理意见](PRO_BQP1_SOURCE_DISPOSITION_2026-09-03.md)：第八条答复已完成并收集，98 个公式完整归档；exact operator 与受限加权 hardness composition 通过，padding-generated denominator 被保留为影响力风险。
- [严格新颖性碰撞审计](NOVELTY_COLLISION_AUDIT_2026-09-03.md)：对六项核心来源做了定点复查；当前价值评为 **MEDIUM, conditional**。King--Kohler 已含大部分任意链估计，Gyurik 等已陈述特例 whole-kernel gap；可主张的增量必须落在可复用的退化核 transfer theorem 与受限 normalized-rank 应用上。
- [第九条 Pro 新颖性任务书](PRO_NOVELTY_REQUEST_2026-09-03.md)：要求直接核查原始来源、区分数学错误与优先权风险，并给出一个可证明的一般 transfer lemma 或明确的 corollary/no-go 结论。
- [第九条冻结审查包](PRO_NOVELTY_PACKET_2026-09-03.md)：从远端已核对的 source commit **6e70274** 固定七份文件；附件 72511 字节，SHA-256 `220304109773ce44ed91f8cf8846a91d9cecaeab82565df13a0a4c06e8c0c3e1`。
- [第九条发送回执](PRO_NOVELTY_DISPATCH_RECEIPT_2026-09-03.md)：原 Pro 5/5 会话中的第九条用户消息已发送一次并观察到运行；消息 ID、时间、source/packet commits、正文与附件哈希均已记录。
- [第九条完整来源/新颖性审查](PRO_NOVELTY_REVIEW_2026-09-03.md)、[原始捕获](PRO_NOVELTY_REVIEW_CAPTURE_2026-09-03.json)与[独立处理意见](PRO_NOVELTY_DISPOSITION_2026-09-03.md)：已完成并收集；70 个公式与 13 个外链完整归档。结论是没有发现显式假设下的数学反例，核心应写成 finite-certificate all-chain leakage；退化核替换、维数闭合与 unweighting 分别是短推论或来源化 corollary。
- [King--Kohler 推论边界](KING_COROLLARY_BOUNDARY_2026-09-03.md)：逐行代数表明，若旧 all-chain 估计具有统一常数，退化核 whole-gap 的定性结论只是短推论；可保留的技术增量是 finite-certificate 证明对增长维数扰动与 padded bulk 的修复，以及最终 gap 对逻辑 \(g\) 的线性依赖。
- [分母影响力关卡](DENOMINATOR_IMPACT_GATE_2026-09-03.md)：主定理可删除所有 dummy padding，并加强表述为固定 \(\beta_d(X_{\rm in})=8\)、persistent rank 六对一的 hardness；增长分母只作为诚实标注的 tensor-replication closure。
- [论文定位与可重启提纲](MANUSCRIPT_POSITIONING_AND_OUTLINE_2026-09-03.md)：把 correctness/source boundary 作为 hard gate，但不再等待 HIGH novelty；第九条审查 disposition 后立即启动 focused theory manuscript v0。
- [论文 v0](manuscript_v0/README.md)：已形成 19 页可编译草稿，正文覆盖 transfer theorem、whole-kernel closure、quotient naturality、fixed-eight \(\mathsf{BQP}_1^{G_2}\) hardness、common-copy unweighting、相关工作与限制；[PDF](manuscript_v0/main.pdf)与模块化 LaTeX 源一并归档。
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

目前最实质的候选是由有限零权重证书推出任意低能几何链的全局 concentration，得到对逻辑 gap 的线性依赖；后面的维数与商空间推理属于标准推论。固定实门 palette 及端到端受限 transfer theorem 已通过分阶段证书和有界审查。任意 threshold 的 unrestricted SDQC1 推论已经否定；八标签构造则给出受限的正结果：在已记录的几何 theorem 假设下，加权 whole-kernel-gapped true normalized persistence 有 \(\mathsf{BQP}_1^{G_2}\)-hard route。第九条 Pro 定点来源审计已完成，并维持 **MEDIUM, conditional**：King--Kohler 的证明已经包含大部分任意链 machinery，Gyurik 等也已陈述一个特例 whole-kernel gap；真正可写的增量是修复 padded bulk 与增长维数扰动问题的 finite-certificate all-chain theorem，以及其 filtered quotient 应用。Unweighted 结果现在作为 Hayakawa 单层谱分解的直接来源化 corollary 纳入 v0。

研究快照 a46f408 的 Pro 请求已完成并完整收集，界面记录处理用时 155 分 30 秒。后续快照 **789f87f** 的请求以“Thinking failed”终止，没有最终答复。快照 **f4ec1b7** 的全链审查、**9f2e088** 的 guard 审查、**23f83cf** 的受限定理整合审查、source commit **b78da7a** 的源复杂度审查、source commit **f11cb4e** 的八标签接口审查，以及 source commit **6e70274** 的来源/新颖性审查均已完成、收集并独立处理。第七条 hard stop 仍适用于 arbitrary-threshold SDQC1；第八条只建立 perfect-completeness BQP1 的受限 route。当前外部来源关卡只剩 final SIAM King--Kohler 详细正文是否已含等价修复；它影响新颖性定位，但不阻止 scoped manuscript v0。本目录不是投稿、发表或 unrestricted 标准复杂性硬度认证。
