# Functional Sequence Characterization Pipeline

## BIOINFORMATICS PIPELINE PROJECT
**In-silico Identification and Functional Characterization of a Target Gene/Protein Using Sequence Analysis and Homology-Based Annotation**

---

##  Project Overview

This project implements a complete bioinformatics pipeline to computationally analyze an unknown biological sequence to predict its quality, similarity, and biological function. The pipeline follows a 6-step workflow from sequence retrieval to biological interpretation.

**Core Research Question:** 
> "Given an unknown or hypothetical biological sequence, how can we computationally analyze it to predict its quality, similarity, and biological function?"

---

##  Pipeline Steps

```
Sequence Retrieval (Step 1)
    ↓
Sequence Quality Analysis (Step 2)
    ↓
Sequence Filtering & Validation (Step 3)
    ↓
Homology Search - BLAST (Step 4)
    ↓
Functional Annotation (Step 5)
    ↓
Biological Interpretation (Step 6)
```

---

##  Project Structure

```
Functional_Sequence_Characterization/
├── data/
│   └── input_sequence.fasta          # Input: Unknown/hypothetical protein
├── analysis/
│   ├── sequence_qc.py                # Step 2: Quality control script
│   └── homology_analysis.py          # Step 4: BLAST analysis script
├── results/
│   ├── qc_summary.txt                # Step 2 output: QC report
│   ├── blast_results.txt             # Step 4 output: BLAST hits
│   └── functional_annotation.txt     # Step 5 output: Annotation report
└── README.md                         # This file
```

---

##  Sequence Information

**Query Sequence:** `unnamed protein product`
- **Length:** 505 amino acids
- **Source:** Hypothetical protein from *Escherichia coli*
- **Type:** Protein sequence

---

##  Results Summary

### Step 2: Quality Control 
- **Status:** PASSED
- **Length:** 505 aa (exceeds 300 aa threshold)
- **Quality:** High - No ambiguous residues, complete ORF
- **Decision:** Suitable for downstream analysis

### Step 4: Homology Search 
- **Top Hit:** dGTPase [Escherichia coli]
- **Identity:** 100% (505/505 aa)
- **E-value:** 0.0 (highly significant)
- **Protein Family:** dGTPase (Deoxyguanosinetriphosphate triphosphohydrolase)

### Step 5: Functional Annotation 
- **Predicted Function:** dGTP triphosphohydrolase activity
- **Pathway:** Nucleotide metabolism
- **EC Number:** EC 3.6.1.15
- **Confidence:** HIGH (Definitive identification)

**Gene Ontology Terms:**
- **Molecular Function:** dGTPase activity, hydrolase activity, metal ion binding
- **Biological Process:** Nucleoside triphosphate catabolic process, DNA metabolic process, DNA repair, DNA replication
- **Cellular Component:** Cytoplasm, cytosol

---

##  How to Run

### Prerequisites
```bash
pip install biopython
```

### Step 1: Quality Control
```bash
python analysis/sequence_qc.py
```
- Input: `data/input_sequence.fasta`
- Output: `results/qc_summary.txt`

### Step 2: BLAST Homology Search
```bash
python analysis/homology_analysis.py
```
- Input: Query sequence
- Output: `results/blast_results.txt`, `data/blastp_result.xml`

### Step 3: Functional Annotation
```bash
python analysis/annotation.py
```
- Input: `data/blastp_result.xml`
- Output: `results/functional_annotation.txt`

---

##  Biological Interpretation (Step 6)

### What does this sequence likely do?
This sequence encodes a **dGTPase (deoxyguanosinetriphosphate triphosphohydrolase)** enzyme, which plays a critical role in nucleotide metabolism.

### Why do we think so?
1. **100% sequence identity** with characterized dGTPase from *E. coli* K-12
2. **E-value of 0.0** indicates extremely significant homology
3. **Conserved across Enterobacteriaceae** family
4. **Multiple PDB structures** available (4X9E, 4XDS, 6OIW, etc.)

### What evidence supports this claim?
- **Experimental evidence:** Crystal structures confirm protein fold and active site
- **Functional studies:** Enzyme activity demonstrated in vitro
- **Genetic evidence:** Essential gene in *E. coli*
- **Evolutionary conservation:** Highly conserved across bacterial species

### Biological Significance:
- **DNA Repair:** Prevents mutagenic dGTP incorporation during replication
- **Nucleotide Pool Sanitization:** Maintains proper dNTP balance
- **Antimicrobial Target:** Potential target for antibiotic development

---

##  Files Description

| File | Description |
|------|-------------|
| `input_sequence.fasta` | Original query sequence (505 aa protein) |
| `qc_summary.txt` | Quality control analysis report |
| `blast_results.txt` | Parsed BLAST homology search results |
| `blastp_result.xml` | Raw BLAST output in XML format |
| `functional_annotation.txt` | Detailed functional annotation with GO terms |
| `sequence_qc.py` | Python script for quality control analysis |
| `homology_analysis.py` | Python script for BLAST parsing |
| `annotation.py` | Python script for functional annotation |

---

##  Tools Used

- **Biopython:** Sequence parsing and analysis
- **NCBI BLAST:** Homology search (blastp against nr database)
- **UniProt:** Protein annotation and GO terms

---

##  References

1. Altschul, S.F., et al. (1997). "Gapped BLAST and PSI-BLAST: a new generation of protein database search programs." Nucleic Acids Res. 25:3389-3402.
2. UniProt Consortium. (2023). "UniProt: the Universal Protein Knowledgebase." Nucleic Acids Res.
3. dGTPase structure: PDB entries 4X9E, 4XDS, 6OIW, 7U65

---

##  Author

**Student:** Muhammad Ali  
**Course:** Biopython - Project    
**Date:** 5-2-2026

---

##  License

This project is for the educational purposes as part of the Biopython course completion.

---

**Conclusion:** The analyzed sequence is definitively identified as **dGTPase** from *Escherichia coli* with 100% confidence, playing a crucial role in nucleotide metabolism and DNA repair processes.
