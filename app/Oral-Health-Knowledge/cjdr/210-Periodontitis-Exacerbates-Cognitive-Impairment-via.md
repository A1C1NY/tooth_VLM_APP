# Periodontitis Exacerbates Cognitive Impairment via

Source: Chinese Journal of Dental Research (CJDR)

Periodontitis Exacerbates Cognitive Impairment via
Endothelial Inflammation: Insights from Single-Nucleus
Transcriptomics
Zong Shan SHEN1,#, Ji Chen YANG1,#, Chuan Jiang ZHAO1, Bin CHENG1
Objective: To explore the underlying mechanisms of the association between periodontitis and
cognitive impairment.
Methods: Single-nucleus transcriptomics of mice were used to investigate the impact of periodontitis on brain and hippocampal cells to gain insights into disease progression. After data
processing, functional enrichment, pathway analysis and cell-cell communication analysis
linked to periodontitis. After cell culture, real-time quantitative polymerase chain reaction
ȃǻ,Ȅ
Results: The present authors identified endothelial inflammation as a key factor in periodon/$/$.ǻ- '
cells was linked to increased antigen presentation and exacerbated neuroinflammation, poten/$
# 
(pal endothelial inflammation and antigen presentation in cognitive impairment. This research
will enhance the understanding of how periodontitis impacts cognition and explore potential
therapeutic strategies to alleviate periodontitis-associated cognitive impairment.
Keywords:
nucleus transcriptomics
ƶƲƶưƵƷƷ
Periodontitis is an inflammatory disease caused by
plaque microbiota and results in the degradation of
tooth-supporting tissues, which in turn leads to tooth
mobility and loss. It has also been reported to be closely
#
1 Hospital of Stomatology, Guangdong Provincial Key Laboratory of
Stomatology, Guanghua School of Stomatology, Sun Yat-sen University,
Guangzhou, P.R. China
# These two authors contributed equally to this work.
Corresponding author: Dr Bin CHENG, Hospital of Stomatology, Guangdong
Provincial Key Laboratory of Stomatology, Guanghua School of Stomatology,
Sun Yat-Sen University, No. 56, Lingyuan West Road, Guangzhou 510055, P.R.
China. Tel: 86-20-83863002. Email: chengbin@mail.sysu.edu.cn
This work was supported by the National Natural Science Foundation of
China (grant no. 82201011) and Young Elite Scientist Sponsorship Program
by CAST (grant no. 2024QNRC001).
Chinese Journal of Dental Research
disease (AD) through pathogenic microorganisms and
inflammation in both mice and humans.1,2 Cognitive
disorders mainly occur in individuals who are aged over
60 years, with an incidence rate of up to 10%.3 As the
population ages worldwide, the prevalence of these diseases is expected to increase. Currently, effective treatment strategies for both periodontitis and cognitive disorders are lacking. Thus, investigating the mechanisms
through which periodontitis influences the development of cognitive disorders and identifying preventive
measures could mitigate the risk they pose.
Recent studies have revealed a strong correlation
between periodontitis and AD. Individuals with higher
levels of periodontitis exhibit faster hippocampal atrophy and cognitive deterioration.4 Periodontitis can
facilitate the infiltration of pathogenic bacteria, virulence factors and inflammatory mediators into the
Shen et al
brain via the blood-brain barrier (BBB).5-7 These substances then change the brain microenvironment,
triggering neuroinflammation and neurodegeneration,
ultimately leading to cognitive decline. The present
impairs macrophage function and promotes reactions
of hippocampal cells to virulence factors and bacteria,
inducing astrocyte abnormalities and neuroinflammation.8 Nevertheless, the precise mechanisms by which
factors damage the BBB and change the microenvironment in the hippocampus require further research.
The brain microvasculature has been proven to be a
key player in the development of AD. Previous studies
have shown vascular disruption in early AD development.9,10 Endothelial cells (ECs) are crucial for cleaning
the central nervous system, whereas inflammation in
ǚ11 Furthermore, ECs can
secrete cytokines and directly activate dysfunction of
surrounding neurons, astrocytes and microglia, leading
to neuroinflammation and cognitive impairment.12-14
However, the precise mechanisms underlying damage
to the brain endothelium from initial contact with periodontitis pathogens and toxins remain unclear.
Single-nucleus transcriptomics enables the examination of cellular changes, shedding light on the
mechanisms by which periodontitis impacts cognitive
function. In the present study, the authors generated
single-nucleus maps of the brain and hippocampus,
delineating key cell populations in these regions, and
revealed that periodontitis upregulates genes in hippocampal ECs linked to AD and suppresses neurogenesis. Specifically, periodontitis induces the upregulation
of monoacylglycerol lipase (MGLL) expression in ECs,
leading to neuroinflammation. The authors demonstrated that increasing antigen presentation through
MGLL-related pathways in ECs while inhibiting MGLL
expression improved periodontitis-induced endothelial dysfunction. This research not only elucidates the
pathogenesis of cognitive dysfunction associated with
periodontitis but also lays the groundwork for targeted
therapeutic interventions for cognitive impairment.
Materials and methods
The methods used were described in a previous study
by the present authors.8 In brief, male C57BL/6 mice for
sequencing were purchased from the National Resource
Center of Model Mice (Nanjing, China) and housed in a
specific pathogen-free facility at the Laboratory Animal
Center of Sun Yat-sen University. The 12-month-old mice
were separated into two groups (n = 6 in each group): the
healthy group (Heal), which acted as a control, and the
periodontitis group (PD). Ligature-induced periodontitis
models were generated in PD group mice. After 6 weeks,
they were euthanised by CO2 inhalation for brain and
hippocampus collection. All experiments were approved
by the Animal Care and Use Committee of Sun Yat-sen
University (SYSU-IACUC-2018-109 000135).
Single-nucleus RNA sequencing (snRNA-seq) was
performed by the DNBelab C Series High-Throughput
Single-Cell System from MGI (Shenzhen, China) and
pre-processed by STAR (v2.5.3). The data were uploaded
to the National Genomics Data Center (NGDC).
The present authors used the Seurat (v5.1.0) package
of R (v4.4.0) for subsequent processing.15 We selected
cells that contained between 500 and 4,000 genes and
had less than 10% mitochondrial DNA and normalised
the data with the -
).!*-( function (Fig S1, provided
on request). After data integration and principal component analysis (PCA), we removed batch effects from
the data with the 0)
-(*)4 function of the Harmony
(v1.2.0) package16 and used uniform manifold approximation and projection (UMAP) for dimensionality reduction in the PCA embeddings. Then, we annotated
cell clusters based on marker genes identified by the
-& -. function (Fig S2, provided on request)
and mentioned in previous studies.8,17-20
Functional enrichment, pathway analysis
and scoring
Differentially expressed genes (DEGs) were identified
-& -. Seurat function with a Wilcoxon
test ( < 0.05). DEGs in the brain and hippocampal ECs
between the PD group and Heal group were selected
with a minimum expression ratio of 0.2 and an average
log fold change (avg logFC) of positive number. DEGs
of hippocampal ECs with high "'' expression (expression > 0) were selected with a minimum average log fold
change (avg logFC) of 3 or a maximum average log fold
pathway analyses were performed using Metascape
(https://www.metascape.org) based on the selected
DEGs to identify enriched functional terms.21 Then, we
integrated the results and visualised them in R with the
Treemapify (v2.5.6) package. We chose visualised terms
with the 10 highest counts. In addition, we calculated
Volume 28, Number 2, 2025
Shen et al
module scores of significant functional terms with the
*- Seurat function.
The optical density (OD) at 450 nm was detected using a
microplate reader (BioTek, Winooski, VT, USA).
Statistical analysis
We analysed cell-cell communication with the CellPhoneDB (v5.0.0) package in Python (v3.12.0),22 then integrated the results and visualised them in R with Ggalluvial (v0.12.5). We chose visualised receptors with the five
highest significant means and corresponding ligands.
Statistical analyses of the snRNA-seq data were performed in R with default parameters. A Wilcoxon test
was employed to compare differences of "'' expression, and an unpaired Student t test was used to compare
differences of module score in violin plots. Differences
with  < 0.05 were considered to indicate statistical significance. Statistical analyses of the cellular experiments were performed in GraphPad Prism (v10.1.2; Dotmatics, Boston, MA, USA) and are presented as means
± standard errors of the means (SEMs). A one-way analysis of variance (ANOVA) followed by a Tukey multiple
comparisons test was used for multiple comparisons.
Differences with  < 0.05 were considered to indicate
statistical significance.
0'/0The immortalised human cerebral microvascular
endothelial cell line (HCMEC/D3) and human umbilical vein endothelial cell line (PUMC-HUVEC-T1) were
purchased from Pricella (Wuhan, China) and cultured
in complete culture medium for ECs from Pricella in a
37°C humidified incubator with 5% CO2. The cells were
expanded through three passages and seeded in 6-well
culture plates with 1,000,000 cells per well.
Lipopolysaccharide (LPS) from *-+#4-*(*)
."$)"$valis was purchased from Sigma-Aldrich (St Louis, MO,
USA) and stored as a 1 mg/ml stock solution in HBSS at
with healthy, 200ng/ml LPS, or 200ng/ml LPS + 10μM
ȃǻ,Ȅ
Total RNA was collected using an RNA quick extraction
kit from GOONIE (Guangzhou, China) according to the
cDNA was obtained with a PrimeScript RT reagent kit
(Takara, Kusatsu, Japan) according to the manufactur-Ǩ.$)./-0
Taq Pro Universal SYBR qPCR Master Mix (Vazyme, Nanjing, China) and a QuantStudio 7 Flex Real-Time PCR
System (Thermo Fisher Scientific, Waltham, MA, USA)
were synthesised by Tsingke Biotech (Beijing, China),
and the sequences are listed in the supplemental information (Table S1, provided on request).
4ȃ Ȅ
Results
atlases of mouse brains and hippocampi
To investigate disorders in the brain and hippocampus
caused by periodontitis, the present authors obtained
single-nucleus transcriptomic data from the brains and
hippocampi of healthy mice and those with experimental periodontitis (Fig 1a). We successfully constructed
the cell atlases of the brain (Fig 1b and c) and hippocampi (Fig 1d and e) of mice with periodontitis. The
present study identified cells as eight clusters according to known markers, including inhibitory neurons (In)
Ʋ+), excitatory neurons (Ex) ('
ƱƷ
++), oligodendrocytes
++, *"+), oligodendrocyte progenitor cells
and endothelial cells (ECs) ('/Ʊ+, #Ƶ+). The present
authors also revealed that the proportions of inhibitory
neurons, microglia and ECs were decreased in both the
brain and hippocampus, that of excitatory neurons and
astrocytes was increased, and that of the entire neural population was slightly decreased (Fig 1f and g).
This finding suggests that periodontitis can affect the
brain and hippocampus in a similar pattern. The atlases
formed the basis of the subsequent analyses.
conducted with an ELISA Kit (MEIMIAN, Yancheng,
Ǻ
Chinese Journal of Dental Research
Shen et al
*MKŷEXSKŴŴ8LIWMRKPIRYGPIYW
XVERWGVMTXSQMG EXPEWIW SJ XLI
QSYWI FVEMR ERH LMTTSGEQ
TYW 3ZIVZMI[ SJ XLI TVSGIWW
MRK SJ WR62%WIU HEXE E ;
91%4 WLS[MRK GIPP GPYWXIVW MR
XLI FVEMR F  HSX TPSXW WLS[
MRK QEVOIV KIRIW SJ IZIV]
GPYWXIV MR XLI FVEMR G  91%4
WLS[MRK GIPP TVSTSVXMSRW MR
XLILMTTSGEQTYW H HSXTPSXW
WLS[MRKQEVOIVKIRIWSJIZIV]
GPYWXIVMRXLILMTTSGEQTYW I ;
TVSTSVXMSRW SJ HMJJIVIRX GIPP
X]TIW MR XLI FVEMR J  ERH XLI
LMTTSGEQTYW K 
#
neighbouring cells in the hippocampal area
To explore the initiating mechanism of cognitive disorders in the hippocampus, the present authors compared
the functions of activated ECs in both the brain and hippocampus of mice with periodontitis through functional
enrichment and pathway analysis (Fig 2a and b). ECs
form the BBB as the first line of defence with pericytes
and fibroblasts in every area of the brain.23 The present
research revealed that ECs in the hippocampus have different gene expression patterns and functions from those
in other areas of the brain when affected by periodontitis. The upregulated genes in ECs of the hippocampus
Ǻǚ
The present study suggests that ECs in the hippocampus
may initiate the development of periodontitis-induced
AD.
Volume 28, Number 2, 2025
Shen et al
*MKŷE XS JŴŴ'LERKIW MR XLI
JYRGXMSRSJFVEMRERHLMTTSGEQ
TEP)'WERHGSQQYRMGEXMSRFI
X[IIRXLI)'WERHRIMKLFSYVMRK
GIPPW MR XLI LMTTSGEQTEP EVIE
8VII QETW WLS[MRK JYRGXMSREP
EREP]WIWSJYTVIKYPEXIHKIRIW
MR XLI FVEMR ERH LMTTSGEQTYW
[MXL TIVMSHSRXMXMW Eɸ ERH F ;
EPPYZMEPTPSXWWLS[MRKXLIQEMR
MRXIVEGXMSRW FIX[IIR IRHSXLI
PMEPGIPPWERHWYVVSYRHMRKGIPPW
MRGPYHMRKMRLMFMXSV]RIYVSRW G ,
I\GMXEXSV] RIYVSRW H  EWXVS
G]XIW I  ERH QMGVSKPME J  MR
XLI LMTTSGEQTYW SJ HMJJIVIRX
KVSYTW
The present authors also investigated the interactions between ECs and other significant clusters in
the neurovascular unit, and observed that ECs in the
hippocampus of mice with periodontitis had disrupted
communication with neurons, astrocytes and microglia
compared to those in healthy mice. Specifically, in ECs,
 Ʋ expression was upregulated, and expression of
 Ʋ receptor was correspondingly upregulated on
neurons (Fig 2c and d). FLRT2 can regulate synapse
formation, which may contribute to the imbalanced
Chinese Journal of Dental Research
activation of neurons.24,25 For ligands to astrocytes, ECs
downregulated the expression of  Ʋ, Ʊ and
Ƴ, whereas  Ʊ and  expression increased
(Fig 2e). Moreover, ECs heightened the expression of
 and  ƱƳ ligands as well as matching receptors
on microglia (Fig 2f). These findings suggest that periodontitis alters intercellular communication between
hippocampal ECs and neighbouring cells, potentially
contributing to cognitive impairment.
Shen et al
*MKŷE XS HŴŴ%GXMZEXMSR SJ
the Mgll MR XLI LMTTSGEQTEP
)'W [MXL TIVMSHSRXMXMW 1SH
YPI WGSVIW SJ WMKRMJMGERXP]
IRVMGLIH TEXL[E] KIRIW MR
XLI LMTTSGEQTEP IRHSXLIPMEP
GIPPW [MXL TIVMSHSRXMXMW E ;
LIEXQETWLS[MRK()+WLMKL
P] IRVMGLIH MR %( MR XLI LMT
TSGEQTEP)'W[MXLTIVMSHSR
XMXMW F  ZMSPMR TPSXW WLS[MRK
XLI XST XLVII QSWX LMKLP]
I\TVIWWIH KIRIW IRVMGLIH MR
%(MRLMTTSGEQTEP)'WMRHMJ
JIVIRXKVSYTW G FEVTPSXWSJ
Mgll I\TVIWWMSR MR HMJJIVIRX
LMTTSGEQTEP GIPP X]TIW H 
with periodontitis
The present authors then conducted a detailed analysis
of the key genes involved in pathways associated with
cognitive dysfunction upregulated in hippocampal ECs
in response to periodontitis. The examination of these
pathways revealed a significant upregulation in the AD
pathway (Fig 3a). Pathways related to the negative regulation of angiogenesis, neurogenesis and macrophage
activation were also upregulated in ECs affected by periodontitis. Heatmap visualisation highlighted specific
genes linked to the AD pathway, such as "'', 
, 
Ʋ, whereas "'' exhibited the greatest increase in expression (Fig 3b and c).
The analysis also indicated that "'' is predominantly
expressed in hippocampal astrocytes and ECs under the
influence of periodontitis, whereas its upregulation in
ECs was most notable (Fig 3d). Consequently, the present authors focused on the expression of "'', as its
upregulation could potentially disrupt endothelial function and impact cellular communication. These findings suggest that "'' is activated in the hippocampal
ECs in mice with periodontitis.
The present authors further investigated the impact of
"'' activation on the functions of ECs by comparing the
gene expression profiles of ECs with high and low "''
levels. Enrichment analysis of differentially expressed
genes revealed that genes associated with the immune
response, apoptotic signalling regulation and antigen
presentation via MHC class II were upregulated in ECs
with high Mgll expression, whereas genes associated
with developmental growth pathways were downregulated in those cells (Fig 4a and b). Statistical analysis confirmed the significant upregulation of immune response
and apoptotic signalling regulation and the downregulation of developmental growth in high "''-expressing
cells (Fig 4c). Examination of immune-related genes in
high "''-expressing cells identified H2-Eb1, Cd74 and
H2-Aa as the top three genes with significantly increased
expression compared to "''-negative cells, indicating
enhanced MHCII complex regulation and inflammatory
functions in ECs with high "'' expression (Fig 4d and
e). The activation of proinflammatory ECs was found to
exacerbate neuroinflammation and cognitive dysfunc-
Volume 28, Number 2, 2025
Shen et al
*MKŷE XS IŴŴ%GXMZEXMSR SJ
Mgll I\EGIVFEXIW MRJPEQQE
XMSRERHERXMKIRTVIWIRXEXMSR
MRXLILMTTSGEQTEP)'W8VII
QETW WLS[MRK JYRGXMSREP
EREP]WIW SJ YTVIKYPEXIH E 
ERH HS[RVIKYPEXIH KIRIW
F  MR LMTTSGEQTEP )'W [MXL
LMKLMgllI\TVIWWMSRQSHYPI
WGSVIWSJWMKRMJMGERXTEXL[E]
KIRIW MR JYRGXMSRW IRVMGLIH
MR XLI LMTTSGEQTEP )'W [MXL
LMKL Mgll I\TVIWWMSR G ; bar
TPSX WLS[MRK XLI VIPEXMZI
I\TVIWWMSRSJKIRIWXLEXTSW
MXMZIP] VIKYPEXI XLI MQQYRI
VIWTSRWIMRLMTTSGEQTEP)'W
[MXL LMKL Mgll I\TVIWWMSR
H  FEV TPSX WLS[MRK XLI XST
XLVIIKIRIW[MXLXLIKVIEXIWX
GLERKIWMRXLII\TVIWWMSRSJ
KIRIW EWWSGMEXIH [MXL TSWM
XMZIVIKYPEXMSRSJXLIMQQYRI
VIWTSRWIMRLMTTSGEQTEP)'W
[MXLLMKLMgllI\TVIWWMSR I 
tion by stimulating T cells and microglia. These findings
suggest that "'' activation amplifies inflammation and
antigen presentation in hippocampal ECs.
ECs exhibiting high "'' expression demonstrate
heightened proinflammatory and enhanced antigen
presenting properties; however, the precise mechanisms through which "'' governs these EC functions
remain ambiguous. Therefore, the present authors
investigated the impact of LPS on simulating bacteria on
HCMEC/D3 cells (Fig 5) and PUMC-HUVEC-T1 cells (Fig
S3, provided on request). After LPS stimulation, elevated
expression levels of type 2 cannabinoid receptors (Ʋ)
were observed, as well as the proinflammatory and
antigen presenting genes
Ʊ expression had no significant change, which corresponded to a previous study.26 2-arachidonoylglycerol
(2-AG) is the ligand of cannabinoid receptors, the activation of which is known to significantly mitigate neuroinflammation and aid disease-related damage repair.27
MGLL predominantly hydrolyses 2-AG to arachidonic
Chinese Journal of Dental Research
acid (AA), which induces cannabinoid receptors to exert
inhibitory effects.26 AA can also attribute to neuroinflammation.28 The present authors observed consistent
results, which affirmed that MGLL played an important
is a common MGLL inhibitor.29 Notably, treatment with
the expression of
ǻƱ and   and restoring
the expression of CB2 (Fig 5b). The present findings
clarified that MGLL decreased the levels of 2-AG and
CB2, attributing to increased CIITA and MHCII expression, leading to neuroinflammation in surrounding
cells (Fig 5c). These results suggest that MGLL inhibitors
can diminish the inflammatory and antigen-presenting
capacities of ECs by augmenting 2-AG levels and suppressing CIITA and MHCII expression, which could be
potential therapies for periodontitis-associated AD.
Discussion
By utilising single-nucleus transcriptomics of brain and
hippocampal cells, the present study revealed that periodontitis exacerbates cognitive impairment by inducing
endothelial inflammation and dysfunction of antigen
Shen et al
*MKŷEXSGŴŴ8LI1+00MRLMFM
XSV QMXMKEXIH MRJPEQQEXMSR
ERH ERXMKIR TVIWIRXEXMSR MR
WIW SJ 1+00 EWWSGMEXIH
KIRIWMRHMJJIVIRXKVSYTW E ;
%% MR HMJJIVIRX KVSYTW F ;
SZIVZMI[SJXLIQIGLERMWQW
F][LMGL1+00MRHYGIWRIY
VSMRJPEQQEXMSR HYVMRK XLI
TVSGIWW F] [LMGL TIVMSHSR
XMXMWI\EGIVFEXIW%( G %&<
GEXIXLIWXERHEVHIVVSVSJXLI
presentation through upregulation of "'' expression.
This study offers valuable perspectives for the advancement of precise therapeutic interventions for cognitive
impairment.
The present study revealed the key role of endothelial inflammation as a significant contributor to periodontitis-associated cognitive impairment. Previous
research has emphasised the importance of endothelial dysfunction during the development of AD, but
has not precisely explored the connection between
endothelial dysfunction and periodontitis-associated
AD. Abnormalities of brain ECs contributing to cognitive impairment have been observed in morphology,
metabolism and immunity.30,31 Periodontitis involves
sophisticated mechanisms that can damage systemic
health,32-34 and may play a pivotal role in brain endothelial abnormalities that exacerbate neuroinflammation
and cognitive decline; however, changes in brain ECs
underlying periodontitis are unclear. Through the snRNA-seq of brain and hippocampal cells, the present
authors identified the distinct pathways upregulated
in the hippocampal ECs of mice with periodontitis that
are linked to AD. Subsequent analysis of cell communication revealed aberrant interactions between ECs
and surrounding cells involving neurons, astrocytes
and microglia in the hippocampus, which may have
intensified neuroinflammation. In summary, the present study provides a comprehensive understanding of
the impact of periodontitis on hippocampal ECs and
elucidates potential mechanisms that contribute to the
exacerbation of neuroinflammation.
The present authors also identified the potential
mechanism through which periodontitis exacerbates
neuroinflammation via endothelial cell dysfunction.
MGLL was identified as one of the key molecules leading to endothelial cell dysfunction. It can participate
in endocannabinoid signalling, cause dysfunction of
astrocytes and microglia and augment inflammatory
mediators such as prostaglandin.28 Previous studies
have shown an imbalanced endocannabinoid system
in gingival crevicular fluid in individuals with periodontitis.35,36 In the central nervous system, a recent
study observed elevated MGLL expression in protein
extracts from the frontal cortex in cases of depression
combined with periodontitis;37 however, its contribution and underlying mechanisms in the hippocampus
with periodontitis-associated AD is unclear. Thus, the
present authors focused on its function by comparing
cells that exhibited high and low "'' expression in
the hippocampal data of periodontitis-afflicted mice.
Analysis of upregulated genes involved in AD-related
pathways revealed the predominant expression of "''
in ECs and astrocytes, and the most significant upregulation was observed in the ECs. Interestingly, the present authors observed an accompanying increase in the
expression of genes associated with MHCII molecules,
including a notable increase of more than sevenfold
in the expression of Ʋǻ
Ʊ, Ʒƴ and Ʋǻ
. MHCII
molecules play a crucial role in the antigen presentation function of ECs, contributing to the activation of T
cells and macrophages and the exacerbation of tissue
inflammation.38,39 The present authors infer that peri-
Volume 28, Number 2, 2025
Shen et al
odontitis may aggravate neuroinflammation and cognitive impairment by activating the antigen presentation
of ECs, leading to the activation of microglia, astrocytes and other cell types. Periodontitis may aggravate
MGLL expression through inflammatory signalling,
#
studies,40-42 which should be studied further. Further
experimental validation is imperative to substantiate
the direct connection between periodontitis, MGLL activation in hippocampal ECs and upregulated antigen
presentation.
Specifically, the present authors elucidated that the
MGLL-2AG-CB2 pathway activates antigen presentation and inflammatory phenotypes in ECs. MGLL can
hydrolyse 2-AG to AA, while the expression of the
2-AG receptor CB1 and CB2 decreases in surrounding
environment.28 CB2 has been shown to play a crucial
role in regulating inflammation and neuronal modulation in the brain, including the transition of microglia
and astrocytes to the M2 phenotype, and the release
of excitatory and inhibitory neurotransmitters.43 CB2
is also widely expressed on immune cells such as
macrophages and dendritic cells, which suggests that
it may participate in antigen presentation.44,45 In the
CB2 suppresses CIITA expression and reduces MHCII
levels, while decreasing CB2 expression can augment
anti-inflammatory antigen presentation in ECs, trigger tissue inflammation and worsen tissue damage.
Therefore, the present authors investigated whether
inhibiting MGLL could enhance CB2 expression and
decrease CIITA and MHCII levels in ECs. The findings
revealed that MGLL inhibition increases 2-AG levels,
activates endothelial CB2 and subsequently downregulates CIITA and MHCII. Targeting MGLL to reduce the
anti-inflammatory antigen presentation and inflammatory profiles of ECs could represent a potential strategy
for mitigating periodontitis-induced neuroinflammation and cognitive impairment; however, the use of LPS
as a model of inflammation may not fully recapitulate
the complex microbial and host interactions in vivo.
Further experimental validation is also necessary to
confirm the efficacy and feasibility of this approach,
which will be the focus of follow-up studies.
Conclusion
In summary, with analyses of snRNA-seq data from
brain and hippocampal cells, this study reveals the role
of the MGLL-2AG-CB2 pathway in linking periodontitis
to inflammation and antigen presentation of ECs, leading to neuroinflammation and cognitive impairment.
Chinese Journal of Dental Research
These insights offer a foundation for targeted therapeutic approaches for cognitive impairment.
Conflicts of interest
The authors declare no conflicts of interest related to
this study.
Author contribution
Drs Zong Shan SHEN, Ji Chen YANG and Bin CHENG
designed and directed the study; Drs Zong Shan SHEN
and Ji Chen YANG contributed to the collection and analysis of the data and the manuscript draft; Drs Chuan
Jiang ZHAO and Bin CHENG critically revised the manuscript. All the authors approved the final submission.
(Received Aug 14, 2024; accepted Jan 21, 2025)
References
Dominy SS, Lynch C, Ermini F, et al. Porphyromonas gingi1
0sation and treatment with small-molecule inhibitors. Sci Adv
ƨǚ 
4
important role in modulating the risk of periodontitis and
3. Jia L, Du Y, Chu L, et al. Prevalence, risk factors, and management of dementia and mild cognitive impairment in adults
aged 60 years or older in China: A cross-sectional study. Lancet Public Health 2020;5:e661–e671.
4. Yamaguchi S, Murakami T, Satoh M, et al. Associations of
dental health with the progression of hippocampal atrophy in
community-dwelling individuals: The ohasama study. Neurology 2023;101:e1056–e1068.
5. Lei S, Li J, Yu J, et al. Porphyromonas gingivalis bacteremia
increases the permeability of the blood-brain barrier via the
Mfsd2a/caveolin-1 mediated transcytosis pathway. Int J Oral
6. Li F, Ma C, Lei S, et al. Gingipains may be one of the key virulence factors of porphyromonas gingivalis to impair cognition
and enhance blood-brain barrier permeability: An animal
study. J Clin Periodontol 2024;51:818–839.
7. Kerkis I, da Silva ÁP, Araldi RP. The impact of interleukin-6
(IL-6) and mesenchymal stem cell-derived IL-6 on neurological conditions. Front Immunol 2024;15:1400533.
8. Shen Z, Kuang S, Zhang Y, et al. Restoring periodontal tissue homoeostasis prevents cognitive decline by reducing the
number of Serpina3nhigh astrocytes in the hippocampus.
9. Bryant A, Li Z, Jayakumar R, et al. Endothelial cells are heterogeneous in different brain regions and are dramatically
10. Custodia A, Ouro A, Romaus-Sanjurjo D, et al. Endothelial

Shen et al
11. Waigi EW, Pernomian L, Crockett AM, et al. Vascular dysfunc/$*) *
ͤ
plaque deposits colocalize with endothelial cells in the hippocampus of female APPswe/PSEN1dE9 mice. Geroscience

methylation in hypoxia-preconditioned endothelial cells may
contribute to hypoxic tolerance of neuronal cells. Mol Biol
13. Linnerbauer M, Wheeler MA, Quintana FJ. Astrocyte crosstalk in CNS inflammation. Neuron 2020;108:608–622.
14. Huo A, Wang J, Li Q, et al. Molecular mechanisms underlying microglial sensing and phagocytosis in synaptic pruning.
15. Hao Y, Stuart T, Kowalski MH, et al. Dictionary learning for
integrative, multimodal and scalable single-cell analysis. Nat
16. Korsunsky I, Millard N, Fan J, et al. Fast, sensitive and accurate integration of single-cell data with harmony. Nat Methods
cellular and transcriptional changes associated with traumatic brain injury. Front Genet 2022;13:861428.
18. Li Y, Li Z, Wang C, et al. Spatiotemporal transcriptome atlas
reveals the regional specification of the developing human
19. Khrameeva E, Kurochkin I, Han D, et al. Single-cell-resolution transcriptome map of human, chimpanzee, bonobo, and
macaque brains. Genome Res 2020;30:776–789.
20. Lau SF, Cao H, Fu AKY, Ip NY. Single-nucleus transcriptome
analysis reveals dysregulation of angiogenic endothelial cells
 
21. Zhou Y, Zhou B, Pache L, et al. Metascape provides a biologistoriented resource for the analysis of systems-level datasets.
22. Troulé K, Petryszak R, Prete M, et al. CellPhoneDB v5: Inferring cell-cell communication from single-cell multiomics
data. http://arxiv.org/abs/2311.04567. Accessed 23 July 2024.
ƨƩǚ 
alters neurovascular unit regulation of microcirculation integrity involved in vascular cognitive impairment. Neurobiol
24. Pederick DT, Lui JH, Gingrich EC, et al. Reciprocal repulsions
instruct the precise assembly of parallel hippocampal networks. Science 2021;372:1068–1073.
25. Maestú F, de Haan W, Busche MA, DeFelipe J. Neuronal excitation/inhibition imbalance: Core element of a translational
perspective on Alzheimer pathophysiology. Ageing Res Rev
-*sis through inhibiting tubular cell lipotoxicity. Theranostics
27. Moe A, Rayasam A, Sauber G, et al. Type 2 cannabinoid receptor expression on microglial cells regulates neuroinflammation during graft-versus-host disease. J Clin Invest
28. Bajaj S, Jain S, Vyas P, Bawa S, Vohora D. The role of endo
disease: Can the inhibitors of MAGL and FAAH prove to be
potential therapeutic targets against the cognitive impair( )/

29. Müller-Vahl KR, Fremer C, Beals C, Ivkovic J, Loft H, Schindler
C. Endocannabinoid modulation using monoacylglycerol lipase
inhibition in tourette syndrome: A phase 1 randomized, placebocontrolled study. Pharmacopsychiatry 2022;55:148–156.
30. Leira Y, Vivancos J, Diz P, Martín Á, Carasol M, Frank A. The
association between periodontitis and cerebrovascular disease, and dementia. Scientific report of the working group of
the Spanish society of periodontology and the Spanish society
of neurology. Neurologia (Engl Ed) 2024;39:302–311.
#anisms of blood brain barrier dysfunction. Nat Commun
32. Shen Z, Zhang R, Huang Y, et al. The spatial transcriptomic
landscape of human gingiva in health and periodontitis. Sci
33. Lu J, Zhang S, Huang Y, et al. Periodontitis-related salivary
crosstalk. Gut Microbes 2022;14:2126272.
34. Herrera D, Molina A, Buhlin K, Klinge B. Periodontal diseases
and association with atherosclerotic disease. Periodontol 2000
35. Nakajima Y, Furuichi Y, Biswas KK, et al. Endocannabinoid,
anandamide in gingival tissue regulates the periodontal
inflammation through NF-kappaB pathway inhibition. FEBS
#Ǳ
Andrukhov O. Endocannabinoids and inflammatory response
in periodontal ligament cells. PloS One 2014;9:e107407.
37. Robledo-Montaña J, Díaz-García C, Martínez M, et al. Microglial morphological/inflammatory phenotypes and endocannabinoid signaling in a preclinical model of periodontitis and
depression. J Neuroinflammation 2024;21:219.
38. Rodor J, Chen SH, Scanlon JP, et al. Single-cell RNA sequencing profiling of mouse endothelial cells in response to pulmonary arterial hypertension. Cardiovasc Res 2022;118:
39. Rustenhoven J, Drieu A, Mamuladze T, et al. Functional characterization of the dural sinuses as a neuroimmune interface.
40. Zhu W, Zhao Y, Zhou J, et al. Monoacylglycerol lipase pro(*/ . +-*"- ..$*) *! # +
 ǱͬǱ
mediated epithelial-mesenchymal transition. J Hematol
41. Gandhi AY, Yu J, Gupta A, Guo T, Iyengar P, Infante RE.
Cytokine-mediated STAT3 transcription supports ATGL/CGI58-dependent adipocyte lipolysis in cancer cachexia. Front
42. Shen S, Fu B, Deng L, et al. Paeoniflorin protects chicken
against APEC-induced acute lung injury by affecting the endo
signaling pathways. Poult Sci 2024;103:103866.
43. Grabon W, Rheims S, Smith J, Bodennec J, Belmeguenai A,
Bezin L. CB2 receptor in the CNS: From immune and neuronal modulation to behavior. Neurosci Biobehav Rev
. - "0lates cannabinoid receptor 2-dependent macrophage activation and cancer progression. Nat Commun 2018;9:2574.
45. Cabral GA, Ferreira GA, Jamerson MJ. Endocannabinoids and
the immune system in health and disease. Handb Exp Pharmacol 2015;231:185–211.
Volume 28, Number 2, 2025
