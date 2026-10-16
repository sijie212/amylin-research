# Amylin Report — Source Verification Log

**Verification date:** 2026-10-16  
**Scope:** every distinct source URL cited in the amylin agonist / weight-loss report (Chinese original + English translation).  
**Method:** each source was actually fetched and read by one of four read-only workers; workers judged ONLY the specific claims attributed to each source, not the page in general. Paywalled / abstract-only reads are recorded as such, never claimed as full-text verification.

## Recount correction

The reports claim **135 source annotations**, but a recount of distinct URLs shows **127 distinct source URLs** (82 in the English version, 125 in the Chinese original; **45 URLs present in the Chinese original were dropped in the English translation**). This log covers the full union of **127** so nothing is missed. The 135 figure counts annotations (some URLs are cited more than once), not distinct sources.

## Counts

| Verdict | Count |
|---|---|
| Verified | 22 |
| Corrected (partially supported / misattributed / needs companion source) | 39 |
| Contradicted (wrong citation / wrong attribution) | 3 |
| Could not access | 63 |
| **Total distinct sources** | **127** |

## Access failures — 429 hard stop

61 of the 63 could-not-access entries are browser-service **429 rate-limit** failures (two of those also reported a 403 / unresolvable error), plus 2 fetch timeouts. Per the standing rate-limit rule, blocked fetches were **not retried in this attempt** and must not be re-dispatched or replaced in this attempt. A later run may retry them. A 429 is a tool limit, **not** evidence that the source lacks the claim.

## Material corrections applied to the English report + knowledge graph

1. **PMID 17393306 REMOVED** — it is a heart-failure exercise-testing review, nothing to do with pramlintide. The pramlintide Pro-substitution conflict itself is real (Wikipedia Amylin: 25, 26, 29; other literature: 25, 28, 29) but this PMID supports neither side.
2. **Eloralintide Phase 2 corrected** (BioSpace / Lilly release): 1 mg −9.5%, 3 mg −12.4%, 6 mg −17.6%, 9 mg −20.1%, placebo −0.4%; Phase 2 NCT06230523 (NOT NCT06536399); **no 1.5 mg arm**; no ≥15% responder figures; safety / half-life / albumin claims are NOT in the release and need the Lancet paper.
3. **BBB attribution contradicted** — the Physiology (AJP-Regu) paper is an accumbens-infusion study and PMC3960470 is a PPI/accumbens study; neither is a BBB-transport study. Do not cite them for Banks & Kastin BBB numbers, striatal accumulation, insulin comparison, or the mRNA claim. Banks claims now rest only on the (unverified) ScienceDirect Banks abstract and are flagged as needing the primary Banks papers.
4. **EC50 114/1492 pM misattributed** — those values are NOT in PMC12410446. Removed from that citation; the numbers need a different source.
5. **Eloralintide selectivity is assay-dependent** — the PubMed abstract gives ~12-fold (AMY1R vs CTR); the ASC39 press release's own EC50s (1,350.8 / 21.2 pM) imply ~64-fold. Both figures are now given with the assay-dependence caveat instead of a single ~12-fold figure.
6. **Cagrilintide / sCT LPBN-cFos misattributed** — NOT in PMC4867080 (2016, predates cagrilintide). Citation removed; the claim needs a later source.
7. **CagriSema blood-pressure claim corrected** — SBP fell 13 mmHg in Phase 3, but the source states *no data* on the indirect (weight-mediated) BP contribution. The report no longer asserts weight mediation as the main mechanism; the weight-mediated share is unquantified.
8. **ACCG-3535** — 'no data' overstated; the DelveInsight page gives minimal listing details (Preclinical, Obesity, Oral). Corrected to 'only minimal listing details, no mechanism or efficacy data.'
9. **MBX 5765 'amycretin prodrug' flagged as suspect** — amycretin is Novo's molecule; the MBX press release (could not be accessed) must be checked before repeating this label. The report now calls it a prodrug candidate with the label marked unverified.
10. **Amycretin Phase 2 T2D conflict flagged** — RemyPeptides gives 'up to 14.6% vs 2.1%', not the report's −14.5% vs −2.6%; the Lancet paper is the arbiter. The SC −24.3% / −13.1% figures are also not on that page.
11. **Viking preclinical codes / selectivity / Phase 1 timing** — NOT in the 2024 press release (which supports only the 8%/10% weight-loss figures). VK3019 Phase 1 + DACRA is supported by AllSci; the compound codes and ~1.4× selectivity need the ADA 2024 poster or a later source.
12. **AZD6234 trial details** — MedCityNews does not contain APRICUS/ARAY/ASCEND n's or timelines. ASCEND n=360 is verified via Close Concerns; APRICUS/ARAY need sources.
13. **Verdiva ADA / H2 2026 / XW015** — NOT in the Pharmaphorum article. Flagged as needing the Morningstar / ADA source (could not be accessed).
14. **EloraTZP 24.6 kg / NCT06603571 / two injections** — NOT in Reuters (which verified the core −23.3% vs −14.8% efficacy and discontinuation numbers). Those three details need the Pharmacy Times companion piece (could not be accessed).
15. **RAMP1 expression certainty downgraded** — the MDPI RAMP1 paper's own conclusion is that antibody IHC cannot confidently assign RAMP1 localization and expression 'needs to be revisited'. mRNA/binding summaries are not validated protein localization.
16. **RAMPs ~30% identity** — NOT found in the portion of the Nature Cell Discovery paper read. Flagged as needing a full-text check or a different citation.
17. **Davalintide preclinical 23 h / 8-week figures** — NOT in the News-Medical article (which verified the termination). Flagged as needing a preclinical source.
18. **Pramlintide '>2 inches' + counter-regulatory claims** — NOT found in the portion of the FDA label read (label says only a distinct site from insulin). Flagged as needing the full label.
19. **Cagrilintide structural details** — NOT in the Springer liraglutide review (which supports only the acylation analogy). They rest on Upmag (secondary). The report now makes the secondary nature explicit.
20. **Indigo AMY1-vs-AMY3 CGRP affinity comparison** — NOT on the Indigo page. Attribution removed.
21. **Wikipedia Amylin receptor CLR+RAMP1** — NOT on that page. Rests on Indigo (verified there).
22. **Zenagamtide dose / 13.1%** — NOT on Wikipedia Zenagamtide. Rests on the PeptideBenchmark blog (verified there as secondary).
23. **Cagrilintide organ-impairment PK** — NOT in the Lancet abstract. Rests on the Springer clinical-pharmacology paper (renal/hepatic conclusion verified; numeric PK needs the results tables).
24. **Petrelintide Tmax / BA** — NOT in Pharmacy Times. Rests on the Zealand deck (verified there). ZUPREME-2 rests on the GlobeNewswire topline (could not be accessed); Roche deal / Phase 3 enrollment figures are NOT in Pharmacy Times and are flagged.
25. **VTA mPFC / dopamine / GABA / fat-vs-sugar details** — NOT in PMC3717548 (which verified the core VTA findings). The extended circuit-mechanism details are attributed to the companion eNeuro paper (fat-vs-sugar dopamine verified from the abstract; circuit details need the full text).
26. **Drugs.com REDEFINE-4 page** — covers REDEFINE-4 only and is dated Feb 2026, after the report's Oct 2025 index date. It cannot be the Oct 2025 source for REDEFINE-1 numbers. REDEFINE-1 numbers (22.7% / 20.4%) need their original source; REDEFINE-4 numbers (23.0% / 25.5%) are supported by this page.
27. **KBP 'all preclinical / terminated' status** — cannot rest on the 2017 Pharmaceutical Technology article (which reports an active collaboration). Status needs a later source; rat efficacy / Q3D dosing likewise need other sources.
28. **Cagrilintide GI 41–63% / nausea 20–47%** — NOT found in the portion of the CJPP review read. Flagged as needing the full CJPP text or the Lancet Phase 2 paper (could not be accessed). The 2–6% vs liraglutide 7% figure IS verified via CJPP.
29. **Human amylin sequence citation** — the EP patent portion read did not contain the sequence. The sequence is standard textbook human amylin, but the citation is flagged as unverified-pending-full-patent.
30. **Pramlintide PK (HIGH-IMPACT GAP)** — the Drugs.com monograph carrying the report's core pramlintide PK numbers (bioavailability 30–40%, Tmax 19–21 min, Vd 0.35–0.83 L/kg, t1/2 ~48 min, protein binding ~60%, renal clearance) could not be accessed. All pramlintide PK numbers are flagged as unverified pending re-check against the label / monograph. The FDA label mirror verified the boxed warning and titration, but not the PK numbers.

## Per-source log

Entries are grouped by verdict. Within each group, sources are in report order (English-report order first, then Chinese-only sources).

## VERIFIED (22)

### 1. http://www.scientific-exchange.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/amylin-module4-infographic.pdf

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — Novo Nordisk educational infographic (industry material, largely preclinical-based)
- **Findings / corrections:** AP amylin-activated neurons mostly noradrenergic, minor 5-HT co-expression; AP is a CVO lacking BBB; plasma solutes reach AP neurons directly. Secondary/industry source, not primary data.
- **Report claims attributed to this source:**
  - EN line 96 (Part 2): | AP cell types | Amylin-activated neurons in AP are mostly noradrenergic, with minor 5-HT co-expression; norepinephrine participates in downstream signaling | Rodent | Satiety signal relay | — | Rodent | http://www.scientific-exchange.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/amylin-module4-infographic.pdf [index, 2026-10-15] |

### 2. https://pmc.ncbi.nlm.nih.gov/articles/PMC2171986/

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text, lines 0-190 of 481 (primary mouse-genetics paper)
- **Findings / corrections:** Amylin KO low bone mass via increased resorption, formation unaffected; in vitro amylin inhibits osteoclast precursor fusion via ERK1/2; compound Calcr+/- + Amylin+/- mice show both phenotypes ruling out CALCR as in vivo mediator (unidentified receptor); CALCR on osteoclasts not osteoblasts — all verified.
- **Report claims attributed to this source:**
  - EN line 114 (Part 2): | Bone (calcitonin-like) | Calcitonin → osteoclast CALCR → ↓ bone resorption, rapid ↓ serum Ca²⁺ (established physiology). Amylin bone effects: amylin KO mice have low bone mass (↑ bone resorption, bone formation unaffected); in vitro amylin inhibits osteoclast precursor fusion via ERK1/2. But Calcr⁺/⁻ + Amylin⁺/⁻ compound mice show both phenotypes, ruling out CALCR as the in vivo mediator of amylin inhibition of osteoclastogenesis → amylin bone effects act via an **unidentified receptor**, not AMY1–3 / CALCR. Human osteoblasts lack CTR expression, further weakening the human AMY bone claim | 

### 3. https://www.academia.edu/417929/Determinants_of_BIBN4096BS_Affinity_for_CGRP_and_Amylin_Receptors_the_Role_of_RAMP1

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — manuscript on Academia.edu (Hay et al., Mol Pharmacol 2006, primary)
- **Findings / corrections:** AMY1(a) ~150-fold less sensitive to BIBN4096BS than CGRP1; AMY3(a)/AM2 insensitive — verified.
- **Report claims attributed to this source:**
  - EN line 45 (Part 1): - **Antagonist cross-reactivity**: Migraine CGRP antagonists (e.g., BIBN4096BS / gepant class) may also antagonize AMY1; AMY1(a) is ~150-fold less sensitive to BIBN4096BS than the CGRP1 receptor; AMY3(a) / AM2 are insensitive. Source: https://www.academia.edu/417929/Determinants_of_BIBN4096BS_Affinity_for_CGRP_and_Amylin_Receptors_the_Role_of_RAMP1 [index, 2026-10-15]

### 4. http://pmc.ncbi.nlm.nih.gov/articles/PMC12992164/

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text, lines 0-163 of 371 (primary)
- **Findings / corrections:** Eloralintide AMY1R-selective agonist; SC once-weekly; ~2-week half-life; 1/3/6/9 mg arms; nausea 11-64% vs placebo 14% — verified as primary-source claims (worker read portion; later-section claims need remainder).
- **Report claims attributed to this source:**
  - ZH line 310 (Part 4): - **Eloralintide（LY3841136）**：SC 每周一次，**不是**口服——勿与名称混淆；选择性 AMY1R 激动剂。来源：http://pmc.ncbi.nlm.nih.gov/articles/PMC12992164/ ；https://pubmed.ncbi.nlm.nih.gov/41109426/ [index, 2026-10-15]
  - ZH line 359 (Part 4): - **Eloralintide**：长半衰期约 2 周（Phase 1b 论文：“约 2 周”）；次级总结：13–15 天；支持每周一次 SC。确切中位 Tmax / CL / Vd / 尿排泄：**未在检索来源中公开披露**。来源：http://pmc.ncbi.nlm.nih.gov/articles/PMC12992164/ [index, 2026-10-15]

### 5. https://en.wikipedia.org/wiki/Calcitonin_receptor

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — Wikipedia (secondary)
- **Findings / corrections:** Mouse Calcr expression (hypothalamus, nucleus accumbens, cerebellum, septum) — verified as secondary-source claims.
- **Report claims attributed to this source:**
  - EN line 76 (Part 1): | Hypothalamus (mouse) | Calcr enriched: arcuate nucleus (ARC), median eminence, dorsomedial nucleus (DMH), paraventricular nucleus (PVN), suprachiasmatic nucleus, lateral hypothalamus, ventromedial nucleus (VMH) — rodent, not equal to human evidence | https://en.wikipedia.org/wiki/Calcitonin_receptor [index, 2026-10-15] |
  - EN line 99 (Part 2): | Hypothalamus ARC / VMH / PVN | ARC POMC / CART (anorexigenic, α-MSH → MC4R in PVN / LHA) vs ARC AgRP / NPY (orexigenic, MC4R antagonists); PVN integrates ARC + hindbrain signals; VMH / DMH / LHA are secondary | Mouse Calcr enriched in ARC, median eminence, DMH, PVN, etc. (rodent); the cagrilintide study explicitly states ARC neuronal activation was not assessed, so AgRP / POMC-mediated anorexia / weight loss cannot be inferred from it; that study cites prior work stating POMC-neuron CTR signaling is required for energy-balance maintenance (via energy expenditure) | If activated, would regula

### 6. https://link.springer.com/article/10.1186/s12951-022-01743-9

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text — Springer SNAC paper (primary)
- **Findings / corrections:** Oral semaglutide F ~0.4-1%; SNAC local buffering/monomerization — verified.
- **Report claims attributed to this source:**
  - ZH line 307 (Part 4): - **SNAC 结果（Semaglutide 基准）**：绝对口服生物利用度提高至约 0.4–1%。来源：https://link.springer.com/article/10.1186/s12951-022-01743-9 [index, 2026-10-15]

### 7. https://nsuworks.nova.edu/hpd_corx_facarticles/29/

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — NSUWorks meta-analysis abstract page (secondary)
- **Findings / corrections:** HbA1c -0.33%; weight -2.57 kg — verified as abstract claims.
- **Report claims attributed to this source:**
  - EN line 172 (Part 3): | Pramlintide (Symlin) | Amylin Pharmaceuticals (originator) | Approved (2005-03-16, diabetes adjunct; **not a weight-loss indication**) | SC, immediately before meals, 2–3×/day | ~48 min | Meta-analysis: HbA1c −0.33%, weight −2.57 kg (insulin-treated T2D) | Boxed warning: severe hypoglycemia with insulin; nausea most common | https://www.drugs.com/pro/symlin.html ; https://nsuworks.nova.edu/hpd_corx_facarticles/29/ [index, 2026-10-15] |
  - EN line 198 (Part 3): - **Efficacy / safety**: Meta-analysis: HbA1c −0.33%, weight −2.57 kg (insulin-treated T2D); boxed warning: severe hypoglycemia with insulin. Source: https://nsuworks.nova.edu/hpd_corx_facarticles/29/ [index, 2026-10-15]

### 8. https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text, partial (Lutz review, primary)
- **Findings / corrections:** AP->NTS->LPBN circuit; postprandial amylin rise; vagotomy findings — verified. Later-section claims need the remainder.
- **Report claims attributed to this source:**
  - EN line 33 (Part 1): | Plasma levels (rodent) | Rats after overnight fast + 5 g meal: ~3–5 → 15–20 pmol/L, peaking within 5–10 minutes | https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/ [index, 2026-10-15] |
  - EN line 95 (Part 2): | Area Postrema (AP) | AP → NTS (dorsal vagal complex, DVC) → lateral parabrachial nucleus (LPBN) → hypothalamus / forebrain; AP is a circumventricular organ without a BBB | AP / NTS lesions abolish the anorectic effect of chronic peripheral amylin in rats; intra-AP injection of amylin antagonist AC187 increases food intake in rats; AP is required for amylin effects | Satiety / reduced meal size; primary hindbrain satiety node | AP CALCR+ neurons in mouse genetics suppress feeding without inducing avoidance (vs AP GLP1R+ neurons driving aversion) — suggesting satiety and nausea are separable, 
  - EN line 111 (Part 2): | Satiety / feeding | Peripheral amylin → central satiety (see AP / NTS / PBN / VTA) | Amylin KO mice: transient hyperphagia, ↑ adiposity; amylin antagonist AC187 ↑ feeding / meal size (peripheral or central); low near-physiological exogenous amylin (~2× postprandial levels) suppresses feeding in rats; pramlintide ↓ appetite in diabetes and non-diabetic obesity | ↓ meal size, ↓ energy intake — core weight-loss mechanism | Third-ventricle central amylin (100 pmol) ↓ rat feeding without conditioned taste aversion — supports non-aversive satiety at that dose / route in rodents | Established (huma
  - EN line 112 (Part 2): | Energy expenditure | Proposed: central amylin (AP / third ventricle) → sympathetic nerves → brown adipose tissue (BAT) thermogenesis; mechanism / site undetermined | Acute + chronic amylin ↑ energy expenditure in rodents; chronic peripheral amylin ↓ fat mass beyond pair-fed rats, with ↑ fat oxidation / energy expenditure; central amylin ↑ BAT sympathetic activity + core temperature (rats); RAMP1 overexpression ↑ BAT sympathetic activity + core temperature. Reviews state human studies "have not yet been performed" | If translatable, would prevent the expected energy-expenditure drop during we
  - EN line 339 (Part 4): - **AP access (NOT BBB crossing)**: The Area Postrema is a circumventricular organ with fenestrated capillaries and no BBB features; plasma drugs diffuse through leaky AP capillaries to AP neurons **without crossing the BBB itself**. AP access is the start of the central relay (AP → NTS → LPBN). Sources: https://www.nature.com/articles/ijosup20164 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/ [index, 2026-10-15]
  - EN line 344 (Part 4): - **Vagal signaling**: Vagal efferents carry the AP signal to the gut to slow gastric emptying; vagal afferents are **not required** for amylin's anorectic effect (subdiaphragmatic vagotomy does not block it). Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/ [index, 2026-10-15]

### 9. https://www.drugs.com/drug-interactions/pramlintide-with-tipranavir-1926-0-2203-0.html?professional=1

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text — Drugs.com interaction page (secondary)
- **Findings / corrections:** Acetaminophen Cmax down 29%, Tmax 48-72 min — verified.
- **Report claims attributed to this source:**
  - ZH line 346 (Part 4): - **胃 / 肠道——胃排空**：AP 刺激 → 迷走传出调节 → 胃排空减慢而不改变营养素总体吸收 → 葡萄糖出现减慢 + 饱感。对其他口服药物的影响：延迟吸收——例如对乙酰氨基酚 Cmax ↓ 29%、Tmax 延至 48–72 分钟（与 Pramlintide 同时 / 2 小时内给药）。来源：https://www.novonordisk.com/content/dam/nncorp/global/en/science-and-technology/pdfs/medical-affairs/amylin-physiology-interactive-module.pdf ；https://www.drugs.com/drug-interactions/pramlintide-with-tipranavir-1926-0-2203-0.html?professional=1 [index, 2026-10-15]

### 10. https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2013.00042/full

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text, partial (primary review)
- **Findings / corrections:** Insulin:amylin ratio conflict framing (~100:1, ~20:1, rat 100:2.3/100:2.6, ~12%) — verified as framing; specific ratios need the remainder for full confirmation.
- **Report claims attributed to this source:**
  - EN line 30 (Part 1): | Insulin : Amylin molar ratio | **Conflicting; no single verified value**: ~100:1 (insulin : amylin); ~20:1; rat fasting 100:2.3, fed 100:2.6; one review states amylin is ~12% of insulin. Results differ by assay / species; any citation must state the assay and species | https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://www.researchgate.net/publication/251247194_Understanding_Amylin_Receptors ; https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2013.00042/full [index, 2026-10-15] |
  - EN line 102 (Part 2): | Hippocampus | Hippocampal CA1 → LTP (memory proxy); AMY3 proposed as Aβ receptor | Aβ1-42 (50 nM) + human amylin (50 nM) inhibit mouse slice hippocampal LTP; AC253 (250 nM) blocks both without affecting baseline / isolated LTP; LTP impairment in TgCRND8 mice improved by AC253 (mouse slices / transgenic) | No established weight-loss role; relevance is Alzheimer's / cognition hypothesis, not an obesity pathway | No established metabolic adverse effect; AMYR antagonism is a research AD direction, opposite to the obesity agonist direction | Emerging, AD-related only | https://www.jneurosci.org/c

### 11. https://journals.plos.org/plosone/article/figure?id=10.1371/journal.pone.0097592.g003

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — figure legend (primary)
- **Findings / corrections:** RAMP2 in human thymus: cortical/medullary epithelium, Hassall's bodies, vessels/mast cells — single-tissue IHC, not whole-body map — verified. (Caption spells 'Hassal's bodies'; trivial spelling variant.)
- **Report claims attributed to this source:**
  - EN line 84 (Part 1): | RAMP2 (overall) | Widespread; human thymus: cortical / medullary epithelium, Hassall's corpuscles, vessels / mast cells — single-tissue IHC, not a whole-body map | https://journals.plos.org/plosone/article/figure?id=10.1371/journal.pone.0097592.g003 [index, 2026-10-15] |

### 12. https://link.springer.com/article/10.1186/s13075-024-03361-2

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text, partial lines 0-155 of 752 (primary)
- **Findings / corrections:** KBP-336 DACRA in preclinical OA model: antiresorptive + analgesic + weight-loss effects — verified (abstract/intro). CTR activation -> inhibition of osteoclastic resorption — verified. Later-line histology/bone-protection detail beyond portion read.
- **Report claims attributed to this source:**
  - ZH line 349 (Part 4): - **骨**：CTR 激活 → 抑制破骨细胞吸收；啮齿类数据：抑制骨吸收，可能刺激骨形成。DACRA（如 KBP-336）在临床前 OA 模型中显示抗吸收 + 镇痛 + 减重效应。Amylin 激动剂的人类治疗性骨效应**未确立**——由降钙素生物学 + 啮齿类数据外推。来源：https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810 ；https://link.springer.com/article/10.1186/s13075-024-03361-2 [index, 2026-10-15]

### 13. https://www.globenewswire.com/news-release/2026/09/22/3366613/0/en/zealand-pharma-announces-initiation-of-the-registrational-phase-3-zupreme-program-of-petrelintide-in-people-with-overweight-or-obesity.html

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text — company press release (secondary)
- **Findings / corrections:** Petrelintide + enicepatide (CT-388): Phase 2 combo trial planned H2 2026; no data; co-formulation planned; petrelintide designed for co-formulation — verified. Enicepatide = Roche dual GLP-1/GIP agonist (formerly CT-388) — verified. Claim appears in Chinese only.
- **Report claims attributed to this source:**
  - ZH line 224 (Part 3): **Petrelintide + Enicepatide（CT-388）——Roche / Zealand**：Zealand Pharma + Roche；Enicepatide = Roche 双 GLP-1 / GIP 激动剂（原 CT-388）。Phase 2 联合试验计划于 2026 年下半年启动；无数据。未获批。给药：计划共配制 / 联合给药（Petrelintide 专为共配制设计）；细节未披露。半衰期 / 疗效 / 安全性：无联合数据公开披露。来源：https://www.globenewswire.com/news-release/2026/09/22/3366613/0/en/zealand-pharma-announces-initiation-of-the-registrational-phase-3-zupreme-program-of-petrelintide-in-people-with-overweight-or-obesity.html [index, 2026-10-15]

