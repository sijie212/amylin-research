#!/usr/bin/env python3
"""Build knowledge_graph.json + index.html (with the same data embedded) for the
amylin agonist / weight-loss knowledge graph.

Source of truth: ~/workspace/research_notes/amylin-agonist-weight-loss-20261015/report.md
(Cninese report, 2026-10-15). Every node/edge below must be traceable to that
report. Evidence grades: established / emerging / unverified.
Run: python3 build_kg.py  (writes knowledge_graph.json and index.html)
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

NODES = [
    # ---------------- Molecules ----------------
    {"id": "amylin", "label": "Amylin (IAPP)", "type": "Molecule",
     "description": "Endogenous 37-amino-acid peptide hormone co-secreted with insulin from pancreatic beta cells. Human amylin readily aggregates into amyloid fibrils."},
    {"id": "insulin", "label": "Insulin", "type": "Molecule",
     "description": "Pancreatic hormone co-secreted with amylin. The insulin:amylin molar ratio is conflicting/unverified (reports range ~100:1 to ~20:1, assay- and species-dependent)."},
    {"id": "glucagon", "label": "Glucagon", "type": "Molecule",
     "description": "Pancreatic alpha-cell hormone; postprandial glucagon is suppressed by amylin signaling."},
    {"id": "calcitonin", "label": "Calcitonin", "type": "Molecule",
     "description": "Thyroid C-cell hormone; cognate ligand of the calcitonin receptor (CTR); inhibits osteoclast-mediated bone resorption."},
    {"id": "cgrp", "label": "CGRP (alpha-CGRP)", "type": "Molecule",
     "description": "Calcitonin gene-related peptide; high-affinity ligand of the CGRP receptor (CLR + RAMP1) and cross-reacts with AMY1."},
    {"id": "salmon_ct", "label": "Salmon calcitonin (sCT)", "type": "Molecule",
     "description": "Potent non-selective amylin/calcitonin receptor agonist used as a research tool; activates AMY receptors and CTR."},
    {"id": "albumin", "label": "Serum albumin", "type": "Molecule",
     "description": "Plasma protein; fatty-acid-acylated amylin analogs bind albumin reversibly, forming a circulating reservoir that slows clearance."},
    {"id": "amyloid_oligomer", "label": "Amylin oligomers", "type": "Molecule",
     "description": "Misfolded amylin oligomers, considered more toxic than fibrils; drive ER stress, mitochondrial dysfunction, and beta-cell apoptosis."},
    # ---------------- Receptors ----------------
    {"id": "ctr", "label": "Calcitonin receptor (CTR / CALCR)", "type": "Receptor",
     "description": "Class B / secretin-family GPCR; alone it is the functional calcitonin receptor; RAMP association creates AMY1-3."},
    {"id": "amy1", "label": "AMY1 receptor (CTR + RAMP1)", "type": "Receptor",
     "description": "Amylin receptor subtype; shares RAMP1 with the CGRP receptor, hence CGRP cross-reactivity."},
    {"id": "amy2", "label": "AMY2 receptor (CTR + RAMP2)", "type": "Receptor",
     "description": "Amylin receptor subtype; reported as more restricted to GI / endocrine tissues (human protein-level map unverified)."},
    {"id": "amy3", "label": "AMY3 receptor (CTR + RAMP3)", "type": "Receptor",
     "description": "Amylin receptor subtype; proposed Abeta receptor in hippocampus (Alzheimer's hypothesis, not a metabolic pathway)."},
    {"id": "cgrp_receptor", "label": "CGRP receptor (CLR + RAMP1)", "type": "Receptor",
     "description": "Classical CGRP receptor; mediates CGRP vasodilation; migraine CGRP antagonists may also antagonize AMY1."},
    {"id": "ramp1", "label": "RAMP1", "type": "Receptor",
     "description": "Receptor activity-modifying protein 1; accessory subunit converting CTR into AMY1 and CLR into the CGRP receptor."},
    {"id": "ramp2", "label": "RAMP2", "type": "Receptor",
     "description": "Receptor activity-modifying protein 2; accessory subunit converting CTR into AMY2."},
    {"id": "ramp3", "label": "RAMP3", "type": "Receptor",
     "description": "Receptor activity-modifying protein 3; accessory subunit converting CTR into AMY3."},
    {"id": "glp1r", "label": "GLP-1 receptor (GLP-1R)", "type": "Receptor",
     "description": "Target of GLP-1 receptor agonists (semaglutide, tirzepatide); co-target of the unimolecular dual agonist amycretin."},
    {"id": "gipr", "label": "GIP receptor (GIPR)", "type": "Receptor",
     "description": "Target of GIP receptor agonists; co-target of tirzepatide, enicepatide, and the MBX 5765 prodrug."},
    {"id": "gcgr", "label": "Glucagon receptor (GCGR)", "type": "Receptor",
     "description": "Target of glucagon receptor agonists; co-target of AZD9550 and the MBX 5765 prodrug."},
    {"id": "lepr", "label": "Leptin receptor (LEPR)", "type": "Receptor",
     "description": "Target of leptin / metreleptin signaling."},
    # ---------------- Brain regions ----------------
    {"id": "ap", "label": "Area Postrema (AP)", "type": "BrainRegion",
     "description": "Circumventricular organ lacking BBB features; fenestrated capillaries let plasma drugs reach AP neurons directly. First central node for amylin satiety."},
    {"id": "nts", "label": "Nucleus Tractus Solitarius (NTS)", "type": "BrainRegion",
     "description": "Dorsal vagal complex nucleus; receives AP input and integrates vagal gut signals; meal termination."},
    {"id": "lpbn", "label": "Lateral Parabrachial Nucleus (LPBN)", "type": "BrainRegion",
     "description": "Receives AP/NTS input via CGRP (Calca) neurons; relays to CeA and BNST; meal termination and alarm/aversion relay."},
    {"id": "cea", "label": "Central Amygdala (CeA)", "type": "BrainRegion",
     "description": "Receives LPBN CGRP input; PKC-delta neurons mediate CCK-induced anorexia; site of conditioned aversion."},
    {"id": "arc", "label": "Arcuate Nucleus (ARC)", "type": "BrainRegion",
     "description": "Hypothalamic nucleus with POMC/CART (anorexigenic) and AgRP/NPY (orexigenic) neurons; direct amylin-to-POMC mechanism not established."},
    {"id": "vmh", "label": "Ventromedial Hypothalamus (VMH)", "type": "BrainRegion",
     "description": "Hypothalamic nucleus; Calcr enriched in rodents; secondary hypothalamic node."},
    {"id": "pvn", "label": "Paraventricular Nucleus (PVN)", "type": "BrainRegion",
     "description": "Hypothalamic nucleus integrating ARC and hindbrain signals."},
    {"id": "vta", "label": "Ventral Tegmental Area (VTA)", "type": "BrainRegion",
     "description": "Dopamine neurons projecting to nucleus accumbens and mPFC; amylin reduces food reward/motivation (rodent-established, human emerging)."},
    {"id": "hippocampus", "label": "Hippocampus", "type": "BrainRegion",
     "description": "AMY3 proposed as Abeta receptor; amylin + Abeta inhibit LTP in rodent slices (Alzheimer's hypothesis only, not a metabolic pathway)."},
    {"id": "bnst", "label": "Bed Nucleus of the Stria Terminalis (BNST)", "type": "BrainRegion",
     "description": "Receives LPBN CGRP input; downstream of PBN in aversion circuitry."},
    {"id": "nac", "label": "Nucleus Accumbens", "type": "BrainRegion",
     "description": "Receives VTA dopamine input; amylin activation in VTA suppresses accumbal dopamine for fat more than sucrose (rat voltammetry)."},
    {"id": "mpfc", "label": "Medial Prefrontal Cortex (mPFC)", "type": "BrainRegion",
     "description": "Receives VTA input; amylin reduces food-evoked mPFC cFos and phasic dopamine."},
    {"id": "ldtg", "label": "Laterodorsal Tegmental Nucleus (LDTg)", "type": "BrainRegion",
     "description": "Direct amylin microinjection site shown to modulate intake/reward in rodents."},
    {"id": "hypothalamus", "label": "Hypothalamus", "type": "BrainRegion",
     "description": "Brain region integrating homeostatic hunger signals; Calcr enriched in ARC, DMH, PVN, VMH (rodent)."},
    {"id": "locus_coeruleus", "label": "Locus Coeruleus", "type": "BrainRegion",
     "description": "Brainstem nucleus with RAMP1 mRNA / CGRP binding reported; expression only, amylin function unestablished."},
    {"id": "dvc", "label": "Dorsal Vagal Complex (DVC)", "type": "BrainRegion",
     "description": "AP + NTS + dorsal motor nucleus of the vagus; integrates hindbrain satiety signals."},
    {"id": "dmh", "label": "Dorsomedial Hypothalamus (DMH)", "type": "BrainRegion",
     "description": "Hypothalamic nucleus with Calcr enrichment in rodents."},
    {"id": "sfo", "label": "Subfornical Organ (SFO)", "type": "BrainRegion",
     "description": "Another circumventricular organ proposed as an amylin action site."},
    # ---------------- Organs ----------------
    {"id": "pancreas", "label": "Pancreas", "type": "Organ",
     "description": "Contains beta cells (amylin + insulin secretion) and alpha cells (glucagon)."},
    {"id": "stomach", "label": "Stomach", "type": "Organ",
     "description": "Gastric emptying is delayed by amylin signaling via vagal efferents."},
    {"id": "gi_tract", "label": "Gastrointestinal Tract", "type": "Organ",
     "description": "Site of oral peptide degradation (acid + proteases) and permeation-enhancer action."},
    {"id": "kidney", "label": "Kidney", "type": "Organ",
     "description": "Main clearance organ for amylin and pramlintide; site of amylin deposition in diabetic nephropathy (observational)."},
    {"id": "liver", "label": "Liver", "type": "Organ",
     "description": "Hepatic glucose production is reduced downstream of glucagon suppression; hepatic fat reduced with CagriSema (REIMAGINE 1 MRI substudy)."},
    {"id": "lung", "label": "Lung", "type": "Organ",
     "description": "Amylin binding sites reported in lung (review-level evidence)."},
    # ---------------- Tissues / cells ----------------
    {"id": "beta_cell", "label": "Pancreatic Beta Cells", "type": "Tissue",
     "description": "Produce and co-secrete amylin with insulin; human beta-cell AMY subtype composition unverified."},
    {"id": "alpha_cell", "label": "Pancreatic Alpha Cells", "type": "Tissue",
     "description": "Secrete glucagon; suppressed by amylin (direct vs central mechanism unresolved; exact AMY subtype unverified)."},
    {"id": "bone", "label": "Bone", "type": "Tissue",
     "description": "Calcitonin inhibits osteoclast resorption; amylin bone effects via CALCR refuted by mouse KO (unidentified receptor); human osteoblasts lack CTR expression."},
    {"id": "osteoclast", "label": "Osteoclasts", "type": "Tissue",
     "description": "Bone-resorbing cells inhibited by calcitonin via CALCR; amylin inhibition of osteoclastogenesis not mediated by CALCR in vivo."},
    {"id": "osteoblast", "label": "Osteoblasts", "type": "Tissue",
     "description": "Human osteoblast samples show high CLR + RAMP1, low RAMP2, no RAMP3 or CTR expression."},
    {"id": "vasculature", "label": "Vasculature", "type": "Tissue",
     "description": "CALCRL protein in capillary endothelium and arterial smooth muscle; amylin vasodilation via CGRP receptor in rodents; human effect unestablished."},
    {"id": "bat", "label": "Brown Adipose Tissue (BAT)", "type": "Tissue",
     "description": "Thermogenesis proposed downstream of central amylin to sympathetic activation; rodent-only evidence."},
    {"id": "skeletal_muscle", "label": "Skeletal Muscle", "type": "Tissue",
     "description": "Amylin binding sites reported; older literature suggests opposition to muscle glycogen synthesis (unverified as AMYR-mediated)."},
    {"id": "adipose", "label": "Adipose Tissue", "type": "Tissue",
     "description": "Amylin receptor distribution reported; fat mass reduced by amylin agonists (largely via reduced intake)."},
    {"id": "choroid_plexus", "label": "Choroid Plexus / Ventricular Wall", "type": "Tissue",
     "description": "CALCR detected in circumventricular organs including choroid plexus and ependymal cells."},
]

NODES += [
    # ---------------- Drugs ----------------
    {"id": "pramlintide", "label": "Pramlintide (Symlin)", "type": "Drug",
     "description": "Only approved amylin agonist (FDA 2005-03-16), diabetes adjunct, NOT a weight-loss indication. SC, 2-3x/day pre-meal; t1/2 ~48 min; F 30-40%."},
    {"id": "cagrilintide", "label": "Cagrilintide", "type": "Drug",
     "description": "Novo Nordisk long-acting acylated amylin analog; dual amylin + calcitonin receptor agonist (DACRA); SC weekly; t1/2 ~7-8 days (secondary source)."},
    {"id": "davalintide", "label": "Davalintide (AC2307)", "type": "Drug",
     "description": "Amylin Pharmaceuticals; terminated after Phase 2 (not superior to pramlintide)."},
    {"id": "petrelintide", "label": "Petrelintide (ZP8396)", "type": "Drug",
     "description": "Zealand Pharma + Roche; long-acting human amylin analog; Phase 3 ZUPREME program started Sep 2026; SC weekly; t1/2 ~240 h; F ~85%."},
    {"id": "eloralintide", "label": "Eloralintide (LY3841136)", "type": "Drug",
     "description": "Lilly selective AMY1 receptor agonist; Phase 2 complete; SC weekly; t1/2 ~310-366 h (secondary source)."},
    {"id": "azd6234", "label": "AZD6234", "type": "Drug",
     "description": "AstraZeneca weekly selective amylin receptor agonist (SARA); Phase 2 (one landscape table claims Phase III - conflict unresolved)."},
    {"id": "abbv295", "label": "ABBV-295 (GUB014295)", "type": "Drug",
     "description": "Gubra to AbbVie; long-acting amylin analog; Phase 1 complete, Phase 2 started Aug 2026 (NCT07752979); t1/2 10.7-12.3 days."},
    {"id": "kbp_series", "label": "KBP Series (DACRA)", "type": "Drug",
     "description": "KeyBioscience DACRA series (KBP-042/-089/-056 etc.); all preclinical or terminated; no clinical program."},
    {"id": "viking_dacra", "label": "Viking DACRA (VK3012/3006/3015; VK3019)", "type": "Drug",
     "description": "Viking Therapeutics dual amylin + calcitonin receptor agonists; preclinical series; VK3019 entered Phase 1 SAD Jun 2026."},
    {"id": "bgm1812", "label": "BGM1812", "type": "Drug",
     "description": "BrightGene preclinical amylin analog; amylin receptor activity 1.8x petrelintide (EC50) in preclinical data."},
    {"id": "cagrisema", "label": "CagriSema", "type": "Drug",
     "description": "Novo Nordisk fixed-dose combination: cagrilintide 2.4 mg + semaglutide 2.4 mg; NDA submitted 2025-12-18; decision expected 2026 Q4; SC weekly."},
    {"id": "eloratzp", "label": "EloraTZP", "type": "Drug",
     "description": "Lilly combination: eloralintide + tirzepatide; Phase 2b complete; separate injections in Phase 2b; single-injection combo planned."},
    {"id": "amycretin", "label": "Amycretin / Zenagamtide (NN9487)", "type": "Drug",
     "description": "Novo Nordisk unimolecular dual GLP-1 + amylin receptor agonist (NOT a two-drug combo); SC weekly and oral daily; Phase 3 AMAZE ongoing. INN now Zenagamtide."},
    {"id": "pramlintide_metreleptin", "label": "Pramlintide + Metreleptin", "type": "Drug",
     "description": "Amylin + leptin combination; terminated Aug 2011 (commercial reassessment; antibody findings)."},
    {"id": "mbx5765", "label": "MBX 5765", "type": "Drug",
     "description": "MBX Biosciences preclinical single-peptide prodrug combining GLP-1 + GIP + glucagon + DACRA activity; designed for monthly dosing."},
    {"id": "accg2671", "label": "ACCG-2671", "type": "Drug",
     "description": "Structure Therapeutics oral, non-peptide, small-molecule dual amylin + calcitonin receptor agonist (DACRA); first oral small-molecule amylin agonist with clinical data; Phase 1 SAD complete Sep 2026; t1/2 ~6 days."},
    {"id": "asc39", "label": "ASC39", "type": "Drug",
     "description": "Ascletis oral small-molecule amylin receptor agonist, amylin-selective; preclinical candidate selected Mar 2026; IND filing expected 2026 Q3."},
    {"id": "asc36", "label": "ASC36", "type": "Drug",
     "description": "Ascletis oral amylin receptor peptide agonist (POTENT delivery platform); Phase 1 started 2026; NHP oral bioavailability 6-8%."},
    {"id": "vrb103", "label": "VRB-103", "type": "Drug",
     "description": "Verdiva Bio weekly oral amylin analog (peptide); preclinical; expected to enter clinic H2 2026."},
    {"id": "vrb102", "label": "VRB-102", "type": "Drug",
     "description": "Verdiva / Sciwind long-acting SC amylin agonist; preclinical."},
    {"id": "semaglutide", "label": "Semaglutide", "type": "Drug",
     "description": "GLP-1 receptor agonist; component of CagriSema (2.4 mg); t1/2 ~7 days."},
    {"id": "tirzepatide", "label": "Tirzepatide", "type": "Drug",
     "description": "Dual GIP/GLP-1 receptor agonist; component of EloraTZP; comparator in REDEFINE 4 / REIMAGINE 4/5."},
    {"id": "metreleptin", "label": "Metreleptin", "type": "Drug",
     "description": "Leptin analog; combined with pramlintide in a terminated obesity program."},
    {"id": "enicepatide", "label": "Enicepatide (CT-388)", "type": "Drug",
     "description": "Roche dual GLP-1/GIP agonist; planned Phase 2 combination with petrelintide; no combination data disclosed."},
    {"id": "enicepatide_combo", "label": "Petrelintide + Enicepatide", "type": "Drug",
     "description": "Roche/Zealand planned Phase 2 combination; no combination data disclosed."},
    {"id": "azd9550", "label": "AZD9550", "type": "Drug",
     "description": "AstraZeneca dual GLP-1/glucagon receptor agonist; component of the ASCEND combination with AZD6234."},
    {"id": "azd9550_combo", "label": "AZD9550 + AZD6234", "type": "Drug",
     "description": "AstraZeneca Phase 2b ASCEND combination (GLP-1/glucagon + amylin); data expected H2 2026; no results disclosed."},
    {"id": "nn9638", "label": "NN9638 (Amylin 355)", "type": "Drug",
     "description": "Novo Nordisk pipeline code listed by DelveInsight; no public mechanism/stage/efficacy details - do not treat as a confirmed clinical candidate."},
    {"id": "nn9839", "label": "NN9839 (Amylin 1213)", "type": "Drug",
     "description": "Novo Nordisk pipeline code listed by DelveInsight; no public mechanism/stage/efficacy details."},
    {"id": "xw015", "label": "XW015", "type": "Drug",
     "description": "Verdiva/Sciwind preclinical SC amylin candidate; no public data."},
    {"id": "accg3535", "label": "ACCG-3535", "type": "Drug",
     "description": "Structure Therapeutics preclinical oral amylin candidate; no public data."},
    {"id": "bibn4096bs", "label": "BIBN4096BS (olcegepant)", "type": "Drug",
     "description": "CGRP antagonist (gepant class); may also antagonize AMY1; ~150-fold lower sensitivity at AMY1(a) than at CGRP1 receptor."},
    {"id": "ac187", "label": "AC187", "type": "Drug",
     "description": "Amylin receptor antagonist (research tool); increases food intake / meal size in rodents."},
    {"id": "ac253", "label": "AC253", "type": "Drug",
     "description": "Amylin receptor antagonist used in Alzheimer's research; blocks amylin + Abeta inhibition of hippocampal LTP in rodent slices."},
    # ---------------- Effects ----------------
    {"id": "satiety", "label": "Satiety / Reduced Meal Size", "type": "Effect",
     "description": "Core weight-loss mechanism; established in humans and rodents."},
    {"id": "delayed_gastric_emptying", "label": "Delayed Gastric Emptying", "type": "Effect",
     "description": "Established in humans; via vagal efferents; contributes to satiety and nausea."},
    {"id": "glucagon_suppression", "label": "Postprandial Glucagon Suppression", "type": "Effect",
     "description": "Established in humans; reduces hepatic glucose output; direct vs central mechanism unresolved."},
    {"id": "nausea", "label": "Nausea", "type": "Effect",
     "description": "Most common adverse effect; dose-dependent, early, mitigated by titration; human AP/PBN mechanism unconfirmed."},
    {"id": "vomiting", "label": "Vomiting", "type": "Effect",
     "description": "Dose-dependent adverse effect; AP chemoreceptor trigger zone / vomiting circuitry."},
    {"id": "weight_loss", "label": "Weight Loss", "type": "Effect",
     "description": "Outcome of reduced intake (and possibly energy expenditure); established for pramlintide (modest) and newer analogs (larger)."},
    {"id": "hypoglycemia", "label": "Severe Hypoglycemia (with Insulin)", "type": "Effect",
     "description": "Boxed warning for pramlintide + insulin, especially T1D, mostly within 3 h of injection."},
    {"id": "energy_expenditure", "label": "Energy Expenditure / BAT Thermogenesis", "type": "Effect",
     "description": "Rodent-only: central amylin increases energy expenditure and BAT sympathetic activity; human studies not performed."},
    {"id": "food_reward_reduction", "label": "Reduced Food Reward / Motivation", "type": "Effect",
     "description": "Rodent-established (VTA); human emerging; fat vs sugar differences in accumbal dopamine suppression."},
    {"id": "blood_pressure_effect", "label": "Blood Pressure / Vasodilation", "type": "Effect",
     "description": "Rodent vasodilation via CGRP receptor; no established human systemic BP effect for amylin agonists."},
    {"id": "bone_resorption_inhibition", "label": "Bone Resorption Inhibition", "type": "Effect",
     "description": "Established for calcitonin; amylin bone effect via CALCR refuted by mouse KO; human therapeutic bone effect unestablished."},
    {"id": "postprandial_glucose", "label": "Postprandial Glucose Lowering", "type": "Effect",
     "description": "Established: blunted postprandial glucose rise via delayed gastric emptying + glucagon suppression."},
    {"id": "aversion", "label": "Conditioned Taste Aversion", "type": "Effect",
     "description": "Aversion memory mediated by PBN to CeA; rodent evidence supports separable satiety vs aversion circuits; human mechanism unconfirmed."},
    {"id": "leptin_responsiveness", "label": "Restored Leptin Responsiveness", "type": "Effect",
     "description": "Preclinical: amylin restores leptin responsiveness in rodent brain."},
    {"id": "fatigue", "label": "Fatigue", "type": "Effect",
     "description": "Reported adverse effect (e.g., eloralintide Phase 2, 0-46% by group)."},
    {"id": "hepatic_glucose_output", "label": "Reduced Hepatic Glucose Output", "type": "Effect",
     "description": "Downstream of glucagon suppression: reduced glycogenolysis / gluconeogenesis."},
    # ---------------- Processes ----------------
    {"id": "sc_absorption", "label": "Subcutaneous Absorption", "type": "Process",
     "description": "Mainstream route; bypasses GI lumen degradation and portal first-pass."},
    {"id": "oral_absorption", "label": "Oral Absorption", "type": "Process",
     "description": "Exceptional for amylin peptides; limited by acid + protease degradation and poor permeability; SNAC improves semaglutide oral F to ~0.4-1%."},
    {"id": "albumin_binding", "label": "Albumin Binding (Reversible)", "type": "Process",
     "description": "Fatty-acid acylation promotes reversible albumin binding, a circulating reservoir that slows clearance and extends half-life."},
    {"id": "proteolysis", "label": "Proteolysis", "type": "Process",
     "description": "Peptide degradation by proteases; IDE degrades amylin; specific proteases for synthetic agonists undisclosed."},
    {"id": "renal_clearance", "label": "Renal Clearance", "type": "Process",
     "description": "Main clearance route for amylin and pramlintide; kidney is the main determinant of plasma amylin levels."},
    {"id": "bbb_crossing", "label": "Blood-Brain Barrier (BBB) Crossing", "type": "Process",
     "description": "Penetration of the tight-junction brain endothelium into parenchyma behind the BBB; NO direct human evidence for synthetic agonists (no CSF data)."},
    {"id": "ap_access", "label": "AP Access via Fenestrated Capillaries", "type": "Process",
     "description": "Plasma drugs diffuse through leaky AP capillaries to AP neurons WITHOUT crossing the BBB itself."},
    {"id": "vagal_efferent", "label": "Vagal Efferent Signaling", "type": "Process",
     "description": "Downstream effector: AP to vagal efferents to gut to slowed gastric emptying."},
    {"id": "vagal_afferent", "label": "Vagal Afferent Signaling", "type": "Process",
     "description": "NOT required for amylin's anorectic effect (subdiaphragmatic vagotomy does not block it)."},
    {"id": "camp_signaling", "label": "Gs to cAMP to PKA Signaling", "type": "Process",
     "description": "Main amylin receptor signaling cascade; also acute pERK1/2, Akt, c-Fos."},
    {"id": "aggregation", "label": "Amylin Aggregation / Amyloid Formation", "type": "Process",
     "description": "Human amylin misfolds into oligomers and fibrils; >70-90% of T2D autopsies show islet amyloid deposits."},
    {"id": "gastric_degradation", "label": "Gastric Acid + Protease Degradation", "type": "Process",
     "description": "Oral barrier: acid + pepsin/trypsin/chymotrypsin/peptidases rapidly degrade peptides."},
    {"id": "snac_enhancement", "label": "SNAC Permeation Enhancement", "type": "Process",
     "description": "SNAC buffers local pH, interferes with pepsinogen activation, fluidizes gastric lipid membrane; oral semaglutide F ~0.4-1%."},
    {"id": "internalization", "label": "Receptor Internalization", "type": "Process",
     "description": "Mostly inferred from CLR-RAMP1: agonist to phosphorylation + dynamin/beta-arrestin-dependent internalization; one HEK293 study showed almost no AMY1R internalization."},
    {"id": "beta_cell_apoptosis", "label": "Beta-Cell Apoptosis", "type": "Process",
     "description": "Downstream of misfolded amylin: ER stress/UPR, mitochondrial dysfunction, BAX up / Bcl-xL down, ROS, IL-1beta to apoptosis."},
    {"id": "dose_titration", "label": "Dose Titration", "type": "Process",
     "description": "Slow dose escalation reduces GI adverse events; e.g., pramlintide start low, increase only after >=3 days without nausea."},
    # ---------------- Pathways ----------------
    {"id": "ap_nts_lpbn", "label": "AP to NTS to LPBN Central Satiety Pathway", "type": "Pathway",
     "description": "Established: AP (CVO) to NTS to LPBN to hypothalamus/forebrain; core weight-loss mechanism."},
    {"id": "vta_reward", "label": "VTA Reward Pathway", "type": "Pathway",
     "description": "Rodent-established; VTA amylin reduces food reward/motivation via dopamine circuits."},
    {"id": "gastric_emptying_pathway", "label": "Gastric Emptying Pathway", "type": "Pathway",
     "description": "AP to vagal efferents to gut; established."},
    {"id": "glucagon_pathway", "label": "Glucagon Suppression Pathway", "type": "Pathway",
     "description": "Amylin to alpha cells (direct and/or islet paracrine); established, exact subtype unverified."},
    {"id": "bat_thermogenesis", "label": "BAT Thermogenesis Pathway", "type": "Pathway",
     "description": "Central amylin to sympathetic to BAT; rodent-only."},
    {"id": "amyloid_toxicity", "label": "Amyloid Toxicity Pathway", "type": "Pathway",
     "description": "Misfolded amylin to ER stress, mitochondrial dysfunction, beta-cell apoptosis (emerging; prion-like seeding hypothesis)."},
    {"id": "aversion_pathway", "label": "PBN to CeA Aversion Pathway", "type": "Pathway",
     "description": "LPBN CGRP to CeA PKC-delta; conditioned taste aversion; amylin-specific human nausea mapping unconfirmed."},
    # ---------------- Enzymes ----------------
    {"id": "ide", "label": "Insulin-Degrading Enzyme (IDE)", "type": "Enzyme",
     "description": "Degrades amylin (also insulin, glucagon, ANP, IGF-1/2, Abeta); cleaves peptides up to ~70 aa."},
    {"id": "neprilysin", "label": "Neprilysin (NEP)", "type": "Enzyme",
     "description": "Established Abeta-degrading protease; NO direct evidence it degrades amylin - do not assert."},
]

# (source, target, relation, evidence, source_ref)  -- source_ref = section of the source report
EDGES = [
    # ---------- Receptor composition ----------
    ("ramp1", "amy1", "SUBUNIT_OF", "established", "§1.2"),
    ("ramp2", "amy2", "SUBUNIT_OF", "established", "§1.2"),
    ("ramp3", "amy3", "SUBUNIT_OF", "established", "§1.2"),
    ("ctr", "amy1", "SUBUNIT_OF", "established", "§1.2"),
    ("ctr", "amy2", "SUBUNIT_OF", "established", "§1.2"),
    ("ctr", "amy3", "SUBUNIT_OF", "established", "§1.2"),
    ("ramp1", "cgrp_receptor", "SUBUNIT_OF", "established", "§1.2"),
    # ---------- Ligand -> receptor ----------
    ("amylin", "amy1", "ACTIVATES", "established", "§1.2"),
    ("amylin", "amy2", "ACTIVATES", "established", "§1.2"),
    ("amylin", "amy3", "ACTIVATES", "established", "§1.2"),
    ("amylin", "ctr", "ACTIVATES", "established", "§1.4 (weak; rAMY pEC50 6.95 at CTR(a))"),
    ("cgrp", "amy1", "ACTIVATES", "established", "§1.2 (high affinity; shared RAMP1)"),
    ("cgrp", "cgrp_receptor", "ACTIVATES", "established", "§1.2"),
    ("calcitonin", "ctr", "ACTIVATES", "established", "§1.2"),
    ("calcitonin", "amy3", "ACTIVATES", "established", "§1.4 (hCT pEC50 8.02 at AMY3(a))"),
    ("salmon_ct", "amy1", "ACTIVATES", "established", "§2.1 (research-tool agonist)"),
    ("salmon_ct", "amy2", "ACTIVATES", "established", "§2.1 (research-tool agonist)"),
    ("salmon_ct", "amy3", "ACTIVATES", "established", "§2.1 (research-tool agonist)"),
    ("salmon_ct", "ctr", "ACTIVATES", "established", "§2.1 (research-tool agonist)"),
    # ---------- Signaling ----------
    ("amy1", "camp_signaling", "ACTIVATES", "established", "§1.3"),
    ("amy2", "camp_signaling", "ACTIVATES", "established", "§1.3"),
    ("amy3", "camp_signaling", "ACTIVATES", "established", "§1.3"),
    ("ctr", "camp_signaling", "ACTIVATES", "established", "§1.3"),
    ("camp_signaling", "ap_nts_lpbn", "PART_OF", "established", "§1.3 + §2.1"),
    ("amy1", "internalization", "CAUSES", "emerging", "§1.3 (mostly inferred; one HEK293 study showed almost no AMY1R internalization)"),
    # ---------- Expression ----------
    ("ctr", "kidney", "EXPRESSED_IN", "established", "§1.5 (HPA protein in renal tubules)"),
    ("ctr", "choroid_plexus", "EXPRESSED_IN", "emerging", "§1.5 (HPA; circumventricular organs)"),
    ("ctr", "beta_cell", "EXPRESSED_IN", "emerging", "§1.5 (mouse co-localization; human unverified)"),
    ("ctr", "ap", "EXPRESSED_IN", "emerging", "§4.2 (rodent mRNA)"),
    ("ctr", "hypothalamus", "EXPRESSED_IN", "emerging", "§1.5 (rodent + HPA)"),
    ("ctr", "arc", "EXPRESSED_IN", "emerging", "§1.5 (mouse Calcr enrichment)"),
    ("ctr", "osteoblast", "NOT_EXPRESSED_IN", "established", "§1.5 (16 human osteoblast samples: no CTR)"),
    ("ramp1", "ap", "EXPRESSED_IN", "emerging", "§1.5 (rodent mRNA)"),
    ("ramp2", "ap", "EXPRESSED_IN", "emerging", "§4.2 (rodent mRNA)"),
    ("ramp3", "ap", "EXPRESSED_IN", "emerging", "§4.2 (rodent mRNA)"),
    ("ramp1", "locus_coeruleus", "EXPRESSED_IN", "emerging", "§1.5 (rodent mRNA)"),
    ("cgrp_receptor", "vasculature", "EXPRESSED_IN", "emerging", "§1.5 (CALCRL IHC, human/rat/mouse)"),
    ("amy2", "ap", "EXPRESSED_IN", "emerging", "§4.2 (CTR + RAMP2 mRNA in AP, rodent)"),
    ("amy3", "ap", "EXPRESSED_IN", "emerging", "§4.2 (CTR + RAMP3 mRNA in AP, rodent)"),
    ("amy3", "hippocampus", "EXPRESSED_IN", "emerging", "§2.1 (AMY3 proposed Abeta receptor)"),
    # ---------- Anatomy / circuits ----------
    ("ap", "dvc", "PART_OF", "established", "§2.1"),
    ("nts", "dvc", "PART_OF", "established", "§2.1"),
    ("ap", "nts", "LEADS_TO", "established", "§2.1 (AP -> NTS)"),
    ("nts", "lpbn", "LEADS_TO", "established", "§2.1 (NTS -> LPBN)"),
    ("lpbn", "cea", "LEADS_TO", "established", "§2.1 (LPBN CGRP -> CeA)"),
    ("lpbn", "bnst", "LEADS_TO", "established", "§2.1 (LPBN -> BNST)"),
    ("lpbn", "hypothalamus", "LEADS_TO", "established", "§2.1 (LPBN -> hypothalamus/forebrain)"),
    ("arc", "hypothalamus", "PART_OF", "established", "§2.1"),
    ("vmh", "hypothalamus", "PART_OF", "established", "§2.1"),
    ("pvn", "hypothalamus", "PART_OF", "established", "§2.1"),
    ("dmh", "hypothalamus", "PART_OF", "established", "§1.5"),
    ("vta", "nac", "LEADS_TO", "established", "§2.1 (VTA dopamine -> NAc)"),
    ("vta", "mpfc", "LEADS_TO", "established", "§2.1 (VTA -> mPFC)"),
    # ---------- Pathways ----------
    ("ap", "ap_nts_lpbn", "PART_OF", "established", "§2.1"),
    ("nts", "ap_nts_lpbn", "PART_OF", "established", "§2.1"),
    ("lpbn", "ap_nts_lpbn", "PART_OF", "established", "§2.1"),
    ("hypothalamus", "ap_nts_lpbn", "PART_OF", "established", "§2.1"),
    ("ap_nts_lpbn", "satiety", "MEDIATES", "established", "§2.1"),
    ("ap_nts_lpbn", "weight_loss", "MEDIATES", "established", "§2.1"),
    ("amy1", "ap_nts_lpbn", "MEDIATES", "established", "§2.1"),
    ("amy2", "ap_nts_lpbn", "MEDIATES", "established", "§2.1"),
    ("amy3", "ap_nts_lpbn", "MEDIATES", "established", "§2.1"),
    ("vta", "vta_reward", "PART_OF", "emerging", "§2.1 (rodent)"),
    ("nac", "vta_reward", "PART_OF", "emerging", "§2.1 (rodent)"),
    ("mpfc", "vta_reward", "PART_OF", "emerging", "§2.1 (rodent)"),
    ("vta_reward", "food_reward_reduction", "MEDIATES", "emerging", "§2.1 (rodent-established; human emerging)"),
    ("vagal_efferent", "gastric_emptying_pathway", "PART_OF", "established", "§2.2"),
    ("stomach", "gastric_emptying_pathway", "PART_OF", "established", "§2.2"),
    ("gastric_emptying_pathway", "delayed_gastric_emptying", "MEDIATES", "established", "§2.2"),
    ("alpha_cell", "glucagon_pathway", "PART_OF", "established", "§2.2"),
    ("glucagon_pathway", "glucagon_suppression", "MEDIATES", "established", "§2.2"),
    ("bat", "bat_thermogenesis", "PART_OF", "emerging", "§2.2 (rodent-only)"),
    ("bat_thermogenesis", "energy_expenditure", "MEDIATES", "emerging", "§2.2 (rodent-only; human unconfirmed)"),
    ("amyloid_oligomer", "amyloid_toxicity", "PART_OF", "emerging", "§1.1"),
    ("beta_cell", "amyloid_toxicity", "PART_OF", "emerging", "§1.1 (target of toxicity)"),
    ("amyloid_toxicity", "beta_cell_apoptosis", "MEDIATES", "emerging", "§1.1"),
    ("lpbn", "aversion_pathway", "PART_OF", "emerging", "§2.1 (rodent)"),
    ("cea", "aversion_pathway", "PART_OF", "emerging", "§2.1 (rodent)"),
    ("aversion_pathway", "aversion", "MEDIATES", "emerging", "§2.1 (rodent)"),
    ("aversion_pathway", "nausea", "CAUSES", "unverified", "§2.5 (human AP/PBN nausea mapping unconfirmed)"),
    # ---------- Endogenous physiology ----------
    ("beta_cell", "amylin", "SECRETS", "established", "§1.1"),
    ("beta_cell", "insulin", "SECRETS", "established", "§1.1"),
    ("amylin", "insulin", "CO_SECRETED_WITH", "established", "§1.1 (same secretory granules)"),
    ("alpha_cell", "glucagon", "SECRETS", "established", "§2.2"),
    ("amylin", "satiety", "CAUSES", "established", "§1.1"),
    ("amylin", "delayed_gastric_emptying", "CAUSES", "established", "§1.1"),
    ("amylin", "glucagon_suppression", "CAUSES", "established", "§1.1"),
    ("amylin", "aggregation", "CAUSES", "emerging", "§1.1 (human amylin readily aggregates)"),
    ("aggregation", "beta_cell_apoptosis", "CAUSES", "emerging", "§1.1"),
    ("glucagon", "liver", "ACTS_ON", "established", "§4.2 (drives hepatic glucose output)"),
    ("glucagon_suppression", "hepatic_glucose_output", "LEADS_TO", "established", "§2.2"),
    ("hepatic_glucose_output", "postprandial_glucose", "LEADS_TO", "established", "§2.2"),
    ("amylin", "energy_expenditure", "CAUSES", "emerging", "§2.2 (rodent-only)"),
    ("amylin", "bone_resorption_inhibition", "CAUSES", "unverified", "§2.2 (via CALCR refuted; unidentified receptor)"),
    ("amylin", "blood_pressure_effect", "CAUSES", "unverified", "§2.2 (no established human systemic effect)"),
    ("cgrp", "blood_pressure_effect", "CAUSES", "emerging", "§2.2 (rodent vasodilation via CGRP receptor)"),
    ("calcitonin", "bone_resorption_inhibition", "CAUSES", "established", "§2.2"),
    ("amylin", "skeletal_muscle", "ACTS_ON", "emerging", "§4.2 (binding sites reported)"),
    ("amylin", "lung", "ACTS_ON", "emerging", "§4.2 (binding sites reported)"),
    ("amylin", "kidney", "ACTS_ON", "established", "§4.2 (binding + clearance)"),
    ("amylin", "leptin_responsiveness", "CAUSES", "emerging", "§4.2 (preclinical)"),
    # ---------- Vagal / AP access ----------
    ("ap", "vagal_efferent", "ACTIVATES", "established", "§4.2 (AP -> vagal efferents)"),
    ("vagal_efferent", "delayed_gastric_emptying", "CAUSES", "established", "§2.2"),
    ("vagal_afferent", "satiety", "NOT_REQUIRED_FOR", "established", "§4.2 (subdiaphragmatic vagotomy does not block anorexia)"),
    ("ap_access", "ap_nts_lpbn", "PART_OF", "established", "§4.2 (AP access starts the central relay)"),
    ("snac_enhancement", "oral_absorption", "ENHANCES", "established", "§4.2 (semaglutide model; F ~0.4-1%)"),
    ("gastric_degradation", "oral_absorption", "INHIBITS", "established", "§4.2"),
    ("albumin_binding", "renal_clearance", "REDUCES", "established", "§4.2 (lowers free fraction for filtration)"),
    ("dose_titration", "nausea", "REDUCES", "established", "§4.2"),
    # ---------- Drug -> receptor ----------
    ("pramlintide", "amy1", "ACTIVATES", "established", "§3.2"),
    ("pramlintide", "amy2", "ACTIVATES", "established", "§3.2"),
    ("pramlintide", "amy3", "ACTIVATES", "established", "§3.2 (biased to AMY3; EC50 114 pM vs CTR 1492 pM)"),
    ("cagrilintide", "amy1", "ACTIVATES", "established", "§3.2 (DACRA, non-selective)"),
    ("cagrilintide", "amy2", "ACTIVATES", "established", "§3.2 (DACRA, non-selective)"),
    ("cagrilintide", "amy3", "ACTIVATES", "established", "§3.2 (DACRA, non-selective)"),
    ("cagrilintide", "ctr", "ACTIVATES", "established", "§3.2 (DACRA)"),
    ("petrelintide", "amy1", "ACTIVATES", "established", "§3.2 (potent amylin + calcitonin agonist)"),
    ("petrelintide", "amy2", "ACTIVATES", "established", "§3.2 (potent amylin + calcitonin agonist)"),
    ("petrelintide", "amy3", "ACTIVATES", "established", "§3.2 (potent amylin + calcitonin agonist)"),
    ("petrelintide", "ctr", "ACTIVATES", "established", "§3.2 (potent amylin + calcitonin agonist)"),
    ("eloralintide", "amy1", "ACTIVATES", "established", "§3.2 (selective AMY1)"),
    ("eloralintide", "ctr", "ACTIVATES", "established", "§3.2 (weak; ~12x lower potency, assay-dependent)"),
    ("azd6234", "amy1", "ACTIVATES", "emerging", "§3.2 (selective amylin RA; limited public detail)"),
    ("abbv295", "amy1", "ACTIVATES", "emerging", "§3.2 (long-acting amylin analog)"),
    ("davalintide", "amy1", "ACTIVATES", "emerging", "§3.2 (terminated; limited detail)"),
    ("davalintide", "amy2", "ACTIVATES", "emerging", "§3.2 (terminated; limited detail)"),
    ("davalintide", "amy3", "ACTIVATES", "emerging", "§3.2 (terminated; limited detail)"),
    ("kbp_series", "amy1", "ACTIVATES", "emerging", "§3.2 (DACRA, preclinical)"),
    ("kbp_series", "ctr", "ACTIVATES", "emerging", "§3.2 (DACRA, preclinical)"),
    ("viking_dacra", "amy1", "ACTIVATES", "emerging", "§3.2 (DACRA, preclinical)"),
    ("viking_dacra", "ctr", "ACTIVATES", "emerging", "§3.2 (DACRA, preclinical)"),
    ("bgm1812", "amy1", "ACTIVATES", "emerging", "§3.2 (preclinical)"),
    ("bgm1812", "ctr", "ACTIVATES", "emerging", "§3.2 (preclinical)"),
    ("accg2671", "amy1", "ACTIVATES", "established", "§3.5 (oral small-molecule DACRA; Phase 1 data)"),
    ("accg2671", "ctr", "ACTIVATES", "established", "§3.5 (oral small-molecule DACRA)"),
    ("asc39", "amy1", "ACTIVATES", "emerging", "§3.5 (preclinical)"),
    ("asc36", "amy1", "ACTIVATES", "emerging", "§3.4 (Phase 1)"),
    ("vrb103", "amy1", "ACTIVATES", "emerging", "§3.4 (preclinical)"),
    ("vrb102", "amy1", "ACTIVATES", "emerging", "§3.4 (preclinical)"),
    ("amycretin", "amy1", "ACTIVATES", "established", "§3.3 (dual GLP-1 + amylin; clinical data)"),
    ("amycretin", "glp1r", "ACTIVATES", "established", "§3.3 (dual GLP-1 + amylin)"),
    ("mbx5765", "amy1", "ACTIVATES", "emerging", "§3.3 (preclinical four-pathway prodrug)"),
    ("mbx5765", "glp1r", "ACTIVATES", "emerging", "§3.3 (preclinical)"),
    ("mbx5765", "gipr", "ACTIVATES", "emerging", "§3.3 (preclinical)"),
    ("mbx5765", "gcgr", "ACTIVATES", "emerging", "§3.3 (preclinical)"),
    ("mbx5765", "ctr", "ACTIVATES", "emerging", "§3.3 (DACRA arm, preclinical)"),
    ("semaglutide", "glp1r", "ACTIVATES", "established", "§3.3"),
    ("tirzepatide", "glp1r", "ACTIVATES", "established", "§3.3"),
    ("tirzepatide", "gipr", "ACTIVATES", "established", "§3.3"),
    ("enicepatide", "glp1r", "ACTIVATES", "emerging", "§3.3 (dual GLP-1/GIP)"),
    ("enicepatide", "gipr", "ACTIVATES", "emerging", "§3.3 (dual GLP-1/GIP)"),
    ("azd9550", "glp1r", "ACTIVATES", "emerging", "§3.3 (dual GLP-1/glucagon)"),
    ("azd9550", "gcgr", "ACTIVATES", "emerging", "§3.3 (dual GLP-1/glucagon)"),
    ("metreleptin", "lepr", "ACTIVATES", "established", "§3.2 (leptin analog)"),
    ("bibn4096bs", "cgrp_receptor", "INHIBITS", "established", "§1.2 (CGRP antagonist)"),
    ("bibn4096bs", "amy1", "INHIBITS", "emerging", "§1.2 (~150-fold lower sensitivity at AMY1(a))"),
    ("ac187", "amy1", "INHIBITS", "emerging", "§2.2 (research-tool antagonist)"),
    ("ac187", "amy2", "INHIBITS", "emerging", "§2.2 (research-tool antagonist)"),
    ("ac187", "amy3", "INHIBITS", "emerging", "§2.2 (research-tool antagonist)"),
    ("ac253", "amy3", "INHIBITS", "emerging", "§2.1 (AD research; blocks LTP inhibition)"),
    # ---------- Drug combinations ----------
    ("cagrisema", "cagrilintide", "CONTAINS", "established", "§3.3"),
    ("cagrisema", "semaglutide", "CONTAINS", "established", "§3.3"),
    ("eloratzp", "eloralintide", "CONTAINS", "established", "§3.3"),
    ("eloratzp", "tirzepatide", "CONTAINS", "established", "§3.3"),
    ("pramlintide_metreleptin", "pramlintide", "CONTAINS", "established", "§3.2"),
    ("pramlintide_metreleptin", "metreleptin", "CONTAINS", "established", "§3.2"),
    ("enicepatide_combo", "petrelintide", "CONTAINS", "established", "§3.3"),
    ("enicepatide_combo", "enicepatide", "CONTAINS", "established", "§3.3"),
    ("azd9550_combo", "azd6234", "CONTAINS", "established", "§3.3"),
    ("azd9550_combo", "azd9550", "CONTAINS", "established", "§3.3"),
    # ---------- Drug -> effects ----------
    ("pramlintide", "satiety", "CAUSES", "established", "§3.2"),
    ("pramlintide", "delayed_gastric_emptying", "CAUSES", "established", "§3.2"),
    ("pramlintide", "glucagon_suppression", "CAUSES", "established", "§3.2"),
    ("pramlintide", "weight_loss", "CAUSES", "established", "§3.2 (modest; meta-analysis -2.57 kg)"),
    ("pramlintide", "nausea", "CAUSES", "established", "§3.2 (most common AE)"),
    ("pramlintide", "vomiting", "CAUSES", "established", "§3.2"),
    ("pramlintide", "hypoglycemia", "CAUSES", "established", "§3.2 (boxed warning with insulin)"),
    ("pramlintide", "postprandial_glucose", "CAUSES", "established", "§3.2"),
    ("pramlintide", "fatigue", "CAUSES", "established", "§2.5"),
    ("cagrilintide", "weight_loss", "CAUSES", "established", "§3.2 (Phase 2: -10.8% at 4.5 mg)"),
    ("cagrilintide", "nausea", "CAUSES", "established", "§3.2"),
    ("cagrilintide", "satiety", "CAUSES", "established", "§3.2"),
    ("petrelintide", "weight_loss", "CAUSES", "established", "§3.2 (Phase 2: -8.7 to -10.7%)"),
    ("petrelintide", "nausea", "CAUSES", "established", "§3.2 (20% vs 6% placebo)"),
    ("eloralintide", "weight_loss", "CAUSES", "established", "§3.2 (Phase 2: -20.1% at 9 mg)"),
    ("eloralintide", "nausea", "CAUSES", "established", "§3.2 (11-64% dose-dependent)"),
    ("eloralintide", "fatigue", "CAUSES", "established", "§3.2 (0-46%)"),
    ("cagrisema", "weight_loss", "CAUSES", "established", "§3.3 (REDEFINE 1: 22.7% / 20.4%)"),
    ("cagrisema", "nausea", "CAUSES", "established", "§3.3 (GI AEs predominant)"),
    ("cagrisema", "postprandial_glucose", "CAUSES", "established", "§3.3"),
    ("eloratzp", "weight_loss", "CAUSES", "established", "§3.3 (Phase 2b: -23.3% at Elora 9 mg + TZP 15 mg)"),
    ("amycretin", "weight_loss", "CAUSES", "established", "§3.3 (SC -24.3% Phase 1b/2a)"),
    ("amycretin", "nausea", "CAUSES", "established", "§3.3 (GI AEs most common)"),
    ("accg2671", "weight_loss", "CAUSES", "emerging", "§3.5 (Phase 1 SAD exploratory; -3.3% unadjusted)"),
    ("accg2671", "nausea", "CAUSES", "established", "§3.5 (SAD: 10 mg nausea + vomiting 6/6)"),
    ("accg2671", "vomiting", "CAUSES", "established", "§3.5 (SAD: 10 mg nausea + vomiting 6/6)"),
    ("abbv295", "weight_loss", "CAUSES", "emerging", "§3.2 (Phase 1 MAD: -7.8% to -9.8%)"),
    ("azd6234", "weight_loss", "CAUSES", "unverified", "§3.2 (no public efficacy results)"),
    ("davalintide", "weight_loss", "CAUSES", "emerging", "§3.2 (Phase 2; not superior to pramlintide)"),
    # ---------- Drug -> PK / brain access ----------
    ("pramlintide", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.2"),
    ("cagrilintide", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.2"),
    ("petrelintide", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.2"),
    ("eloralintide", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.2"),
    ("azd6234", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.2"),
    ("abbv295", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.2"),
    ("cagrisema", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.3"),
    ("eloratzp", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.3"),
    ("amycretin", "sc_absorption", "ADMINISTERED_VIA", "established", "§3.3"),
    ("amycretin", "oral_absorption", "ADMINISTERED_VIA", "established", "§3.3 (oral daily; SNAC)"),
    ("accg2671", "oral_absorption", "ADMINISTERED_VIA", "established", "§3.5 (oral small molecule)"),
    ("asc36", "oral_absorption", "ADMINISTERED_VIA", "emerging", "§3.4 (Phase 1)"),
    ("vrb103", "oral_absorption", "ADMINISTERED_VIA", "emerging", "§3.4 (preclinical)"),
    ("asc39", "oral_absorption", "ADMINISTERED_VIA", "emerging", "§3.5 (preclinical)"),
    ("cagrilintide", "albumin_binding", "USES", "established", "§4.2 (fatty-acid acylation)"),
    ("eloralintide", "albumin_binding", "USES", "established", "§4.2 (C20 fatty diacid)"),
    ("petrelintide", "albumin_binding", "USES", "emerging", "§4.2 (acylated; exact chain/% undisclosed)"),
    ("pramlintide", "proteolysis", "METABOLIZED_BY", "established", "§4.2 (renal proteolysis)"),
    ("pramlintide", "renal_clearance", "CLEARED_BY", "established", "§4.2"),
    ("pramlintide", "ide", "METABOLIZED_BY", "unverified", "§4.2 (IDE degrades amylin; synthetic-agonist proteases undisclosed)"),
    ("amylin", "ide", "METABOLIZED_BY", "established", "§4.2 (IDE degrades amylin)"),
    ("amylin", "neprilysin", "METABOLIZED_BY", "unverified", "§4.2 (no direct evidence NEP degrades amylin)"),
    ("amylin", "renal_clearance", "CLEARED_BY", "established", "§1.1"),
    ("cagrilintide", "proteolysis", "METABOLIZED_BY", "emerging", "§4.2 (inferred fragments + renal clearance; proportions undisclosed)"),
    ("cagrilintide", "renal_clearance", "CLEARED_BY", "emerging", "§4.2 (inferred)"),
    ("eloralintide", "proteolysis", "METABOLIZED_BY", "emerging", "§4.2 (inferred)"),
    ("petrelintide", "proteolysis", "METABOLIZED_BY", "emerging", "§4.2 (inferred)"),
    ("amylin", "ap", "ACTS_ON", "established", "§2.1"),
    ("pramlintide", "ap", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("cagrilintide", "ap", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("eloralintide", "ap", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("petrelintide", "ap", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("amylin", "ap_access", "REACHES_VIA", "established", "§4.2 (fenestrated CVO capillaries)"),
    ("pramlintide", "ap_access", "REACHES_VIA", "established", "§4.2"),
    ("cagrilintide", "ap_access", "REACHES_VIA", "established", "§4.2"),
    ("eloralintide", "ap_access", "REACHES_VIA", "established", "§4.2"),
    ("petrelintide", "ap_access", "REACHES_VIA", "established", "§4.2"),
    ("amylin", "bbb_crossing", "CROSSES", "emerging", "§4.2 (rat radiolabeled evidence only)"),
    ("pramlintide", "bbb_crossing", "CROSSES", "unverified", "§4.2 (no human CSF data)"),
    ("cagrilintide", "bbb_crossing", "CROSSES", "unverified", "§4.2 (no human CSF data)"),
    ("eloralintide", "bbb_crossing", "CROSSES", "unverified", "§4.2 (no human CSF data)"),
    ("petrelintide", "bbb_crossing", "CROSSES", "unverified", "§4.2 (no human CSF data)"),
    ("pramlintide", "ap_nts_lpbn", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("cagrilintide", "ap_nts_lpbn", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("eloralintide", "ap_nts_lpbn", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("petrelintide", "ap_nts_lpbn", "ACTS_ON", "established", "§2.1 + §4.2"),
    ("pramlintide", "gastric_emptying_pathway", "ACTS_ON", "established", "§2.2"),
    ("pramlintide", "glucagon_pathway", "ACTS_ON", "established", "§2.2"),
]

# ---------------- Validation + output ----------------
def main():
    ids = {n["id"] for n in NODES}
    assert len(ids) == len(NODES), "duplicate node ids"
    for s, t, rel, ev, ref in EDGES:
        assert s in ids, f"edge source missing: {s}"
        assert t in ids, f"edge target missing: {t}"
        assert ev in ("established", "emerging", "unverified"), f"bad evidence: {ev}"
    graph = {
        "nodes": NODES,
        "edges": [
            {"source": s, "target": t, "relation": rel, "evidence": ev, "source_ref": ref}
            for (s, t, rel, ev, ref) in EDGES
        ],
    }
    with open(os.path.join(HERE, "knowledge_graph.json"), "w") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    print(f"nodes={len(NODES)} edges={len(EDGES)}")

    # ---- index.html: single self-contained file, graph data embedded inline ----
    data_json = json.dumps(graph, ensure_ascii=False)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Amylin Agonist / Weight Loss Knowledge Graph</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  body { font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 0; }
  header { padding: 14px 18px 8px; }
  header h1 { margin: 0 0 4px; font-size: 20px; }
  header p { margin: 2px 0; color: #444; font-size: 13px; }
  #controls { display: flex; gap: 10px; flex-wrap: wrap; padding: 6px 18px 10px; align-items: center; }
  #controls input, #controls select { padding: 6px 8px; font-size: 14px; }
  #layout { display: flex; height: calc(100vh - 190px); min-height: 420px; }
  #graph { flex: 1; border-top: 1px solid #ddd; border-right: 1px solid #ddd; }
  #detail { width: 340px; padding: 12px 14px; overflow-y: auto; font-size: 13px; }
  #detail h3 { margin: 4px 0 6px; }
  .badge { display: inline-block; padding: 1px 7px; border-radius: 10px; font-size: 11px; color: #fff; }
  .established { background: #2e7d32; } .emerging { background: #ef6c00; } .unverified { background: #9e9e9e; }
  .edge-row { border-bottom: 1px solid #eee; padding: 5px 0; }
  #legend { padding: 6px 18px; font-size: 12px; color: #333; }
  .swatch { display: inline-block; width: 11px; height: 11px; border-radius: 50%; margin: 0 3px 0 10px; vertical-align: middle; }
</style>
</head>
<body>
<header>
  <h1>Amylin Agonist / Weight-Loss Knowledge Graph</h1>
  <p>Entities and relations extracted from the amylin agonist / weight-loss research report (compiled 2026-10-15 from public sources). Every edge carries an evidence flag: <b>established</b> (human + rodent consistent evidence), <b>emerging</b> (mostly rodent / emerging), <b>unverified</b> (no direct evidence or conflicting sources). Edge evidence flags are shown in the detail panel when a node is selected. The graph is a summary, not a substitute for the full report.</p>
</header>
<div id="controls">
  <input id="search" type="text" placeholder="Search a node (e.g. CagriSema, AP, AMY1)..." size="42">
  <button id="searchBtn">Highlight</button>
  <label>Filter by type:
    <select id="typeFilter"><option value="">All types</option></select>
  </label>
  <button id="resetBtn">Reset view</button>
  <span id="counts"></span>
</div>
<div id="legend"></div>
<div id="layout">
  <div id="graph"></div>
  <div id="detail"><p>Click a node to see its description and connected edges.</p></div>
</div>
<script>
const graphData = __DATA_JSON__;
const COLORS = {"Drug":"#e53935","Receptor":"#8e24aa","BrainRegion":"#3949ab","Organ":"#00897b","Tissue":"#7cb342","Effect":"#fb8c00","Process":"#5d4037","Pathway":"#d81b60","Molecule":"#1e88e5","Enzyme":"#00acc1"};
const nodes = new vis.DataSet(graphData.nodes.map(n => ({id: n.id, label: n.label, title: n.label, color: COLORS[n.type] || "#888", group: n.type, _meta: n})));
const edges = new vis.DataSet(graphData.edges.map((e, i) => ({id: i, from: e.source, to: e.target, label: e.relation, arrows: "to", color: e.evidence === "established" ? "#2e7d32" : e.evidence === "emerging" ? "#ef6c00" : "#9e9e9e", dashes: e.evidence === "unverified", _meta: e})));
const container = document.getElementById("graph");
const network = new vis.Network(container, {nodes, edges}, {physics: {stabilization: {iterations: 250}}, interaction: {hover: true}, nodes: {shape: "dot", size: 14, font: {size: 12}}, edges: {font: {size: 10, align: "middle"}}});
const byId = Object.fromEntries(graphData.nodes.map(n => [n.id, n]));
const labelById = id => byId[id] ? byId[id].label : id;
document.getElementById("counts").textContent = graphData.nodes.length + " nodes / " + graphData.edges.length + " edges";
const legend = document.getElementById("legend");
legend.innerHTML = Object.entries(COLORS).map(([t, c]) => '<span class="swatch" style="background:' + c + '"></span>' + t).join("");
const typeFilter = document.getElementById("typeFilter");
[...new Set(graphData.nodes.map(n => n.type))].sort().forEach(t => { const o = document.createElement("option"); o.value = t; o.textContent = t; typeFilter.appendChild(o); });
function showDetail(nodeId) {
  const n = byId[nodeId]; if (!n) return;
  const connected = graphData.edges.filter(e => e.source === nodeId || e.target === nodeId);
  let html = "<h3>" + n.label + "</h3><p><b>Type:</b> " + n.type + "</p><p>" + n.description + "</p><h4>Connected edges (" + connected.length + ")</h4>";
  connected.forEach(e => {
    const other = e.source === nodeId ? e.target : e.source;
    const dir = e.source === nodeId ? "&#8594;" : "&#8592;";
    html += '<div class="edge-row">' + dir + " <b>" + e.relation + "</b> " + labelById(other) + ' <span class="badge ' + e.evidence + '">' + e.evidence + "</span><br><small>Source: " + e.source_ref + "</small></div>";
  });
  document.getElementById("detail").innerHTML = html;
}
network.on("click", p => { if (p.nodes.length) showDetail(p.nodes[0]); });
function highlight(q) {
  const ql = q.trim().toLowerCase(); if (!ql) return;
  const found = graphData.nodes.find(n => n.label.toLowerCase().includes(ql) || n.id.toLowerCase().includes(ql));
  if (found) { network.selectNodes([found.id]); network.focus(found.id, {scale: 1.4}); showDetail(found.id); }
  else alert("No node matching: " + q);
}
document.getElementById("searchBtn").onclick = () => highlight(document.getElementById("search").value);
document.getElementById("search").addEventListener("keydown", e => { if (e.key === "Enter") highlight(e.target.value); });
typeFilter.onchange = () => {
  const t = typeFilter.value;
  nodes.forEach(n => nodes.update({id: n.id, hidden: !!(t && n.group !== t)}));
};
document.getElementById("resetBtn").onclick = () => { typeFilter.value = ""; nodes.forEach(n => nodes.update({id: n.id, hidden: false})); network.fit(); };
</script>
</body>
</html>
"""
    html = html.replace("__DATA_JSON__", data_json)
    with open(os.path.join(HERE, "index.html"), "w") as f:
        f.write(html)
    print("wrote knowledge_graph.json and index.html")


if __name__ == "__main__":
    main()
