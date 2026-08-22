# Transcriptomics and Functional Analysis of Graphene-Guided

Source: Chinese Journal of Dental Research (CJDR)

Transcriptomics and Functional Analysis of Graphene-Guided
Osteogenic Differentiation of Mesenchymal Stem Cells
Long Wei LV1, Yun Song LIU1, Ping ZHANG1, Ming GU1, Xiang Song BAI1,
Chun Yang XIONG2, Yong Sheng ZHOU1
Objective: To explore graphene’s effects on the gene expression profile of mesenchymal stem
cells, and to reveal the mechanisms of graphene-guided osteogenic differentiation.
Methods: Human adipose-derived mesenchymal stem cells (hASCs) were cultured on singlelayer graphene-coated titanium disks or titanium disks in proliferation medium (control) or
osteoinduction medium for 7 days before RNA extraction. After library construction and RNA
sequencing, identification of differentially expressed genes was performed through Limma
package of R platform, with a cut-off value of log fold change (logFC) > = |1|. Pathway
and Gene ontology (GO) analyses were conducted on DAVID Bioinformatics Resources 6.8
(NIAID/NIH). Network analyses were performed by the Ingenuity Pathways Analysis (IPA).
Results: Signalling pathway analysis revealed the top five pathways – cytokine-cytokine
receptor interaction, neuroactive-ligand receptor interaction, calcium signalling pathway,
PI3K-Akt signalling pathway and cell adhesion molecules. GO analyses demonstrated significant changes on cell adhesion, calcium signalling, and epigenetic regulation. IPA network
analyses demonstrated that inflammation-related pathways were influenced by graphene,
while the downstream factors of histone H3 and H4 were also altered especially under the
existence of osteoinduction medium.
Conclusion: Graphene promotes osteogenic differentiation of hASCs mainly by influencing
cell adhesion, cytokine-cytokine receptor interactions, inflammatory responses, and potentially influences histone H3 and H4 through epigenetic regulation.
Key words: bone tissue engineering, epigenetics, graphene, inflammation, RNA sequencing
1 Department of Prosthodontics, Peking University School and
Hospital of Stomatology, National Engineering Laboratory for
Digital and Material Technology of Stomatology, National Clinical
Research Center for Oral Disease, Beijing Key Laboratory of Digital
Stomatology, Beijing, P.R. China.
2 Department of Mechanics and Aerospace Engineering, College of
Engineering, Peking University, Beijing, P.R. China.
Corresponding author: Dr Yong Sheng ZHOU, Department of Prosthodontics, Peking University School and Hospital of Stomatology, 22#
Zhongguancun South Avenue, HaiDian District, Beijing 100081, P.R.
hsc.pku.edu.cn
This work was supported by the grant of Young Elite Scientist Sponsorship Program by CAST (2015QNRC001), and the grant (31600787,
81470769) from the National Natural Science Foundation of China, the
Project for Culturing Leading Talents in Scientific and Technological
Innovation of Beijing (Z171100001117169), the PKU School of Stomatology for Talented Young Investigators (PKUSS20150107).
Chinese Journal of Dental Research
ell-surface interactions are believed to represent a
promising management to precisely control seed
cell function and differentiation in bone tissue engineering1.
Therefore, biomaterial surface modification has
attracted lots of attention. Although bone has the ability
to repair minor injuries by remodelling, for large bone
defects caused by severe trauma, congenital malformations, tumours and non-union fractures, remodelling is
limited. Bone tissue engineering, which aims to regenerate bone, is a promising solution for these problems.
Traditionally, bone tissue engineering consists of three
factors, seed cells, scaffolds, and chemical osteoinductive factors2. Many researches employed chemical
factors to induce differentiation in vitro, but guided
differentiation of stem cells using these strategies is not
LV et al
efficient and often requires a long cell culture time for
maturation into osteogenic lineages. This has limited the
widespread use of bone tissue engineering. Therefore, it
is urgent to develop more efficient methods to enhance
differentiation of mesenchymal stem cells (MSCs), and
scaffold surface modification is likely to be a more
convenient and stable manner3.
Graphene, a 2D single-atomic-thick nanomaterial,
holds great potential as coatings of bone implants and
scaffolds, because it not only has exceptional mechanical, electronic, thermal properties, but also anti-bacteria
and osteoinductive ability4-7. Single-layer graphene on
copper foil can be produced in large scale by chemical
vapour deposition (CVD) and then transferred to other
substrates using polymethyl methacrylate (PMMA)810. Several studies have reported promising effects of
graphene and its derivatives on cell adhesion, proliferation, and osteogenic differentiation4-6,11. In a previous
study, we also confirmed that single-layer graphene
could promote the osteogenic differentiation of human
adipose-derived stem cells (hASCs) and human bone
marrow-derived mesenchymal stem cells (hBMMSCs)
in vitro and in vivo, and explored the underlying epigenetic mechanism in the fate of stem cells12.
However, a clear view of graphene-cell interactions and its internal mechanisms is still incomplete.
A few researches proposed various possible mechanisms of how graphene interacted with stem cells. Lee
et al demonstrated that graphene and graphene oxide
(GO) can accelerate MSC osteogenic differentiation
as a result of preconcentration of osteogenic inducers,
such as dexamethasone and -glycerolphosphate, due
to graphene s strong
stacking, hydrogen bonding,
and electrostatic interactions with proteins5. Kim et al
hypothesised that the unique nanotopography of the GO
film would influence the formation of focal adhesions
(FAs) and alter cell morphology13. Changes in cell
adhesion and cell shape are important regulatory factors in stem cell lineage commitment14. Our previous
researches revealed graphene’s epigenetic role during
the process of osteogenic differentiation and found that
graphene accelerated the osteogenic differentiation of
hASCs by enhancing the methylation level of histone
H3 at lysine 4 (H3K4) at the promoter regions of osteogenic related genes12. However, a whole picture and the
overall mechanisms of how graphene influences cell
behaviours remains to be uncovered, and a clear mechanism is important for further graphene-related studies,
safety evaluation and its future clinical applications.
Therefore, we investigated the response of hASCs to
single-layer graphene on titanium substrate using the
next generation sequencing bioinformatics approach.
The changes on the whole gene expression profile will
provide a more thorough picture to elucidate the regulatory network, and evaluate the safety and biocompatibility of graphene.
Materials and methods
Preparation of single-layer graphene sheets on titanium
substrates
CVD grown single-layer graphene was purchased on a
copper foil substrate from the American Chemical Society (ACS). Titanium (Ti) disks (23 mm × 23 mm for
6-well-plate cell culture, 10 mm × 10 mm for 24-wellplate cell culture, 99.6% purity, Leiden, Beijing, China)
were cleaned in acetone, ethanol, and de-ionized water
successively, each for 15 min using an ultrasonic cleaning machine. Graphene on copper foil was cut into optimal sizes to fit the sizes of Ti discs. For the transfer
process, a PMMA thin film (950 K grade, 2 wt% in
chlorobenzene) was spin-coated on the surface of graphene via a two-step process (step 1: 600 rpm for 10 s;
step 2: 3000 rpm for 40 s) using a Laurell WS-400BZ6NPP/LITE spin coater. After treatment at 180°C for
4 min, the copper foil substrate was then etched using
FeCl3 solution (0.05 g/mL in water), and the PMMA
(top)/graphene (bottom) film floated to the surface of the
solution. The film was rinsed twie with distilled water,
and then a Ti disk was placed in de-ionized water with a
tilting angle of 30 degrees underneath the floating film,
and was picked up from the water with the coating of the
graphene film. Finally, the thin PMMA film on the top of
graphene was removed in an acetone bath for 30 min12.
Atomic force microscopy (AFM) was used to confirm the presence of single-layer graphene on the Ti
discs, and to measure surface roughness of the samples. Before AFM measurement, different samples
were rinsed with ethanol and Milli-Q water, and then
air-dried. The measurements were conducted under
contact mode in dry conditions with a spring constant
of 0.25 N/m, a scan rate of 1 Hz and a scan area of
3 m × 3 m. Measurements were run in triplicate for
each sample.
Before using them for the cell culture, both graphenecoated Ti discs and the control group’s smooth Ti discs
were disinfected by soaking in 75% alcohol for 30 min.
hASCs culture and osteogenic induction
hASCs were purchased from ScienCell Company (San
Diego, CA, USA). Dulbecco’s modified Eagle’s medium
Volume 21, Number 2, 2018
LV et al
(DMEM), foetal bovine serum (FBS), 100 × penicillin and streptomycin mixture were bought from Gibco
(Grand Island, NY, USA). hASCs were cultured in fresh
DMEM containing 10% (v/v) FBS, 100 U/mL penicillin G and 100 mg/mL streptomycin at 37°C in an incubator with an atmosphere consisting of 95% air, 5% CO2 and
100% relative humidity. Cells at the fourth passage were
used for the experiments. Osteoinduction medium (OM)
comprised fresh DMEM containing 10% (v/v) FBS,
100 U/mL penicillin G and 100 mg/mL streptomycin
(Sigma-Aldrich, St. Louis, MO, USA), 10nM dexamethasone (Sigma-Aldrich), 10 mM -glycerophosphate, and
50 g/ml L-ascorbic acid (Sigma-Aldrich).
Immunofluorescence
hASCs were seeded in 24-well plates on graphene or Ti
surfaces. After 7 days of osteoinduction, samples were
rinsed with PBS and fixed in 4% paraformaldehyde for
20 min at room temperature. Samples were then rinsed
three times in PBS and post-fixed in 0.1% Triton X-100
for 15 min at room temperature. After another three lots
of PBS rinsing, the samples were incubated overnight
with 1:200 anti-osteocalcin primary antibodies (Santa
Cruz, Dallas, TX, USA) at 4°C. Samples were rinsed
and then incubated in 1:500 anti-rabbit secondary antibodies (4412S, Cell Signaling Technology, Beverly,
MA, USA) for 1 h at room temperature. The samples
were washed and incubated in 5 g/ml DAPI solution for
10 min at 37°C, before being visualised with a Confocal Zeiss Axiovert 650 microscope (Carl Zeiss Microimaging, Oberkochen, Germany), using the laser with
wavelengths of 488 nm (green, osteocalcin) and 405 nm
(blue, DAPI)1.
RNA extraction, reverse transcription, and quantitative
realtime PCR
hASCs were seeded in 6-well plates on graphene or
Ti surfaces. Total cellular RNAs were isolated after
7 days of osteoinduction using the Trizol reagent (Invitrogen, Carlsbad, CA, USA) and used for first strand
cDNA synthesis with the Reverse Transcription System (Roche, Basel, Switzerland). Quantifications of all
gene transcripts were performed by quantitative realtime polymerase chain reaction (qPCR) using a Power
SYBR Green PCR Master Mix and an ABI PRISM 7500
sequence detection system (Applied Biosystems, Foster
City, CA, USA). The expression of GAPDH was detected
as the internal control. The primers used were listed in
Table 1. The cycle threshold values (Ct values) were used
to calculate the fold differences by the Ct method15.
Chinese Journal of Dental Research
RNA sequencing and bioinformatics
Total RNA was extracted from hASCs using the GeneJet
RNA purification kit (Thermo Scientific). One μg RNA
was used for sequencing library generation using the
Truseq RNA Library Prep Kit V2 (Illumina) for mRNA
seq according to the manufacturer’s instructions. All
libraries were sequenced on the NextSeq sequencer (Illumina) using the 35 nt paired-end sequencing protocol.
Differentially expressed gene (DEG) presenting a
log fold change (logFC) 1 , e.g. expression changes 2 or 0.5, was set to identify significant results.
After we obtained the DEGs list, we performed Kyoto
Encyclopedia of Genes and Genomes (KEGG) pathway
analysis and Gene Ontology (GO) enrichment analyses,
including biological processes (BP), cellular components (CC) and molecular functions (MF), associated
with those DEGs through the online software DAVID
Bioinformatics Resources 6.7 (https://david.ncifcrf.
gov/)16. As for both KEGG and GO analyses, P < 0.05
were considered as significant, and the results were
shown in log10 (P value). Additionally, we identified the
enriched networks, molecular functions and pathways
in the Ingenuity Pathways Analysis (IPA, Ingenuity
Systems) platform via a license to Ingenuity Systems
(www.ingenuity.com)17.
Statistical analysis
All results were presented as mean ± standard deviation;
the data were analysed using the SPSS 19.0 software
(SPSS, Chicago, IL, USA) by one-way ANOVA plus
Tukey test. For all tests, P values less than 0.05 were
considered indicative of statistically significant differences.
Results
Surface characterisation
Atomic force microscope (AFM) observation (Fig 1A)
demonstrated that there were many ripples and wrinkles
on the surface of graphene-coated Ti. The roughness
increased on graphene-coated Ti compared with smooth
Ti substrate (Fig 1B). Therefore, graphene was transferred on Ti substrate successfully.
Enhanced osteogenic differentiation by graphene
OC expression detected by immunofluorescence showed
that after 7 days of cell culture, hASCs in osteoinduction
LV et al
Fig 1 Surface characterisation
and osteoinductive ability of graphene. (A) AFM images of graphene and Ti surface; (B) Roughness (Ra) analysis of graphene and
Ti surface; (C) Immunofluorescent
staining of osteocalcin (OCN) in
hASCs cultured on graphene and
Ti surfaces after 7 days of osteoinduction. OCN and nuclei are
coloured green and blue respectively. (*P < 0.05). GPM: graphene
with proliferation medium; GOM:
graphene with osteoinduction
medium; TPM: titanium with proliferation medium; TOM: titanium
with osteoinduction medium.
medium (OM) cultured on graphene surface demonstrated obvious stronger OC-positive staining than Ti
surface. As for hASCs cultured on a graphene surface in
proliferation medium (PM), sporadic green fluorescence
could be observed, while little green staining could be
seen on Ti surface (Fig 1C).
Gene expression profile by RNA sequencing
To further investigate the overall mechanisms during the
osteogenic process of graphene, gene expression profiles of hASCs cultured on graphene with proliferation
medium (GPM), graphene with osteoinduction medium
(GOM), Ti with proliferation medium (TPM), and Ti
with osteoinduction medium (TOM) were analysed
using RNA sequencing (RNA-seq). Differences of gene
expression levels between graphene and titanium were
compared: GPM versus TPM, GOM vs TOM. Differences of gene expression levels before and after osteoinduction were also compared: TOM vs TPM; GOM
vs GPM. Statistics about DEG lists are summarised in
Fig 1D. There were 565 upregulated DEGs and 586
downregulated DEGs when comparing GPM with TPM.
There were 599 upregulated DEGs and 651 downregulated DEGs when comparing GOM with TOM. There
were 1385 upregulated DEGs and 1072 downregulated
DEGs when comparing TOM with TPM. There were
1824 upregulated DEGs and 1074 downregulated DEGs
when comparing GOM with GPM (Fig 1D). Fig 1E
demonstrated that the co-occurrence of upregulated
DEGs in four cases was 16, and the co-occurrence of
upregulated DEGs in both GPM/TPM and GOM/TOM
Volume 21, Number 2, 2018
LV et al
Fig 2 KEGG
pathway
analysis and verification of
representative DEGs. (A)
KEGG pathway analysis; (B)
Verification of representative differentially expressed
genes (DEGs) by realtime
PCR. (*P < 0.05). Abbreviations as in Figure 1.
was 54. Fig 1F demonstrates that there was no co-occurrence of downregulated DEGs in four cases, while the
co-occurrence of downregulated DEGs in both GPM/
TPM and GOM/TOM was 33.
Kyoto encyclopedia of genes and genomes (KEGG)
pathways analysis
Database of essential genes (DEG) annotations were
conducted by DAVID (version 6.7) online software
according to the information of the official gene symbol,
and further analyses were performed on DEGs of annotated genes. KEGG analysis revealed that a significant
proportion of DEGs intervened into cytokine-cytokine
receptor interaction, neuroactive receptor interaction,
calcium signalling pathways, PI3K-Akt (phosphati-
Chinese Journal of Dental Research
dylinositol 3 kinase, PI-3K; protein kinase B, PKB or
Akt) signalling pathway, and cell adhesion molecules
(Fig 2A). Upregulated genes and downregulated genes
in cytokine-cytokine receptor interaction, neuroactive
receptor interaction, calcium signalling pathways, and
cell adhesion molecules are shown in Table 2.
Verification of representative DEGs by real-time PCR
Real-time PCR was used to confirm the expression level
of six representative genes, which were significantly
changed DEGs. TNFSF10 (TNF superfamily member
10), CCL20 (C-C motif chemokine ligand 20), CXCL12
(C-X-C motif chemokine ligand 12), CSF1 (colony
stimulating factor 1), KDR (kinase insert domain receptor) expression was significantly increased after osteo105
LV et al
Table 1
Primers for real-time PCR.
Gene
Forward primers
Reverse primers
GAPDH
GAAGGTGAAGGTCGGAGTC
GAAGATGGTGATGGGATTTC
TNFSF10
TCCGTCAGCTCGTTAGAAAGATGAT
GGTCCCAGTTATGTGAGCTGC
CXCL12
GCCCTTCAGATTGTAGCCCG
CTCGAGTGGGTCTAGCGGAA
CCL20
GCGAATCAGAAGCAGCAAGCA
TGCCGTGTGAAGCCCACAAT
CSF1
CTGCAGCGGCTGATTGACAG
TCTGAAGCGCATGGTGTCCT
KDR
AGCGGTCAACAAAGTCGGGA
TTTCAGGACCCCTGGTCACG
CHRM5
AACAAACCACTGCCAGGAACC
TGCAAGGCTGAGAATGATTTCCT
Table 2 Differentially expressed genes of hASCs on graphene vs titanium in proliferation medium by KEGG signalling pathway
analysis.
KEGG pathways
Upregulated genes
Downregulated genes
TNFSF10, IL1R2, IL17B, IL23A, CNTF,
TNFSF11, TNFSF15, IL6R, CXCL11,
TNFSF18, TNFSF8
TNF, IL22RA1, IL7, TGFB3, CCL8, PF4, CNTFR, HGF, PF4V1, CCL7, TNFRSF11B, IFNE,
BMPR1B, IL3RA
RXFP4, PTGER4, GRIK2, OPRK1, RXFP2,
DRD4, GNRHR, P2RX5, CRHR2, P2RX7,
CHRM5, SSTR3, CHRM3, CHRNA9,
CHRM2, P2RY2, CHRNA10, GRID1
F2RL3, PTGER1, CCKBR, GRIK1, GABRB3,
PTH2R, FPR1, EDNRB, P2RY10, GPR35,
SSTR2, MTNR1B, CHRNA5, HTR2C, PTAFR,
CHRNG
Calcium signalling pathway
P2RX5, P2RX7, CHRM5, PLCE1, PLCB4,
PDE1B, CHRM3, CHRM2, MYLK3, PLN,
PLCB2
PTGER1, CCKBR, ITPKA, EDNRB, PLCG2,
RYR2, HTR2C, PTAFR
Cell adhesion molecules
(CAMs)
NRCAM, NCAM2, CD274, PECAM1,
CLDN1, HLA-DRB5, ICOSLG
CLDN9, MPZ, ITGA8, NTNG1, CLDN10, ITGB2,
JAM2, HLA-DMA, HLA-DRA
Cytokine-cytokine receptor
interaction
Neuroactive ligand-receptor
interaction
Count
induction on graphene, while the difference between
graphene and titanium in proliferation medium was not
significant. CHRM5 (cholinergic receptor muscarinic
5) expression was significantly increased on graphene
without osteoinduction.
Gene ontology analysis
Gene Ontology (GO) enrichment analyses, including biological process (BP), cellular component (CC)
and molecular function (MF) were also performed by
Volume 21, Number 2, 2018
LV et al
Fig 3 Gene ontology analyses. (A) GO biological process analysis of GPM vs TPM; (B) GO biological process analysis of GOM vs
TOM; (C) GO cellular component analysis of GPM vs TPM; (D) GO cellular component analysis of GOM vs TOM; (E) GO molecular
function analysis of GPM vs TPM; (F) GO molecular function analysis of GOM vs TOM. Abbreviations as in Figure 1.
DAVID online software. According to GO analyses of
GPM vs TPM, cell adhesion, cytoskeleton, cell metabolism, and cellular interactions, as well as calcium pathway and mineralization were significantly influenced
On the other hand, as for GOM vs TOM, graphene not
only influenced cell adhesion, cytoskeleton, cell metabolism, cellular interactions, and calcium pathway, but
Chinese Journal of Dental Research
also impacted cell nucleus and epigenetic regulation
(Figs 3B, D and F).
Network analysis
Network analysis between GPM and TPM by IPA demonstrated that inflammation-related signalling pathways
including NF- B, P38-MAPK, and Jnk were likely to
LV et al
Fig 4 IPA network analyses. (A) IPA network of GPM
vs TPM; (B) IPA network of
GOM vs TOM. Abbreviations as in Figure 1.
be associated with this process. Potential downstream
factors, including CORO1A (coronin 1A), KYNU
(kynureninase), EDNRB (endothelin receptor type B),
LSP1 (lymphocyte-specific protein 1) of NF- B, were
down regulated, while SLC2A5 (solute carrier family 2
member 5) was upregulated (Fig 4A).
Meanwhile, we found that the downstream factors of
histone H3, H4, including TUBA3C/D (tubulin alpha
3c/d), ZBTB5 (zinc finger and BTB domain containing
5), ZNF793 (zinc finger protein 793), PCBD2 (pterin-4
alpha-carbinolamine dehydratase 2), estrogen receptor 1, were upregulated by graphene under the existence
of osteoinduction medium. Therefore, graphene may
regulate cell functions through an epigenetic network
(Fig 4B). And these results of IPA network analyses
were in consistent with that of GO analyses, confirming
the role of graphene on epigenetic regulation under the
existence of OM.
Volume 21, Number 2, 2018
LV et al
Discussion
In this study, we successfully transferred single-layer
graphene from Cu substrate to Ti substrate, providing a
potential and wide application of surface modification
method for Ti-based bone implants and medical devices. We found that single-layer graphene on Ti substrate
accelerated osteogenic differentiation of hASCs compared with pure Ti. RNA sequencing and bioinformatics analyses revealed that graphene mainly influenced
cell adhesion, cytokine-cytokine receptor interactions,
inflammatory responses, and calcium signalling pathways. Moreover, epigenetic regulation was also involved
in graphene-guided osteogenic differentiation of hASCs.
Cell adhesion, the beginning of cell-surface interactions
The minute a cell adheres to the substrate, their interactions begin. The cell spreads and thus cell shape changes under the guidance of material substrate. Material
topography, adhesiveness, and 3D-dimensionality will
all lead to reorganisation of the cytoskeleton. Forces
generated by the cytoskeleton components including
actin and myosin can be transmitted to the nucleus via
physical links on the nuclear envelope18. And cell morphology and nuclear deformation are important factors
to guide cell functions, including cell proliferation and
lineage commitment19,20. Meanwhile, these influences
are relayed by adhered cells to surrounding cells through
cell synapse and cell-cell junctions, as well as secretion of cytokines or exosomes into extracellular region.
In this research, we found that cell adhesion molecules
and PI3K-Akt pathway were significantly influenced
by graphene according to KEGG pathway analysis
(Fig 2A). Meanwhile, GO analyses also revealed significant changes in plasma membrane, cytoskeleton, and
thus influencing transmembrane transport, extracellular
matrix, cell-cell junction, and cell-cell signalling transduction (Fig 3). Therefore, graphene-guided osteogenic
differentiation begins from cell adhesion and changes in
cell morphology, and is extended to surrounding cells
through cell-cell junctions and alterations in the microenvironment of residing cells.
Inflammatory response, inevitable and indispensable
process for bone regeneration
The process of bone repair begins from inflammatory
responses21. In the past, inflammation was viewed as a
negative factor of bone regeneration. On the contrary,
inflammation and immune response is indispensable in
new bone formation, since the essence of bone regenera-
Chinese Journal of Dental Research
tion is a balance between osteogenesis and bone resorption. Biomaterials can exert profound impacts on the
host immune response, thus the concept has emerged
to design biomaterials that can trigger desired immunological outcomes and support the healing process22.
However, engineering immune-modulating biomaterials
requires an in-depth understanding of the host inflammatory and wound healing response to implanted materials. Fortunately, high throughput experiments provide
a promising resolution. In this study, cytokine-cytokine
receptor interactions were significantly influenced by
graphene according to KEGG pathway analysis, leading to upregulation of cytokines including TNFSF10,
CCL20, CXCL12, CSF1, KDR and CHRM5 as verified
by real-time PCR (Fig 2). Meanwhile, downstream factors of NF- B, P38-MAPK, and Jnk were mainly downregulated according to IPA network analysis (Fig 4A).
These results provide a more thorough insight into the
inflammation process of how graphene interacts with
host cells.
Epigenetic regulation, non-negligible mechanism in
cell-material interactions
Epigenetic regulation plays an important role in cell functions14. Epigenetics refers to heritable changes in gene
expression pattern that do not alter the DNA sequence.
The epigenome helps to stabilise cell status, which can
be altered during stem cell differentiation and somatic
cell reprogramming23. Interestingly, biomaterial cues,
which act as outside signals, can influence the internal
epigenetic state through various epigenetic regulatory
mechanisms, including DNA methylation, chromatin
remodelling, and non-coding RNAs. Our research group
found that graphene promoted osteogenic differentiation
of hASCs by enhancing H3K4 methylation level at the
promoter regions of osteogenic related genes through
inhibiting histone demethylase retinoblastoma protein 2
(RBP2)12. Meanwhile, graphene can also improve cellular reprogramming efficiency by inducing a mesenchymal-to-epithelial transition (MET) process, which
is known to affect H3K4me3 levels24. In this research,
we found that graphene influenced an epigenetic-related process, including nuclear inner membrane, nuclear
envelop, DNA binding, nucleic acid binding, -catenin
binding, and DNA templated as well as transcription
under the existence of OM (Figs 3B, D and F). Meanwhile, histone H3, H4 related regulators were significantly altered by graphene, demonstrating graphene’s
potential regulatory network through epigenetic regulation (Fig 4B). Compared with small-molecule drugs,
using biomaterials to direct cell behaviours is safer and
LV et al
therefore more promising in the clinical use of human
cells.
Meanwhile, epigenetic regulation exerted by biomaterials on the biological effects of stem cells not
only plays an important role in regenerative medicine,
but is also a potential set of tools for biomaterial safety
evaluation25-27. Epigenetic alteration is a mechanism,
which explains the long-lasting and memorable effects
of cells directed by biomaterial cues. Meanwhile,
epigenetic regulation is an important process, which
breaks through the barrier of cell lineage commitment. The assessment of epigenetic effects may also
be approached as new model systems that can directly
assess transgenerational effects or potentially sensitive
stem cell populations. These will expand the scope of
safety assessment tools for evaluating new materials.
Perspectives and applications
Graphene is a promising material for the coating of bone
implants and medical devices. It is only one-atom thick,
thus introducing the least amount of artificial material
in surface modification. Meanwhile, it enjoys a large
number of remarkable properties, including exceptional
mechanical, electronic, and thermal properties28. Specifically, graphene has the highest Young’s modulus (0.51TPa) among any known material, so it is not brittle29,30.
Moreover, graphene can be transferred onto any flat or
irregular-shaped surface31. These extraordinary properties make graphene a promising choice as a component
of scaffold material or a potential surface modification
in bone tissue engineering. By utilising the novel method of next generation sequencing, an overall picture of
graphene’s regulating mechanism has been drawn, thus
providing potent evidence for future clinical application
of graphene in the field of bone tissue engineering.
Conclusions
Single-layer graphene on titanium substrate promotes
osteogenic differentiation of hASCs. RNA sequencing
and bioinformatics analyses reveal that the underlying
mechanisms mainly relate to cell adhesion, cytokinecytokine receptor interactions, inflammatory responses,
and calcium signalling pathways. Moreover, graphene
potentially regulates the state of histone H3, H4 through
an epigenetic regulatory network.
Conflicts of interest
The authors reported no conflicts of interest related to
this study.
Author contribution
Dr Long Wei LV designed the study, performed experiments, collected and analysed data, interpreted results,
and prepared the manuscript; Drs Yun Song LIU and
Ping ZHANG performed experiments, analysed data
and interpreted the results; Drs Ming GU and Xiang
Song BAI performed experiments, collected and analysed data; Dr Chun Yang XIONG designed the study
and revised the manuscript; Dr Yong Sheng ZHOU
designed the study, analysed data, interpreted results,
and critically revised the manuscript.
(Received Nov 6, 2017; accepted Jan 3, 2018)
References
Lv L, Liu Y, Zhang P, et al. The nanoscale geometry of TiO2 nanotubes influences the osteogenic differentiation of human adiposederived stem cells by modulating H3K4 trimethylation. Biomaterials
2. Henkel J, Woodruff MA, Epari DR, et al.. Bone Regeneration Based
on Tissue Engineering Conceptions A 21st Century Perspective.
3. Gu M, Liu Y, Chen T, et al. Is graphene a promising nano-material for
promoting surface modification of implants or scaffold materials in
bone tissue engineering Tissue Eng Part B Rev 2014;20:477 491.
4. Nayak TR, Andersen H, Makam VS, et al. Graphene for controlled
and accelerated osteogenic differentiation of human mesenchymal
5. Lee WC, Lim CH, Shi H, et al. Origin of enhanced stem cell growth
and differentiation on graphene and graphene oxide. ACS Nano
6. Talukdar Y, Rashkow J, Lalwani G, Kanakia S, Sitharaman B. The
effects of graphene nanostructures on mesenchymal stem cells. Biomaterials 2014;35:4863 4877.
7. Some S, Ho SM, Dua P, et al. Dual functions of highly potent graphene derivative-poly-L-lysine composites to inhibit bacteria and
support human cells. ACS Nano 2012;6:7151 7161.
8. Zhang Y, Zhang L, Zhou C. Review of chemical vapor deposition of graphene and related applications. Acc Chem Res 2013;46:
9. Reina A, Jia X, Ho J, et al. Large area, few-layer graphene films on
arbitrary substrates by chemical vapor deposition. Nano Lett 2009;9:
10. Grandthyll S, Gsell S, Weinl M, Schreck M, Hüfner S, Müller F.
Epitaxial growth of graphene on transition metal surfaces: chemical
vapor deposition versus liquid phase deposition. J Phys Condens Matter 2012;24:314204.
11. Qiu J, Geng H, Wang D, et al. Layer-Number Dependent Antibacterial and Osteogenic Behaviors of Graphene Oxide Electrophoretic Deposited on Titanium. ACS Appl Mater Interfaces 2017;9:
12. Liu Y, Chen T, Du F, et al. Single-Layer Graphene Enhances the
Osteogenic Differentiation of Human Mesenchymal Stem Cells In
Vitro and In Vivo. J Biomed Nanotechnol 2016;12:1270 1284.
13. Kim J, Choi KS, Kim Y, et al..Bioactive effects of graphene oxide
cell culture substratum on structure and function of human adiposederived stem cells. J Biomed Mater Res A 2013;101:3520 3530.
14. Lv L, Tang Y, Zhang P, Liu Y, Bai X, Zhou Y. Biomaterial Cues
Regulate Epigenetic State and Cell Functions-A Systematic Review.
Volume 21, Number 2, 2018
LV et al
[Epub ahead of print]
15. Lv L, Ge W, Liu Y, et al. Lysine-specific demethylase 1 inhibitor
rescues the osteogenic ability of mesenchymal stem cells under
osteoporotic conditions by modulating H3K4 methylation. Bone Res
16. Huang da W, Sherman BT, Lempicki RA. Systematic and integrative
analysis of large gene lists using DAVID bioinformatics resources.
17. Juss J, Herre J, Begg M, et al. Genome-wide transcription profiling in neutrophils in acute respiratory distress syndrome. Lancet
18. Jain N, Iyer KV, Kumar A, Shivashankar GV. Cell geometric constraints induce modular gene-expression patterns via redistribution
of HDAC3 regulated by actomyosin contractility. Proc Natl Acad Sci
19. Talwar S, Jain N, Shivashankar GV. The regulation of gene expression
during onset of differentiation by nuclear mechanical heterogeneity.
20. Badique F, Stamov DR, Davidson PM, et al. Directing nuclear deformation on micropillared surfaces by substrate geometry and cytoskeleton organization. Biomaterials 2013;34:2991 3001.
21. Hadjidakis DJ, Androulakis II. Bone remodeling. Ann N Y Acad Sci
22. Franz S, Rammelt S, Scharnweber D, Simon JC. Immune responses
to implants a review of the implications for the design of immunomodulatory biomaterials. Biomaterials 2011;32:6692 6709.
Chinese Journal of Dental Research
23. Bintu L, Ishibashi T, Dangkulwanich M, et al. Nucleosomal elements that control the topography of the barrier to transcription. Cell
24. Yoo J, Kim J, Baek S, Park Y, Im H, Kim J. Cell reprogramming into
the pluripotent state using graphene based substrates. Biomaterials
25. Miousse IR, Currie R, Datta K, et al. Importance of investigating
epigenetic alterations for industry and regulators: An appraisal of
current efforts by the Health and Environmental Sciences Institute.
26. Dearfield KL, Gollapudi BB, Bemis JC, et al. Next generation testing
strategy for assessment of genomic damage: A conceptual framework
and considerations. Environ Mol Mutagen 2017;58:264 283.
27. Igarashi K, Ideta-Otsuka M, Narita M. The Current State and Future
Development of Epigenetic Toxicology [Article in Japanese]. Yakugaku Zasshi 2017;137:265 271.
28. Geim AK. Graphene: status and prospects. Science 2009;324:
29. Garcia-Sanchez D, van der Zande AM, Paulo AS, Lassagne B,
McEuen PL, Bachtold A. Imaging mechanical vibrations in suspended graphene sheets. Nano Lett 2008;8:1399 1403.
30. Lee C, Wei X, Kysar JW, Hone J. Measurement of the elastic properties and intrinsic strength of monolayer graphene. Science 2008;321:
31. Lee Y, Bae S, Jang H, et al. Wafer-scale synthesis and transfer of
graphene films. Nano Lett 2010;10:490 493.