### 14. https://www.mdpi.com/1999-4923/18/4/466

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text, partial lines 0-148 of 487 (primary review/perspective)
- **Findings / corrections:** SNAC = sodium N-(8-[2-hydroxybenzoyl]amino)caprylate; tablet erodes in stomach -> SNAC buffers local pH, interferes with pepsinogen activation -> protects from enzymatic degradation + promotes monomerization; fluidizes gastric lipid membrane -> increased transcellular permeability; dosing: fasting, <=120 mL water, wait >=30 min before food/other oral drugs — verified. Claim appears in Chinese only.
- **Report claims attributed to this source:**
  - ZH line 306 (Part 4): - **SNAC 机制（口服 Semaglutide 模型）**：SNAC = N-(8-[2-羟基苯甲酰基]氨基)辛酸钠 / Salcaprozate Sodium；片剂在胃内崩解 → SNAC 缓冲局部 pH、干扰胃蛋白酶原激活 → 保护免受酶降解 + 促进单体化；使胃脂质膜流化 → 增加跨细胞通透性。给药：空腹、≤ 120 mL 水、等待 ≥ 30 分钟再进食 / 其他口服药物。来源：https://www.mdpi.com/1999-4923/18/4/466 [index, 2026-10-15]

### 15. https://www.medchemexpress.eu/gene/10268.html

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — vendor gene page (secondary)
- **Findings / corrections:** RAMP3 widely expressed: lung RPKM 28.4, lymph node 13.1 + 20 other tissues (NCBI/RefSeq summary via vendor) — verified verbatim.
- **Report claims attributed to this source:**
  - EN line 85 (Part 1): | RAMP3 (overall) | Widely expressed: lung RPKM 28.4, lymph node 13.1 + 20 other tissues (NCBI / RefSeq summary via vendor) | https://www.medchemexpress.eu/gene/10268.html [index, 2026-10-15] |

### 16. https://www.zealandpharma.com/media/vrypyzy1/zealand-pharma-at-obesity-week-2024.pdf

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text, partial lines 0-619 of 681 — company slide deck (secondary, largely 'data on file')
- **Findings / corrections:** Petrelintide: 36-amino-acid acylated peptide based on human amylin; SC once-weekly; potent amylin + calcitonin receptor agonist; chemically/physically stable at neutral pH, minimal fibrillation; 0.6-9.0 mg Cmax + AUCtau dose-proportional; steady-state Tmax 24 h; SC bioavailability 85%; terminal half-life ~240 h (~10 days), supports once-weekly dosing — verified. ZUPREME-1/2 efficacy numbers in the long Chinese claim are NOT in this 2024 Phase 1b deck (correctly attributed by the report to other sources).
- **Report claims attributed to this source:**
  - ZH line 198 (Part 3): **Petrelintide（ZP8396）**：Zealand Pharma 原研；自 2025 年起与 Roche 共同开发 / 共同商业化（最高 53 亿美元交易）。Phase 2 完成；Phase 3 ZUPREME-3/4/5 注册项目于 2026 年 9 月启动（总计约 7,000 名参与者）。未获批。机制：长效人 Amylin 类似物；强效 Amylin + 降钙素受体激动剂；经工程化实现稳定性 / 中性 pH 下无纤维化（可共配制）。皮下注射，每周一次；Phase 2 剂量 1.0–9.0 mg，起始 0.5 mg，每 4 周递增。半衰期约 240 小时（约 10 天），Tmax 约 24 小时，SC 生物利用度约 85%，0.6–9.0 mg 剂量成比例 PK。疗效：ZUPREME-1（Phase 2，n = 493，肥胖 / 超重无 T2D）：第 28 周减重 7.9–9.8%（1–9 mg）vs 安慰剂 1.7%；第 42 周 8.7–10.7% vs 安慰剂约 1.7%（治疗策略：高达 10.2% vs 1.4%）；5 mg 以上达平台；34–56% 减重 ≥ 10%（第 42 周）vs 安慰剂 9%。ZUPREME-2（Phase 2，NCT06926842，n = 220，超重 / 肥胖 + T2D，28 周）：减重 7.4–9.2% vs 安慰剂 2.
  - ZH line 311 (Part 4): - **Petrelintide（ZP8396）**：SC 每周一次；36 氨基酸酰化肽，基于人 Amylin。来源：https://www.zealandpharma.com/media/vrypyzy1/zealand-pharma-at-obesity-week-2024.pdf [index, 2026-10-15]
  - ZH line 318 (Part 4): - **脂肪酸酰化 / 白蛋白结合——半衰期延长**：Cagrilintide：Pramlintide 样骨架 + 3 个取代（N14E、V17R、P37Y）+ N 端 C20 二十烷二酸脂肪二酸经 γ-Glu 接头 → 促进可逆白蛋白结合 → 清除显著延长（vs 未修饰 Amylin 类似物）。Eloralintide：Amylin 类似物偶联 C20 脂肪二酸实现可逆白蛋白结合；经工程化实现高 AMY1R 效力 / 选择性、低纤维化 / 自聚集风险、长血浆半衰期。Petrelintide：酰化肽；确切酰基链 / 白蛋白结合 % **未在检索来源中公开披露**（仅“酰化”）。通用酰化效应（以利拉鲁肽为类比——**勿将 % 转移至 Cagrilintide**）：SC 吸收减慢 + 经减慢代谢 / 肾滤过降低消除 → Tmax 延迟、半衰期延长。**Cagrilintide 血浆蛋白 / 白蛋白结合 % 未在检索来源中公开披露**。来源：https://upmag.com/cagrilintide-peptide-research-amylin-receptor-pharmacology-and-the-purity-verification-standards-behind-the-compound/ ；https://waltersport.com/wp-content/upl
  - ZH line 319 (Part 4): - **Petrelintide**：0.6–9.0 mg Cmax + AUCtau 剂量成比例；稳态 Tmax 24 小时；SC 生物利用度先前确定为 85%（Zealand 存档资料 deck）。来源：https://www.zealandpharma.com/media/vrypyzy1/zealand-pharma-at-obesity-week-2024.pdf [index, 2026-10-15]
  - ZH line 344 (Part 4): - **受体基础**：Amylin 受体 = CTR 核心（降钙素受体，Class B GPCR）+ RAMP1 / 2 / 3 → AMY1R / AMY2R / AMY3R。Cagrilintide = 双 Amylin + 降钙素受体激动剂（DACRA，非选择性）；Eloralintide = AMY1R 选择性（人 assay 中约 12 倍 > CTR、约 11 倍 > AMY3R）；Petrelintide = 强效 Amylin + 降钙素受体激动剂。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC12410446/ ；https://pubmed.ncbi.nlm.nih.gov/41109426/ ；https://www.zealandpharma.com/media/vrypyzy1/zealand-pharma-at-obesity-week-2024.pdf [index, 2026-10-15]
  - ZH line 360 (Part 4): - **Petrelintide**：终末半衰期约 240 小时（约 10 天）已确认；支持每周一次给药；中性 pH 下化学 / 物理稳定，纤维化最小。来源：https://www.zealandpharma.com/media/vrypyzy1/zealand-pharma-at-obesity-week-2024.pdf ；https://www.pharmacytimes.com/view/petrelintide-yields-up-to-10-7-weight-loss-with-mild-gi-effects [index, 2026-10-15]

### 17. http://www.scientific-exchange.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/amylin-module3-infographic.pdf

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — Novo Nordisk educational infographic (industry material)
- **Findings / corrections:** Gs->cAMP/PKA in vitro; AC187 blocks; Gs/Gi biased agonism at AMY3; Gq/ERK for CGRP — verified.
- **Report claims attributed to this source:**
  - EN line 49 (Part 1): - **Main pathway**: Gs → adenylyl cyclase → cAMP ↑ → PKA; simultaneously acute ↑ pERK1/2 and Akt, c-Fos / appetite-gene activation; the mapping of individual pathways to specific effects / subtypes is only partially established. Source: http://www.scientific-exchange.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/amylin-module3-infographic.pdf [index, 2026-10-15]

### 18. https://cckb.closeconcerns.com/r/7a45f1f8/pdf

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text — Close Concerns conference memo (secondary)
- **Findings / corrections:** ASCEND Phase 2 n=360, AZD9550 + AZD6234 (1.5/3.5/7.5 mg), data 2H26 — verified. The memo's claims stand.
- **Report claims attributed to this source:**
  - ZH line 226 (Part 3): **AZD9550 + AZD6234——AstraZeneca**：Phase 2b ASCEND（n = 360，肥胖 / 超重 + ≥1 合并症），数据预计 2026 年下半年；检索来源中无结果。组分：AZD9550 = 双 GLP-1 / 胰高血糖素 RA；AZD6234 = 选择性 Amylin RA（见上）。来源：https://cckb.closeconcerns.com/r/7a45f1f8/pdf [index, 2026-10-15]

### 19. https://en.wikipedia.org/wiki/Amylin

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — Wikipedia (secondary)
- **Findings / corrections:** Human amylin sequence; proline substitutions at 25, 26, 29; proline disruption of beta-sheet — verified. RELEVANT TO SUBSTITUTION CONFLICT: Wikipedia says 25, 26, 29; other literature says 25, 28, 29. Conflict is real; PMID 17393306 supports neither side (see below).
- **Report claims attributed to this source:**
  - EN line 27 (Part 1): | Identity | 37-amino-acid peptide hormone, also called Islet Amyloid Polypeptide (IAPP); Cys2–Cys7 disulfide bond + C-terminal amide; processed from an 89-amino-acid precursor / 67-amino-acid proIAPP | https://en.wikipedia.org/wiki/Amylin [index, 2026-10-15] |
  - EN line 31 (Part 1): | Physiological roles | Delays gastric emptying, suppresses postprandial glucagon, promotes satiety / fullness, prevents sharp postprandial glucose spikes | https://en.wikipedia.org/wiki/Amylin [index, 2026-10-15] |

### 20. https://mdpi-res.com/d_attachment/pharmaceutics/pharmaceutics-18-01171/article_deploy/pharmaceutics-18-01171.pdf

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text, lines 0-170 of 318 (SNAC review, primary)
- **Findings / corrections:** SNAC mechanism: stomach pH buffering, pepsinogen activation interference, monomerization, gastric lipid membrane fluidization -> transcellular permeability; fasting + <=120 mL water + >=30 min wait — verified.
- **Report claims attributed to this source:**
  - ZH line 303 (Part 4): - **口服肽屏障（通用）**：胃酸 + 蛋白水解酶（胃蛋白酶、胰蛋白酶、糜蛋白酶、肽酶）快速降解肽链；大分子量、亲水性、电荷阻碍跨细胞 + 细胞旁通道；多数天然肽口服生物利用度可忽略。来源：https://mdpi-res.com/d_attachment/pharmaceutics/pharmaceutics-18-01171/article_deploy/pharmaceutics-18-01171.pdf [index, 2026-10-15]

### 21. https://peptidebenchmark.com/blog/amycretin-next-generation-obesity-drug-oral-subcutaneous-phase-3/

- **Verdict:** verified
- **Cited in:** Chinese original
- **What was read:** full text — PeptideBenchmark blog (secondary)
- **Findings / corrections:** Oral amycretin Phase 1 13.1% vs placebo 1.1% at 12 wks; SC Phase 1b/2a 24.3% (20 mg) / 13.1% (1.25 mg) at 36 wks; SC Phase 2 T2D ~14.6% at 36 wks; Phase 2b/3 program — verified as secondary-source claims. Blog calls SC Phase 1b/2a numbers '22%' in another place — internal inconsistency noted; Lancet paper is the arbiter.
- **Report claims attributed to this source:**
  - ZH line 312 (Part 4): - **口服 Amylin 通路尝试——Amycretin / Zenagamtide（NN9487）**：单分子双 GLP-1 + Amylin 受体激动剂；口服剂型含 SNAC 作为促渗剂；SC 剂型平行（无 SNAC）；口服 Phase 1 测试两种 SNAC 剂型，剂量高达每日两片 50 mg，长达 12 周；早期报告最高剂量 12 周减重约 13.1%。来源：https://en.wikipedia.org/wiki/Zenagamtide ；https://peptidebenchmark.com/blog/amycretin-next-generation-obesity-drug-oral-subcutaneous-phase-3/ [index, 2026-10-15]

### 22. https://upmag.com/cagrilintide-peptide-research-amylin-receptor-pharmacology-and-the-purity-verification-standards-behind-the-compound/

- **Verdict:** verified
- **Cited in:** English report, Chinese original
- **What was read:** full text — Upmag blog (secondary, commercial)
- **Findings / corrections:** Secondary/commercial caveat noted. Cagrilintide substitutions N14E/V17R/P37Y, C20 fatty diacid via gamma-Glu, half-life 159-195 h, 2.4 mg weekly, AC187 antagonism, amylin receptor family — verified as secondary-source claims.
- **Report claims attributed to this source:**
  - EN line 55 (Part 1): - **Cryo-EM (cagrilintide)**: A secondary-source summary states that an *Acta Pharmacologica Sinica* cryo-EM study depicted cagrilintide acting on AMY1R + CTR via "bypass" binding, with roughly comparable potency at AMY1R / CTR in a cAMP assay; the original Acta paper was not directly verified in the retrieved text for this synthesis and is labeled **secondary source**. Source: https://upmag.com/cagrilintide-peptide-research-amylin-receptor-pharmacology-and-the-purity-verification-standards-behind-the-compound/ [index, 2026-10-15]
  - EN line 204 (Part 3): - **PK**: ~7–8 day half-life (**secondary source**); protein binding, Vd / CL, proteases, urinary fraction **not publicly disclosed**. Source: https://upmag.com/cagrilintide-peptide-research-amylin-receptor-pharmacology-and-the-purity-verification-standards-behind-the-compound/ [index, 2026-10-15]

## CORRECTED (39)

### 1. https://cdnsciencepub.com/doi/10.1139/cjpp-2025-0151

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text (commentary/review), lines 0-133 of 246 read
- **Findings / corrections:** Cagrilintide GI AEs dose-dependent 2-6% vs liraglutide 7% verified. GI AEs 41-63% vs placebo 32%; nausea 20-47% NOT found in portion read — do not cite this source for those figures without reading the remainder.
- **Report claims attributed to this source:**
  - EN line 158 (Part 2): - **Human (cagrilintide)**: GI adverse events dose-dependent, 2–6% in a 26-week trial (one summary) vs liraglutide 7% — trial-specific, not a class rate. Source: https://cdnsciencepub.com/doi/10.1139/cjpp-2025-0151 [index, 2026-10-15]
  - EN line 206 (Part 3): - **Safety**: GI adverse events 41–63% vs placebo 32%; nausea 20–47%; fatigue, injection-site reactions. Source: https://cdnsciencepub.com/doi/10.1139/cjpp-2025-0151 [index, 2026-10-15]

### 2. https://en.wikipedia.org/wiki/Amylin_receptor

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — Wikipedia (secondary)
- **Findings / corrections:** AMY1/2/3 = CTR+RAMP1/2/3; secretin-family; human CGRP higher affinity for AMY1 than AMY3; AMY2 affinity less understood — verified. Classical CGRP receptor = CLR+RAMP1 NOT on this page — must rest on the Indigo source.
- **Report claims attributed to this source:**
  - EN line 41 (Part 1): - **Definition**: Each amylin receptor = calcitonin receptor CTR (CALCR) + one RAMP: AMY1 = CTR + RAMP1, AMY2 = CTR + RAMP2, AMY3 = CTR + RAMP3. Class B / Secretin-family GPCRs. Source: https://en.wikipedia.org/wiki/Amylin_receptor [index, 2026-10-15]
  - EN line 44 (Part 1): - **CGRP receptor cross-reactivity**: The classical CGRP receptor = CLR (CALCRL) + RAMP1; AMY1 also binds CGRP with high affinity because it shares RAMP1; human CGRP has higher affinity for AMY1 than AMY3, and AMY2 affinity is less well understood. Sources: https://indigobiosciences.com/understanding-the-amylin-receptor-family/ ; https://en.wikipedia.org/wiki/Amylin_receptor [index, 2026-10-15]

### 3. https://encyclopedia.pub/entry/history/compare_revision/39791

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — MDPI Encyclopedia comparison page (secondary, AD-focused)
- **Findings / corrections:** CTR+RAMPs expressed in brain incl. hippocampus, cortex, locus coeruleus — verified. Lateral hypothalamus / BNST / accumbens as downstream (not direct activation sites) is NOT established by this source.
- **Report claims attributed to this source:**
  - EN line 103 (Part 2): | Other brain regions (locus coeruleus, cortex, hippocampus, septum, lateral hypothalamus, BNST, nucleus accumbens) | — | Expression reports only (AD review: CTR + RAMPs in brain including hippocampus, cortex, locus coeruleus); lateral hypothalamus, BNST, nucleus accumbens are downstream of PBN / VTA circuits, not shown to be direct amylin receptor activation sites | — | — | Expression only / unverified function | https://encyclopedia.pub/entry/history/compare_revision/39791 [index, 2026-10-15] |

### 4. https://ir.vikingtherapeutics.com/2024-06-24-Viking-Therapeutics-Presents-Preclinical-Data-on-Novel-Dual-Amylin-and-Calcitonin-Receptor-Agonists-at-84th-Scientific-Sessions-of-the-American-Diabetes-Association

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — company press release, June 2024 (secondary/industry)
- **Findings / corrections:** Single SC dose up to 8% weight loss in 72 h in lean rats; DIO mice up to 10% over 24 days comparable to cagrilintide — verified. Compound codes VK3012/VK3006/VK3015, VK3012 ~1.4x selectivity, VK3019 Phase 1 timing NOT in this 2024 release — need a different/later source.
- **Report claims attributed to this source:**
  - EN line 180 (Part 3): | Viking DACRA (VK3012 / VK3006 / VK3015; VK3019) | Viking Therapeutics | Preclinical series (no candidate selected); VK3019 entered Phase 1 single-ascending-dose in Jun 2026 | SC (preclinical / Phase 1 SAD) | Not publicly disclosed | Preclinical only: single SC dose → up to 8% weight loss in 72 h in lean rats; DIO mice up to 10% over 24 days of treatment, comparable to cagrilintide | No human safety data | https://ir.vikingtherapeutics.com/2024-06-24-Viking-Therapeutics-Presents-Preclinical-Data-on-Novel-Dual-Amylin-and-Calcitonin-Receptor-Agonists-at-84th-Scientific-Sessions-of-the-American-
  - EN line 242 (Part 3): - VK3012 / VK3006 / VK3015 series (no candidate selected); VK3019 entered Phase 1 SAD Jun 2026. Preclinical: single SC dose → up to 8% weight loss in 72 h in lean rats; DIO mice up to 10% over 24 days, comparable to cagrilintide. Source: https://ir.vikingtherapeutics.com/2024-06-24-Viking-Therapeutics-Presents-Preclinical-Data-on-Novel-Dual-Amylin-and-Calcitonin-Receptor-Agonists-at-84th-Scientific-Sessions-of-the-American-Diabetes-Association [index, 2026-10-15]

### 5. https://link.springer.com/article/10.1007/s40262-026-01654-0

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text, lines 0-174 of 614 (abstract + methods start)
- **Findings / corrections:** Single-dose renal (0.6 mg) / hepatic (0.9 mg) impairment: no PK effect; dose adjustment unlikely; small samples; CL/F and Vz/F exploratory — verified. Numeric Vd/CL, half-life 159-195 h / 184 +/- 7.4 h, AUC/Cmax ranges NOT in portion read — need results tables.
- **Report claims attributed to this source:**
  - ZH line 324 (Part 4): - **Cagrilintide**：Phase 1b：血浆清除率 + Vd “各治疗组相似”——数值 Vd / CL **未在摘要 / 检索来源中公开披露**；PK 剂量成比例 + 线性；暴露主要由表观清除率（CL/F）决定；AUC = 剂量 / (CL/F)。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_ ；https://link.springer.com/article/10.1007/s40262-026-01654-0 [index, 2026-10-15]
  - ZH line 348 (Part 4): - **肾**：Amylin 结合位点见于肾；肾是 Amylin + Pramlintide 主要清除 / 蛋白水解部位（见第六步）。Cagrilintide：单剂量肾或肝损害未影响 PK / 安全性 / 耐受性 → 作者结论剂量调整可能性低（局限：单次低剂量 0.6 mg 肾 / 0.9 mg 肝，非 2.4 mg 维持剂量，重度损害组样本小）。仅假说：Amylin 激动剂可能激活肾素–血管紧张素系统（RAS）→ 可能削弱心肾获益；RAS 阻断被假设可重定向至保护性 Ang-(1–7) / Mas 通路——**假说，非确立**。来源：https://www.medscape.com/viewarticle/523581_4 ；https://link.springer.com/article/10.1007/s40262-026-01654-0 ；https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)01776-3/abstract [index, 2026-10-15]
  - ZH line 358 (Part 4): - **Cagrilintide**：半衰期 Phase 1b 中 159–195 小时（0.16–4.5 mg + Semaglutide）；另一综述：2.4 mg 时 184 ± 7.4 小时；支持每周一次给药。肾 / 肝损害单剂量研究：无 PK 效应 → 剂量调整可能性低（低剂量 / 小样本局限如上）。蛋白酶 / 排泄途径（完整 vs 片段、尿比例）：**未公开披露**。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_ ；https://link.springer.com/article/10.1007/s40262-026-01654-0 [index, 2026-10-15]

