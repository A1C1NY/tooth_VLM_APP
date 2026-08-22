# Identification of Cuproptosis-related Gene

Source: Chinese Journal of Dental Research (CJDR)

Identification of Cuproptosis-related Gene
Lipoyltransferase 1 as a Promising Biomarker in Oral
Squamous Cell Carcinoma
Kuang Min SHEN1, Yu Meng ZHOU2,3, Mu Chun LIANG3,4, De Mao ZHANG3,4, Qiang
WEI3, Yi Lin PING2
Objective: To find efficient cuproptosis-related biomarkers to explore the oncogenesis and progression of oral squamous cell carcinoma (OSCC).
database. Univariate Cox analysis and Kaplan-Meier survival analysis were used to identify
the gene related to survival. Tumor Immune Estimation Resource 2.0 (TIMER 2.0) was used to
reveal the different expression of cuproptosis-related gene lipoyltransferase 1 (LIPT1) in various
kinds of tumours.
Results: LIPT1, as a cuproptosis-related gene, was found to be differentially expressed in the
OSCC group and the control group. It was also found to be related to the prognosis of OSCC. Pan
cancer analysis showed LIPT1 was also involved in various kinds of tumours.
Conclusion: All the results demonstrate that the cuproptosis-related gene LIPT1 is highly
involved in the oncogenesis and progression of OSCC. These findings give new insight for further
research into the cuproptosis-related biomarkers in OSCC.
Keywords: biomarker, lipoyltransferase 1, oral squamous cell carcinoma
Oral squamous cell carcinoma (OSCC) is a malignant
tumour that has been associated with the oral microbiome.1 Among all oral malignant and premalignant
lesions, OSCC has the highest occurrence2, and the incidence rate increases with age.3 Despite advancements
in treatments, the 5-year survival rate for OSCC remains
relatively low at 64%.4 Thus, there is an urgent need to
discover new biomarkers to improve therapy for OSCC.
1 Tongde Hospital of Zhejiang Province, Hangzhou, P.R. China.
2 Liangzhu Street community Health Service center, Yuhang District,
Hangzhou, P.R. China.
3 State Key Laboratory of Oral Diseases, West China Hospital of
Stomatology, Sichuan University, Chengdu, P.R. China.
4   West China School of Basic Medical Sciences & Forensic Medicine,
Sichuan University, Chengdu, P.R. China.
Corresponding author: Dr Yi Lin PING, #159, Yucong Road, Liangzhu
Street, Yuhang District, Hangzhou, P.R. China. Tel: 86-13616719620. Email:
pylpyl2023@163.com
This work was supported by the National Natural Science Foundation of China
(no. 82001062), China Postdoctoral Science Foundation (2022M722249) and
Fundamental Research Funds for the Central Universities (2022SCU12029).
Chinese Journal of Dental Research
Recently, immune checkpoint inhibitors targeting
programmed cell death protein 1 (PD-1) and programmed death ligand 1 (PD-L1) have been utilised
in therapy; however, resistance to immunotherapy is
a frequently encountered issue.5 Therefore, exploring
alternative therapies such as ferroptosis and apoptosis
may provide new insights into enhancing the survival
and prognosis of OSCC patients.6-8 Cuproptosis, a distinct form of cell death, is triggered by the interaction
of copper with lipoylated components of the tricarboxylic acid cycles.9 However, the specific biomarkers
associated with cuproptosis in relation to OSCC remain
largely unknown. Thus, the present study aims to
explore a novel therapeutic approach for OSCC based
on cuproptosis. To achieve this, it is crucial to identify
key cuproptosis-related genes, which will further elucidate the underlying mechanisms of OSCC.
The present authors identified 10 cuproptosis-related genes based on the existing literature (Fig 1).9
Among these genes, lipoyltransferase 1 (LIPT1) exhibited lower expression levels in OSCC samples compared
to para-tumour samples. In addition, increased expression of LIPT1 was found to be associated with a poorer
Shen et al
Fig 1
prognosis among individuals diagnosed with OSCC.
Pan-cancer analysis was conducted to assess the role
of LIPT1 across various tumour types. A nomogram
incorporating clinicopathological characteristics was
developed to predict the 1-, 3- and 5-year overall survival of OSCC patients. To explore the potential mechanisms involving LIPT1, the authors performed an
analysis of genes associated with LIPT1. Additionally,
Gene Ontology (GO)10 and Kyoto Encyclopedia of Genes
and Genomes (KEGG)11 enrichment analyses were conducted. The present authors’ comprehensive research
efforts aim to identify a potential therapeutic target for
cuproptosis and provide insights into the prognosis and
therapy for OSCC.
Materials and methods
Data acquisition and preprocessing
RNA sequencing data were obtained from The Cancer Genome Atlas (TCGA) and Head and Neck Squamous Cell Carcinoma (HNSC) database (https://portal.
Study flowchart.
gdc.cancer.gov).12 The data were downloaded and the
expression values were converted into Log2 Fragments
Per Kilobase Million (FPKM) format. A total of 361 samples with clinical data were selected, excluding samples
from non-oral locations such as the hypopharynx, larynx, oropharynx and tonsils. Samples without clinical
data were excluded from the analysis.
Identification of cuproptosis-related genes and survival analysis
Ten cuproptosis-related genes, namely ferredoxin 1
(FDX1, Gene ID: 2230), lipoic acid synthetase (LIAS, Gene
ID: 11019), LIPT1 (Gene ID: 51601), dihydrolipoamide
dehydrogenase (DLD, Gene ID: 1738), dihydrolipoamide S-acetyltransferase (DLAT, Gene ID: 1737), pyruvate
dehydrogenase E1 subunit alpha 1 (PDHA1, Gene ID:
5160), pyruvate dehydrogenase E1 subunit beta (PDHB,
Gene ID: 5162), glutaminase (GLS, Gene ID: 2744), cyclin
dependent kinase inhibitor 2A (CDKN2A, Gene ID: 1029)
and metal regulatory transcription factor 1 (MTF1, ID:
4520), were analysed individually to determine the gene
that exhibited differential expression between the para-
Volume 27, Number 2, 2024
Shen et al
tumour group and tumour group samples. Univariate
Cox analysis and Kaplan-Meier survival analysis were
performed using R survival and survminer software (R
Core Team, Vienna, Austria) to identify genes associated with overall survival.13 The univariate Cox analysis
involved fitting a Cox proportional hazards model to the
gene expression data using the survival package in R.14
This model calculates hazard ratios and their associated
P values, providing a measure of the gene’s impact on
overall survival. For the Kaplan-Meier survival analysis,
the survminer package was used to estimate the probability of survival over time for different gene expression groups. Log-rank tests were performed to compare
the survival curves between these groups, determining
if there were significant differences in survival outcomes based on gene expression levels. These methods
were chosen for their ability to effectively assess the
association between gene expression and overall survival in this specific dataset, providing robust statistical
analysis for the present study.
Gene expression and clinical prognosis of LIPT1
Expression analysis and clinical characteristics
To assess the expression pattern of LIPT1 across different cancers, the present authors utilised TIMER 2.0
(Tumor Immune Estimation Resource 2.0, http://timer.
cistrome.org) to show the expression situation of LIPT1
in different cancers.15 A Wilcoxon rank-sum test and
Dunn test were employed to examine the differential
expression of LIPT1 in relation to clinicopathological
characteristics such as age, sex and histological grade.
These analyses were conducted using the R package
ggplot2.16 Additionally, a nomogram incorporating clinicopathological characteristics was developed using the
R packages rms and survival to predict the prognosis of
OSCC patients. Furthermore, univariate and multivariate Cox regression analyses were performed to demonstrate that LIPT1 serves as an independent factor for
assessing the overall survival of OSCC patients.
Correlation analysis of LIPT1 in OSCC
Pearson correlation analysis was conducted to evaluate
the correlation of LIPT1 with other genes, considering
a correlation coefficient with an absolute value greater
than 0.5 and a significance threshold of P < 0.05. The
correlation heatmap was generated using the R package
ggplot2.
Chinese Journal of Dental Research
Differential expression analysis and functional
enrichment analysis
To identify differentially expressed genes (DEGs), samples were divided into two groups based on the median
expression of LIPT1, and DEGs were determined using
the criteria |LogFC| > 2 and P < 0.05. Functional enrichment analyses, including GO and KEGG analysis, were
performed to elucidate the molecular mechanisms and
associated signalling pathways of the DEGs. These analyses were conducted using the R package clusterProfiler.17
Immune checkpoint and infiltration assay
To explore the relationship between LIPT1 and immune
cell infiltration, the present authors utilised the R package GSVA and conducted single-sample Gene Set Enrichment Analysis (ssGSEA). Spearman correlation analysis
was conducted to assess the relationship between LIPT1
and immune checkpoint genes, and a correlation heatmap was generated to visualise the results.
Results
Deregulation of LIPT1 in OSCC
In this study, a total of 361 RNA sequencing data samples, consisting of 329 tumour and 32 paratumour samples, were obtained from the TCGA database. Among
the ten cuproptosis-related genes analysed, FDX1, LIAS,
LIPT1, DLD, DLAT, PDHA1 and PDHB showed higher
expression in the paratumour group, whereas GLS and
CDKN2A exhibited lower expression in the paratumour
group. The gene MTF1 did not show significant differential expression between the tumour and paratumour
groups.
Based on univariate Cox analysis (Fig 2a, P < 0.05),
we identified LIPT1, DLD, and CDKN2A as prognostic genes among the differentially expressed genes.
Subsequently, K-M analysis revealed that LIPT1 was
specifically associated with overall survival and was
selected for further analysis (Fig 2b, P < 0.05). Moreover,
it has been reported that LIPT1 is involved in various
other tumorigenesis, including liver hepatocellular
carcinoma, melanoma and prostate cancer.18-20 The
area under the curves (AUCs) for LIPT1 in relation to
overall survival was calculated as 0.550, 0.631 and 0.635
at 1, 3 and 5 years, respectively (Fig 2c).21 Moreover,
the authors observed a decrease in the expression level
Shen et al
Fig 2 Identification of
prognostic genes associated with cuproptosis
in OSCC. Univariate Cox
regression analysis results
presented in a forest plot
(a). Kaplan-Meier survival
curves illustrating overall
survival in OSCC patients
based on LIPT1 tumour
expression (b). Timedependent receiver operating characteristic curves
showcasing the predictive
value of LIPT1 for overall
survival at 1, 3 and 5 years
(c). Expression of LIPT1
was found to be lower in
OSCC samples compared
to normal samples (d).
of LIPT1 in the tumour group compared to the paratumour group (Fig 2d).
Pan-cancer expression analysis of LIPT1
A pan-cancer expression analysis of LIPT1 was performed (Fig 3, P < 0.05). In CHOL, COAD, ESCA, GBM,
LIHC and STAD, LIPT1 demonstrated elevated expression in the tumor group when compared to the normal
group. Conversely, in BRCA, CESC, KICH, KIRC, KIRP,
THCA and UCEC, LIPT1 exhibited decreased expression in the tumor group compared to the normal group.
Additionally, LIPT1 expression was higher in the HNSCHPV+ group compared to the HNSC-HPV- group, as well
as in the SKCM metastasis group compared to the SKCM
group.
Differential expression of LIPT1 in clinicopathological characteristics of OSCC and predictive nomogram
Significantly higher expression of LIPT1 was observed
in the male group compared to the female group (Fig 4a,
P < 0.05). In terms of histological grade, LIPT1 exhibited
higher expression in grades 3 and 4 compared to grade
1, and higher expression in grades 3 and 4 compared to
grade 2 (Fig 4b, P < 0.05). A prognostic nomogram was
constructed based on clinicopathological characteris-
tics including age, sex, race, smoking history, T stage,
alcohol history, histological grade, N stage and LIPT1
expression (Fig 4c). The calibration curves demonstrated that the model fit well with the optimal one, reflecting 1-, 3- and 5-year overall survival (Fig 4d). Table 1
was utilised to conduct univariate and multivariate Cox
regression analyses, aiming to determine whether clinicopathological characteristics could act as independent
predictors. The results indicated that LIPT1 expression
was an independent predictor associated with overall
survival.
Genes correlated with LIPT1 and differentially
expressed genes in OSCC
Using a Pearson correlation analysis, we identified
300 genes that exhibited a correlation coefficient > 0.5
and a significant P value (< 0.05) with LIPT1 (Table S1).
The top 9 genes showing the strongest correlation with
LIPT1 were selected to generate a correlation heatmap
(Fig 5a). Furthermore, the authors identified 141 genes
that showed differential expression between the LIPT1
high expression group and the low expression group,
meeting the criteria of |log2FoldChange| > 2 and P < 0.05
(data provided on request). Out of these genes, 8 were
found to be downregulated whereas 132 were upregulated in the LIPT1 high expression group. GO analysis
Volume 27, Number 2, 2024
Shen et al
highlighted GO:0001523 (retinoid metabolic process)
as the most significantly associated biological process
for these genes (Fig 5b). Furthermore, KEGG analysis
indicated that the most important pathway involved was
hsa00830 (retinol metabolism) (Fig 5c).
Immune cell infiltration and immune checkpoint
genes
Using ssGSEA, the relationship between LIPT1 and
immune cells was analysed (Fig 6a). It was observed that
dendritic cells (DCs), immature DCs (iDCs), mast cells,
neutrophils, NK CD56dim cells, central memory T cells
(Tcm), Th1 cells, regulatory T cells (Tregs) and eosinophils showed a negative correlation with LIPT1. Conversely, NK CD56bright cells and T helper cells exhibited
a positive correlation with LIPT1. Furthermore, the correlation between LIPT1 and immune checkpoint genes
was explored, and the results were presented in a correlation heatmap (Fig 6b). LIPT1 showed a positive correlation with TNFRSF25, TNFSF15, TNFSF4, TNFRSF18,
TNFRSF4, CD200R1, CTLA4 and TNFRSF14, and a negative correlation with PDCDILG2 (P < 0.05).
Discussion
Fig 3 Pan-cancer expression analysis of LIPT1 in normal
and tumour samples according to TIMER 2.0. BLCA, bladder
urothelial carcinoma; BRCA, breast invasive carcinoma; CESC,
cervical squamous cell carcinoma and endocervical adenocarcinoma; CHOL, cholangiocarcinoma; ESCA, oesophageal
carcinoma; GBM, glioblastoma multiforme; HNSC, head and
neck squamous cell carcinoma; KIRC, kidney renal clear cell
carcinoma; KIRP, kidney renal papillary cell carcinoma; LUSC,
lung squamous cell carcinoma; PCPG, pheochromocytoma
and paraganglioma; PRAD, prostate adenocarcinoma; STAD,
stomach adenocarcinoma; THCA, thyroid carcinoma; UCEC,
uterine corpus endometrial carcinoma (*P < 0.05, **P < 0.01,
Chinese Journal of Dental Research
LIPT1, a pro-cuproptosis gene, is responsible for lipoate
transfer and is typically considered downstream of
LIPT2.22 LIPT1 deficiency can manifest as early infantile
epileptic encephalopathy, Leigh disease and secondary
pyruvate dehydrogenase complex deficiency.23 LIPT1
also plays a crucial role in the transfer of the lipoyl group
from the H-protein of the glycine cleavage system to the
E2 subunits of mitochondrial 2-ketoacid dehydrogenase
complexes. This process is essential for the proper functioning of these complexes, which are involved in key
metabolic pathways such as the tricarboxylic acid (TCA)
cycle.24 Dysfunction of LIPT1 may lead to alterations
in TCA cycle metabolism.25,26 Despite advancements in
various treatment modalities, the prognosis for OSCC
patients remains poor.27-29 Cuproptosis has shown potential in overcoming resistance that may arise during
chemotherapy treatment of malignant cells; however,
the mechanisms underlying cuproptosis, particularly
in the context of OSCC, are still largely unknown. Thus,
the present authors’ research aims to explore potential
prognostic biomarkers associated with cuproptosis in
OSCC.
A study integrated genomics and metabolomics to
identify the cause of lactic acidosis and epilepsy, and
revealed that LIPT1 mutations lead to metabolic defects
and broader aspects of inborn errors of metabolism
Shen et al
Fig 4 Correlation
between LIPT1 and clinical
characteristics. Sex distribution in the high and low
LIPT1 expression groups
(a). Histological grade distribution in the high and low
LIPT1 expression groups.
G1-4, histologic grade 1-4,
based on clinical characteristics (b). Nomogram
for predicting overall survival, incorporating age,
sex, race, smoking history,
T stage, alcohol history,
histological grade, N stage
and LIPT1 expression as
parameters (c). Calibration
curves of the nomogram
for predicting 1-, 3-, 5- and
10-year overall survival (d).
Table 1
Univariate and multivariate Cox regression analysis of clinical characteristics for overall survival prediction.
Characteristics
Univariate analysis
Multivariate analysis
Hazard ratio (95% CI)
P value
Hazard ratio (95% CI)
P value
Age
Sex
Race
Smoking
T stage
Alcohol history
Histological grade
N stage
LIPT1
NA
NA
NA
NA
NA
NA
NA
NA
NA
NA
NA, not available.
(IEM) pathophysiology.25 LIPT1 is an essential enzyme
for the activation of mitochondrial 2-ketoacid dehydrogenase, which is involved in fatty acylation. LIPT1
deficiency leads to impaired lipoylation and activity of
2-ketoacid dehydrogenase, resulting in increased 2-HG
and depletion of structural lipids in plasma. While
LIPT1 deficiency impedes lipogenesis, it increases
fatty acid oxidation and regulates the balance between oxidative and reductive glutamine metabolism.25
Pathogenic variants in the LIPT1 gene have been linked
to severe lactic acidosis and poor neurocognitive outcomes, leading to neonatal death. A study presented the
Volume 27, Number 2, 2024
Shen et al
Fig 5 Identification of related genes, pathways and cellular functions of LIPT1. Heatmap showing the correlation of LIPT1 with
9 genes in OSCC samples (a). GO analysis results: GO:0001523 (retinoid metabolic process), GO:0072562 (blood microparticle),
GO:0048018 (receptor ligand activity) (b). KEGG enrichment analysis results: hsa00830 (retinol metabolism), hsa00982 (drug
metabolism - cytochrome P450), hsa00980 (metabolism of xenobiotics by cytochrome P450), hsa05204 (chemical carcinogenesis),
hsa05150 (Staphylococcus aureus infection), hsa00053 (ascorbate and aldarate metabolism), hsa00983 (drug metabolism – other
enzymes), hsa00040 (pentose and glucuronate interconversions), hsa04080 (neuroactive ligand-receptor interaction), hsa04610
(complement and coagulation cascades) (c).
case of a 2-month-old boy with LIPT1 deficiency and its
progression to early infantile epileptic encephalopathy,
highlighting the need for exome sequencing to diagnose LIPT1 deficiency and its overlap with other metabolic disorders.23 LIPT1 has been identified as a novel
prognostic target in liver hepatocellular carcinoma and
skin cutaneous melanoma.19,20 In the present study, it
was also identified as a prognosis-related cuproptosis
gene. The expression of LIPT1 was significantly lower
in the OSCC group compared to the paratumour group.
However, during the prognostic analysis, the authors
discovered that lower expression of LIPT1 correlated
with a better prognosis. Cuproptosis may exhibit different effects in distinct situations. On one hand, the
upregulation of LIPT1 in the paratumour group suggests that an LIPT1 deficiency might reduce cuprop-
Chinese Journal of Dental Research
tosis, which plays a role in targeting tumour cell death
in OSCC initiation. On the other hand, as the tumour
progresses over time, the expression of LIPT1 increases, but the prognosis of OSCC patients worsens. This
finding aligns with the observations made by Chen30 in
uterine corpus endometrial carcinoma. Furthermore,
in pan-cancer analysis, LIPT1 was found to be downregulated in BRCA, CESC, KICH, KIRC, KIRP and THCA,
indicating that LIPT1, as a pro-cuproptosis gene, may
contribute to molecular mechanisms underlying cancer initiation and progression. However, the specific
mechanisms by which LIPT1 affects the occurrence
and progression of OSCC remain unknown.
The findings from the GO and KEGG analyses demonstrated that the DEGs were predominantly linked
to metabolic processes, aligning with the observa-
Shen et al
Fig 6 Correlation between LIPT1 and immune infiltration. Lollipop graph depicting the correlation between LIPT1 expression and
immune infiltration, as determined by ssGSEA (a). Correlation between LIPT1 and immune checkpoint-related genes (b).
tions made by Zheng et al31. Their study revealed that
cuproptosis can hinder cancer progression by targeting
mitochondrial metabolism.31 This consistency further
supports the present authors’ observations. In cancer
patients, the tumour microenvironment plays a crucial role in influencing therapy response and clinical
outcomes.32 In the immune cell infiltration analysis,
the present authors found a positive correlation between LIPT1 and certain immune cells, including Tregs
and neutrophils. Lv et al19 also reported higher levels
of regulatory Tregs and neutrophils in the LIPT1 low
expression group in melanoma; however, Jiang et al33
found a positive correlation between neutrophils and
LIPT1 expression in breast cancer. Moreover, mutations in the patient’s LIPT1 gene result in a fatal disease
characterised by a specific lipoylation defect of the
2-ketoacid dehydrogenase complexes. This patient presented with early onset fatal lactic acidosis and a combined defect of pyruvate dehydrogenase and 2-ketoglutarate dehydrogenase activities, indicating a deficiency
in lipoic acid metabolism. Immunostaining analysis
revealed reduced lipoylated E2-PDH and E2-KGDH,
suggesting a defect in lipoic acid transfer to specific
proteins. Sequence analysis identified two heterozygous missense mutations in LIPT1, which were shown
to be disease-causing and essential for the activation of
2-ketoacid dehydrogenases in humans.34
However, there are certain limitations to consider.
Firstly, all the data used in this study were obtained
from public databases, and further validation is necessary. Additionally, the 1-year AUC value for overall
survival prediction was below 0.6, despite good fit in
the calibration curves of the nomogram. Furthermore,
DLD and CDKN2A were both found to be associated
with overall survival, indicating the potential for developing a prognostic model incorporating these genes
and other clinical characteristics in the future.
Conclusion
This study identified LIPT1 as a novel potential molecular biomarker associated with cuproptosis in OSCC.
Acknowledgements
The authors would like to express their gratitude to Dr
Mi Su from the Functional Laboratory at the West China
School of Basic Medical Sciences & Forensic Medicine
for the technical support for this study.
Conflicts of interest
The authors declare no conflicts of interest related to
this study.
Author contribution
Dr Kuang Min SHEN contributed to the study design,
methodology and manuscript draft; Dr Yu Meng ZHOU
contributed to the analysis and manuscript draft; Dr
Mu Chun LIANG contributed to the data analysis; Dr
De Mao ZHANG contributed to the supervision, review
Volume 27, Number 2, 2024
Shen et al
and editing of the manuscript; Dr Qiang WEI contributed to conception, methodology and supervision; Dr Yi
Lin PING contributed to conception, methodology and
administration. All authors approved the final version
of the manuscript.
(Received Aug 25, 2023; accepted Feb 02, 2024)
References
Irfan M, Delgado RZR, Frias-Lopez J. The oral microbiome
and cancer. Front Immunol 2020;11:591088.
de Menezes SAF, Miranda YMS, da Silva YM, et al. Prevalence
and genotyping of HPV in oral squamous cell carcinoma in
Northern Brazil. Pathogens 2022;11:1106.
Ghazawi FM, Lu J, Savin E, et al. Epidemiology and patient
distribution of oral cavity and oropharyngeal SCC in Canada.
Bai XX, Zhang J, Wei L. Analysis of primary oral and oropharyngeal squamous cell carcinoma in inhabitants of Beijing, China-A 10-year continuous single-center study. BMC
Moskovitz J, Moy J, Ferris RL. Immunotherapy for head and
neck squamous cell carcinoma. Curr Oncol Rep 2018;20:22.
Gu W, Kim M, Wang L, Yang Z, Nakajima T, Tsushima Y. Multiomics analysis of ferroptosis regulation patterns and characterization of tumor microenvironment in patients with oral
squamous cell carcinoma. Int J Biol Sci 2021;17:3476–3492.
Yang YT, Hsieh MJ, Chuang YC, et al. Anticancer effects of picrasidine I on oral squamous cell carcinoma. Environ Toxicol
Zhu W, Ye Z, Chen L, Liang H, Cai Q. A pyroptosis-related
lncRNA signature predicts prognosis and immune microenvironment in head and neck squamous cell carcinoma. Int
Immunopharmacol 2021;101(Pt B):108268.
Tsvetkov P, Coy S, Petrova B, et al. Copper induces cell
death by targeting lipoylated TCA cycle proteins. Science
Gene Ontology Consortium. Gene Ontology Consortium: Going forward. Nucleic Acids Res 2015;43(Database
Kanehisa M, Goto S. KEGG: Kyoto encyclopedia of genes and
genomes. Nucleic Acids Res 2000;28:27–30.
Wang Z, Jensen MA, Zenklusen JC. A practical guide to
The Cancer Genome Atlas (TCGA). Methods Mol Biol
Ranstam J, Cook JA. Kaplan-Meier curve. Br J Surg 2017;104:
Emura T, Matsui S, Chen HY. Compound.Cox: Univariate feature selection and compound covariate for predicting survival. Comput Methods Programs Biomed 2019;168:21–37.
Li T, Fu J, Zeng Z, et al. TIMER2.0 for analysis of tumorinfiltrating immune cells. Nucleic Acids Res 2020;48(W1):
Chinese Journal of Dental Research
16. Ito K, Murphy D. Application of ggplot2 to pharmacometric
graphics. CPT Pharmacometrics Syst Pharmacol 2013;2:e79.
17. Wu T, Hu E, Xu S, et al. clusterProfiler 4.0: A universal enrichment tool for interpreting omics data. Innovation (Camb)
18. Cheng B, Tang C, Xie J, et al. Cuproptosis illustrates tumor
micro-environment features and predicts prostate cancer
therapeutic sensitivity and prognosis. Life Sci 2023;325:121659.
19. Lv H, Liu X, Zeng X, et al. Comprehensive analysis of cuproptosis-related genes in immune infiltration and prognosis in
melanoma. Front Pharmacol 2022;13:930041.
20. Yan C, Niu Y, Ma L, Tian L, Ma J. System analysis based on the
cuproptosis-related genes identifies LIPT1 as a novel therapy target for liver hepatocellular carcinoma. J Transl Med
21. Park SH, Goo JM, Jo CH. Receiver operating characteristic
(ROC) curve: Practical review for radiologists. Korean J Radiol
22. Mayr JA, Feichtinger RG, Tort F, Ribes A, Sperl W. Lipoic acid
biosynthesis defects. J Inherit Metab Dis 2014;37:553-563.
23. Stowe RC, Sun Q, Elsea SH, Scaglia F. LIPT1 deficiency presenting as early infantile epileptic encephalopathy, Leigh disease, and secondary pyruvate dehydrogenase complex deficiency. Am J Med Genet A 2018;176:1184–1189.
24. Solmonson A, DeBerardinis RJ. Lipoic acid metabolism and
mitochondrial redox regulation. J Biol Chem 2018;293:7522–
25. Ni M, Solmonson A, Pan C, et al. Functional assessment of
lipoyltransferase-1 deficiency in cells, mice, and humans. Cell
26. Solmonson A, Faubert B, Gu W, et al. Compartmentalized
metabolism supports midgestation mammalian development. Nature 2022;604:349–353.
27. Zanoni DK, Montero PH, Migliacci JC, et al. Survival outcomes
after treatment of cancer of the oral cavity (1985-2015). Oral
28. Garzino-Demo P, Zavattero E, Franco P, et al. Parameters and
outcomes in 525 patients operated on for oral squamous cell
carcinoma. J Craniomaxillofac Surg 2016;44:1414–1421.
29. Wang B, Zhang S, Yue K, Wang XD. The recurrence and survival of oral squamous cell carcinoma: A report of 275 cases.
30. Chen Y. Identification and validation of cuproptosis-related
prognostic signature and associated regulatory axis in uterine
corpus endometrial carcinoma. Front Genet 2022;13:912037.
31. Zheng P, Zhou C, Lu L, Liu B, Ding Y. Elesclomol: A copper
ionophore targeting mitochondrial metabolism for cancer
therapy. J Exp Clin Cancer Res 2022;41:271.
32. Wu T, Dai Y. Tumor microenvironment and therapeutic response. Cancer Lett 2017;387:61–68.
33. Jiang B, Zhu H, Feng W, et al. Database mining detected a
cuproptosis-related prognostic signature and a related regulatory axis in breast cancer. Dis Markers 2022;2022:9004830.
34. Tort F, Ferrer-Cortès X, Thió M, et al. Mutations in the lipoyltransferase LIPT1 gene cause a fatal disease associated with
a specific lipoylation defect of the 2-ketoacid dehydrogenase
complexes. Hum Mol Genet 2014;23:1907–1915.
