# Hub Genes, Possible Pathways and Predicted Drugs in

Source: Chinese Journal of Dental Research (CJDR)

Hub Genes, Possible Pathways and Predicted Drugs in
Hereditary Gingival Fibromatosis by Bioinformatics
Analysis
Rong Xia YANG1, Fan SHI1, Shu Ning DU1, Xin Yu LUO1, Wan Qing WANG1,
Zhi Lu YUAN1, Dong CHEN1
Objective: To explore potential pathogenic processes and possible treatments using unbiased
and reliable bioinformatic tools.
Methods: Gene expression profiles of control and hepatocyte growth factor (HGF) samples
conducted using R software (version 4.2.1, R Foundation, Vienna, Austria). Functional enrichment analyses were performed using the Gene Ontology (GO), Kyoto Encyclopaedia of Genes
and Genomes (KEGG) and Gene Set Enrichment Analysis (GSEA) databases, then the proteinprotein interaction (PPI) network was constructed to screen the top 10 hub genes. Finally,
five genes related to cell junctions were selected to build gene-miRNA interactions and predict
small-molecule drugs.
Results: A total of 342 downregulated genes and 188 upregulated genes were detected. Candidate pathways include the extracellular matrix (ECM) receptor interaction pathway, the TGF-β
signalling pathway and the cell adhesion molecule (CAM) pathway, which were discovered
through KEGG and GSEA enrichment studies. GO analyses revealed that these DEGs were
significantly enriched in cell adhesion, the adherens junction and focal adhesion. Five hub
genes (CDH1, SNAP25, RAC2, APOE and ITGB4) associated with cell adhesion were identified through PPI analysis. Finally, the gene-miRNA regulatory network identified three target
­miRNAs: hsa-miR-7110-5p, hsa-miR-149-3p and hsa-miR-1207-5p. Based on the gene expression profile, the small-molecule drugs zebularine, ecuronium and prostratin were selected for
their demonstrated binding activity when docked with the mentioned molecules.
Conclusion: This study offered some novel insights into molecular pathways and identified five
hub genes associated with cell adhesion. Based on these hub genes, three potential therapeutic
miRNAs and small-molecule drugs were predicted, which are expected to provide guidance for
the treatment of patients with HGF.
Keywords: CDH1, cell-cell junction, hereditary gingival fibromatosis, MiRNA, small-molecule
drugs
1 Department of Stomatology, The First Affiliated Hospital of Zhengzhou
University, Zhengzhou, P.R. China.
Corresponding author: Dr Dong CHEN, Department of Stomatology, The
First Affiliated Hospital of Zhengzhou University, No.1 Jianshe East Road,
Erqi District, Zhengzhou 450052, P.R. China. Tel: 86-371-66913114. Email:
chendongfmmu@163.com
This study was supported by The National Natural Science Foundation of
Chinese Journal of Dental Research
Hereditary gingival fibromatosis (HGF) is an uncommon condition characterised by localised or widespread
lesions on the gingiva and its cause is still unclear. It can
be inherited as autosomal dominant or recessive mode
and cause enlargement of the gingiva.1 An excessive
amount of gum tissue can cover the visible part of the
teeth, leading to tooth displacement, retention of primary teeth, and difficulties with speech and chewing.2
Rarely present at birth, alveolar ridge thickening often
Yang et al
starts when permanent teeth begin to emerge. It tends
to worsen during childhood and may occasionally persist into adolescence.3 Some drugs, including immunosuppressants, calcium channel blockers and antiseizure
medications, are also linked to gingival overgrowth.4 It
is important to establish an antidiastole and develop appropriate treatment plans based on the aetiology.
The pathological manifestations of the gingiva consisted of dense connective tissue that is rich in collagen fibre bundles and infiltrated by inflammatory
cells. Researchers have identified several hallmarks of
epithelial-to-mesenchymal transition (EMT), including
basal lamina rupture and migration of epithelial cells
into connective tissue.5,6 EMT is the process whereby
epithelial cells transform into fibroblast-like cells associated with organ development, oral submucous fibrosis and the invasion of oral squamous cell carcinoma
in oral tissue. Recently, EMT has been proposed as a
new pathogenic mechanism that contributes to the development of drug-induced gingival fibrosis.7,8 Cellular
proliferation and the abnormal accumulation of extracellular matrix (ECM) components, including collagen,
integrin, fibronectin and glycosaminoglycans, are also
the causes of gingival fibrosis. The molecular processes
that cause this pathogenic process, however, are not
fully understood.
Current treatment options for this condition are
limited to surgical procedures, such as gingivectomy
and gingivoplasty, which unfortunately have a high
recurrence rate.9 For clinical diagnosis and treatment,
it is crucial to understand the molecular and pathophysiological mechanisms of HGF. The purpose of this
study is to investigate the molecular pathways associated with the HGF RNA-seq datasets obtained from the
China National GeneBank Database (CNGBdb) and to
explore potential therapeutic targets.
Materials and methods
Data collection and processing
We downloaded the BAM-formatted human genome
RNA-seq datasets of primary fibroblasts from HGFs
and normal gingival tissues, which included two HGFs
and three normals (the BAM data of CNR0453836 is
incomplete), from CNGBdb (https://db.cngb.org/). In
our study, the data were first processed through a series
of steps: Trim Galore was used for quality control of
the CNP000099510 high-throughput data. STAR was
employed to compare the reference genome and RSEM
software was used to quantify gene expression.
Identification of differentially expressed genes (DEGs)
The original datasets were converted into a recognisable
format using R software (version 4.2.1), The “DESeq2”
R package was then used to normalise and identify differentially expressed genes (DEGs). The threshold values for DEG detection were determined to be |log2(fold
change [FC])| > 1 and P < 0.05. A volcano plot was created
using http://www.sangerbox.com.11
Kyoto Encyclopedia of Genes and Genomes (KEGG)
and Gene Ontology (GO) analysis
Kyoto Encyclopedia of Genes and Genomes (KEGG)
pathway enrichment analysis was conducted in R software using the package “clusterProfiler”. Gene Ontology
(GO) analysis, which includes enrichment for biological
processes (BPs), cellular components (CCs) and molecular functions (MFs), was conducted via http://metascape.
org. P < 0.05 was considered statistically significant.
Further Gene Set Enrichment Analysis (GSEA) analysis
All genomic data from both HGFs and normal gingival
samples were uploaded to for Gene Set Enrichment Analysis (GSEA). Enrichments were considered significant
when the NES > 1.0, the normalised P < 0.05 and the
Construction of protein-protein interaction (PPI)
network
The Search Tool for the Retrieval of Interacting Genes
(STRING, https://string-db.org) was used to identify
protein-protein interactions (PPI) among DEGs. The
interaction score was set at 0.4. The result of the PPI
network was processed and analysed using Cytoscape
version 3.9.1. The key genes in the PPI network were
then screened using the CytoHubb plugin.
Further screening of hub genes
Hub gene–associated cell junctions according to the
STRING database were further screened and the evidence was listed.
Gene-miRNA network construction
Targeted miRNAs were predicted using miRWalk 3.0
(http://mirwalk.umm.uni-heidelberg.de/) and the
miRDB database (http://www.mirdb.org/). The minimum seed sequence length was set to 6 mer and the
Volume 27, Number 1, 2024
Yang et al
Fig 1 Volcano plot of 530 DEGs. The black dots represent genes with no appreciable variation in expression, whereas the red and
green dots represent genes that are upregulated and downregulated genes, respectively (a). Heatmap of all DEGs in the HGF group
and normal group. N represents gingival fibroblasts from normal and H represents gingival fibroblasts from HGF (b). Upregulated
genes as identified by KEGG, ECM receptor interaction and the TGF-β signalling pathway are significantly enriched (c). Downregulated
genes as identified by KEGG and CAMs are significantly enriched (d). Upregulated genes as identified by GO analysis and extracellular matrix are significantly enriched (e). Downregulated genes as identified by GO analysis and cell‐cell adhesion are significantly
enriched (f). Pathway and CC enrichment plots of GSEA showed CAMs pathways, ECM receptor interaction pathway, TGF-β signalling
pathway and cell-cell adhesion in HGF are more active than normal (g).
Chinese Journal of Dental Research
Yang et al
selection criteria were set at P < 0.95. MiRNAs that target
more than two genes were selected as a result.
Small-molecule drug prediction
Connectivity Map (https://clue.io/) is an online database of chemical reagent action expression profiles.
We inputted the top 150 upregulated genes and the top
150 downregulated DEGs into the Query tool. From the
results, we selected the top three small-molecule chemical medicines with the highest scores to be molecularly
docked with hub genes.
Molecular docking
The PDB database (http://www.rcsb.org/) was used to
obtain the 3D structures of the protein molecules, and
the PubChem database (https://pubchem.ncbi.nlm.nih.
gov/) was employed to obtain the structures of the smallmolecule medications. The 3D structure was examined using the molecular docking program AutoDock
Vina1.2.0 and 3D docking pictures were generated using
PyMOL 2.5.2. It is widely acknowledged that a specific
binding activity between the small-molecule medication and the protein when the binding energy is less
than −4.25 kcal/mol. Additionally, when the binding energy is less than −5.0 kcal/mol, it is deemed that the two
have a strong binding activity.12
d). GO analysis results showed that changes in BPs of
DEGs were significantly enriched in several categories,
including cell‐cell adhesion, cell junction organisation,
extracellular matrix, regulation of transforming growth
factor beta production and collagen fibril organisation.
Changes in cell-substrate junctions and the extracellular
matrix were primarily enriched in CCs (Fig 1e and f).
GSEA analysis
GSEA analysis found that cell-cell junctions, CAMs pathways, the ECM receptor interaction pathway and TGF-β
signalling pathway were significantly enriched in the
HGF group (Fig 1g).
Construction and analysis of the PPI network
A PPI network was established that included upregulated and downregulated genes based on a combined
score > 0.4, which was considered statistically significant. Cytoscape software (version 3.9.1) was used to
visualise the integrated regulatory network and identify
the high (marked in red) and low (marked in green) levels of gene expression (Fig 2a). The top 10 genes, ranked
by betweenness level using the CytoHubba plugin in
Cytoscape, were chosen (Fig 2b). These genes included
CDH1, SNAP25, RAC2, APOE, ITGB4, SFN, AHR, CXCL12,
SCN2A and CD24 (Table 1).
Statistical analysis
Further screening of hub genes
All analyses were performed using R software. The
“DESeq2” R package used negative binomial distribution
and functional enrichment anlyses used a hypergeometric test. Significance was defined as P < 0.05.
Five hub genes associated with cell adhesion according
to the String database were screened out, namely CDH1,
SNAP25, RAC2, APOE and ITGB4 (Fig 2c), and the evidence was listed (knowledge and text mining) (Table 2).
Results
Further miRNA mining and interaction network
analysis
DEG analysis
Predicted miRNAs for five genes associated with cell
adhesion and gene-miRNA interactions were visualised
in Cytoscape 3.9.1 (Fig 3). Target miRNAs with a high
number of gene crosslinks ≥ 2 were selected, including
hsa-miR-7110-5p, hsa-miR-149-3p and hsa-miR-1207-5p.
The CNP0000995 dataset contained 530 DEGs, including
188 upregulated genes and 342 downregulated genes.
These DEGs were presented in a volcano plot (Fig 1a)
and a heatmap (Fig 1b).
Enriched GO, KEGG pathway analysis of the DEGs
For the analysis of GO and KEGG pathway enrichment,
the ECM receptor interaction pathway, TGF-β signalling pathway and cell adhesion molecule (CAM) were
significantly enriched in the KEGG analysis (Fig 1c and
Small-molecule drug screening
The gene expression profile was compared and examined using the Connectivity Map database. We selected
three small-molecule drugs with the potential to modify the expression profile and ranked them in order of
effectiveness, from highest to lowest. First was zebular-
Volume 27, Number 1, 2024
Yang et al
Fig 2 PPI network of DEGs formed using
Cytoscape, with red and green dots representing genes that are upregulated and downregulated, respectively (a). Ten hub genes (CDH1,
SNAP25, RAC2, APOE, ITGB4, SFN, AHR,
CXCL12, SCN2A and CD24) with the greatest
significance were chosen in the PPI network
and the colour from red to yellow indicates
high to low scores (b). Five hub genes (CDH1,
SNAP25, RAC2, APOE and ITGB4) associated
with cell adhesion were chosen (marked in
green) (c).
Table 1
Top 10 genes in the network ranked by betweenness method.
Rank
Symbol
Up/down
Score
DH1
SNAP25
RAC2
APOE
ITGB4
SFN
AHR
CXCL12
SCN2A
CD24
Down
Down
Down
Down
Down
Down
Up
Down
Down
Down
Table 2
Evidence for five genes.
Knowledge
Text mining
Name
Source
Evidence
Confidence
APOE
UniProtKB
IDA/CURATED
★★★★★
CDH1
UniProtKB
IDA
★★★★★
ITGB4
UniProtKB
IDA/CURATED
★★★★★
Confidence
Name
Z-score
CDH1
★★★★
RAC2
★★★
SNAP25
★★★★
ine, a DNA methyltransferase inhibitor, with an enrichment score of −85.32. Second was vecuronium, which
acts as an antagonist to the acetylcholine receptor, with
Chinese Journal of Dental Research
an enrichment score of −82.22, and third was prostratin, a PKC activator, with an enrichment score of −81.29
(Table 3).
Yang et al
Fig 3 Gene-miRNA interactions were constructed according to miRWalk 3.0 and the miRDB database. Genes are represented by
the red dot, and target miRNAs are represented by the blue dot. Target miRNAs include hsa-miR-7110-5p, hsa-miR-149-3p and hsamiR-1207-5p.
Table 3
Small-molecule drug Information.
Rank
ID
Type
Name
Description
Score
CP
CP
CP
Zebularine
Vecuronium
Prostratin
DNA methyltransferase inhibitor
Acetylcholine receptor antagonist
PKC activator
CP, compound; ID, broad identity.
Molecular docking
We docked zebularine, vecuronium and prostratin with
the five molecules (APOE, CDH1, RAC2, SNAP25 and
ITGB4). Table 4 displays the data for molecular docking
and binding energy. The binding site map for vecuronium and APOE is shown in Fig 4a. Through ARG-32,
APOE interacts with ligands to form hydrogen bonds.
The binding energy of Selumetinib with DCT is −6.18
kcal/mol, indicating high binding activity. The binding site map for vecuronium and CDH1 is presented in
Fig 4b. Through ILE-146, CDH1 interacts with ligands
to form hydrogen bonds. The binding energy of Selumetinib with DCT is −4.52 kcal/mol, indicating strong
binding activity. A diagram of the prostratin and CDH1
binding site is shown in Fig 4c. Through ALA-132, GLU129 and TYR-148, CDH1 interacts with ligands via hydrogen bonds. The binding energy of Selumetinib with DCT
is 4.52 kcal/mol, suggesting some binding activity. Fig 4d
shows the binding site map of zebularine and RAC2.
RAC2 interacts with ligands through GLN-180 and TYR154, forming a hydrogen bond. Zebularine and RAC2
have a binding energy of −4.44 kcal/ mol, suggesting that
they exhibit binding activity.
Volume 27, Number 1, 2024
Yang et al
Fig 4 Molecular docking
modes according to AutoDock Vina1.2.0. The binding energy of APOE complexed with vecuronium
was −6.18 kcal/mol (a).
The binding energy of CDH1
complexed with vecuronium was −4.52 kcal/mol (b).
The binding energy of CDH1
complexed with prostratin
was −4.52 kcal/mol (c).
The binding energy of RAC2
complexed with zebularine
was −4.44 kcal/mol (d).
Table 4
Docking parameters and results.
No.
Target
Protein
Compound
Minimum binding energy(kcal/mol)
APOE
APOE
APOE
CDH1
CDH1
CDH1
RAC2
RAC2
RAC2
SNAP25
SNAP25
SNAP25
ITGB4
ITGB4
ITGB4
Synaptosomal-associated protein 25
Synaptosomal-associated protein 25
Synaptosomal-associated protein 25
Cadherin 1
Cadherin 1
Cadherin 1
Rac Family Small GTPase 2
Rac Family Small GTPase 2
Rac Family Small GTPase 2
Synaptosome Associated Protein 25
Synaptosome Associated Protein 25
Synaptosome Associated Protein 25
Integrin Subunit Beta 4
Integrin Subunit Beta 4
Integrin Subunit Beta 4
Vecuronium
Prostratin
Zebularine
Vecuronium
Prostratin
Zebularine
Vecuronium
Prostratin
Zebularine
Vecuronium
Prostratin
Zebularine
Vecuronium
Prostratin
Zebularine
Discussion
The present authors identified 530 DEGs, including 188
upregulated genes and 342 downregulated genes. The
ECM receptor interaction pathway, TGF-β signalling
pathway and CAMs pathway were all involved in HGF,
according to KEGG and GSEA enrichment studies. GO
functional analysis showed that DEGs were primarily
enriched in cell adhesion, the adherens junction and
focal adhesion. In addition, five genes (CDH1, SNAP25,
RAC2, APOE and ITGB4) associated with cell adhesion
were screened. Finally, the authors made predictions of
Chinese Journal of Dental Research
miRNA molecules and small-molecule drugs based on
these five hub genes.
The aetiology of HGF is most significant histologically in terms of increased ECM accumulation and
degeneration. TGF-β, a multifunctional cytokine that
plays a key role in inflammation, wound healing and
fibrosis, is an important contributor to ECM deposition
and EMT processes in tissue fibrosis.13,14 The findings
of our bioinformatics analytics fully align with these
conclusions.
In this study, we also discovered that the CAMs pathway was significantly enriched in the KEGG and GSEA
Yang et al
analyses. Furthermore, the GO analysis focused on cell
adhesion, adherens junction and focal adhesion. Cell
adhesion refers to the ability of a single cell to adhere to
the surface of another cell or another inanimate object,
such as ECM. To establish connections between cells
or between cells and the extracellular matrix, the process of cell adhesion relies on a wide range of proteins
known as CAMs, including integrins, selectins, cadherins, members of the immunoglobulin superfamily
(IgSF) and mucins.15 CAMs have mostly been studied
in relation to tumours and can mediate the interaction
between tumour cells and host cells and ECM, playing
a crucial role in the multi-stage sequential process of
tumour metastasis.16 However, some studies also suggest that CAMs can contribute to fibrosis in different
organs, such as the liver17 and lungs.18
CDH1, a transmembrane adhesion receptor involved
in the regulation of cell adhesion, migration and epithelial cell proliferation19, scored highest among the
five hub genes. Downregulation of CDH1 is considered
a crucial event in the progression of EMT. Iwano et
al20 found that type II EMT is the primary source of
fibroblasts in connective tissue fibrosis. Another study
suggests that cyclosporin A can induce type II EMT in
gingiva by modifying the morphology of epithelial cells
and changing the EMT markers, such as CDH1.21 The
pathogenic function of type II EMT in HGF, however,
remains unclear. Roman-Malo et al5 observed some
histologic features that have been described for EMT in
gingival lesions of HGF patients. Based on the above information, we hypothesise that the downregulation of
CDH1 leads to the loss of intercellular adhesion, which
in turn induces type II EMT and ultimately results in
HGF fibrosis. Nevertheless, this is only an initial hypothesis, and more trials are required to confirm it.
The laminin receptor ITGB4, a vital structural component of the hemidesmosome in epithelial cells, was
found to be downregulated in our study.22 It plays a
crucial role in tissue morphogenesis by regulating cell
adhesion, morphology, polarity and differentiation.
According to studies, renal fibrosis and herpes epidermolysis bullosa are linked to the ITGB4 gene.23,24
Nevertheless, there is insufficient data regarding the
connection between IGTB4 and gingival fibrosis.
MiRNAs are a type of traditional non-coding RNA
that play a role in regulating various physiological and
pathological functions.25 Current studies have shown
that microRNA may participate in the fibrosis of various organs.26 In HGF, the expression of miR-355-3p is
downregulated in gingival fibroblasts as well as in nor-
mally occurring human gingival fibroblasts stimulated
by TGF-β.27 In this study, we predicted the miRNAs
through the database, resulting in three: hsa-miR-71105p, hsa-miR-149-3p and hsa-miR-1207-5p.
Hsa-miR-1207-5p has been reported to be closely
associated with cancer development and metastasis.
It may function as a novel EMT-negative regulator
inhibiting the invasion and metastasis of cancer cells
in nasopharyngeal, gastric, lung and oral cancers.28-30
MiR-149-3p has been proven to be closely associated
with liver and lung fibrosis and may be involved in
the EMT process in tumour cells. However, no study
has shown that the aforementioned miRNA molecules
are associated with therapeutic treatments for gingival fibrosis. This association needs to be confirmed
through further trials.
The present study has certain limitations because
the sample size is small, which restricts the scope of
analysis. In the absence of experimental confirmation,
further fundamental studies are required to validate
the results and identify the crucial genes and pathways.
Additionally, further research must be conducted to investigate whether small-molecule medications and the
miRNAs discovered can serve as potential therapeutic
targets for HGF.
Conclusion
The present authors found potential pathogenic pathways, such as the CAMs pathway and ECM receptor interaction pathway. GO analysis suggested that cell adhesion may potentially play a role in HGF. The authors also
screened hub genes involved in cell adhesion, including
CDH1, SNAP25, RAC2, APOE and ITGB4.
Conflicts of interest
The authors declare no conflicts of interest related to
this study.
Author contribution
Drs Rong Xia YANG, Fan SHI, Shu Ning DU, Xin Yu LUO,
Wan Qing WANG and Zhi Lu YUAN contributed to the
data analysis; Dr Rong Xia YANG contributed to the
manu­script draft; Dr Dong CHEN contributed to the
study conception and manuscript revision.
(Received Jun 30, 2023; accepted Nov 23, 2023)
Volume 27, Number 1, 2024
Yang et al
References
Strzelec K, Dziedzic A, Łazarz-Bartyzel K, et al. Clinics and
genetic background of hereditary gingival fibromatosis.
Orphanet J Rare Dis 2021;16:492.
Afonso RA, Godinho GV, Silva CA, Silva EJ, Volpato LE. Hereditary gingival fibromatosis and developmental anomalies: A
case report. Cureus 2022;14:e24219.
Resende EP, Xavier MT, Matos S, Antunes AC, Silva HC. Nonsyndromic hereditary gingival fibromatosis: Characterization
of a family and review of genetic etiology. Spec Care Dentist
Bakshi SS, Choudhary M, Agrawal A, Chakole S. Drug-induced
gingival hyperplasia in a hypertensive patient: A case report.
Roman-Malo L, Bullon B, de Miguel M, Bullon P. Fibroblasts
collagen production and histological alterations in hereditary
gingival fibromatosis. Diseases 2019;7:39.
Bawazir M, Islam MN, Cohen DM, Fitzpatrick S, Bhattacharyya I. Gingival fibroma: An emerging distinct gingival lesion with well-defined histopathology. Head Neck Pathol
Hazzaa HH, Gouda OM, Kamal NM, et al. Expression of CD163
in hereditary gingival fibromatosis: A possible association
Kamal NM, Hamouda MA, Abdelgawad N. Expression of
TGF-β and MMP-2 in hereditary gingival fibromatosis epithelial cells. A possible contribution of the epithelium to its
pathogenesis. J Oral Biol Craniofac Res 2022;12:617−622.
Bektaş-Kayhan K, Selvi F, Koca-Ünsal RB. Surgical treatment
of hereditary gingival fibromatosis by diode laser: Report
of five rare cases in the same family. Spec Care Dentist
Wu J, Chen D, Huang H, et al. A novel gene ZNF862 causes
hereditary gingival fibromatosis. Elife 2022;11:e66646.
Shen W, Song Z, Zhong X, et al. Sangerbox: A comprehensive,
interaction-friendly clinical bioinformatics analysis platform.
Li C, Shi Y, Zuo L, et al. Identification of biomarkers associated with cancerous change in oral leukoplakia based on
integrated transcriptome analysis. J Oncol 2022;2022:4599305.
Budi EH, Schaub JR, Decaris M, Turner S, Derynck R. TGF-β as
a driver of fibrosis: Physiological roles and therapeutic opportunities. J Pathol 2021;254:358−373.
Walton KL, Johnson KE, Harrison CA. Targeting TGF-β mediated SMAD signaling for the prevention of fibrosis. Front
Samanta D, Almo SC. Nectin family of cell-adhesion molecules: Structural and molecular aspects of function and specificity. Cell Mol Life Sci 2015;72:645−658.
Chinese Journal of Dental Research
16. Harjunpää H, Llort Asens M, Guenther C, Fagerholm SC.
Cell adhesion molecules and their roles and regulation in
the immune and tumor microenvironment. Front Immunol
17. Hintermann E, Christen U. The many roles of cell adhesion
molecules in hepatic fibrosis. Cells 2019;8:1503.
18. Hu Q, Saleem K, Pandey J, Charania AN, Zhou Y, He C. Cell
adhesion molecules in fibrotic diseases. Biomedicines
19. Meigs TE, Fedor-Chaiken M, Kaplan DD, Brackenbury R, Casey
PJ. Galpha12 and Galpha13 negatively regulate the adhesive
functions of cadherin. J Biol Chem 2002;277:24594−24600.
20. Iwano M, Plieth D, Danoff TM, Xue C, Okada H, Neilson EG.
Evidence that fibroblasts derive from epithelium during tissue fibrosis. J Clin Invest 2002;110:341−350.
21. Fu MM, Chin YT, Fu E, et al. Role of transforming growth
factor-beta1 in cyclosporine-induced epithelial-to-mesenchymal transition in gingival epithelium. J Periodontol
22. Du X, Yuan L, Yao Y, et al. ITGB4 deficiency in airway epithelium aggravates RSV infection and increases HDM sensitivity.
23. Luo C, Yang L, Huang Z, et al. Case report: A case of epidermolysis bullosa complicated with pyloric atresia and a literature
review. Front Pediatr 2023;11:1098273.
24. Wee LWY, Tan EC, Bishnoi P, et al. Epidermolysis bullosa with
pyloric atresia associated with compound heterozygous ITGB4
pathogenic variants: Minimal skin involvement but severe
mucocutaneous disease. Pediatr Dermatol 2021;38:908−912.
25. Ho PTB, Clark IM, Le LTT. MicroRNA-based diagnosis and
therapy. Int J Mol Sci 2022;23:7167.
26. Ghafouri-Fard S, Abak A, Talebi SF, et al. Role of miRNA and
lncRNAs in organ fibrosis and aging. Biomed Pharmacother
27. Gao Q, Yang K, Chen D, et al. Antifibrotic potential of MiR335-3p in hereditary gingival fibromatosis. J Dent Res
28. Chen L, Lü MH, Zhang D, et al. miR-1207-5p and miR-1266
suppress gastric cancer growth and invasion by targeting telomerase reverse transcriptase. Cell Death Dis 2014;5:e1034.
29. Alvarez ML, Khosroheidari M, Eddy E, Kiefer J. Role of microRNA 1207-5P and its host gene, the long non-coding RNA
Pvt1, as mediators of extracellular matrix accumulation in
the kidney: Implications for diabetic nephropathy. PLoS One
30. Dang W, Qin Z, Fan S, et al. miR-1207-5p suppresses lung
cancer growth and metastasis by targeting CSF1. Oncotarget