### 6. https://medcitynews.com/2026/01/astrazeneca-obesity-diabetes-cspc-glp-1-gip-agonist-metabolic-disease-azn/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — news article (secondary)
- **Findings / corrections:** AZD6234 weekly injectable selective amylin receptor agonist, Phase 2, chronic weight management — verified. APRICUS n=262 / ARAY n=64 / ASCEND n=360, readout timelines, AZD9550 combination NOT in this article — need other sources.
- **Report claims attributed to this source:**
  - EN line 177 (Part 3): | AZD6234 | AstraZeneca | Phase 2 (one 2026 landscape table calls it Phase III, **conflicting** with AZ's own Phase 2 description; use Phase 2 until AZ confirms) | SC, once weekly | Not publicly disclosed | No publicly disclosed efficacy results (APRICUS / ARAY / ASCEND readouts not found) | Not publicly disclosed | https://medcitynews.com/2026/01/astrazeneca-obesity-diabetes-cspc-glp-1-gip-agonist-metabolic-disease-azn/ [index, 2026-10-15] |
  - EN line 230 (Part 3): - AstraZeneca selective amylin receptor agonist; weekly SC; designed to be combined with AZD9550 (dual GLP-1 / glucagon agonist) in the Phase 2b ASCEND combination. No public efficacy results; Phase 2 per AZ's own description (one 2026 landscape table calls it Phase III — conflicting). Source: https://medcitynews.com/2026/01/astrazeneca-obesity-diabetes-cspc-glp-1-gip-agonist-metabolic-disease-azn/ [index, 2026-10-15]

### 7. https://pharmaphorum.com/news/verdiva-bio-raises-411m-obesity-pipeline

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text — news article (secondary)
- **Findings / corrections:** VRB-103 once-weekly oral amylin agonist; VRB-102 long-acting SC amylin agonist; both preclinical, licensed from Sciwind; mono + GLP-1 combo planned — verified. In vitro potency/selectivity (ADA 2026), H2 2026 clinical entry, DelveInsight listing, XW015 NOT in this article — need other sources.
- **Report claims attributed to this source:**
  - ZH line 230 (Part 3): **Verdiva / Sciwind Amylin 候选**：VRB-103（每周一次口服 Amylin 类似物，肽）——Verdiva Bio（自 Sciwind 许可）；临床前；体外对人 Amylin 受体高 potency / 选择性（ADA 2026 临床前数据）；预计 2026 年下半年进入临床，作为单药及 + VRB-101（口服 GLP-1）；无人类数据。VRB-102（长效 SC Amylin 激动剂）——Verdiva / Sciwind；临床前；计划作为单药及 + GLP-1；检索来源中无数据。VRB-101 + VRB-103 列为 DelveInsight 管线中临床前口服联合。XW015——列为临床前 SC 候选（见上）。来源：https://pharmaphorum.com/news/verdiva-bio-raises-411m-obesity-pipeline ；https://www.morningstar.com/news/business-wire/20260605931887/verdiva-bio-presents-preclinical-data-on-investigational-obesity-drug-candidates-at-the-american-diabetes-association-86th-scientific-

### 8. https://pmc.ncbi.nlm.nih.gov/articles/PMC5503810/

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text, lines 0-181 of 766 (LDTg paper, primary)
- **Findings / corrections:** LDTg amylin-receptor expression and intra-LDTg effects (amylin decreases intake over 6 h, not 24 h; sCT over 24 h) verified. Hypothalamic 8-h figure and VTA/NAc specifics are NOT this paper's experiments. Do not cite this LDTg paper for hypothalamic 8-h effect or VTA/NAc specifics.
- **Report claims attributed to this source:**
  - ZH line 338 (Part 4): - **直接注射研究**：显示受体在直接放置药物时*功能存在*，但**不证明**全身药物到达该处：下丘脑内 Amylin 减少进食 8 小时；VTA 内 / 伏隔核内 / LDTg 内 Amylin 受体信号调节摄入 / 奖赏。来源：https://www.sciencedirect.com/science/article/abs/pii/000689939191644G ；https://pmc.ncbi.nlm.nih.gov/articles/PMC5503810/ ；https://www.nature.com/articles/ijosup20164 [index, 2026-10-15]
  - ZH line 347 (Part 4): - **脑——AP / NTS / LPB-PBN / 下丘脑 / VTA / LDTg / 伏隔核**：AP = 首要传感器；NTS + LPB = 中继；下丘脑 = 稳态饱感；VTA / LDTg / 伏隔核 = 奖赏 / 动机进食；亦恢复瘦素反应性（临床前）。功能结局：↓ 摄食、↑ 饱感、↓ 体重。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/ ；https://www.novonordiskmedical.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/the-physiological-functions-of-amylin.pdf ；https://pmc.ncbi.nlm.nih.gov/articles/PMC5503810/ [index, 2026-10-15]

### 9. https://pubmed.ncbi.nlm.nih.gov/41109426/

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** abstract only — PubMed abstract (full text not read)
- **Findings / corrections:** Eloralintide AMY1R-selective; human ~12-fold > CTR, ~11-fold > AMY3R — verified. Eloralintide SC once-weekly, not oral — route NOT stated in abstract text read; needs full text.
- **Report claims attributed to this source:**
  - ZH line 310 (Part 4): - **Eloralintide（LY3841136）**：SC 每周一次，**不是**口服——勿与名称混淆；选择性 AMY1R 激动剂。来源：http://pmc.ncbi.nlm.nih.gov/articles/PMC12992164/ ；https://pubmed.ncbi.nlm.nih.gov/41109426/ [index, 2026-10-15]
  - ZH line 344 (Part 4): - **受体基础**：Amylin 受体 = CTR 核心（降钙素受体，Class B GPCR）+ RAMP1 / 2 / 3 → AMY1R / AMY2R / AMY3R。Cagrilintide = 双 Amylin + 降钙素受体激动剂（DACRA，非选择性）；Eloralintide = AMY1R 选择性（人 assay 中约 12 倍 > CTR、约 11 倍 > AMY3R）；Petrelintide = 强效 Amylin + 降钙素受体激动剂。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC12410446/ ；https://pubmed.ncbi.nlm.nih.gov/41109426/ ；https://www.zealandpharma.com/media/vrypyzy1/zealand-pharma-at-obesity-week-2024.pdf [index, 2026-10-15]
  - ZH line 366 (Part 4): - **恶心 / 呕吐机制**：AP = 化学感受器触发区 / 呕吐回路；AP + NTS 激活 → 恶心 / 呕吐；剂量依赖，起始 / 递增期最重，随时间 / 耐受减轻。Pramlintide 说明书：恶心起始较高，随时间下降；逐渐滴定使发生率 / 严重程度最小化。T2D 汇总试验：恶心 28%（Symlin 120 mcg BID + 胰岛素）vs 安慰剂 12%；呕吐 8% vs 4%；头痛 13% vs 7%；厌食 9% vs 2%。来源：https://www.medicinenet.com/side_effects_of_symlin_pramlintide/side-effects.htm ；https://www.drugs.com/pro/symlin.html [index, 2026-10-15]。Cagrilintide Phase 1b：胃肠疾病占不良事件 37%（207/566），多为轻中度。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_sem

### 10. https://waltersport.com/wp-content/uploads/2025/12/LANCET-Elorantide-Billings-et-al.-2025.pdf

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text, lines 0-399 of 1929 (Lancet Phase 2 paper PDF on third-party mirror)
- **Findings / corrections:** Eloralintide: amylin analogue conjugated to C20 fatty diacid for reversible albumin binding; engineered high AMY1R potency/selectivity, low fibrillation/self-aggregation risk, long half-life — verified. Cagrilintide N14E/V17R/P37Y + C20 via gamma-Glu; petrelintide acyl details NOT in this eloralintide-only paper.
- **Report claims attributed to this source:**
  - ZH line 318 (Part 4): - **脂肪酸酰化 / 白蛋白结合——半衰期延长**：Cagrilintide：Pramlintide 样骨架 + 3 个取代（N14E、V17R、P37Y）+ N 端 C20 二十烷二酸脂肪二酸经 γ-Glu 接头 → 促进可逆白蛋白结合 → 清除显著延长（vs 未修饰 Amylin 类似物）。Eloralintide：Amylin 类似物偶联 C20 脂肪二酸实现可逆白蛋白结合；经工程化实现高 AMY1R 效力 / 选择性、低纤维化 / 自聚集风险、长血浆半衰期。Petrelintide：酰化肽；确切酰基链 / 白蛋白结合 % **未在检索来源中公开披露**（仅“酰化”）。通用酰化效应（以利拉鲁肽为类比——**勿将 % 转移至 Cagrilintide**）：SC 吸收减慢 + 经减慢代谢 / 肾滤过降低消除 → Tmax 延迟、半衰期延长。**Cagrilintide 血浆蛋白 / 白蛋白结合 % 未在检索来源中公开披露**。来源：https://upmag.com/cagrilintide-peptide-research-amylin-receptor-pharmacology-and-the-purity-verification-standards-behind-the-compound/ ；https://waltersport.com/wp-content/upl

### 11. https://www.drugs.com/clinical_trials/cagrisema-demonstrated-23-weight-loss-open-label-head-head-redefine-4-trial-obesity-primary-22309.html

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text — Drugs.com republication of Novo press release (secondary), dated 23 Feb 2026
- **Findings / corrections:** This page covers REDEFINE 4 only (23.0% vs tirzepatide 25.5% at 84 weeks; 20.2% vs 23.6% treatment-regimen estimand). Do NOT cite it for REDEFINE-1 efficacy numbers. NDA Dec 2025, decision late 2026, REDEFINE 1 n=3,417 verified. TEMPORAL FLAG: page dated Feb 2026, after the report's Oct 2025 index date — it cannot have been the Oct 2025 source for REDEFINE-1 numbers.
- **Report claims attributed to this source:**
  - ZH line 218 (Part 3): **CagriSema（Cagrilintide 2.4 mg + Semaglutide 2.4 mg）**：Novo Nordisk。NDA 已于 2025 年 12 月 18 日递交 FDA（减重管理）；决定预计 2026 年 Q4；截至 2026 年 10 月未获批。REDEFINE = 肥胖项目；REIMAGINE = T2D 项目。皮下注射，每周一次，固定剂量复方。半衰期：组分半衰期适用（Semaglutide 约 7 天；Cagrilintide 约 7–8 天，据次级来源）。疗效：REDEFINE 1（Phase 3，NCT05567796，n = 3,417，肥胖 / 超重无 T2D，68 周）：CagriSema 22.7%（试验产品 estimand）/ 20.4%（治疗策略）vs 安慰剂 2.3% / 3.0%；Semaglutide 单药 16.1% / 14.9%；Cagrilintide 单药 11.8% / 11.5%；91.9% 减重 ≥ 5%；基线肥胖参与者中 54% 降至肥胖阈值以下 vs 安慰剂 11.1%；DXA 亚组：−23.9%（CagriSema）vs −16.6%（Semaglutide）vs −15.0%（Cagrilintide）vs −2.8%（安慰剂）；减重中 66.9% 为脂肪量。REDEFINE 2（Phase 3，NC

### 12. https://www.eneuro.org/content/11/6/ENEURO.0133-24.2024.abstract

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** abstract only — eNeuro abstract (full text not read)
- **Findings / corrections:** VTA amylin activation suppresses fat/sugar intake; fat evokes greater accumbens dopamine than isocaloric sucrose; VTA activation suppresses fat-evoked dopamine more robustly than sucrose-evoked — verified. VTA CTR on GABA interneurons; monosynaptic VTA->mPFC; intra-VTA AC187; mPFC cFos/phasic dopamine; GABA blockade; no nausea/malaise or locomotor suppression — NOT in abstract; need full text or companion PMC3717548.
- **Report claims attributed to this source:**
  - EN line 100 (Part 2): | VTA / Reward Circuit | VTA dopamine → nucleus accumbens core + medial prefrontal cortex (mPFC); VTA CTR located on GABAergic interneurons → monosynaptic input to the VTA → mPFC pathway | Rat VTA contains mRNA for all AMYR components; intra-VTA amylin / sCT ↓ regular chow + palatable sucrose intake (↓ meal size, ↓ progressive-ratio responding / breakpoint), without nausea / malaise or long-term locomotor suppression; intra-VTA AC187 blockade ↑ 24-h chow intake and blunts peripheral amylin-analog effects. Mechanism: intra-VTA amylin ↓ food-evoked mPFC cFos, ↓ food-evoked mPFC phasic dopamine; 

### 13. https://allsci.com/news/business/viking-therapeutics-vk2735-funding-raises-usd/

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text — AllSci news (secondary)
- **Findings / corrections:** Supports ONLY VK3019 Phase 1 + DACRA (dual amylin + calcitonin receptor agonist) + subcutaneous delivery. Does NOT support VK3012/3006/3015 codes, ~1.4x selectivity, or preclinical efficacy numbers.
- **Report claims attributed to this source:**
  - ZH line 208 (Part 3): **Viking DACRA（VK3012 / VK3006 / VK3015 临床前；VK3019 Phase 1）**：Viking Therapeutics。临床前系列（VK3012、VK3006、VK3015）——截至 ADA 2024 海报未选出候选；VK3019 于 2026 年 6 月进入 Phase 1 单剂量递增研究（单药或 + VK2735）。未获批。机制：双 Amylin + 降钙素受体激动剂（DACRA）；VK3012 最平衡（约 1.4× Amylin : 降钙素选择性），在瘦大鼠 / DIO 小鼠中减重最佳（临床前海报）。皮下注射（临床前 / Phase 1 SAD）。半衰期未公开披露。疗效（仅临床前）：单次 SC 给药 → 瘦大鼠 72 小时减重高达 8%；DIO 小鼠 24 天治疗减重高达 10%，与 Cagrilintide 相当；改善血糖。无人类疗效。无人类安全性数据。来源：https://ir.vikingtherapeutics.com/2024-06-24-Viking-Therapeutics-Presents-Preclinical-Data-on-Novel-Dual-Amylin-and-Calcitonin-Receptor-Agonists-at-84th-Scientific-Sessions-of-the-American-

### 14. https://pmc.ncbi.nlm.nih.gov/articles/PMC5929477/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text, partial (Palmiter review, primary)
- **Findings / corrections:** General alarm / PBN CGRP relay framing verified. Amylin/CCK/cagrilintide/sCT-specific statements need the remainder.
- **Report claims attributed to this source:**
  - EN line 98 (Part 2): | Parabrachial Nucleus (PBN), especially lateral PBN (LPBN) | AP / NTS → LPBN CGRP (Calca) neurons → central amygdala (CeA) + bed nucleus of the stria terminalis (BNST) | Systemic amylin / CCK activate CGRP-PBN neurons; PBN CGRP neurons control meal termination (activation ↓ meal size; inactivation disrupts meal-size control); cagrilintide / sCT activate LPBN cFos in WT mice | Meal termination / satiety; strong weight-loss relevance | PBN CGRP neurons are a general alarm / aversion relay (food poisoning, pain, itch, hypercapnia) → CeA / BNST; chronic activation → severe anorexia / starvation i

### 15. https://remypeptides.com/research/zenagamtide-amycretin-glp1-amylin

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text — RemyPeptides vendor page (secondary)
- **Findings / corrections:** CONTRADICTS the report's Amycretin Phase 2 T2D numbers: page says up to 14.6% vs 2.1% (NOT the report's -14.5% vs -2.6%); Phase 1b/2a -24.3%/-13.1% NOT on this page. Needs the Lancet paper to resolve.
- **Report claims attributed to this source:**
  - ZH line 222 (Part 3): **Amycretin / Zenagamtide（NNC0487-0111 / NN9487）**：Novo Nordisk。**INN 现为 Zenagamtide；Amycretin 为原开发名，同一分子**。Phase 1b/2a + Phase 2（T2D）完成；Phase 3 AMAZE 项目进行中（包括 AMAZE-12 减重维持，NCT07503210；HF-POLARIS Phase 3；AMBIENCE 心血管结局试验计划 2026 年 Q4）。未获批。机制：单分子（unimolecular）双 GLP-1 + Amylin 受体激动剂（亦激活 Amylin 受体的降钙素侧）——**不是**两药复方。给药：皮下每周一次 **与** 口服每日一次（两种剂型）。半衰期未公开披露。疗效：SC Phase 1b/2a（n = 125，超重 / 肥胖，长达 36 周）：60 mg 每周 −24.3% vs 安慰剂 −1.1%；报告指出高退出率（未在检索来源中量化）。口服 Phase 1（n = 144，长达 12 周）：高达 50 mg −10.4%；2× 50 mg −13.1% vs 安慰剂 −1.2%；未达平台。Phase 2 T2D（NCT06542874，n = 262，36 周，SC）：HbA1c −高达 1.8 个百分点（SC）/ −高达 1.5 个百分点（

### 16. https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralintide-demonstrated-meaningful-weight-loss-and-favorable-tolerability-in-a-phase-2-study-of-adults-with-obesity-or-overweight

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — BioSpace republication of Lilly press release (secondary)
- **Findings / corrections:** CORRECTED Phase 2 numbers: 1 mg -9.5%, 3 mg -12.4%, 6 mg -17.6%, 9 mg -20.1%, placebo -0.4%. Phase 2 NCT06230523 (NOT NCT06536399). No 1.5 mg arm. No >=15% responder figures. Safety/half-life/albumin NOT in this release — those need the Lancet paper.
- **Report claims attributed to this source:**
  - EN line 176 (Part 3): | Eloralintide (LY3841136) | Eli Lilly and Company (code LY3841136; "TZP" is the tirzepatide abbreviation, not this drug) | Phase 2 complete; Phase 3 monotherapy enrollment reportedly starting end of 2025 / "next month" (Oct 2026 status not confirmed in retrieved sources) | SC, once weekly | ~310–366 h (~13–15 days, **secondary source, not in Lilly press releases**) | Phase 2 (48 weeks): 9 mg −20.1% vs placebo −0.4%; 6 mg −17.6% | Mainly mild–moderate GI + fatigue; nausea 11–64% (dose-dependent) vs placebo 14% | https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralinti
  - EN line 222 (Part 3): - **Selectivity**: AMY1-biased (Lilly: "selective AMY1 receptor agonist"); potency fold varies by assay — one source states ~64-fold AMY1 vs CTR, another states ~12-fold (EC50 AMY1 21.2 pM vs CTR 1,350.8 pM in the Ascletis comparator data). Source: https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralintide-demonstrated-meaningful-weight-loss-and-favorable-tolerability-in-a-phase-2-study-of-adults-with-obesity-or-overweight ; https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-effi
  - EN line 225 (Part 3): - **Trials**: Phase 2 (NCT06536399) 48 weeks: 9 mg −20.1% vs placebo −0.4%; 6 mg −17.6%; 3 mg −14.4%; 1.5 mg −8.7%; ≥15% weight loss achieved by 78% at 9 mg vs 5% placebo. NCT number for the Phase 2 monotherapy program is from one secondary source and is **not confirmed** here (see "Could not verify"). Sources: https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralintide-demonstrated-meaningful-weight-loss-and-favorable-tolerability-in-a-phase-2-study-of-adults-with-obesity-or-overweight ; https://en.wikipedia.org/wiki/Eloralintide [index, 2026-10-15]
  - EN line 226 (Part 3): - **Safety**: Nausea 11–64% (dose-dependent) vs placebo 14%; fatigue 0–46% vs placebo 5%; most GI events mild–moderate, transient; discontinuation due to AEs low at 3 mg (1%), higher at 6 mg (9%), 9 mg (7%). Source: https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralintide-demonstrated-meaningful-weight-loss-and-favorable-tolerability-in-a-phase-2-study-of-adults-with-obesity-or-overweight [index, 2026-10-15]
  - EN line 338 (Part 4): - **Albumin binding (long-acting design)**: Fatty-acid acylation promotes reversible albumin binding, forming a circulating reservoir that slows clearance and extends half-life (cagrilintide, eloralintide C20 fatty diacid, petrelintide acylated — exact chains / % undisclosed). This lowers the free fraction available for filtration. Source: https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralintide-demonstrated-meaningful-weight-loss-and-favorable-tolerability-in-a-phase-2-study-of-adults-with-obesity-or-overweight [index, 2026-10-15]

### 17. https://www.globenewswire.com/news-release/2026/09/21/3365319/0/en/novo-s-cagrisema-delivers-superior-weight-loss-versus-tirzepatide-in-reimagine-5-trial.html

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — GlobeNewswire republication of Novo press release (secondary)
- **Findings / corrections:** Supports ONLY REIMAGINE 5 + REDEFINE 9. Does NOT support REDEFINE 1/2/4 numbers — those need their own sources.
- **Report claims attributed to this source:**
  - EN line 182 (Part 3): | CagriSema (cagrilintide 2.4 mg + semaglutide 2.4 mg) | Novo Nordisk | NDA submitted to FDA for weight management on 2025-12-18; decision expected 2026 Q4; not approved as of Oct 2026 | SC, once weekly, fixed-dose combination | Component half-lives apply (semaglutide ~7 days; cagrilintide ~7–8 days, secondary source) | REDEFINE 1: 22.7% (trial-product estimand) / 20.4% (treatment-policy) vs placebo 2.3% / 3.0%; REDEFINE 2 (T2D): 13.7% vs placebo 3.4%; REDEFINE 4 (vs tirzepatide 15 mg): 23.0% vs 25.5%, **did not meet non-inferiority** | Mainly GI adverse events, mostly mild–moderate, transient
  - EN line 252 (Part 3): - Fixed-dose combination, once-weekly SC; NDA submitted to FDA for weight management on 2025-12-18; decision expected 2026 Q4; not approved as of Oct 2026. Source: https://www.globenewswire.com/news-release/2026/09/21/3365319/0/en/novo-s-cagrisema-delivers-superior-weight-loss-versus-tirzepatide-in-reimagine-5-trial.html [index, 2026-10-15]
  - EN line 253 (Part 3): - REDEFINE 1 (68 weeks, obesity without diabetes): 22.7% (trial-product estimand) / 20.4% (treatment-policy) vs placebo 2.3% / 3.0%. REDEFINE 2 (T2D): 13.7% vs placebo 3.4%. REDEFINE 4 (vs tirzepatide 15 mg): 23.0% vs 25.5%, did not meet non-inferiority. REDEFINE 8 / 11 and high-dose CagriSema results were **not found** (see "Could not verify"). REIMAGINE 1 (MRI substudy): CagriSema reduced hepatic fat and glycemia; REIMAGINE 4 (vs tirzepatide in T2D): numbers **not confirmed** (see "Could not verify"). Sources: https://www.docwirenews.com/post/cagrilintide-and-semaglutide-combo-highly-effecti

### 18. http://pmc.ncbi.nlm.nih.gov/articles/PMC3717548/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text, partial lines 0-147 of 687 (primary)
- **Findings / corrections:** Rat VTA contains mRNA for all AMYR components; intra-VTA amylin/sCT decrease chow + sucrose intake via decreased meal size and progressive-ratio responding, no nausea/malaise or long-term locomotor suppression; intra-VTA AC187 blockade increases 24-h chow intake and blunts peripheral amylin-analog effects — verified. VTA CTR on GABAergic interneurons -> monosynaptic VTA->mPFC; intra-VTA amylin decreases food-evoked mPFC cFos / mPFC phasic dopamine; dopamine agonist blocks effect; GABA blockade/silencing weakens effect — NOT found in portion read (in-page find for 'mPFC' returned no match). VTA AMYR activation suppresses NAc dopamine more for fat than isocaloric sucrose (voltammetry) — NOT found in portion read. Those mechanistic details likely come from the companion eNeuro paper, not this one.
- **Report claims attributed to this source:**
  - EN line 100 (Part 2): | VTA / Reward Circuit | VTA dopamine → nucleus accumbens core + medial prefrontal cortex (mPFC); VTA CTR located on GABAergic interneurons → monosynaptic input to the VTA → mPFC pathway | Rat VTA contains mRNA for all AMYR components; intra-VTA amylin / sCT ↓ regular chow + palatable sucrose intake (↓ meal size, ↓ progressive-ratio responding / breakpoint), without nausea / malaise or long-term locomotor suppression; intra-VTA AC187 blockade ↑ 24-h chow intake and blunts peripheral amylin-analog effects. Mechanism: intra-VTA amylin ↓ food-evoked mPFC cFos, ↓ food-evoked mPFC phasic dopamine; 

### 19. https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-efficacy-in-preclinical-models-525584.shtml

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — company press release (secondary)
- **Findings / corrections:** ASC39 hAMY1R EC50 21.4 pM vs eloralintide 21.2 pM; hCTR EC50 846.1 pM vs 1,350.8 pM; 40-fold vs 64-fold selectivity — verified. DIO rats placebo-corrected weight loss 6.6% (ASC39 oral) vs 5.6% (eloralintide) — verified. Candidate selected Mar 2026; IND filing expected 2026 Q3 — verified (release dated Mar 17, 2026). ASC36 NHP oral bioavailability 6-8% NOT in this source (release describes ASC36 only as once-monthly to once-quarterly SQ peptide). Eloralintide selectivity ~12-fold CONTRADICTED by this source's own numbers: 1,350.8/21.2 = ~64-fold. The report's assay-dependence caveat on the fold is appropriate — present both figures as assay-dependent.
- **Report claims attributed to this source:**
  - EN line 188 (Part 3): | ASC39 (oral small molecule) | Ascletis Pharma | Preclinical candidate selected Mar 2026; oral tablet IND filing expected 2026 Q3; no human data | Oral tablet (planned) | Not publicly disclosed | Preclinical: hAMY1R EC50 21.4 pM (vs eloralintide 21.2 pM); hCTR EC50 846.1 pM (vs eloralintide 1,350.8 pM); DIO rats head-to-head: placebo-corrected weight loss 6.6% (ASC39 oral) vs 5.6% (eloralintide) | No human safety data | https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-efficacy-in-preclinical-models-525
  - EN line 222 (Part 3): - **Selectivity**: AMY1-biased (Lilly: "selective AMY1 receptor agonist"); potency fold varies by assay — one source states ~64-fold AMY1 vs CTR, another states ~12-fold (EC50 AMY1 21.2 pM vs CTR 1,350.8 pM in the Ascletis comparator data). Source: https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralintide-demonstrated-meaningful-weight-loss-and-favorable-tolerability-in-a-phase-2-study-of-adults-with-obesity-or-overweight ; https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-effi
  - EN line 281 (Part 3): Sources: https://www.pharmacytimes.com/view/amycretin-shows-significant-weight-loss-hba1c-reductions-in-type-2-diabetes ; https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-efficacy-in-preclinical-models-525584.shtml [index, 2026-10-15]
  - EN line 297 (Part 3): - Source: https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-efficacy-in-preclinical-models-525584.shtml [index, 2026-10-15]
  - EN line 337 (Part 4): - **Oral delivery (exceptional for peptides)**: Oral peptides face gastric acid + pepsin / trypsin / chymotrypsin / peptidases + poor membrane permeability. SNAC (used for oral semaglutide / amycretin) buffers local pH, interferes with pepsinogen activation, and fluidizes the gastric lipid membrane; oral semaglutide bioavailability ~0.4–1%. ASC36 NHP oral bioavailability 6–8%. Sources: https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-efficacy-in-preclinical-models-525584.shtml ; https://www.pharmacytime

### 20. https://en.wikipedia.org/wiki/Eloralintide

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — Wikipedia (secondary, short page)
- **Findings / corrections:** Eloralintide = LY3841136, selective amylin receptor agonist — verified. Half-life ~310-366 h (~13-15 days) NOT on this page. Phase 2 numbers (9 mg -20.1% vs placebo -0.4%; 6 mg -17.6%; nausea 11-64% vs placebo 14%) NOT on this page (page only says ~20% at highest dose over 48 weeks). Phase 2 NCT06536399; Phase 3 enrollment starting end of 2025 / 'next month' NOT on this page (page only notes Phase 3 planned for EloraTZP). Nearly all quantitative claims attributed to this page are not on it; they must rest on the Lilly press release / Lancet paper.
- **Report claims attributed to this source:**
  - EN line 176 (Part 3): | Eloralintide (LY3841136) | Eli Lilly and Company (code LY3841136; "TZP" is the tirzepatide abbreviation, not this drug) | Phase 2 complete; Phase 3 monotherapy enrollment reportedly starting end of 2025 / "next month" (Oct 2026 status not confirmed in retrieved sources) | SC, once weekly | ~310–366 h (~13–15 days, **secondary source, not in Lilly press releases**) | Phase 2 (48 weeks): 9 mg −20.1% vs placebo −0.4%; 6 mg −17.6% | Mainly mild–moderate GI + fatigue; nausea 11–64% (dose-dependent) vs placebo 14% | https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralinti
  - EN line 225 (Part 3): - **Trials**: Phase 2 (NCT06536399) 48 weeks: 9 mg −20.1% vs placebo −0.4%; 6 mg −17.6%; 3 mg −14.4%; 1.5 mg −8.7%; ≥15% weight loss achieved by 78% at 9 mg vs 5% placebo. NCT number for the Phase 2 monotherapy program is from one secondary source and is **not confirmed** here (see "Could not verify"). Sources: https://www.biospace.com/press-releases/lillys-selective-amylin-agonist-eloralintide-demonstrated-meaningful-weight-loss-and-favorable-tolerability-in-a-phase-2-study-of-adults-with-obesity-or-overweight ; https://en.wikipedia.org/wiki/Eloralintide [index, 2026-10-15]

### 21. https://fda.report/DailyMed/4aea30ff-eb0d-45c1-b114-3127966328ff

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text, partial lines 0-325 of 2329 (label mirror, primary)
- **Findings / corrections:** Boxed warning (severe hypoglycemia with mealtime insulin, mainly T1D, within 3 h of injection); start: reduce mealtime insulin ~50%, wait >=3 days before titrating; T1D start 15 mcg; do not mix with insulin; skip if meal <250 kcal or <30 g carbs — verified. Injection site >2 inches from insulin site NOT found in portion read (label says only a distinct site from insulin). Pramlintide does not change counter-regulatory hormone response or hypoglycemia symptom perception (down to 45 mg/dL) NOT found in portion read.
- **Report claims attributed to this source:**
  - ZH line 367 (Part 4): - **低血糖风险（Pramlintide + 胰岛素）**：黑框警告：与餐时胰岛素合用 ↑ 胰岛素诱导严重低血糖风险，主要为 T1D；严重低血糖发生时多在注射后 3 小时内观察到。说明书：起始时餐时胰岛素减量约 50%；低血糖时 / 跳过餐食 / 餐食 < 250 kcal 或 < 30 g 碳水时勿注射。Pramlintide 不改变胰岛素诱导低血糖的反调节激素反应，也不改变低血糖症状感知（低至 45 mg/dL）。来源：https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf ；https://fda.report/DailyMed/4aea30ff-eb0d-45c1-b114-3127966328ff [index, 2026-10-15]。Cagrilintide / CagriSema 在无糖尿病肥胖中：综述称**未**伴随低血糖风险增加——无数据时勿外推至胰岛素治疗 T1D / T2D。来源：https://www.passeidireto.com/arquivo/158376647/efficacy-and-safety-of-cagrilintide-alone-and-in-2 [index, 2026-10-15]
  - ZH line 368 (Part 4): - **剂量滴定原理**：Pramlintide：低剂量起始（T1D 15 mcg；T2D 按说明书滴定），仅在换剂量后 ≥ 3 天无恶心时才增加；切勿与胰岛素混合；注射部位与胰岛素相距 > 2 英寸。来源：https://fda.report/DailyMed/4aea30ff-eb0d-45c1-b114-3127966328ff [index, 2026-10-15]。长效激动剂：缓慢递增减少胃肠不良事件——Cagrilintide Phase 1b 每 4 周递增；Petrelintide 起始 0.5 mg，固定 4 周递增步长，73% 恶心发生于递增期，88–98% 达到目标维持剂量；Eloralintide 较慢递增 → 胃肠不良事件发生率更低，1–3 mg 时与安慰剂相似。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_

### 22. https://patents.google.com/patent/EP2241327A1/en

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text, partial lines 0-288 of 4521; in-page find for the sequence returned no match
- **Findings / corrections:** Human amylin sequence KCNTATCATQRLANFLVHSSNNFGAILSSTNVGSNTY-NH2, disulfide between the two Cys — NOT found in portion read. Sequence is standard textbook human amylin, but this citation did not verify it in the portion read.
- **Report claims attributed to this source:**
  - EN line 28 (Part 1): | Human sequence | KCNTATCATQRLANFLVHSSNNFGAILSSTNVGSNTY-NH2, disulfide bond between the two Cys residues | https://patents.google.com/patent/EP2241327A1/en [index, 2026-10-15] |

### 23. https://www.globenewswire.com/news-release/2026/07/28/3334604/0/en/Amylin-Analogs-and-Combination-Therapies-Clinical-Trial-Landscape-Expands-as-15-Leading-Companies-Accelerate-Drug-Development-DelveInsight.html

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text — press release for DelveInsight report (secondary, vendor)
- **Findings / corrections:** NN9638 (Amylin 355) / NN9839 (Amylin 1213) listed with no mechanism/stage/efficacy/safety details — verified (names only). XW015 — Verdiva Bio/Sciwind, preclinical SC amylin candidate for obesity/NASH/T2D — largely verified (table: preclinical, SC, NASH/obesity/T2D; Sciwind-Verdiva licensing noted). ACCG-3535: 'no data' overstated — page DOES give minimal details (Preclinical, Obesity, Oral). Correct to 'only minimal listing details (phase/indication/route), no mechanism or efficacy data.'
- **Report claims attributed to this source:**
  - ZH line 212 (Part 3): **其他仅代码的管线候选（公开细节极少——仅代码）**：NN9638（Amylin 355）/ NN9839（Amylin 1213）——Novo Nordisk，列于 DelveInsight Amylin 管线；检索来源中无机制、阶段、疗效或安全性公开细节，请勿视为已确认的临床候选。XW015——Verdiva Bio / Sciwind，列为临床前 SC Amylin 候选（肥胖 / NASH / T2D）；检索来源中无数据。ACCG-3535——Structure Therapeutics，列为临床前口服 Amylin 候选；检索来源中无数据。管线列表来源：https://www.globenewswire.com/news-release/2026/07/28/3334604/0/en/Amylin-Analogs-and-Combination-Therapies-Clinical-Trial-Landscape-Expands-as-15-Leading-Companies-Accelerate-Drug-Development-DelveInsight.html [index, 2026-10-15]

### 24. https://www.mdpi.com/1422-0067/23/24/16035

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text (partial view + targeted finds, primary antibody-validation study)
- **Findings / corrections:** RAMP1 mRNA in cerebellum, nucleus accumbens, locus coeruleus, AP, cortex (rodent) — partially supported: paper summarizes prior mRNA/binding literature as supporting RAMP1 in these regions, with prior data focused on rat cerebellum; AP/cortex mRNA not individually confirmed in lines found. CGRP binding strong in cerebellum, NAc, LC, AP — verified. CORRECTION: this paper's own conclusion is that antibody IHC cannot confidently assign RAMP1 localization and that RAMP1 expression 'needs to be revisited' — the report's flat expression listing overstates certainty. Add the paper's caution: mRNA/binding summaries do not equal validated protein localization.
- **Report claims attributed to this source:**
  - EN line 77 (Part 1): | Area Postrema / brainstem | RAMP1 mRNA in cerebellum, nucleus accumbens, locus coeruleus, AP, cortex (rodent); CGRP binding strong in cerebellum, nucleus accumbens, locus coeruleus, AP | https://www.mdpi.com/1422-0067/23/24/16035 [index, 2026-10-15] |

### 25. https://www.nature.com/articles/celldisc201612

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text, partial lines 0-138 of 707; in-page find for 'identity' returned no match (primary)
- **Findings / corrections:** CTR alone is a functional calcitonin receptor; RAMPs change ligand selectivity (CTR+RAMP1-3 -> AMY1-3, high-affinity amylin receptors) — verified. RAMPs change trafficking — NOT confirmed in portion read. RAMPs share only ~30% amino-acid identity with each other — NOT found in portion read; needs a different citation or full-text check.
- **Report claims attributed to this source:**
  - EN line 42 (Part 1): - **CTR alone**: CTR alone is a functional calcitonin receptor; RAMPs change ligand selectivity and trafficking; RAMPs share only ~30% amino-acid identity with each other. Source: https://www.nature.com/articles/celldisc201612 [index, 2026-10-15]

### 26. https://www.news-medical.net/news/20100223/Amylin-Pharmaceuticals-and-Takeda-Pharmaceutical-to-advance-pramlintidemetreleptin-combination-therapy-development.aspx

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — news reprint of company release (secondary)
- **Findings / corrections:** Davalintide (AC2307), Amylin + Takeda; terminated after Phase 2; efficacy/tolerability not superior to pramlintide, inferior to pramlintide/metreleptin combo; development halted — verified. Preclinical: eating inhibition 23 h vs 6 h for amylin; dose-dependent fat-specific weight loss up to 8 weeks in animals — NOT found in this source; needs a different source.
- **Report claims attributed to this source:**
  - EN line 174 (Part 3): | Davalintide (AC2307) | Amylin Pharmaceuticals (+ Takeda collaboration) | Terminated (after Phase 2) | Injection (regimen not detailed) | Not publicly disclosed | Phase 2: efficacy / tolerability not superior to pramlintide | Human safety details not publicly disclosed | https://www.news-medical.net/news/20100223/Amylin-Pharmaceuticals-and-Takeda-Pharmaceutical-to-advance-pramlintidemetreleptin-combination-therapy-development.aspx [index, 2026-10-15] |
  - EN line 210 (Part 3): - Phase 2: efficacy / tolerability not superior to pramlintide; terminated after Phase 2; no public detailed PK / AE numbers. Source: https://www.news-medical.net/news/20100223/Amylin-Pharmaceuticals-and-Takeda-Pharmaceutical-to-advance-pramlintidemetreleptin-combination-therapy-development.aspx [index, 2026-10-15]

### 27. https://www.pharmaceutical-technology.com/news/newseli-lilly-and-keybioscience-collaborate-to-develop-potential-type-2-diabetes-treatment-5838359/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — short trade-press article (secondary)
- **Findings / corrections:** KeyBioscience (Nordic Bioscience subsidiary); Lilly licensed DACRA platform in 2017; $55M upfront + milestones — verified (upfront $55M, global rights, DACRA platform; 2017 date from deal context, not stated in fetched text). KBP-042, KBP-089, KBP-056 named; KBP-042 Phase 2 initiated — verified (at time of article). 'All preclinical/terminated, no clinical program in development' NOT supported by this 2017 article (it reports an active collaboration) — needs a later source. Rats: weight loss, reduced fat, improved glucose tolerance; injection rat Q3D — NOT found in this source; need other sources.
- **Report claims attributed to this source:**
  - EN line 179 (Part 3): | KBP series (DACRA) | KeyBioscience (Nordic Bioscience subsidiary); Lilly licensed the DACRA platform in 2017 | All preclinical / terminated, no clinical program in development | Injection (rat Q3D) | Not applicable (no human data) | No human data; rats: weight loss, reduced fat, improved glucose tolerance | Not applicable | https://www.pharmaceutical-technology.com/news/newseli-lilly-and-keybioscience-collaborate-to-develop-potential-type-2-diabetes-treatment-5838359/ ; https://www.medscape.com/medline/abstract/37329973 [index, 2026-10-15] |
  - EN line 238 (Part 3): - KeyBioscience DACRA series (KBP-042 / -089 / -056 etc.); Lilly licensed the DACRA platform in 2017; all preclinical or terminated, no clinical program. Source: https://www.pharmaceutical-technology.com/news/newseli-lilly-and-keybioscience-collaborate-to-develop-potential-type-2-diabetes-treatment-5838359/ ; https://www.medscape.com/medline/abstract/37329973 [index, 2026-10-15]

### 28. https://www.pharmacytimes.com/view/petrelintide-yields-up-to-10-7-weight-loss-with-mild-gi-effects

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — trade press summarizing Lancet Diabetes Endocrinol paper (secondary)
- **Findings / corrections:** ZUPREME-1 (42 wks): 8.7-10.7% vs placebo ~1.7%; week 28: 7.9-9.8% vs 1.7%; n=493; 34-56% lost >=10% vs 9% placebo; plateau above 5 mg; nausea 20% vs placebo 6%; GI discontinuation ~1%; 73% of nausea during escalation; 88-98% reached target dose; anti-drug antibodies 38% with no apparent effect on weight loss; half-life ~10 days; start 0.5 mg, fixed 4-week escalation steps — verified. Tmax ~24 h; SC bioavailability ~85% NOT in this source (belong to the Zealand deck, verified there). ZUPREME-2 (28 wks, T2D): 7.4-9.2% vs placebo 2.0% NOT in this source (belongs to the GlobeNewswire topline release, could-not-access). Roche deal up to $5.3B; Phase 3 ZUPREME-3/4/5 ~7,000 participants NOT in this source.
- **Report claims attributed to this source:**
  - EN line 175 (Part 3): | Petrelintide (ZP8396) | Zealand Pharma (originator); with Roche (2025, up to $5.3B deal) | Phase 2 complete; Phase 3 ZUPREME-3/4/5 started Sep 2026 (~7,000 participants) | SC, once weekly | ~240 h (~10 days); Tmax ~24 h; SC bioavailability ~85% | ZUPREME-1 (42 weeks): 8.7–10.7% vs placebo ~1.7%; ZUPREME-2 (28 weeks, T2D): 7.4–9.2% vs placebo 2.0% | Nausea 20% vs placebo 6%; GI discontinuation ~1%; anti-drug antibodies 38% (no apparent effect on weight loss) | https://www.globenewswire.com/news-release/2026/10/07/3376750/0/en/zealand-pharma-announces-positive-phase-2-zupreme-2-topline-results
  - EN line 215 (Part 3): - **PK**: t1/2 ~240 h, Tmax ~24 h, SC bioavailability ~85% (secondary source, likely from a recent review; primary Phase 1 PK not fully re-verified in the retrieved text). Source: https://www.pharmacytimes.com/view/petrelintide-yields-up-to-10-7-weight-loss-with-mild-gi-effects [index, 2026-10-15]
  - EN line 216 (Part 3): - **Trials**: ZUPREME-1 Phase 2 (42 weeks, obesity without diabetes): 8.7–10.7% vs placebo ~1.7%; ZUPREME-2 (28 weeks, T2D): 7.4–9.2% vs placebo 2.0%. ZUPREME Phase 3 started Sep 2026 (ZUPREME-3 / 4 / 5, ~7,000 participants). NCT numbers for ZUPREME-1 and the Phase 2 monotherapy program were **not confirmed** in the retrieved sources (see "Could not verify"). Sources: https://www.globenewswire.com/news-release/2026/10/07/3376750/0/en/zealand-pharma-announces-positive-phase-2-zupreme-2-topline-results-for-amylin-analog-petrelintide-in-people-with-overweight-or-obesity-and-type-2-diabetes.html ;
  - EN line 336 (Part 4): - **Subcutaneous injection (mainstream)**: Bypasses GI lumen degradation and portal first-pass; delivers the full dose to systemic circulation; SC bioavailability examples: pramlintide 30–40%, petrelintide ~85% (secondary source). Sources: https://www.drugs.com/monograph/pramlintide.html ; https://www.pharmacytimes.com/view/petrelintide-yields-up-to-10-7-weight-loss-with-mild-gi-effects [index, 2026-10-15]

### 29. https://www.proteinatlas.org/ENSG00000004948-CALCR

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — summary page (primary database)
- **Findings / corrections:** CALCR: HPA tissue-enhanced (brain, kidney); brain expression cluster = hypothalamus-neuropeptide signaling; CALCR protein in renal tubules (tissue profile: hypothalamic neurons + renal tubules) — verified. Mouse RNA/protein mainly restricted to hypothalamus, septum, few midbrain/medulla nuclei (e.g., locus coeruleus) NOT found on this human summary page. Renal amylin deposition reported in diabetic nephropathy NOT on this page (belongs to the kidney paper cited alongside).
- **Report claims attributed to this source:**
  - EN line 74 (Part 1): | Brain (overall) | CALCR: HPA tissue-enhanced (brain, kidney); brain expression cluster = hypothalamus–neuropeptide signaling; mouse RNA / protein mainly restricted to hypothalamus, septum, a few midbrain / medulla nuclei (e.g., locus coeruleus) | HPA: https://www.proteinatlas.org/ENSG00000004948-CALCR [index, 2026-10-15] |
  - EN line 80 (Part 1): | Kidney | CALCR protein in renal tubules (HPA); kidney is the main amylin clearance organ; renal amylin deposition reported in diabetic nephropathy | https://www.proteinatlas.org/ENSG00000004948-CALCR ; https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext [index, 2026-10-15] |

### 30. https://www.reuters.com/legal/litigation/experimental-lilly-combination-drug-tops-zepbound-weight-loss-trial-2026-09-30/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — news (secondary)
- **Findings / corrections:** EloraTZP Phase 2b (48 wks): Elora 9 mg + TZP 15 mg -23.3% vs tirzepatide 15 mg -14.8% vs placebo -3.0%; HbA1c -2.9 vs -2.4 pp; n=367 T2D; Phase 3 planned Q4 2026; discontinuation due to AEs 10.8-27% (combo) vs tirzepatide 2.9%, placebo 16.7% — verified. 24.6 kg absolute loss NOT found in this source. NCT06603571; Phase 2b used two separate injections NOT found in this source (presumably the Pharmacy Times companion piece, could-not-access).
- **Report claims attributed to this source:**
  - EN line 183 (Part 3): | EloraTZP (eloralintide + tirzepatide) | Eli Lilly | Phase 2b complete; single-injection combination + Phase 3 planned before end of 2026; Phase 2b used two separate injections | SC, once weekly (Phase 2b: two separate injections) | Not stated separately; components: eloralintide ~13–15 days (reported), tirzepatide ~5 days (well known, not re-verified here) | Phase 2b (NCT06603571, 48 weeks): Elora 9 mg + TZP 15 mg −23.3% (24.6 kg) vs tirzepatide 15 mg alone −14.8% vs placebo −3.0% | Discontinuation due to AEs 10.8–27% (dose-dependent, combination arms) vs tirzepatide 2.9%, placebo 16.7% | ht
  - EN line 258 (Part 3): - Phase 2b (NCT06603571, 48 weeks): Elora 9 mg + TZP 15 mg −23.3% (24.6 kg) vs tirzepatide 15 mg alone −14.8% vs placebo −3.0%; Phase 2b used two separate injections; single-injection combination + Phase 3 planned before end of 2026. Discontinuation due to AEs 10.8–27% (dose-dependent, combination arms) vs tirzepatide 2.9%, placebo 16.7%. Sources: https://www.pharmacytimes.com/view/eloratzp-delivers-up-to-23-3-weight-loss-in-adults-with-obesity-and-t2d ; https://www.reuters.com/legal/litigation/experimental-lilly-combination-drug-tops-zepbound-weight-loss-trial-2026-09-30/ [index, 2026-10-15]

### 31. https://www.sciencedirect.com/science/article/abs/pii/000689939191644G

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** abstract only — paywalled full text (primary)
- **Findings / corrections:** Intrahypothalamic amylin reduced feeding for 8 hours — verified (abstract). VTA / NAc / LDTg amylin receptor signaling modulates intake/reward NOT found in this abstract (belongs to the other two sources cited alongside). Only the hypothalamic part is verified by this source. Claim appears in Chinese only.
- **Report claims attributed to this source:**
  - ZH line 338 (Part 4): - **直接注射研究**：显示受体在直接放置药物时*功能存在*，但**不证明**全身药物到达该处：下丘脑内 Amylin 减少进食 8 小时；VTA 内 / 伏隔核内 / LDTg 内 Amylin 受体信号调节摄入 / 奖赏。来源：https://www.sciencedirect.com/science/article/abs/pii/000689939191644G ；https://pmc.ncbi.nlm.nih.gov/articles/PMC5503810/ ；https://www.nature.com/articles/ijosup20164 [index, 2026-10-15]

### 32. https://www.sciencedirect.com/science/article/abs/pii/S0167011501003007

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** abstract + section snippets (primary)
- **Findings / corrections:** Amylin + GLP-1 cause dose-/time-dependent relaxation of pre-contracted rat pulmonary artery rings — verified. Amylin (8-37) direct vasodilator action in isolated rat mesenteric resistance arteries NOT found in this source. Amylin via CGRP1-preferring receptors increases rat ventricular cardiomyocyte contractility (EC50 216 pM vs CGRP 21 pM) NOT found in this source.
- **Report claims attributed to this source:**
  - EN line 113 (Part 2): | Blood pressure / vasodilation | Amylin mediates vasodilation via CGRP receptors (rodent ex vivo) | Amylin (8-37) has direct vasodilator action in isolated rat mesenteric resistance arteries; amylin + GLP-1 cause dose- / time-dependent relaxation of pre-contracted rat pulmonary artery rings; amylin via CGRP1-preferring receptors ↑ rat ventricular cardiomyocyte contractility (EC50 216 pM vs CGRP 21 pM) — rodent, ex vivo / isolated cells | No established systemic blood-pressure effect of amylin agonists in humans; do not assume blood-pressure lowering | No established hypertension / hypotension

### 33. https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text, partial lines 0-468 + targeted finds (primary review)
- **Findings / corrections:** Bone: CTR activation -> inhibit osteoclast resorption; rodent data inhibit resorption, may stimulate formation; human therapeutic bone effect unestablished (extrapolated) — verified. Vascular/BP: rodent amylin -> CGRP-receptor vasodilation -> decreased BP; contradictory preclinical/clinical results; human CGRP activation needs supratherapeutic doses; short infusion may not alter BP; long-term unclear — verified. CagriSema Phase 3 BP drop mainly weight-mediated, unquantified — CORRECTED: source reports CagriSema decreased SBP 13 mmHg and separately states no data are available on the indirect BP contribution via weight reduction — it does NOT assert weight mediation. Rephrase: SBP fell 13 mmHg; the weight-mediated share is unquantified (no data), not established as the main mechanism. Muscle: amylin opposes glycogen synthesis, activates glycogenolysis/glycolysis — verified. Endogenous amylin: circulating half-life <20 min; renal excretion + proteolytic degradation — verified. KBP-336 preclinical OA antiresorptive + analgesic + weight-loss specifics NOT found in this source (belong to the KBP-336 paper). Claims appear in Chinese only.
- **Report claims attributed to this source:**
  - ZH line 349 (Part 4): - **骨**：CTR 激活 → 抑制破骨细胞吸收；啮齿类数据：抑制骨吸收，可能刺激骨形成。DACRA（如 KBP-336）在临床前 OA 模型中显示抗吸收 + 镇痛 + 减重效应。Amylin 激动剂的人类治疗性骨效应**未确立**——由降钙素生物学 + 啮齿类数据外推。来源：https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810 ；https://link.springer.com/article/10.1186/s13075-024-03361-2 [index, 2026-10-15]
  - ZH line 350 (Part 4): - **血管 / 血压**：啮齿类：Amylin → 经 CGRP 受体强效血管舒张 → ↓ 血压；亦有内皮依赖性舒张受损 + RAS 激活 → 可能高血压的报告；临床前 / 临床结果矛盾。人类：CGRP 受体激活需超治疗剂量；短期输注可能不改变血压；长期效应不清楚。CagriSema Phase 3 血压下降可能主要由减重介导——间接贡献**未量化**。来源：https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810 [index, 2026-10-15]
  - ZH line 351 (Part 4): - **骨骼肌 / 脂肪 / 肝（次要，证据薄）**：Amylin 受体报告分布于脑、胰腺、脂肪、胃肠。较老文献：Amylin 反对肌肉糖原合成、激活糖原分解 / 糖酵解；可能调节乳糜微粒摄取 / 脂蛋白受体。是否由充分表征的外周 AMYR 介导**未证实**（外周 CTR + RAMP 共表达数据自 1998 年以来稀疏）。来源：https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01487-X/abstract ；https://www.mdpi.com/1589566 ；https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810 [index, 2026-10-15]
  - ZH line 355 (Part 4): - **内源性 Amylin**：循环半衰期 < 20 分钟；经肾排泄 + 蛋白水解降解代谢。来源：https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810 [index, 2026-10-15]

### 34. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)01776-3/abstract

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** abstract only — paywalled full text (comment/hypothesis piece, primary)
- **Findings / corrections:** Hypothesis only: amylin agonists may activate RAS -> potentially undermine cardiorenal benefit; RAS blockade hypothesized to redirect to protective Ang-(1-7)/Mas pathway — hypothesis, not established — verified. CagriSema showed substantial BP reductions in Phase 3 — verified (abstract). Cagrilintide: single-dose renal/hepatic impairment did not affect PK/safety/tolerability -> low likelihood of dose adjustment (limited: single low dose 0.6 mg renal / 0.9 mg hepatic, not 2.4 mg maintenance, small severe-impairment groups) NOT found in this abstract (belongs to the clinical-pharmacology paper cited alongside). Amylin binding sites in kidney NOT stated in this abstract. Claim appears in Chinese only.
- **Report claims attributed to this source:**
  - ZH line 348 (Part 4): - **肾**：Amylin 结合位点见于肾；肾是 Amylin + Pramlintide 主要清除 / 蛋白水解部位（见第六步）。Cagrilintide：单剂量肾或肝损害未影响 PK / 安全性 / 耐受性 → 作者结论剂量调整可能性低（局限：单次低剂量 0.6 mg 肾 / 0.9 mg 肝，非 2.4 mg 维持剂量，重度损害组样本小）。仅假说：Amylin 激动剂可能激活肾素–血管紧张素系统（RAS）→ 可能削弱心肾获益；RAS 阻断被假设可重定向至保护性 Ang-(1–7) / Mas 通路——**假说，非确立**。来源：https://www.medscape.com/viewarticle/523581_4 ；https://link.springer.com/article/10.1007/s40262-026-01654-0 ；https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)01776-3/abstract [index, 2026-10-15]

### 35. https://en.wikipedia.org/wiki/Zenagamtide

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text — Wikipedia (secondary)
- **Findings / corrections:** Zenagamtide is the INN for amycretin (Novo Nordisk) — verified. Dose/duration/13.1% weight-loss numbers NOT on this page — attribute to PeptideBenchmark blog / Lancet paper.
- **Report claims attributed to this source:**
  - ZH line 312 (Part 4): - **口服 Amylin 通路尝试——Amycretin / Zenagamtide（NN9487）**：单分子双 GLP-1 + Amylin 受体激动剂；口服剂型含 SNAC 作为促渗剂；SC 剂型平行（无 SNAC）；口服 Phase 1 测试两种 SNAC 剂型，剂量高达每日两片 50 mg，长达 12 周；早期报告最高剂量 12 周减重约 13.1%。来源：https://en.wikipedia.org/wiki/Zenagamtide ；https://peptidebenchmark.com/blog/amycretin-next-generation-obesity-drug-oral-subcutaneous-phase-3/ [index, 2026-10-15]

### 36. https://indigobiosciences.com/understanding-the-amylin-receptor-family/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text — vendor blog post (secondary)
- **Findings / corrections:** AMY1/2/3 = CTR+RAMP1/2/3; CLR+RAMP1 = canonical CGRP receptor; RAMP3 role unclear — verified. AMY1-vs-AMY3 CGRP affinity comparison NOT on this page — remove that attribution.
- **Report claims attributed to this source:**
  - EN line 44 (Part 1): - **CGRP receptor cross-reactivity**: The classical CGRP receptor = CLR (CALCRL) + RAMP1; AMY1 also binds CGRP with high affinity because it shares RAMP1; human CGRP has higher affinity for AMY1 than AMY3, and AMY2 affinity is less well understood. Sources: https://indigobiosciences.com/understanding-the-amylin-receptor-family/ ; https://en.wikipedia.org/wiki/Amylin_receptor [index, 2026-10-15]
  - EN line 79 (Part 1): | GI tract | A review states AMY2 is more restricted to GI / endocrine tissues — human protein-level map **unverified** | https://indigobiosciences.com/understanding-the-amylin-receptor-family/ [index, 2026-10-15] |

### 37. https://link.springer.com/article/10.1007/s40262-015-0343-6

- **Verdict:** corrected
- **Cited in:** Chinese original
- **What was read:** full text, lines 0-149 of 407 (liraglutide review, primary)
- **Findings / corrections:** Supports ONLY the acylation analogy (liraglutide C16 fatty acid via gamma-Glu, reversible albumin binding, t1/2 ~13 h). Does NOT support cagrilintide specifics (N14E/V17R/P37Y, C20 diacid, t1/2 7-8 days) — those rest on Upmag (secondary).
- **Report claims attributed to this source:**
  - ZH line 318 (Part 4): - **脂肪酸酰化 / 白蛋白结合——半衰期延长**：Cagrilintide：Pramlintide 样骨架 + 3 个取代（N14E、V17R、P37Y）+ N 端 C20 二十烷二酸脂肪二酸经 γ-Glu 接头 → 促进可逆白蛋白结合 → 清除显著延长（vs 未修饰 Amylin 类似物）。Eloralintide：Amylin 类似物偶联 C20 脂肪二酸实现可逆白蛋白结合；经工程化实现高 AMY1R 效力 / 选择性、低纤维化 / 自聚集风险、长血浆半衰期。Petrelintide：酰化肽；确切酰基链 / 白蛋白结合 % **未在检索来源中公开披露**（仅“酰化”）。通用酰化效应（以利拉鲁肽为类比——**勿将 % 转移至 Cagrilintide**）：SC 吸收减慢 + 经减慢代谢 / 肾滤过降低消除 → Tmax 延迟、半衰期延长。**Cagrilintide 血浆蛋白 / 白蛋白结合 % 未在检索来源中公开披露**。来源：https://upmag.com/cagrilintide-peptide-research-amylin-receptor-pharmacology-and-the-purity-verification-standards-behind-the-compound/ ；https://waltersport.com/wp-content/upl

### 38. https://pmc.ncbi.nlm.nih.gov/articles/PMC12410446/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text, lines 0-170 of 322 (primary)
- **Findings / corrections:** Eloralintide internalization verified. EC50 114/1492 pM and eloralintide selectivity numbers NOT in this paper — MISATTRIBUTED; remove attribution to this source. Those numbers need a different source.
- **Report claims attributed to this source:**
  - EN line 52 (Part 1): - **β-arrestin / trafficking (mostly inferred)**: AMYR regulation / trafficking is little studied; inferred from CLR–RAMP1: agonist → phosphorylation + dynamin / β-arrestin-dependent internalization; one HEK293 study showed almost no AMY1R internalization. Sources: https://www.researchgate.net/publication/251247194_Understanding_Amylin_Receptors ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12410446/ [index, 2026-10-15]
  - EN line 195 (Part 3): - **Receptor**: Amylin receptor agonist; **biased to AMY3** (EC50 114 pM) vs CTR (1492 pM) in the cited cAMP assay. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12410446/ [index, 2026-10-15]

### 39. https://pmc.ncbi.nlm.nih.gov/articles/PMC4867080/

- **Verdict:** corrected
- **Cited in:** English report, Chinese original
- **What was read:** full text, lines 0-145 of 292 (2016 paper, primary)
- **Findings / corrections:** Cagrilintide/sCT LPBN-cFos NOT in this paper — it predates cagrilintide (2016). Remove attribution. LPBN cFos claims need a later source.
- **Report claims attributed to this source:**
  - EN line 98 (Part 2): | Parabrachial Nucleus (PBN), especially lateral PBN (LPBN) | AP / NTS → LPBN CGRP (Calca) neurons → central amygdala (CeA) + bed nucleus of the stria terminalis (BNST) | Systemic amylin / CCK activate CGRP-PBN neurons; PBN CGRP neurons control meal termination (activation ↓ meal size; inactivation disrupts meal-size control); cagrilintide / sCT activate LPBN cFos in WT mice | Meal termination / satiety; strong weight-loss relevance | PBN CGRP neurons are a general alarm / aversion relay (food poisoning, pain, itch, hypercapnia) → CeA / BNST; chronic activation → severe anorexia / starvation i
  - EN line 101 (Part 2): | Central Amygdala (CeA) | LPBN CGRP → CeA PKC-δ neurons; CeA PKC-δ mediates CCK-induced anorexia | CGRP-PBN axons synapse onto most PKC-δ CeA neurons; CeA Fos induced by CCK / Exendin-4 is abolished by PBN CGRP inactivation (mice); some PKC-δ CeA neurons express CGRP receptors. Direct amylin → CeA activation not shown; amylin acts upstream via PBN | Meal termination / anorexia; if co-activated with malaise signals, forms aversion memory | CeA is a site of malaise-induced conditioned avoidance — amylin-specific CeA nausea mechanism **unverified** | Indirect / emerging | https://pmc.ncbi.nlm.ni

## CONTRADICTED (3)

### 1. https://journals.physiology.org/doi/full/10.1152/ajpregu.2001.281.4.R1232

- **Verdict:** contradicted
- **Cited in:** Chinese original
- **What was read:** full text — Physiology (AJP-Regu) paper, primary
- **Findings / corrections:** CONTRADICTED as BBB source: this is an accumbens-infusion study, NOT a BBB-transport study. Do NOT cite for Banks & Kastin 1998/1995 BBB numbers, striatal accumulation, insulin comparison, or the mRNA claim.
- **Report claims attributed to this source:**
  - ZH line 336 (Part 4): - **支持 BBB 本身穿透的证据（内源性 Amylin，大鼠，放射性标记）**：Banks & Kastin 1998, *Peptides*：静脉放射性标记 Amylin 穿过 BBB，在多个脑结构蓄积包括纹状体；脑穿透超过胰岛素。Banks et al. 1995：BBB 对 Amylin 的通透性（放射性标记研究）。脑中未检出 Amylin mRNA → 脑 Amylin 来自循环，与血液到脑转运一致。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC3960470/ ；https://journals.physiology.org/doi/full/10.1152/ajpregu.2001.281.4.R1232 ；https://www.sciencedirect.com/science/article/abs/pii/002432059502197Q [index, 2026-10-15]

### 2. https://pmc.ncbi.nlm.nih.gov/articles/PMC3960470/

- **Verdict:** contradicted
- **Cited in:** Chinese original
- **What was read:** full text — PMC paper, primary
- **Findings / corrections:** CONTRADICTED as BBB source: this is a PPI/accumbens study. Do NOT cite for BBB penetration.
- **Report claims attributed to this source:**
  - ZH line 336 (Part 4): - **支持 BBB 本身穿透的证据（内源性 Amylin，大鼠，放射性标记）**：Banks & Kastin 1998, *Peptides*：静脉放射性标记 Amylin 穿过 BBB，在多个脑结构蓄积包括纹状体；脑穿透超过胰岛素。Banks et al. 1995：BBB 对 Amylin 的通透性（放射性标记研究）。脑中未检出 Amylin mRNA → 脑 Amylin 来自循环，与血液到脑转运一致。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC3960470/ ；https://journals.physiology.org/doi/full/10.1152/ajpregu.2001.281.4.R1232 ；https://www.sciencedirect.com/science/article/abs/pii/002432059502197Q [index, 2026-10-15]

### 3. https://pubmed.ncbi.nlm.nih.gov/17393306/

- **Verdict:** contradicted
- **Cited in:** English report
- **What was read:** full text — PubMed abstract
- **Findings / corrections:** WRONG CITATION: PMID 17393306 is a heart-failure exercise-testing review, nothing to do with pramlintide or amylin substitutions. REMOVE this citation entirely.
- **Report claims attributed to this source:**
  - EN line 194 (Part 3): - **Substitution sites**: **Conflicting** — one source states pramlintide substitutes human amylin residues 25, 28, 29 with Pro; another states residues 25, 26, 29 with Pro (and rat amylin differs from human at 6 residues, 3 of which are Pro at 25, 28, 29); the difference is unverified. Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://pubmed.ncbi.nlm.nih.gov/17393306/ [index, 2026-10-15]

## COULD-NOT-ACCESS (63)

### 1. http://ndl.ethernet.edu.et/bitstream/123456789/37143/1/Andrew%20Young.pdf

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** fetch timed out; not retried
- **Findings / corrections:** Claim: rat amylin terminal half-life 13 min; cleared mainly by renal proteolysis. Not verified.
- **Report claims attributed to this source:**
  - EN line 34 (Part 1): | Clearance / half-life | Cleared mainly by renal proteolysis; rat amylin terminal half-life in rats 13 minutes (rodent only) | http://ndl.ethernet.edu.et/bitstream/123456789/37143/1/Andrew%20Young.pdf [index, 2026-10-15] |

### 2. https://www.globenewswire.com/news-release/2026/09/08/3357602/0/en/structure-therapeutics-reports-positive-clinical-data-across-oral-small-molecule-amylin-and-glp-1-programs-for-chronic-weight-management.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried (tool limit, not source failure)
- **Findings / corrections:** ACCG-2671 SAD -3.3% Day 24, CTX-1 down ~60%, t1/2 ~6 days, Tmax 1-1.5 h, nausea/vomiting counts, no SAE — not verified.
- **Report claims attributed to this source:**
  - EN line 187 (Part 3): | ACCG-2671 (oral small molecule) | Structure Therapeutics | Phase 1/2a — single-ascending-dose (SAD) completed (Sep 2026); multiple-ascending-dose (MAD) ongoing (including evaluation with injectable GLP-1 RA) | Oral; daily and weekly dosing both under evaluation | Terminal ~6 days; Tmax 1–1.5 h; dose-proportional exposure | Phase 1 SAD (n = 31, healthy adults without obesity, single dose): single 10 mg → mean −3.3% body weight at Day 24 (exploratory, **not placebo-corrected** in the source); CTX-1 (bone-resorption biomarker) ↓ ~60% on Day 2 (target-engagement signal) | No SAE, no discontinuat
  - EN line 291 (Part 3): - Source: https://www.globenewswire.com/news-release/2026/09/08/3357602/0/en/structure-therapeutics-reports-positive-clinical-data-across-oral-small-molecule-amylin-and-glp-1-programs-for-chronic-weight-management.html [index, 2026-10-15]
  - EN line 345 (Part 4): - **Dose titration**: Slow dose escalation reduces GI adverse events (e.g., pramlintide: start low, increase only after ≥3 days without nausea; ACCG-2671 SAD was not titrated and showed dose-related nausea / vomiting; MAD testing titration). Sources: https://www.medscape.com/viewarticle/523581_6 ; https://www.globenewswire.com/news-release/2026/09/08/3357602/0/en/structure-therapeutics-reports-positive-clinical-data-across-oral-small-molecule-amylin-and-glp-1-programs-for-chronic-weight-management.html [index, 2026-10-15]

### 3. https://www.jneurosci.org/content/32/48/17401

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Abeta1-42 50 nM + human amylin 50 nM inhibit hippocampal LTP; AC253 250 nM blocks both; TgCRND8 rescue — not verified.
- **Report claims attributed to this source:**
  - EN line 102 (Part 2): | Hippocampus | Hippocampal CA1 → LTP (memory proxy); AMY3 proposed as Aβ receptor | Aβ1-42 (50 nM) + human amylin (50 nM) inhibit mouse slice hippocampal LTP; AC253 (250 nM) blocks both without affecting baseline / isolated LTP; LTP impairment in TgCRND8 mice improved by AC253 (mouse slices / transgenic) | No established weight-loss role; relevance is Alzheimer's / cognition hypothesis, not an obesity pathway | No established metabolic adverse effect; AMYR antagonism is a research AD direction, opposite to the obesity agonist direction | Emerging, AD-related only | https://www.jneurosci.org/c

### 4. https://www.mdpi.com/1422-0067/26/14/6693

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** IDE degrades amylin; IDE cleaves insulin/glucagon/amylin/ANP/IGF-1/2/Abeta; up to ~70-aa peptides — not verified.
- **Report claims attributed to this source:**
  - ZH line 357 (Part 4): - **蛋白酶**：**胰岛素降解酶（IDE）**：Amylin 部分经 IDE 降解；IDE 切割胰岛素、胰高血糖素、Amylin、ANP、IGF-1/2、Aβ；切割长达约 70 氨基酸的肽。来源：https://en.wikipedia.org/wiki/Amylin ；https://www.mdpi.com/1422-0067/26/14/6693 [index, 2026-10-15]。**Neprilysin（NEP）**：检索来源中**未发现直接证据**表明 NEP 降解 Amylin / Pramlintide / Cagrilintide；NEP + IDE 为已确立的 Aβ 降解蛋白酶——**勿在无证据时将 NEP → Amylin 转移**。合成激动剂的其他肽酶：具体蛋白酶身份**未在 FDA 说明书 / 检索论文中公开披露**；肾脏蛋白水解推定为多肽酶。

### 5. https://www.medchemexpress.eu/Targets/amylin-receptor.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amylin vasodilation / cardiomyocyte contractility EC50 216 pM vs CGRP 21 pM — not verified. Vendor page (secondary) even when read.
- **Report claims attributed to this source:**
  - EN line 113 (Part 2): | Blood pressure / vasodilation | Amylin mediates vasodilation via CGRP receptors (rodent ex vivo) | Amylin (8-37) has direct vasodilator action in isolated rat mesenteric resistance arteries; amylin + GLP-1 cause dose- / time-dependent relaxation of pre-contracted rat pulmonary artery rings; amylin via CGRP1-preferring receptors ↑ rat ventricular cardiomyocyte contractility (EC50 216 pM vs CGRP 21 pM) — rodent, ex vivo / isolated cells | No established systemic blood-pressure effect of amylin agonists in humans; do not assume blood-pressure lowering | No established hypertension / hypotension

### 6. https://www.medscape.com/medline/abstract/37329973

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** KBP series preclinical/terminated; Lilly licensed DACRA platform 2017 — not verified.
- **Report claims attributed to this source:**
  - EN line 179 (Part 3): | KBP series (DACRA) | KeyBioscience (Nordic Bioscience subsidiary); Lilly licensed the DACRA platform in 2017 | All preclinical / terminated, no clinical program in development | Injection (rat Q3D) | Not applicable (no human data) | No human data; rats: weight loss, reduced fat, improved glucose tolerance | Not applicable | https://www.pharmaceutical-technology.com/news/newseli-lilly-and-keybioscience-collaborate-to-develop-potential-type-2-diabetes-treatment-5838359/ ; https://www.medscape.com/medline/abstract/37329973 [index, 2026-10-15] |
  - EN line 238 (Part 3): - KeyBioscience DACRA series (KBP-042 / -089 / -056 etc.); Lilly licensed the DACRA platform in 2017; all preclinical or terminated, no clinical program. Source: https://www.pharmaceutical-technology.com/news/newseli-lilly-and-keybioscience-collaborate-to-develop-potential-type-2-diabetes-treatment-5838359/ ; https://www.medscape.com/medline/abstract/37329973 [index, 2026-10-15]

### 7. https://www.medscape.com/viewarticle/549147

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pramlintide 15 min pre-meal slows gastric emptying, suppresses glucagon, increases satiety, no change in net absorption — not verified.
- **Report claims attributed to this source:**
  - EN line 109 (Part 2): | Delayed gastric emptying | AP amylin receptors → vagal efferent fibers → gut → slowed gastric emptying | Human: pramlintide injected 15 min before meals slows gastric emptying, suppresses glucagon, ↑ satiety, blunts postprandial hyperglycemia; slows gastric emptying without changing net carbohydrate / nutrient absorption | ↓ postprandial glucose appearance, ↑ fullness / satiety; contributes to weight loss via reduced intake | Slowed gastric emptying may contribute to nausea / fullness / vomiting, but causal separation from central nausea is **unverified**; pramlintide nausea is dose-dependen

### 8. https://www.ncbi.nlm.nih.gov/books/NBK548949/pdf/Bookshelf_NBK548949.pdf

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Glucagon suppression without impairing hypoglycemia response; pramlintide AE profile / titration / 50% insulin reduction — not verified.
- **Report claims attributed to this source:**
  - EN line 110 (Part 2): | Glucagon suppression | Amylin → islet alpha cells (direct and/or islet paracrine; exact alpha-cell AMY subtype **unverified**) → ↓ postprandial glucagon → ↓ hepatic glycogenolysis / glucose production | Human: pramlintide suppresses inappropriately elevated glucagon during hyperglycemia without impairing the normal glucagon response to hypoglycemia; endogenous anti-amylin antiserum ↑ arginine-stimulated glucagon (and insulin / somatostatin) (ex vivo rat islets) | ↓ postprandial glucose swings; weight-loss relevance indirect (glycemic control, not a primary anorexia mechanism) | No establishe
  - EN line 157 (Part 2): - **Human (pramlintide)**: Common nausea, vomiting, anorexia, fatigue, headache, dizziness, hypoglycemia (with insulin); nausea is dose-dependent, mostly mild–moderate, early, and fades over time; slow titration + 50% mealtime insulin reduction ↓ risk. Sources: https://www.ncbi.nlm.nih.gov/books/NBK548949/pdf/Bookshelf_NBK548949.pdf ; https://www.medscape.com/viewarticle/523581_6 [index, 2026-10-15]

### 9. https://www.novonordiskmedical.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/the-physiological-functions-of-amylin.pdf

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pancreatic alpha-cell glucagon suppression mechanism unresolved; brain AP/NTS/LPB/hypothalamus/VTA/LDTg/accumbens circuit — not verified.
- **Report claims attributed to this source:**
  - ZH line 345 (Part 4): - **胰腺——α 细胞 → 胰高血糖素抑制**：抑制餐后 α 细胞胰高血糖素分泌 → ↓ 肝糖原分解 / 糖异生 → ↓ 内源性葡萄糖输出 → ↓ 餐后血糖。机制未解决：(a) 假设直接经胰岛门脉循环（β 细胞 → α 细胞局部高浓度），(b) AP 刺激后的中枢神经元介导减少。来源将通路描述为“了解不充分” / 神经元介导。来源：https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S1054358905520088 ；https://tmedweb.tulane.edu/pharmwiki/doku.php/pramlintide?do=export_pdf ；https://www.novonordiskmedical.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/the-physiological-functions-of-amylin.pdf [index, 2026-10-15]
  - ZH line 347 (Part 4): - **脑——AP / NTS / LPB-PBN / 下丘脑 / VTA / LDTg / 伏隔核**：AP = 首要传感器；NTS + LPB = 中继；下丘脑 = 稳态饱感；VTA / LDTg / 伏隔核 = 奖赏 / 动机进食；亦恢复瘦素反应性（临床前）。功能结局：↓ 摄食、↑ 饱感、↓ 体重。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/ ；https://www.novonordiskmedical.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/the-physiological-functions-of-amylin.pdf ；https://pmc.ncbi.nlm.nih.gov/articles/PMC5503810/ [index, 2026-10-15]

### 10. https://www.pharmacytimes.com/view/cagrisema-curbs-food-noise-organ-fat-in-patients-with-obesity-t2d-respectively

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** CagriSema REDEFINE-1 efficacy block — not verified.
- **Report claims attributed to this source:**
  - ZH line 218 (Part 3): **CagriSema（Cagrilintide 2.4 mg + Semaglutide 2.4 mg）**：Novo Nordisk。NDA 已于 2025 年 12 月 18 日递交 FDA（减重管理）；决定预计 2026 年 Q4；截至 2026 年 10 月未获批。REDEFINE = 肥胖项目；REIMAGINE = T2D 项目。皮下注射，每周一次，固定剂量复方。半衰期：组分半衰期适用（Semaglutide 约 7 天；Cagrilintide 约 7–8 天，据次级来源）。疗效：REDEFINE 1（Phase 3，NCT05567796，n = 3,417，肥胖 / 超重无 T2D，68 周）：CagriSema 22.7%（试验产品 estimand）/ 20.4%（治疗策略）vs 安慰剂 2.3% / 3.0%；Semaglutide 单药 16.1% / 14.9%；Cagrilintide 单药 11.8% / 11.5%；91.9% 减重 ≥ 5%；基线肥胖参与者中 54% 降至肥胖阈值以下 vs 安慰剂 11.1%；DXA 亚组：−23.9%（CagriSema）vs −16.6%（Semaglutide）vs −15.0%（Cagrilintide）vs −2.8%（安慰剂）；减重中 66.9% 为脂肪量。REDEFINE 2（Phase 3，NC

### 11. https://www.prnewswire.com/news-releases/abbvie-presents-detailed-phase-1-data-for-abbv-295-a-long-acting-amylin-analog-demonstrating-favorable-tolerability-and-pharmacokinetic-profile-at-easd-2026-302893611.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** ABBV-295 MAD weekly -7.8% to -9.8%; EOW 14 mg -9.7%; monthly 8 mg -7.9% vs placebo ~-0.3%; t1/2 10.7-12.3 days; Tmax 24.0-48.1 h; Phase 2 Aug 2026 — not verified.
- **Report claims attributed to this source:**
  - EN line 178 (Part 3): | ABBV-295 (GUB014295) | Gubra (originator GUB014295) → AbbVie (Mar 2025 license, up to $2.23B) | Phase 1 complete; Phase 2 started Aug 2026 (NCT07752979) | SC; weekly, every-other-week, and monthly tested | Mean 10.7–12.3 days; median Tmax 24.0–48.1 h | Phase 1 MAD (12–13 weeks): weekly −7.8% to −9.8%; every-other-week 14 mg −9.7%; monthly 8 mg −7.9% vs placebo ~−0.3% | Per AbbVie "well tolerated"; detailed AE rates not disclosed in retrieved press releases | https://www.prnewswire.com/news-releases/abbvie-presents-detailed-phase-1-data-for-abbv-295-a-long-acting-amylin-analog-demonstrating-f
  - EN line 234 (Part 3): - Phase 1 (NCT06795132) MAD: weekly −7.8% to −9.8%; every-other-week 14 mg −9.7%; monthly 8 mg −7.9% vs placebo ~−0.3%; mean t1/2 10.7–12.3 days; median Tmax 24.0–48.1 h; AbbVie states "well tolerated"; detailed AE rates not disclosed. Phase 2 started Aug 2026 (NCT07752979). Source: https://www.prnewswire.com/news-releases/abbvie-presents-detailed-phase-1-data-for-abbv-295-a-long-acting-amylin-analog-demonstrating-favorable-tolerability-and-pharmacokinetic-profile-at-easd-2026-302893611.html [index, 2026-10-15]

### 12. https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Cagrilintide Phase 1b Tmax 24-72 h; AUC/Cmax ranges; t1/2 159-195 h; GI AEs 207/566 (37%); titration claims — not verified.
- **Report claims attributed to this source:**
  - ZH line 309 (Part 4): - **Cagrilintide**：SC 每周一次，在研；CagriSema 中与 Semaglutide 2.4 mg 共配制 / 联合给药。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_ [index, 2026-10-15]
  - ZH line 317 (Part 4): - **Cagrilintide**：Phase 1b 多剂量 + Semaglutide 研究中位 Tmax 24–72 小时；另一综述引用 2.4 mg 时中位 Tmax 约 24 小时；暴露量剂量成比例；AUC0–168h 926–24,271 nmol×h/L，Cmax 6.14–170 nmol/L（0.16–4.5 mg）；人类 SC 绝对生物利用度**未在检索来源中公开披露**——请勿假设；大鼠 IV vs SC 半衰期 20±2 小时 vs 27±3 小时（仅临床前，非人类生物利用度）。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_ ；https://www.medchemexpress.eu/cagrilintide.html [index, 2026-10-15]
  - ZH line 324 (Part 4): - **Cagrilintide**：Phase 1b：血浆清除率 + Vd “各治疗组相似”——数值 Vd / CL **未在摘要 / 检索来源中公开披露**；PK 剂量成比例 + 线性；暴露主要由表观清除率（CL/F）决定；AUC = 剂量 / (CL/F)。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_ ；https://link.springer.com/article/10.1007/s40262-026-01654-0 [index, 2026-10-15]
  - ZH line 358 (Part 4): - **Cagrilintide**：半衰期 Phase 1b 中 159–195 小时（0.16–4.5 mg + Semaglutide）；另一综述：2.4 mg 时 184 ± 7.4 小时；支持每周一次给药。肾 / 肝损害单剂量研究：无 PK 效应 → 剂量调整可能性低（低剂量 / 小样本局限如上）。蛋白酶 / 排泄途径（完整 vs 片段、尿比例）：**未公开披露**。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_ ；https://link.springer.com/article/10.1007/s40262-026-01654-0 [index, 2026-10-15]
  - ZH line 366 (Part 4): - **恶心 / 呕吐机制**：AP = 化学感受器触发区 / 呕吐回路；AP + NTS 激活 → 恶心 / 呕吐；剂量依赖，起始 / 递增期最重，随时间 / 耐受减轻。Pramlintide 说明书：恶心起始较高，随时间下降；逐渐滴定使发生率 / 严重程度最小化。T2D 汇总试验：恶心 28%（Symlin 120 mcg BID + 胰岛素）vs 安慰剂 12%；呕吐 8% vs 4%；头痛 13% vs 7%；厌食 9% vs 2%。来源：https://www.medicinenet.com/side_effects_of_symlin_pramlintide/side-effects.htm ；https://www.drugs.com/pro/symlin.html [index, 2026-10-15]。Cagrilintide Phase 1b：胃肠疾病占不良事件 37%（207/566），多为轻中度。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_sem
  - ZH line 368 (Part 4): - **剂量滴定原理**：Pramlintide：低剂量起始（T1D 15 mcg；T2D 按说明书滴定），仅在换剂量后 ≥ 3 天无恶心时才增加；切勿与胰岛素混合；注射部位与胰岛素相距 > 2 英寸。来源：https://fda.report/DailyMed/4aea30ff-eb0d-45c1-b114-3127966328ff [index, 2026-10-15]。长效激动剂：缓慢递增减少胃肠不良事件——Cagrilintide Phase 1b 每 4 周递增；Petrelintide 起始 0.5 mg，固定 4 周递增步长，73% 恶心发生于递增期，88–98% 达到目标维持剂量；Eloralintide 较慢递增 → 胃肠不良事件发生率更低，1–3 mg 时与安慰剂相似。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_

### 13. https://www.science.org/doi/10.1126/science.abm9609

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amylin-bound AMYR conformations similar across AMY1/2/3; RAMP-constrained; bypass motif; CT-bound complexes differ — not verified.
- **Report claims attributed to this source:**
  - EN line 54 (Part 1): - **Cryo-EM**: Amylin-bound AMYR conformations are similar across AMY1 / 2 / 3, constrained by RAMP and an ordered mid-region peptide "bypass" motif; CT-bound AMYR complex conformations differ and overlap with CT-bound CTR. Source: https://www.science.org/doi/10.1126/science.abm9609 [index, 2026-10-15]

### 14. https://www.sciencedirect.com/science/article/abs/pii/0167011595001204

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amylin vasodilation / cardiomyocyte contractility EC50 216 pM vs CGRP 21 pM — not verified.
- **Report claims attributed to this source:**
  - EN line 113 (Part 2): | Blood pressure / vasodilation | Amylin mediates vasodilation via CGRP receptors (rodent ex vivo) | Amylin (8-37) has direct vasodilator action in isolated rat mesenteric resistance arteries; amylin + GLP-1 cause dose- / time-dependent relaxation of pre-contracted rat pulmonary artery rings; amylin via CGRP1-preferring receptors ↑ rat ventricular cardiomyocyte contractility (EC50 216 pM vs CGRP 21 pM) — rodent, ex vivo / isolated cells | No established systemic blood-pressure effect of amylin agonists in humans; do not assume blood-pressure lowering | No established hypertension / hypotension

### 15. https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S1054358905520088

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Glucagon suppression via islet portal circulation vs AP-mediated neuronal route; pathway 'poorly understood' — not verified.
- **Report claims attributed to this source:**
  - ZH line 345 (Part 4): - **胰腺——α 细胞 → 胰高血糖素抑制**：抑制餐后 α 细胞胰高血糖素分泌 → ↓ 肝糖原分解 / 糖异生 → ↓ 内源性葡萄糖输出 → ↓ 餐后血糖。机制未解决：(a) 假设直接经胰岛门脉循环（β 细胞 → α 细胞局部高浓度），(b) AP 刺激后的中枢神经元介导减少。来源将通路描述为“了解不充分” / 神经元介导。来源：https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S1054358905520088 ；https://tmedweb.tulane.edu/pharmwiki/doku.php/pramlintide?do=export_pdf ；https://www.novonordiskmedical.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/the-physiological-functions-of-amylin.pdf [index, 2026-10-15]

### 16. https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(25)00280-4/fulltext

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** DVC cFos, AP cFos -57% in RAMP1/3 KO; LPBN cFos; ARC not assessed; petrelintide pEC50 AMY1R 10.6 / CTR 9.5 — not verified.
- **Report claims attributed to this source:**
  - EN line 97 (Part 2): | NTS / Dorsal Vagal Complex (DVC) | AP → NTS; NTS integrates vagal gut signals; DVC = AP + NTS + dorsal motor nucleus of the vagus | Cagrilintide + salmon calcitonin activate DVC cFos in WT mice; DVC cFos reduced in RAMP1/3 KO; AP cFos reduced 57% | Meal termination / satiety; vagal efferent link to gastric emptying | — | Established (rodent) | https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(25)00280-4/fulltext [index, 2026-10-15] |
  - EN line 98 (Part 2): | Parabrachial Nucleus (PBN), especially lateral PBN (LPBN) | AP / NTS → LPBN CGRP (Calca) neurons → central amygdala (CeA) + bed nucleus of the stria terminalis (BNST) | Systemic amylin / CCK activate CGRP-PBN neurons; PBN CGRP neurons control meal termination (activation ↓ meal size; inactivation disrupts meal-size control); cagrilintide / sCT activate LPBN cFos in WT mice | Meal termination / satiety; strong weight-loss relevance | PBN CGRP neurons are a general alarm / aversion relay (food poisoning, pain, itch, hypercapnia) → CeA / BNST; chronic activation → severe anorexia / starvation i
  - EN line 99 (Part 2): | Hypothalamus ARC / VMH / PVN | ARC POMC / CART (anorexigenic, α-MSH → MC4R in PVN / LHA) vs ARC AgRP / NPY (orexigenic, MC4R antagonists); PVN integrates ARC + hindbrain signals; VMH / DMH / LHA are secondary | Mouse Calcr enriched in ARC, median eminence, DMH, PVN, etc. (rodent); the cagrilintide study explicitly states ARC neuronal activation was not assessed, so AgRP / POMC-mediated anorexia / weight loss cannot be inferred from it; that study cites prior work stating POMC-neuron CTR signaling is required for energy-balance maintenance (via energy expenditure) | If activated, would regula
  - EN line 202 (Part 3): - **Mechanism**: Non-selective DACRA (dual amylin + calcitonin receptor agonist). Source: https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(25)00280-4/fulltext [index, 2026-10-15]
  - EN line 214 (Part 3): - **Potency / mechanism**: Potent amylin + calcitonin receptor agonist (DACRA-type, not subtype-selective); in vitro pEC50 AMY1R 10.6 (comparable to cagrilintide 10.4) and CTR 9.5. Source: https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(25)00280-4/fulltext [index, 2026-10-15]

### 17. https://www.tipranks.com/news/company-announcements/astrazenecas-azd6234-trial-completion-adds-new-catalyst-in-obesity-and-diabetes

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** AZD6234 APRICUS/ARAY/ASCEND trial details and completion status — not verified.
- **Report claims attributed to this source:**
  - ZH line 202 (Part 3): **AZD6234（AstraZeneca）**：每周注射选择性 Amylin 受体激动剂（SARA）/ 长效 Amylin 类似物。皮下注射，每周一次。半衰期未公开披露。无公开披露的疗效结果。试验：Phase 2b APRICUS（n = 262，超重 / 肥胖；数据预计 2026 年上半年——未找到读数）；Phase 2 ARAY（n = 64，超重 / 肥胖 + T2D，使用稳定 GLP-1 RA；据 2026 年 9 月更新已完成，结果未披露）；Phase 2b ASCEND（n = 360）测试 AZD9550（GLP-1 / 胰高血糖素）+ AZD6234，数据预计 2026 年下半年。安全性未公开披露。来源：https://medcitynews.com/2026/01/astrazeneca-obesity-diabetes-cspc-glp-1-gip-agonist-metabolic-disease-azn/ ；https://www.tipranks.com/news/company-announcements/astrazenecas-azd6234-trial-completion-adds-new-catalyst-in-obesity-and-diabetes [index, 2026-10-15]

### 18. https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pramlintide FDA label details — not verified (FDA.report mirror of the same label was read in batch 4; see that entry).
- **Report claims attributed to this source:**
  - ZH line 308 (Part 4): - **Pramlintide（Symlin）**：仅 SC；合成 Amylin 类似物；主要餐前即刻注射。内源性 Amylin 因不溶 / 溶液中聚集而不适合药用；Pramlintide 经脯氨酸取代 → 稳定、可溶类似物。来源：https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf ；https://tmedweb.tulane.edu/pharmwiki/doku.php/pramlintide?do=export_pdf [index, 2026-10-15]
  - ZH line 316 (Part 4): - **Pramlintide**：绝对 SC 生物利用度约 30–40%；Cmax + AUC 线性、剂量依赖；Tmax 约 19–21 分钟（30 mcg → 21 分钟；60 mcg → 20 分钟；90 mcg → 19 分钟；120 mcg → 21 分钟）；作用持续时间 < 150 分钟；手臂注射 → 肥胖者总体暴露 +20–36% 且变异更大（vs 腹部 / 大腿）。来源：https://www.drugs.com/pro/symlin.html ；https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf ；https://www.drugs.com/monograph/pramlintide.html [index, 2026-10-15]
  - ZH line 356 (Part 4): - **Pramlintide**：主要经肾脏代谢 → 活性代谢物 des-Lys¹ Pramlintide（2–37 Pramlintide）；消除半衰期约 48 分钟（说明书表 5：48–55 分钟，30–120 mcg 剂量范围；30 mcg → 55 分钟，60 mcg → 49 分钟，90 mcg → 51 分钟，120 mcg → 48 分钟）；排泄主要经尿（次级来源）；肝损害 / 年龄 / 性别 / 种族影响据说明书未知。来源：https://www.drugs.com/monograph/pramlintide.html ；https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf [index, 2026-10-15]
  - ZH line 367 (Part 4): - **低血糖风险（Pramlintide + 胰岛素）**：黑框警告：与餐时胰岛素合用 ↑ 胰岛素诱导严重低血糖风险，主要为 T1D；严重低血糖发生时多在注射后 3 小时内观察到。说明书：起始时餐时胰岛素减量约 50%；低血糖时 / 跳过餐食 / 餐食 < 250 kcal 或 < 30 g 碳水时勿注射。Pramlintide 不改变胰岛素诱导低血糖的反调节激素反应，也不改变低血糖症状感知（低至 45 mg/dL）。来源：https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf ；https://fda.report/DailyMed/4aea30ff-eb0d-45c1-b114-3127966328ff [index, 2026-10-15]。Cagrilintide / CagriSema 在无糖尿病肥胖中：综述称**未**伴随低血糖风险增加——无数据时勿外推至胰岛素治疗 T1D / T2D。来源：https://www.passeidireto.com/arquivo/158376647/efficacy-and-safety-of-cagrilintide-alone-and-in-2 [index, 2026-10-15]

### 19. https://escholarship.org/content/qt1g34z6bf/qt1g34z6bf_noSplash_d801507b3399ac0542ca798718da4131.pdf

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** HTTP 403 / browser 429; not retried
- **Findings / corrections:** KBP-042/089/056 preclinical data — not verified.
- **Report claims attributed to this source:**
  - EN line 95 (Part 2): | Area Postrema (AP) | AP → NTS (dorsal vagal complex, DVC) → lateral parabrachial nucleus (LPBN) → hypothalamus / forebrain; AP is a circumventricular organ without a BBB | AP / NTS lesions abolish the anorectic effect of chronic peripheral amylin in rats; intra-AP injection of amylin antagonist AC187 increases food intake in rats; AP is required for amylin effects | Satiety / reduced meal size; primary hindbrain satiety node | AP CALCR+ neurons in mouse genetics suppress feeding without inducing avoidance (vs AP GLP1R+ neurons driving aversion) — suggesting satiety and nausea are separable, 

### 20. https://web.cdn.cyagen.com/product-hub/pdf/C001822%20B6-hRAMP1_EN_Strain%20Datasheet.pdf

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** unresolvable / browser 429; not retried
- **Findings / corrections:** Cyagen RAMP1 mouse strain claims — not verified.
- **Report claims attributed to this source:**
  - EN line 83 (Part 1): | RAMP1 (overall) | Widely expressed: brain (hypothalamus, brainstem, cortex), adrenal, digestive system, bone, reproductive system, muscle, immune cells (NK / T / B / CD14+ monocytes) — from a humanized-mouse datasheet summary, not original HPA quantification | https://web.cdn.cyagen.com/product-hub/pdf/C001822%20B6-hRAMP1_EN_Strain%20Datasheet.pdf [index, 2026-10-15] |

### 21. https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Renal amylin deposition in diabetic nephropathy — not verified.
- **Report claims attributed to this source:**
  - EN line 35 (Part 1): | Aggregation and T2D | Autopsy finds islet amyloid deposition in >90% (one review) or 70–90% (another review) of T2D patients; oligomers are considered more toxic than fibers / deposits; mechanisms include membrane permeabilization, ER stress, mitochondrial damage, beta-cell death; insulin prevents aggregation inside secretory granules | https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext ; https://www.mdpi.com/2073-4409/7/8/95 [index, 2026-10-15] |
  - EN line 80 (Part 1): | Kidney | CALCR protein in renal tubules (HPA); kidney is the main amylin clearance organ; renal amylin deposition reported in diabetic nephropathy | https://www.proteinatlas.org/ENSG00000004948-CALCR ; https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext [index, 2026-10-15] |
  - EN line 115 (Part 2): | Other peripheral (kidney, GI secretion) | Kidney: renal amylin deposition reported in diabetic nephropathy; kidney clears IAPP; strict metabolic control hypothesized to reduce deposition (observational / hypothesis). GI secretion: exogenous amylin inhibits gastric acid secretion, digestive enzymes, bile (review, rodent / limited human data) | Observational / hypothesis; GI secretion is an **unverified** independent clinical pathway | — | — | Emerging / limited | https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext ; https://www.medscape.com/viewarticle/523581_4 [index,

### 22. https://www.mdpi.com/1589566

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** MDPI amylin claims — not verified.
- **Report claims attributed to this source:**
  - ZH line 337 (Part 4): - **反对假设治疗性 BBB 穿透的证据 / caveat**：Pramlintide / Cagrilintide / Eloralintide / Petrelintide 的人类 CSF 数据**未公开披露 / 未找到**。放射性标记研究年代久远、大鼠、内源性 Amylin——不能证明大分子酰化、白蛋白结合类似物（Cagrilintide 约 4,409 Da + 白蛋白复合物、Eloralintide、Petrelintide）在人类治疗游离浓度下穿透 BBB 本身；白蛋白结合预期降低游离脑穿透部分——定量数据**未披露**。全身给药后的下丘脑 / VTA 效应主要由 AP → NTS → PBN 神经接力 + c-Fos 激活解释，而非药物直接扩散至这些部位。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/ ；https://www.mdpi.com/1589566 [index, 2026-10-15]
  - ZH line 339 (Part 4): - **CTR + RAMP 同细胞共表达（完全活性 AMYR 所需）**：主要在 AP + 部分下丘脑被证实；外周 / 其他脑区共表达数据薄弱。来源：https://www.mdpi.com/1589566 [index, 2026-10-15]
  - ZH line 351 (Part 4): - **骨骼肌 / 脂肪 / 肝（次要，证据薄）**：Amylin 受体报告分布于脑、胰腺、脂肪、胃肠。较老文献：Amylin 反对肌肉糖原合成、激活糖原分解 / 糖酵解；可能调节乳糜微粒摄取 / 脂蛋白受体。是否由充分表征的外周 AMYR 介导**未证实**（外周 CTR + RAMP 共表达数据自 1998 年以来稀疏）。来源：https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01487-X/abstract ；https://www.mdpi.com/1589566 ；https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810 [index, 2026-10-15]

### 23. https://www.medchemexpress.eu/cagrilintide.html

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Cagrilintide vendor-page claims — not verified.
- **Report claims attributed to this source:**
  - ZH line 317 (Part 4): - **Cagrilintide**：Phase 1b 多剂量 + Semaglutide 研究中位 Tmax 24–72 小时；另一综述引用 2.4 mg 时中位 Tmax 约 24 小时；暴露量剂量成比例；AUC0–168h 926–24,271 nmol×h/L，Cmax 6.14–170 nmol/L（0.16–4.5 mg）；人类 SC 绝对生物利用度**未在检索来源中公开披露**——请勿假设；大鼠 IV vs SC 半衰期 20±2 小时 vs 27±3 小时（仅临床前，非人类生物利用度）。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_semaglutide_24_mg_for_weight_management_a_randomised_controlled_phase_1b_ ；https://www.medchemexpress.eu/cagrilintide.html [index, 2026-10-15]

### 24. https://www.medscape.com/viewarticle/523581_4

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Medscape review claims (amylin physiology) — not verified.
- **Report claims attributed to this source:**
  - EN line 78 (Part 1): | Pancreas | Mouse islet beta cells: RAMP1 and RAMP3 mRNA co-localize with CTR mRNA; amylin binding sites also seen in beta cells, skeletal muscle, kidney, lung, brain (review). Human beta-cell AMY subtype composition **unverified** | https://www.medscape.com/viewarticle/523581_4 [index, 2026-10-15] |
  - EN line 110 (Part 2): | Glucagon suppression | Amylin → islet alpha cells (direct and/or islet paracrine; exact alpha-cell AMY subtype **unverified**) → ↓ postprandial glucagon → ↓ hepatic glycogenolysis / glucose production | Human: pramlintide suppresses inappropriately elevated glucagon during hyperglycemia without impairing the normal glucagon response to hypoglycemia; endogenous anti-amylin antiserum ↑ arginine-stimulated glucagon (and insulin / somatostatin) (ex vivo rat islets) | ↓ postprandial glucose swings; weight-loss relevance indirect (glycemic control, not a primary anorexia mechanism) | No establishe
  - EN line 115 (Part 2): | Other peripheral (kidney, GI secretion) | Kidney: renal amylin deposition reported in diabetic nephropathy; kidney clears IAPP; strict metabolic control hypothesized to reduce deposition (observational / hypothesis). GI secretion: exogenous amylin inhibits gastric acid secretion, digestive enzymes, bile (review, rodent / limited human data) | Observational / hypothesis; GI secretion is an **unverified** independent clinical pathway | — | — | Emerging / limited | https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext ; https://www.medscape.com/viewarticle/523581_4 [index,

### 25. https://www.morningstar.com/news/business-wire/20260605931887/verdiva-bio-presents-preclinical-data-on-investigational-obesity-drug-candidates-at-the-american-diabetes-association-86th-scientific-sessions

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Verdiva ADA 2026 preclinical data — not verified.
- **Report claims attributed to this source:**
  - ZH line 230 (Part 3): **Verdiva / Sciwind Amylin 候选**：VRB-103（每周一次口服 Amylin 类似物，肽）——Verdiva Bio（自 Sciwind 许可）；临床前；体外对人 Amylin 受体高 potency / 选择性（ADA 2026 临床前数据）；预计 2026 年下半年进入临床，作为单药及 + VRB-101（口服 GLP-1）；无人类数据。VRB-102（长效 SC Amylin 激动剂）——Verdiva / Sciwind；临床前；计划作为单药及 + GLP-1；检索来源中无数据。VRB-101 + VRB-103 列为 DelveInsight 管线中临床前口服联合。XW015——列为临床前 SC 候选（见上）。来源：https://pharmaphorum.com/news/verdiva-bio-raises-411m-obesity-pipeline ；https://www.morningstar.com/news/business-wire/20260605931887/verdiva-bio-presents-preclinical-data-on-investigational-obesity-drug-candidates-at-the-american-diabetes-association-86th-scientific-

### 26. https://www.ncbi.nlm.nih.gov/gene?LinkName=geoprofiles_gene&from_uid=55342411

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** NCBI Gene expression claims — not verified.
- **Report claims attributed to this source:**
  - EN line 43 (Part 1): - **CTR subtypes**: NCBI lists CALCR transcript variants encoding subtype 1 and a shorter subtype 2 (lacking an in-frame variable exon in the 5′ coding region); the 16-amino-acid insert details of CTRa / CTRb are **unverified**. Source: https://www.ncbi.nlm.nih.gov/gene?LinkName=geoprofiles_gene&from_uid=55342411 [index, 2026-10-15]

### 27. https://www.passeidireto.com/arquivo/158376647/efficacy-and-safety-of-cagrilintide-alone-and-in-2

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Cagrilintide Phase 2 efficacy/safety (PasseiDireto mirror) — not verified.
- **Report claims attributed to this source:**
  - ZH line 367 (Part 4): - **低血糖风险（Pramlintide + 胰岛素）**：黑框警告：与餐时胰岛素合用 ↑ 胰岛素诱导严重低血糖风险，主要为 T1D；严重低血糖发生时多在注射后 3 小时内观察到。说明书：起始时餐时胰岛素减量约 50%；低血糖时 / 跳过餐食 / 餐食 < 250 kcal 或 < 30 g 碳水时勿注射。Pramlintide 不改变胰岛素诱导低血糖的反调节激素反应，也不改变低血糖症状感知（低至 45 mg/dL）。来源：https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf ；https://fda.report/DailyMed/4aea30ff-eb0d-45c1-b114-3127966328ff [index, 2026-10-15]。Cagrilintide / CagriSema 在无糖尿病肥胖中：综述称**未**伴随低血糖风险增加——无数据时勿外推至胰岛素治疗 T1D / T2D。来源：https://www.passeidireto.com/arquivo/158376647/efficacy-and-safety-of-cagrilintide-alone-and-in-2 [index, 2026-10-15]

### 28. https://www.pharmacytimes.com/view/eloratzp-delivers-up-to-23-3-weight-loss-in-adults-with-obesity-and-t2d

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** EloraTZP 24.6 kg absolute loss, NCT06603571, two separate injections — not verified. Reuters verified the core efficacy/safety numbers instead.
- **Report claims attributed to this source:**
  - EN line 183 (Part 3): | EloraTZP (eloralintide + tirzepatide) | Eli Lilly | Phase 2b complete; single-injection combination + Phase 3 planned before end of 2026; Phase 2b used two separate injections | SC, once weekly (Phase 2b: two separate injections) | Not stated separately; components: eloralintide ~13–15 days (reported), tirzepatide ~5 days (well known, not re-verified here) | Phase 2b (NCT06603571, 48 weeks): Elora 9 mg + TZP 15 mg −23.3% (24.6 kg) vs tirzepatide 15 mg alone −14.8% vs placebo −3.0% | Discontinuation due to AEs 10.8–27% (dose-dependent, combination arms) vs tirzepatide 2.9%, placebo 16.7% | ht
  - EN line 258 (Part 3): - Phase 2b (NCT06603571, 48 weeks): Elora 9 mg + TZP 15 mg −23.3% (24.6 kg) vs tirzepatide 15 mg alone −14.8% vs placebo −3.0%; Phase 2b used two separate injections; single-injection combination + Phase 3 planned before end of 2026. Discontinuation due to AEs 10.8–27% (dose-dependent, combination arms) vs tirzepatide 2.9%, placebo 16.7%. Sources: https://www.pharmacytimes.com/view/eloratzp-delivers-up-to-23-3-weight-loss-in-adults-with-obesity-and-t2d ; https://www.reuters.com/legal/litigation/experimental-lilly-combination-drug-tops-zepbound-weight-loss-trial-2026-09-30/ [index, 2026-10-15]

### 29. https://www.prnewswire.com/news-releases/ascletis-announces-initiation-of-phase-i-study-in-us-for-oral-amylin-receptor-peptide-agonist-asc36-for-the-treatment-of-obesity-302872005.html

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** ASC36 Phase 1 initiation, once-monthly to once-quarterly SQ peptide — not verified.
- **Report claims attributed to this source:**
  - ZH line 235 (Part 3): - **ASC36**——Ascletis；口服 Amylin 受体肽激动剂（POTENT 递送平台）；Phase 1 于 2026 年启动（n = 86，肥胖 / 超重，SAD / MAD）；临床前 NHP：口服生物利用度 6–8%，稳态半衰期 116–167 小时；NHP 口服片剂每日一次 7 天后减重高达 −13.2%；DIO 大鼠 SC 约 32% / 约 91% 大于 Eloralintide / Petrelintide 的减重；尚无人类数据。另有 ASC36_35FDC（ASC36 + ASC35 GLP-1 / GIP）每月一次 FDC 处于 Phase 1。来源：https://www.prnewswire.com/news-releases/ascletis-announces-initiation-of-phase-i-study-in-us-for-oral-amylin-receptor-peptide-agonist-asc36-for-the-treatment-of-obesity-302872005.html [index, 2026-10-15]

### 30. https://www.researchgate.net/publication/8040818_Hay_DL_Christopoulos_G_Christopoulos_A_Poyner_DR_Sexton_PM_Pharmacological_discrimination_of_calcitonin_receptor_receptor_activity-modifying_protein_complexes_Mol_Pharmacol_67_1655-1665

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Hay et al. 2005 RAMP discrimination claims — not verified.
- **Report claims attributed to this source:**
  - EN line 61 (Part 1): | hCT | pEC50 8.99 | 8.93 | 8.02 | Hay et al. 2005, via https://www.researchgate.net/publication/8040818_Hay_DL_Christopoulos_G_Christopoulos_A_Poyner_DR_Sexton_PM_Pharmacological_discrimination_of_calcitonin_receptor_receptor_activity-modifying_protein_complexes_Mol_Pharmacol_67_1655-1665 [index, 2026-10-15] |

### 31. https://www.science.org/doi/10.1126/scisignal.adt8127

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Science Signaling amylin claims — not verified.
- **Report claims attributed to this source:**
  - EN line 53 (Part 1): - **Subunit dynamics (2025)**: AMY1R / AMY2R are biased toward free CTR + RAMP at baseline; rat amylin and αCGRP promote AMY1R / AMY2R subunit association; human / salmon calcitonin promote AMY1R / AMY3R dissociation; AMY3R is a more stable heterodimer; these changes alter cAMP signaling. Source: https://www.science.org/doi/10.1126/scisignal.adt8127 [index, 2026-10-15]

### 32. https://www.sciencedirect.com/science/article/abs/pii/0196978196000046

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Ca2+ signaling claims — not verified.
- **Report claims attributed to this source:**
  - EN line 51 (Part 1): - **Gq / Ca²⁺ evidence (cell-type-specific)**: In rat AR42J pancreatic acinar cells, amylin ↑ [Ca²⁺]i via IP3-sensitive calcium stores and ↑ IP3; CGRP / salmon calcitonin at 10 µM did not mobilize Ca²⁺ — indicating receptor behavior is cell-context-dependent and cannot be generalized as a universal conclusion for AMY1–3. Source: https://www.sciencedirect.com/science/article/abs/pii/0196978196000046 [index, 2026-10-15]

### 33. https://www.sigmaaldrich.com/MX/es/tech-docs/paper/115983

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Sigma-Aldrich amylin claims — not verified.
- **Report claims attributed to this source:**
  - EN line 81 (Part 1): | Bone (human osteoblasts) | 16 human osteoblast samples: high CLR + RAMP1, low RAMP2, no RAMP3 or CTR expression. Suggests human osteoblast calcitonin-family signaling is mainly via CLR / RAMP1, not CTR / AMY — an important caveat for bone AMY claims | https://www.sigmaaldrich.com/MX/es/tech-docs/paper/115983 [index, 2026-10-15] |
  - EN line 114 (Part 2): | Bone (calcitonin-like) | Calcitonin → osteoclast CALCR → ↓ bone resorption, rapid ↓ serum Ca²⁺ (established physiology). Amylin bone effects: amylin KO mice have low bone mass (↑ bone resorption, bone formation unaffected); in vitro amylin inhibits osteoclast precursor fusion via ERK1/2. But Calcr⁺/⁻ + Amylin⁺/⁻ compound mice show both phenotypes, ruling out CALCR as the in vivo mediator of amylin inhibition of osteoclastogenesis → amylin bone effects act via an **unidentified receptor**, not AMY1–3 / CALCR. Human osteoblasts lack CTR expression, further weakening the human AMY bone claim | 

### 34. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(21)01751-7/abstract

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Cagrilintide Lancet Phase 2 numbers (-10.8% at 4.5 mg etc.) — not verified.
- **Report claims attributed to this source:**
  - EN line 173 (Part 3): | Cagrilintide | Novo Nordisk | Phase 3 (as a CagriSema component); standalone Phase 3 / filing status not publicly disclosed | SC, once weekly | ~7–8 days (**secondary source, not verified against original PK**) | Phase 2 (NCT03856047, 26 weeks): 4.5 mg −10.8% vs placebo −3.0% | GI adverse events 41–63% vs placebo 32%; nausea 20–47% | https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(21)01751-7/abstract [index, 2026-10-15] |
  - EN line 205 (Part 3): - **Efficacy**: Phase 2 (NCT03856047, 26 weeks): 4.5 mg −10.8% vs placebo −3.0%; all doses (0.3–4.5 mg) achieved ≥5% weight loss at 26 weeks. Source: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(21)01751-7/abstract [index, 2026-10-15]

### 35. https://www.valuespectrum.com/corporate_news/1288431-novo-nordisk-s-subcutaneous-and-oral-amycretin-data-published-in-the-lancet-and-presented-at-ada-2025

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amycretin Lancet/ADA 2025 data — not verified.
- **Report claims attributed to this source:**
  - EN line 184 (Part 3): | Amycretin / Zenagamtide (NNC0487-0111 / NN9487) | Novo Nordisk (INN now Zenagamtide; Amycretin is the former development name, same molecule) | Phase 1b/2a + Phase 2 (T2D) complete; Phase 3 AMAZE program ongoing | SC once weekly **and** oral once daily (two formulations) | Not publicly disclosed | SC Phase 1b/2a (36 weeks): 60 mg weekly −24.3% vs placebo −1.1%; oral Phase 1 (12 weeks): 2× 50 mg −13.1% vs placebo −1.2%; Phase 2 T2D (36 weeks): SC −14.5% vs placebo −2.6%, oral −10.1% vs −2.5% | GI adverse events most common, mostly mild–moderate, dose-related; Novo states "no new safety signal
  - EN line 263 (Part 3): - SC Phase 1b/2a (36 weeks): 60 mg weekly −24.3% vs placebo −1.1%. Oral Phase 1 (12 weeks): 2× 50 mg −13.1% vs placebo −1.2%. Phase 2 T2D (36 weeks): SC −14.5% vs placebo −2.6%, oral −10.1% vs −2.5%. Phase 3 AMAZE program ongoing. GI adverse events most common, mostly mild–moderate, dose-related; Novo states "no new safety signals". Sources: https://www.pharmacytimes.com/view/amycretin-shows-significant-weight-loss-hba1c-reductions-in-type-2-diabetes ; https://www.valuespectrum.com/corporate_news/1288431-novo-nordisk-s-subcutaneous-and-oral-amycretin-data-published-in-the-lancet-and-presented-

### 36. https://arxiv.org/pdf/2503.17887

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** fetch timed out; not retried
- **Findings / corrections:** Modeling paper pramlintide Vp ~104.5 mL/kg (model estimate, not label value) — not verified. Claim appears in Chinese only.
- **Report claims attributed to this source:**
  - ZH line 323 (Part 4): - **Pramlintide**：血浆蛋白结合约 60%；不广泛结合白蛋白；不广泛结合血细胞；人乳汁分布未知；分布容积（Vd）**未见于 FDA 说明书**；一篇建模论文给出 Vp 约 104.5 mL/kg——视为模型估计，非说明书数值。来源：https://www.drugs.com/monograph/pramlintide.html ；https://arxiv.org/pdf/2503.17887 [index, 2026-10-15]

### 37. https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Insulin:amylin ratios; islet amyloid in >90% or 70-90% of T2D; toxicity cycle (ER stress/UPR, BAX/Bcl-xL, ROS, IL-1beta); pramlintide Pro substitutions 25/28/29 vs 25/26/29; IDE degrades amylin — all not verified against this source.
- **Report claims attributed to this source:**
  - EN line 30 (Part 1): | Insulin : Amylin molar ratio | **Conflicting; no single verified value**: ~100:1 (insulin : amylin); ~20:1; rat fasting 100:2.3, fed 100:2.6; one review states amylin is ~12% of insulin. Results differ by assay / species; any citation must state the assay and species | https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://www.researchgate.net/publication/251247194_Understanding_Amylin_Receptors ; https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2013.00042/full [index, 2026-10-15] |
  - EN line 35 (Part 1): | Aggregation and T2D | Autopsy finds islet amyloid deposition in >90% (one review) or 70–90% (another review) of T2D patients; oligomers are considered more toxic than fibers / deposits; mechanisms include membrane permeabilization, ER stress, mitochondrial damage, beta-cell death; insulin prevents aggregation inside secretory granules | https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext ; https://www.mdpi.com/2073-4409/7/8/95 [index, 2026-10-15] |
  - EN line 36 (Part 1): | Toxicity cycle | Misfolded amylin → ER stress / UPR, proteostasis imbalance, mitochondrial dysfunction, BAX ↑ / Bcl-xL ↓, ROS, IL-1β → beta-cell apoptosis; progressive loss worsens aggregation | https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ [index, 2026-10-15] |
  - EN line 194 (Part 3): - **Substitution sites**: **Conflicting** — one source states pramlintide substitutes human amylin residues 25, 28, 29 with Pro; another states residues 25, 26, 29 with Pro (and rat amylin differs from human at 6 residues, 3 of which are Pro at 25, 28, 29); the difference is unverified. Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://pubmed.ncbi.nlm.nih.gov/17393306/ [index, 2026-10-15]
  - EN line 341 (Part 4): - **Proteolysis**: Peptide degradation by proteases. **IDE (insulin-degrading enzyme) degrades amylin** — also insulin, glucagon, ANP, IGF-1/2, Aβ; cleaves peptides up to ~70 aa. Specific proteases for synthetic agonists (cagrilintide / eloralintide / petrelintide) are **undisclosed**. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ [index, 2026-10-15]

### 38. https://pmc.ncbi.nlm.nih.gov/articles/PMC4016184/

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Central amylin -> sympathetic -> BAT thermogenesis; chronic peripheral amylin reduces fat beyond pair-fed; RAMP1 overexpression increases BAT sympathetic activity; human studies 'not yet performed' — not verified.
- **Report claims attributed to this source:**
  - EN line 112 (Part 2): | Energy expenditure | Proposed: central amylin (AP / third ventricle) → sympathetic nerves → brown adipose tissue (BAT) thermogenesis; mechanism / site undetermined | Acute + chronic amylin ↑ energy expenditure in rodents; chronic peripheral amylin ↓ fat mass beyond pair-fed rats, with ↑ fat oxidation / energy expenditure; central amylin ↑ BAT sympathetic activity + core temperature (rats); RAMP1 overexpression ↑ BAT sympathetic activity + core temperature. Reviews state human studies "have not yet been performed" | If translatable, would prevent the expected energy-expenditure drop during we

### 39. https://pubmed.ncbi.nlm.nih.gov/14715154/

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** AP is a CVO lacking BBB features; fenestrated/leaky capillaries; AP expresses CTR(a) + RAMP2/3 mRNA; peripheral amylin + sCT induce AP c-fos — not verified.
- **Report claims attributed to this source:**
  - ZH line 331 (Part 4): - **Area Postrema（AP）= 环脑室器官（CVO），不受 BBB 保护**：AP 为缺乏 BBB 特征的 CVO；毛细血管有窗 / 渗漏 → 血浆溶质直接到达 AP 神经元，无需穿过 BBB 本身。外周 Amylin + 鲑鱼降钙素诱导 AP c-fos；AP 表达 CTR(a) + RAMP2/3 mRNA。Amylin 也被提议经穹窿下器（SFO，另一 CVO）作用。来源：https://pubmed.ncbi.nlm.nih.gov/14715154/ ；http://www.scientific-exchange.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/amylin-module4-infographic.pdf [index, 2026-10-15]

### 40. https://tmedweb.tulane.edu/pharmwiki/doku.php/pramlintide?do=export_pdf

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pramlintide SC only, synthetic analog, pre-meal; endogenous amylin unsuitable due to insolubility/aggregation; Pro substitutions give stable soluble analog; glucagon suppression via direct islet/paracrine vs AP-mediated neuronal route 'poorly understood' — not verified. Secondary source (teaching pharmwiki) even when read.
- **Report claims attributed to this source:**
  - ZH line 308 (Part 4): - **Pramlintide（Symlin）**：仅 SC；合成 Amylin 类似物；主要餐前即刻注射。内源性 Amylin 因不溶 / 溶液中聚集而不适合药用；Pramlintide 经脯氨酸取代 → 稳定、可溶类似物。来源：https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=4aea30ff-eb0d-45c1-b114-3127966328ff&type=pdf ；https://tmedweb.tulane.edu/pharmwiki/doku.php/pramlintide?do=export_pdf [index, 2026-10-15]
  - ZH line 345 (Part 4): - **胰腺——α 细胞 → 胰高血糖素抑制**：抑制餐后 α 细胞胰高血糖素分泌 → ↓ 肝糖原分解 / 糖异生 → ↓ 内源性葡萄糖输出 → ↓ 餐后血糖。机制未解决：(a) 假设直接经胰岛门脉循环（β 细胞 → α 细胞局部高浓度），(b) AP 刺激后的中枢神经元介导减少。来源将通路描述为“了解不充分” / 神经元介导。来源：https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S1054358905520088 ；https://tmedweb.tulane.edu/pharmwiki/doku.php/pramlintide?do=export_pdf ；https://www.novonordiskmedical.com/content/dam/medical/novonordiskmedical/scientific-evidence/amylin/resource-documents/the-physiological-functions-of-amylin.pdf [index, 2026-10-15]

### 41. https://www.Proteinatlas.Org/ENSG00000004948-CALCR/brain

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** CALCR detectable across human brain regions, low regional specificity (Tau 0.62); neuronal nuclei/dendrites; CVOs of choroid plexus, ventricular wall, ependymal cells — not verified from this exact URL (the lowercase proteinatlas.org CALCR summary page did load and corroborates part of the overlapping HPA content).
- **Report claims attributed to this source:**
  - EN line 75 (Part 1): | Brain (human) | CALCR detectable across multiple human brain regions with low regional specificity (Tau 0.62); cellular localization: neuronal nuclei / dendrites; circumventricular organs of the choroid plexus, ventricular wall, ependymal cells | HPA brain: https://www.Proteinatlas.Org/ENSG00000004948-CALCR/brain [index, 2026-10-15] |
  - EN line 99 (Part 2): | Hypothalamus ARC / VMH / PVN | ARC POMC / CART (anorexigenic, α-MSH → MC4R in PVN / LHA) vs ARC AgRP / NPY (orexigenic, MC4R antagonists); PVN integrates ARC + hindbrain signals; VMH / DMH / LHA are secondary | Mouse Calcr enriched in ARC, median eminence, DMH, PVN, etc. (rodent); the cagrilintide study explicitly states ARC neuronal activation was not assessed, so AgRP / POMC-mediated anorexia / weight loss cannot be inferred from it; that study cites prior work stating POMC-neuron CTR signaling is required for energy-balance maintenance (via energy expenditure) | If activated, would regula

### 42. https://www.cell.com/trends/neurosciences/abstract/S0166-2236(18)30068-7

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** AP/NTS -> LPBN CGRP neurons -> CeA + BNST; systemic amylin/CCK activate CGRP-PBN; PBN CGRP controls meal termination; cagrilintide/sCT activate LPBN cFos; PBN CGRP as general alarm/aversion relay — not verified.
- **Report claims attributed to this source:**
  - EN line 98 (Part 2): | Parabrachial Nucleus (PBN), especially lateral PBN (LPBN) | AP / NTS → LPBN CGRP (Calca) neurons → central amygdala (CeA) + bed nucleus of the stria terminalis (BNST) | Systemic amylin / CCK activate CGRP-PBN neurons; PBN CGRP neurons control meal termination (activation ↓ meal size; inactivation disrupts meal-size control); cagrilintide / sCT activate LPBN cFos in WT mice | Meal termination / satiety; strong weight-loss relevance | PBN CGRP neurons are a general alarm / aversion relay (food poisoning, pain, itch, hypercapnia) → CeA / BNST; chronic activation → severe anorexia / starvation i

### 43. https://www.drugs.com/monograph/pramlintide.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** HIGHEST-IMPACT GAP: pramlintide 15 min pre-meal slows gastric emptying, suppresses glucagon, increases satiety, no change in net nutrient absorption; PK: SC bioavailability 30-40%, Tmax 19-21 min, Vd 0.35-0.83 L/kg, t1/2 ~48 min, urine main excretion; plasma protein binding ~60%, not extensively albumin/RBC-bound; Vd not in FDA label; Vp ~104.5 mL/kg modeling estimate; renal metabolism -> des-Lys1 pramlintide; t1/2 ~48-55 min by dose; renal clearance main route for amylin/pramlintide — NONE verified. The report's pramlintide PK numbers all cite this page.
- **Report claims attributed to this source:**
  - EN line 109 (Part 2): | Delayed gastric emptying | AP amylin receptors → vagal efferent fibers → gut → slowed gastric emptying | Human: pramlintide injected 15 min before meals slows gastric emptying, suppresses glucagon, ↑ satiety, blunts postprandial hyperglycemia; slows gastric emptying without changing net carbohydrate / nutrient absorption | ↓ postprandial glucose appearance, ↑ fullness / satiety; contributes to weight loss via reduced intake | Slowed gastric emptying may contribute to nausea / fullness / vomiting, but causal separation from central nausea is **unverified**; pramlintide nausea is dose-dependen
  - EN line 110 (Part 2): | Glucagon suppression | Amylin → islet alpha cells (direct and/or islet paracrine; exact alpha-cell AMY subtype **unverified**) → ↓ postprandial glucagon → ↓ hepatic glycogenolysis / glucose production | Human: pramlintide suppresses inappropriately elevated glucagon during hyperglycemia without impairing the normal glucagon response to hypoglycemia; endogenous anti-amylin antiserum ↑ arginine-stimulated glucagon (and insulin / somatostatin) (ex vivo rat islets) | ↓ postprandial glucose swings; weight-loss relevance indirect (glycemic control, not a primary anorexia mechanism) | No establishe
  - EN line 196 (Part 3): - **PK**: SC bioavailability 30–40% (T1D) / ~35–40% (T2D); Tmax 19–21 min; apparent volume of distribution 0.35–0.83 L/kg; renal proteolysis; t1/2 ~48 min (T1D) / 46 min (T2D); urine is the main excretion route. Source: https://www.drugs.com/monograph/pramlintide.html [index, 2026-10-15]
  - EN line 336 (Part 4): - **Subcutaneous injection (mainstream)**: Bypasses GI lumen degradation and portal first-pass; delivers the full dose to systemic circulation; SC bioavailability examples: pramlintide 30–40%, petrelintide ~85% (secondary source). Sources: https://www.drugs.com/monograph/pramlintide.html ; https://www.pharmacytimes.com/view/petrelintide-yields-up-to-10-7-weight-loss-with-mild-gi-effects [index, 2026-10-15]
  - EN line 343 (Part 4): - **Renal clearance**: Main clearance route for amylin and pramlintide; kidney is the main determinant of plasma amylin levels; urine is the main excretion route for pramlintide. For cagrilintide / eloralintide / petrelintide, renal-clearance proportions are **inferred** (fragments + renal clearance), not publicly disclosed. Sources: https://www.drugs.com/monograph/pramlintide.html ; https://www.medscape.com/viewarticle/523581_5 [index, 2026-10-15]

### 44. https://www.medscape.com/viewarticle/523581_5

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Healthy fasting amylin ~4-8 pmol/L, postprandial 15-25 pmol/L; kidney main determinant of clearance; deficient in T1D, elevated in IGT/insulin-resistant obesity/T2D; alternate assay 2.03->3.78 pM, insulin 48.3->265 pM, r=0.74; renal clearance main route — not verified. Secondary source (Medscape review) even when read.
- **Report claims attributed to this source:**
  - EN line 32 (Part 1): | Plasma levels (assay-dependent) | Healthy fasting ~4–8 pmol/L, rising postprandially to 15–25 pmol/L; kidney is the main determinant of clearance; amylin is deficient in T1D and often elevated in IGT / insulin-resistant obesity / T2D. Another assay: lean non-diabetic subjects after glucose ingestion 2.03 ± 0.22 → 3.78 ± 0.39 pM, insulin 48.3 → 265 pM, correlation r = 0.74 | https://www.medscape.com/viewarticle/523581_5 ; https://www.academia.edu/34229415/Effects_of_meal_ingestion_on_plasma_amylin_concentration_in_NIDDM_and_nondiabetic_humans [index, 2026-10-15] |
  - EN line 343 (Part 4): - **Renal clearance**: Main clearance route for amylin and pramlintide; kidney is the main determinant of plasma amylin levels; urine is the main excretion route for pramlintide. For cagrilintide / eloralintide / petrelintide, renal-clearance proportions are **inferred** (fragments + renal clearance), not publicly disclosed. Sources: https://www.drugs.com/monograph/pramlintide.html ; https://www.medscape.com/viewarticle/523581_5 [index, 2026-10-15]

### 45. https://www.academia.edu/34229415/Effects_of_meal_ingestion_on_plasma_amylin_concentration_in_NIDDM_and_nondiabetic_humans

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Postprandial amylin: NIDDM 2.03->3.78 pM, insulin 48.3->265 pM, r=0.74 — not verified.
- **Report claims attributed to this source:**
  - EN line 32 (Part 1): | Plasma levels (assay-dependent) | Healthy fasting ~4–8 pmol/L, rising postprandially to 15–25 pmol/L; kidney is the main determinant of clearance; amylin is deficient in T1D and often elevated in IGT / insulin-resistant obesity / T2D. Another assay: lean non-diabetic subjects after glucose ingestion 2.03 ± 0.22 → 3.78 ± 0.39 pM, insulin 48.3 → 265 pM, correlation r = 0.74 | https://www.medscape.com/viewarticle/523581_5 ; https://www.academia.edu/34229415/Effects_of_meal_ingestion_on_plasma_amylin_concentration_in_NIDDM_and_nondiabetic_humans [index, 2026-10-15] |

### 46. https://www.docwirenews.com/post/cagrilintide-and-semaglutide-combo-highly-effective-for-weight-loss

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** CagriSema REDEFINE-1 efficacy block — not verified.
- **Report claims attributed to this source:**
  - EN line 182 (Part 3): | CagriSema (cagrilintide 2.4 mg + semaglutide 2.4 mg) | Novo Nordisk | NDA submitted to FDA for weight management on 2025-12-18; decision expected 2026 Q4; not approved as of Oct 2026 | SC, once weekly, fixed-dose combination | Component half-lives apply (semaglutide ~7 days; cagrilintide ~7–8 days, secondary source) | REDEFINE 1: 22.7% (trial-product estimand) / 20.4% (treatment-policy) vs placebo 2.3% / 3.0%; REDEFINE 2 (T2D): 13.7% vs placebo 3.4%; REDEFINE 4 (vs tirzepatide 15 mg): 23.0% vs 25.5%, **did not meet non-inferiority** | Mainly GI adverse events, mostly mild–moderate, transient
  - EN line 253 (Part 3): - REDEFINE 1 (68 weeks, obesity without diabetes): 22.7% (trial-product estimand) / 20.4% (treatment-policy) vs placebo 2.3% / 3.0%. REDEFINE 2 (T2D): 13.7% vs placebo 3.4%. REDEFINE 4 (vs tirzepatide 15 mg): 23.0% vs 25.5%, did not meet non-inferiority. REDEFINE 8 / 11 and high-dose CagriSema results were **not found** (see "Could not verify"). REIMAGINE 1 (MRI substudy): CagriSema reduced hepatic fat and glycemia; REIMAGINE 4 (vs tirzepatide in T2D): numbers **not confirmed** (see "Could not verify"). Sources: https://www.docwirenews.com/post/cagrilintide-and-semaglutide-combo-highly-effecti
  - EN line 254 (Part 3): - Safety: Mainly GI adverse events, mostly mild–moderate, transient, waning over time; REDEFINE 1 GI AEs ~80% vs placebo ~40% (secondary report). Source: https://www.docwirenews.com/post/cagrilintide-and-semaglutide-combo-highly-effective-for-weight-loss [index, 2026-10-15]

### 47. https://www.drugs.com/pro/symlin.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pramlintide label details (titration, AEs, interactions) — not verified.
- **Report claims attributed to this source:**
  - EN line 172 (Part 3): | Pramlintide (Symlin) | Amylin Pharmaceuticals (originator) | Approved (2005-03-16, diabetes adjunct; **not a weight-loss indication**) | SC, immediately before meals, 2–3×/day | ~48 min | Meta-analysis: HbA1c −0.33%, weight −2.57 kg (insulin-treated T2D) | Boxed warning: severe hypoglycemia with insulin; nausea most common | https://www.drugs.com/pro/symlin.html ; https://nsuworks.nova.edu/hpd_corx_facarticles/29/ [index, 2026-10-15] |

### 48. https://www.globenewswire.com/news-release/2026/08/06/3340221/0/en/MBX-Biosciences-Reports-Second-Quarter-2026-Financial-Results-and-Corporate-Highlights.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** MBX 5765 prodrug details — not verified. FLAG: Chinese text calls MBX 5765 an 'amycretin prodrug' — SUSPECT (amycretin is Novo's molecule). Verify against this press release on re-check; do not state 'amycretin prodrug' as fact.
- **Report claims attributed to this source:**
  - EN line 186 (Part 3): | MBX 5765 | MBX Biosciences | Preclinical; IND-enabling studies ongoing (nominated May 2026) | Planned injection (prodrug); route not clearly stated in retrieved sources | No human data | No human data; no animal numbers in retrieved sources | No human safety data | https://www.globenewswire.com/news-release/2026/08/06/3340221/0/en/MBX-Biosciences-Reports-Second-Quarter-2026-Financial-Results-and-Corporate-Highlights.html [index, 2026-10-15] |
  - EN line 271 (Part 3): - MBX Biosciences single-peptide prodrug combining GLP-1 + GIP + glucagon + DACRA (dual amylin + calcitonin) activity; designed for monthly dosing; IND-enabling studies ongoing (nominated May 2026); no human data. Source: https://www.globenewswire.com/news-release/2026/08/06/3340221/0/en/MBX-Biosciences-Reports-Second-Quarter-2026-Financial-Results-and-Corporate-Highlights.html [index, 2026-10-15]

### 49. https://www.globenewswire.com/news-release/2026/10/07/3376750/0/en/zealand-pharma-announces-positive-phase-2-zupreme-2-topline-results-for-amylin-analog-petrelintide-in-people-with-overweight-or-obesity-and-type-2-diabetes.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Petrelintide ZUPREME-2 (28 wks, T2D): 7.4-9.2% vs placebo 2.0% — not verified.
- **Report claims attributed to this source:**
  - EN line 175 (Part 3): | Petrelintide (ZP8396) | Zealand Pharma (originator); with Roche (2025, up to $5.3B deal) | Phase 2 complete; Phase 3 ZUPREME-3/4/5 started Sep 2026 (~7,000 participants) | SC, once weekly | ~240 h (~10 days); Tmax ~24 h; SC bioavailability ~85% | ZUPREME-1 (42 weeks): 8.7–10.7% vs placebo ~1.7%; ZUPREME-2 (28 weeks, T2D): 7.4–9.2% vs placebo 2.0% | Nausea 20% vs placebo 6%; GI discontinuation ~1%; anti-drug antibodies 38% (no apparent effect on weight loss) | https://www.globenewswire.com/news-release/2026/10/07/3376750/0/en/zealand-pharma-announces-positive-phase-2-zupreme-2-topline-results
  - EN line 216 (Part 3): - **Trials**: ZUPREME-1 Phase 2 (42 weeks, obesity without diabetes): 8.7–10.7% vs placebo ~1.7%; ZUPREME-2 (28 weeks, T2D): 7.4–9.2% vs placebo 2.0%. ZUPREME Phase 3 started Sep 2026 (ZUPREME-3 / 4 / 5, ~7,000 participants). NCT numbers for ZUPREME-1 and the Phase 2 monotherapy program were **not confirmed** in the retrieved sources (see "Could not verify"). Sources: https://www.globenewswire.com/news-release/2026/10/07/3376750/0/en/zealand-pharma-announces-positive-phase-2-zupreme-2-topline-results-for-amylin-analog-petrelintide-in-people-with-overweight-or-obesity-and-type-2-diabetes.html ;
  - EN line 217 (Part 3): - **Safety**: Nausea 20% vs placebo 6%; GI discontinuation ~1%; anti-drug antibodies 38% (no apparent effect on weight loss). Source: https://www.globenewswire.com/news-release/2026/10/07/3376750/0/en/zealand-pharma-announces-positive-phase-2-zupreme-2-topline-results-for-amylin-analog-petrelintide-in-people-with-overweight-or-obesity-and-type-2-diabetes.html [index, 2026-10-15]

### 50. https://www.mdpi.com/1422-0067/24/4/3960/html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** CALCRL expression / CGRP receptor biology — not verified.
- **Report claims attributed to this source:**
  - EN line 82 (Part 1): | Vasculature | CALCRL protein in capillary endothelium, small-artery / artery smooth muscle, glomerular capillaries (human / rat / mouse IHC); this is CLR, not CTR / AMY — do not confuse with AMY vascular expression | https://www.mdpi.com/1422-0067/24/4/3960/html [index, 2026-10-15] |

### 51. https://www.mdpi.com/2073-4409/7/8/95

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Islet amyloid in >90% or 70-90% of T2D; oligomer toxicity; insulin prevents aggregation — not verified.
- **Report claims attributed to this source:**
  - EN line 35 (Part 1): | Aggregation and T2D | Autopsy finds islet amyloid deposition in >90% (one review) or 70–90% (another review) of T2D patients; oligomers are considered more toxic than fibers / deposits; mechanisms include membrane permeabilization, ER stress, mitochondrial damage, beta-cell death; insulin prevents aggregation inside secretory granules | https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://www.kidney-international.org/article/S0085-2538(15)52620-3/fulltext ; https://www.mdpi.com/2073-4409/7/8/95 [index, 2026-10-15] |
  - EN line 37 (Part 1): | Prion-like seeding | **Emerging**: intraperitoneal injection of amylin aggregates can seed endogenous human amylin in transgenic mice and raise blood glucose; transmission of T2D via aggregates is only a hypothesis, not established in humans | https://www.mdpi.com/2073-4409/7/8/95 [index, 2026-10-15] |

### 52. https://www.medicinenet.com/side_effects_of_symlin_pramlintide/side-effects.htm

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pramlintide AE profile — not verified.
- **Report claims attributed to this source:**
  - ZH line 366 (Part 4): - **恶心 / 呕吐机制**：AP = 化学感受器触发区 / 呕吐回路；AP + NTS 激活 → 恶心 / 呕吐；剂量依赖，起始 / 递增期最重，随时间 / 耐受减轻。Pramlintide 说明书：恶心起始较高，随时间下降；逐渐滴定使发生率 / 严重程度最小化。T2D 汇总试验：恶心 28%（Symlin 120 mcg BID + 胰岛素）vs 安慰剂 12%；呕吐 8% vs 4%；头痛 13% vs 7%；厌食 9% vs 2%。来源：https://www.medicinenet.com/side_effects_of_symlin_pramlintide/side-effects.htm ；https://www.drugs.com/pro/symlin.html [index, 2026-10-15]。Cagrilintide Phase 1b：胃肠疾病占不良事件 37%（207/566），多为轻中度。来源：https://www.researchgate.net/publication/351114083_Safety_tolerability_pharmacokinetics_and_pharmacodynamics_of_concomitant_administration_of_multiple_doses_of_cagrilintide_with_sem

### 53. https://www.medscape.com/viewarticle/523581_6

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pramlintide PK / label details — not verified.
- **Report claims attributed to this source:**
  - EN line 109 (Part 2): | Delayed gastric emptying | AP amylin receptors → vagal efferent fibers → gut → slowed gastric emptying | Human: pramlintide injected 15 min before meals slows gastric emptying, suppresses glucagon, ↑ satiety, blunts postprandial hyperglycemia; slows gastric emptying without changing net carbohydrate / nutrient absorption | ↓ postprandial glucose appearance, ↑ fullness / satiety; contributes to weight loss via reduced intake | Slowed gastric emptying may contribute to nausea / fullness / vomiting, but causal separation from central nausea is **unverified**; pramlintide nausea is dose-dependen
  - EN line 111 (Part 2): | Satiety / feeding | Peripheral amylin → central satiety (see AP / NTS / PBN / VTA) | Amylin KO mice: transient hyperphagia, ↑ adiposity; amylin antagonist AC187 ↑ feeding / meal size (peripheral or central); low near-physiological exogenous amylin (~2× postprandial levels) suppresses feeding in rats; pramlintide ↓ appetite in diabetes and non-diabetic obesity | ↓ meal size, ↓ energy intake — core weight-loss mechanism | Third-ventricle central amylin (100 pmol) ↓ rat feeding without conditioned taste aversion — supports non-aversive satiety at that dose / route in rodents | Established (huma
  - EN line 157 (Part 2): - **Human (pramlintide)**: Common nausea, vomiting, anorexia, fatigue, headache, dizziness, hypoglycemia (with insulin); nausea is dose-dependent, mostly mild–moderate, early, and fades over time; slow titration + 50% mealtime insulin reduction ↓ risk. Sources: https://www.ncbi.nlm.nih.gov/books/NBK548949/pdf/Bookshelf_NBK548949.pdf ; https://www.medscape.com/viewarticle/523581_6 [index, 2026-10-15]
  - EN line 197 (Part 3): - **Dose**: T1D 30 → 60 µg; T2D 60 → 120 µg, before meals (2–3 meals/day). Source: https://www.medscape.com/viewarticle/523581_6 [index, 2026-10-15]
  - EN line 345 (Part 4): - **Dose titration**: Slow dose escalation reduces GI adverse events (e.g., pramlintide: start low, increase only after ≥3 days without nausea; ACCG-2671 SAD was not titrated and showed dose-related nausea / vomiting; MAD testing titration). Sources: https://www.medscape.com/viewarticle/523581_6 ; https://www.globenewswire.com/news-release/2026/09/08/3357602/0/en/structure-therapeutics-reports-positive-clinical-data-across-oral-small-molecule-amylin-and-glp-1-programs-for-chronic-weight-management.html [index, 2026-10-15]

### 54. https://www.nature.com/articles/ijosup20164

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** AP->NTS->LPBN circuit support — not verified.
- **Report claims attributed to this source:**
  - EN line 95 (Part 2): | Area Postrema (AP) | AP → NTS (dorsal vagal complex, DVC) → lateral parabrachial nucleus (LPBN) → hypothalamus / forebrain; AP is a circumventricular organ without a BBB | AP / NTS lesions abolish the anorectic effect of chronic peripheral amylin in rats; intra-AP injection of amylin antagonist AC187 increases food intake in rats; AP is required for amylin effects | Satiety / reduced meal size; primary hindbrain satiety node | AP CALCR+ neurons in mouse genetics suppress feeding without inducing avoidance (vs AP GLP1R+ neurons driving aversion) — suggesting satiety and nausea are separable, 
  - EN line 339 (Part 4): - **AP access (NOT BBB crossing)**: The Area Postrema is a circumventricular organ with fenestrated capillaries and no BBB features; plasma drugs diffuse through leaky AP capillaries to AP neurons **without crossing the BBB itself**. AP access is the start of the central relay (AP → NTS → LPBN). Sources: https://www.nature.com/articles/ijosup20164 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11114503/ [index, 2026-10-15]

### 55. https://www.novonordisk.com/content/dam/nncorp/global/en/science-and-technology/pdfs/medical-affairs/amylin-physiology-interactive-module.pdf

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amylin physiology module claims — not verified.
- **Report claims attributed to this source:**
  - EN line 29 (Part 1): | Production and co-secretion | Produced by pancreatic beta cells, stored in the same secretory granules as insulin, co-secreted in response to meals / glucose stimulation | https://www.novonordisk.com/content/dam/nncorp/global/en/science-and-technology/pdfs/medical-affairs/amylin-physiology-interactive-module.pdf [index, 2026-10-15] |
  - EN line 109 (Part 2): | Delayed gastric emptying | AP amylin receptors → vagal efferent fibers → gut → slowed gastric emptying | Human: pramlintide injected 15 min before meals slows gastric emptying, suppresses glucagon, ↑ satiety, blunts postprandial hyperglycemia; slows gastric emptying without changing net carbohydrate / nutrient absorption | ↓ postprandial glucose appearance, ↑ fullness / satiety; contributes to weight loss via reduced intake | Slowed gastric emptying may contribute to nausea / fullness / vomiting, but causal separation from central nausea is **unverified**; pramlintide nausea is dose-dependen

### 56. https://www.pharmacytimes.com/view/amycretin-shows-significant-weight-loss-hba1c-reductions-in-type-2-diabetes

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amycretin Phase 2 T2D numbers (-14.5% vs -2.6%; HbA1c -1.8 vs -0.2 pp) — not verified.
- **Report claims attributed to this source:**
  - EN line 184 (Part 3): | Amycretin / Zenagamtide (NNC0487-0111 / NN9487) | Novo Nordisk (INN now Zenagamtide; Amycretin is the former development name, same molecule) | Phase 1b/2a + Phase 2 (T2D) complete; Phase 3 AMAZE program ongoing | SC once weekly **and** oral once daily (two formulations) | Not publicly disclosed | SC Phase 1b/2a (36 weeks): 60 mg weekly −24.3% vs placebo −1.1%; oral Phase 1 (12 weeks): 2× 50 mg −13.1% vs placebo −1.2%; Phase 2 T2D (36 weeks): SC −14.5% vs placebo −2.6%, oral −10.1% vs −2.5% | GI adverse events most common, mostly mild–moderate, dose-related; Novo states "no new safety signal
  - EN line 263 (Part 3): - SC Phase 1b/2a (36 weeks): 60 mg weekly −24.3% vs placebo −1.1%. Oral Phase 1 (12 weeks): 2× 50 mg −13.1% vs placebo −1.2%. Phase 2 T2D (36 weeks): SC −14.5% vs placebo −2.6%, oral −10.1% vs −2.5%. Phase 3 AMAZE program ongoing. GI adverse events most common, mostly mild–moderate, dose-related; Novo states "no new safety signals". Sources: https://www.pharmacytimes.com/view/amycretin-shows-significant-weight-loss-hba1c-reductions-in-type-2-diabetes ; https://www.valuespectrum.com/corporate_news/1288431-novo-nordisk-s-subcutaneous-and-oral-amycretin-data-published-in-the-lancet-and-presented-
  - EN line 281 (Part 3): Sources: https://www.pharmacytimes.com/view/amycretin-shows-significant-weight-loss-hba1c-reductions-in-type-2-diabetes ; https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-efficacy-in-preclinical-models-525584.shtml [index, 2026-10-15]
  - EN line 337 (Part 4): - **Oral delivery (exceptional for peptides)**: Oral peptides face gastric acid + pepsin / trypsin / chymotrypsin / peptidases + poor membrane permeability. SNAC (used for oral semaglutide / amycretin) buffers local pH, interferes with pepsinogen activation, and fluidizes the gastric lipid membrane; oral semaglutide bioavailability ~0.4–1%. ASC36 NHP oral bioavailability 6–8%. Sources: https://en.prnasia.com/releases/apac/oral-small-molecule-amylin-receptor-agonist-asc39-demonstrated-eloralintide-like-amylin-selectivity-and-efficacy-in-preclinical-models-525584.shtml ; https://www.pharmacytime

### 57. https://www.prnewswire.co.uk/news-releases/brightgene-presents-positive-phase-2-data-for-dual-glp-1rgipr-agonist-for-weight-management-and-type-2-diabetes-and-preclinical-data-for-novel-amylin-analog-at-american-diabetes-associations-85th-scientific-sessions-302488874.html

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** BGM1812 amylin analog claims — not verified.
- **Report claims attributed to this source:**
  - EN line 181 (Part 3): | BGM1812 | BrightGene | Preclinical (amylin analog) | Not publicly disclosed | Not publicly disclosed | Preclinical only: amylin receptor agonist activity 1.8× petrelintide, calcitonin receptor 2.2× (EC50); DIO rats dose-dependent weight loss | No human safety data | https://www.prnewswire.co.uk/news-releases/brightgene-presents-positive-phase-2-data-for-dual-glp-1rgipr-agonist-for-weight-management-and-type-2-diabetes-and-preclinical-data-for-novel-amylin-analog-at-american-diabetes-associations-85th-scientific-sessions-302488874.html [index, 2026-10-15] |
  - EN line 246 (Part 3): - BrightGene preclinical amylin analog; amylin receptor activity 1.8× petrelintide (EC50), calcitonin receptor 2.2×; DIO rats dose-dependent weight loss. Source: https://www.prnewswire.co.uk/news-releases/brightgene-presents-positive-phase-2-data-for-dual-glp-1rgipr-agonist-for-weight-management-and-type-2-diabetes-and-preclinical-data-for-novel-amylin-analog-at-american-diabetes-associations-85th-scientific-sessions-302488874.html [index, 2026-10-15]

### 58. https://www.researchgate.net/publication/251247194_Understanding_Amylin_Receptors

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amylin receptor family background — not verified.
- **Report claims attributed to this source:**
  - EN line 30 (Part 1): | Insulin : Amylin molar ratio | **Conflicting; no single verified value**: ~100:1 (insulin : amylin); ~20:1; rat fasting 100:2.3, fed 100:2.6; one review states amylin is ~12% of insulin. Results differ by assay / species; any citation must state the assay and species | https://pmc.ncbi.nlm.nih.gov/articles/PMC12154432/ ; https://www.researchgate.net/publication/251247194_Understanding_Amylin_Receptors ; https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2013.00042/full [index, 2026-10-15] |
  - EN line 50 (Part 1): - **Pleiotropic coupling**: CTR can couple Gαs, Gαq, Gαi/o → cAMP, intracellular Ca²⁺, ERK1/2, FAK; the effect of RAMPs on signaling bias is underexplored; preliminary COS7 data: AMY1a / AMY3a preferentially signal via Gαs, with no parallel Ca²⁺ / ERK1/2 elevation. Source: https://www.researchgate.net/publication/251247194_Understanding_Amylin_Receptors [index, 2026-10-15]
  - EN line 52 (Part 1): - **β-arrestin / trafficking (mostly inferred)**: AMYR regulation / trafficking is little studied; inferred from CLR–RAMP1: agonist → phosphorylation + dynamin / β-arrestin-dependent internalization; one HEK293 study showed almost no AMY1R internalization. Sources: https://www.researchgate.net/publication/251247194_Understanding_Amylin_Receptors ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12410446/ [index, 2026-10-15]

### 59. https://www.roche.com/media/releases/med-cor-2025-03-10

- **Verdict:** could-not-access
- **Cited in:** English report
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Petrelintide Roche deal ($5.3B) and co-formulation claims — not verified.
- **Report claims attributed to this source:**
  - EN line 218 (Part 3): - **Combination**: Planned Phase 2 with enicepatide (CT-388, Roche dual GLP-1 / GIP agonist); no combination data disclosed. Source: https://www.roche.com/media/releases/med-cor-2025-03-10 [index, 2026-10-15]

### 60. https://www.sciencedirect.com/science/article/abs/pii/002432059502197Q

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Banks & Kastin 1995/1998 BBB claims (blood-to-brain influx, striatal accumulation, insulin comparison) — not verified. FLAG: the two other BBB citations (Physiology AJP, PMC3960470) are CONTRADICTED as BBB sources; this one remains the only plausible BBB citation and is unverified.
- **Report claims attributed to this source:**
  - ZH line 336 (Part 4): - **支持 BBB 本身穿透的证据（内源性 Amylin，大鼠，放射性标记）**：Banks & Kastin 1998, *Peptides*：静脉放射性标记 Amylin 穿过 BBB，在多个脑结构蓄积包括纹状体；脑穿透超过胰岛素。Banks et al. 1995：BBB 对 Amylin 的通透性（放射性标记研究）。脑中未检出 Amylin mRNA → 脑 Amylin 来自循环，与血液到脑转运一致。来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC3960470/ ；https://journals.physiology.org/doi/full/10.1152/ajpregu.2001.281.4.R1232 ；https://www.sciencedirect.com/science/article/abs/pii/002432059502197Q [index, 2026-10-15]

### 61. https://www.sciencedirect.com/science/article/abs/pii/S0196978102000220

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Third-ventricle / hypothalamic amylin claims — not verified.
- **Report claims attributed to this source:**
  - EN line 111 (Part 2): | Satiety / feeding | Peripheral amylin → central satiety (see AP / NTS / PBN / VTA) | Amylin KO mice: transient hyperphagia, ↑ adiposity; amylin antagonist AC187 ↑ feeding / meal size (peripheral or central); low near-physiological exogenous amylin (~2× postprandial levels) suppresses feeding in rats; pramlintide ↓ appetite in diabetes and non-diabetic obesity | ↓ meal size, ↓ energy intake — core weight-loss mechanism | Third-ventricle central amylin (100 pmol) ↓ rat feeding without conditioned taste aversion — supports non-aversive satiety at that dose / route in rodents | Established (huma

### 62. https://www.takeda.com/en-us/newsroom/news-releases/2011/amylin-and-takeda-discontinue-development-of-pramlintidemetreleptin-combination-treatment-for-obesity-following-commercial-reassessment-of-the-program/

- **Verdict:** could-not-access
- **Cited in:** English report, Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Pramlintide/metreleptin discontinuation details — not verified.
- **Report claims attributed to this source:**
  - EN line 185 (Part 3): | Pramlintide + Metreleptin (amylin + leptin) | Amylin Pharmaceuticals + Takeda | Terminated (Aug 2011, commercial reassessment; Phase 2 trial paused Mar 2011 after antibody laboratory findings related to metreleptin in 2 patients in a previously completed study) | Twice-daily injections (Phase 2 formulation) | — | Phase 2 (28 weeks + 52-week extension): most robust efficacy in BMI < 35 subgroup (numbers not obtained in retrieved sources) | Nausea + injection-site adverse events most common, appearing at initiation and declining with duration | https://www.takeda.com/en-us/newsroom/news-releas
  - EN line 267 (Part 3): - Terminated Aug 2011 (commercial reassessment; Phase 2 trial paused Mar 2011 after antibody laboratory findings related to metreleptin in 2 patients). Phase 2 (28 weeks + 52-week extension): most robust efficacy in BMI < 35 subgroup (numbers not obtained). Nausea + injection-site adverse events most common, appearing at initiation and declining with duration. Source: https://www.takeda.com/en-us/newsroom/news-releases/2011/amylin-and-takeda-discontinue-development-of-pramlintidemetreleptin-combination-treatment-for-obesity-following-commercial-reassessment-of-the-program/ [index, 2026-10-15]

### 63. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01487-X/abstract

- **Verdict:** could-not-access
- **Cited in:** Chinese original
- **What was read:** browser 429 rate limit; not retried
- **Findings / corrections:** Amycretin Lancet Phase 2 data — not verified. NOTE: URL contains '(26)' year suffix; identifier needs confirmation on re-check.
- **Report claims attributed to this source:**
  - ZH line 351 (Part 4): - **骨骼肌 / 脂肪 / 肝（次要，证据薄）**：Amylin 受体报告分布于脑、胰腺、脂肪、胃肠。较老文献：Amylin 反对肌肉糖原合成、激活糖原分解 / 糖酵解；可能调节乳糜微粒摄取 / 脂蛋白受体。是否由充分表征的外周 AMYR 介导**未证实**（外周 CTR + RAMP 共表达数据自 1998 年以来稀疏）。来源：https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01487-X/abstract ；https://www.mdpi.com/1589566 ；https://www.springermedizin.de/amylin-from-mode-of-action-to-future-clinical-potential-in-diabe/50958810 [index, 2026-10-15]
