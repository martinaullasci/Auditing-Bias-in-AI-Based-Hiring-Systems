# Auditing Bias in AI-Based Hiring Systems
### A Fairness Analysis of Nationality and Gender Discrimination

This repository contains the replication package for the paper:

> *Auditing Bias in AI-Based Hiring Systems: A Fairness Analysis of Nationality and Gender Discrimination*  

---

## Overview

This study audits an embedding-based CV–job matching pipeline built on [Sentence-BERT (SBERT)](https://www.sbert.net/) to evaluate systematic disparities related to **gender** and **nationality**. Using a synthetic dataset of controlled candidate profiles, the analysis is conducted across three stages of the recruitment pipeline: similarity score computation, threshold-based screening and Top-K ranking.

---

## Repository Structure

```
├── cv_dataset_expanded/        # 384 synthetic candidate profiles (.txt)
│                               # Filename format: JOB_LEVEL_NAT_GENDER_VERSION.txt
│                               # e.g., MKT_JR_IT_F_V1.txt
├── job_descriptions/           # 16 job descriptions (4 roles × 4 hierarchy levels)
│   ├── JD_CC_JR.txt            # Content/Creative Manager – Junior
│   ├── JD_HR_SR.txt            # HR Specialist – Senior
│   └── ...                     # (PM, MKT, HR, CC × JR, MID, SR, MGR)
├── results/
│   ├── final_bias_audit_results.csv          # Similarity scores with full metadata
│   ├── final_bias_audit_results_for_excel.xlsx
│   ├── ANOVA__no_hierarchy_level_.csv        # ANOVA results (aggregate)
│   ├── ANOVA__with_hierarchy_level___interactions_.csv
│   ├── ANOVA_within_each_level__Gender___Nationality_effects_.csv
│   ├── bias_audit_tables.md                  # Summary tables
│   └── bias_audit_tables_full.md
├── scripts_graphs/             # Visualization scripts for figures in the paper
├── mass_generator.py           # Generates cv_dataset_expanded from base profiles
├── run_audit.py                # Main pipeline: computes cosine similarity scores
├── requirements.txt
└── README.md
```

---

## Dataset

The synthetic dataset follows a **full factorial design**:

| Dimension | Levels |
|---|---|
| Job roles | Project Manager (PM), Market Research Analyst (MKT), HR Specialist (HR), Content/Creative Manager (CC) |
| Hierarchy levels | Junior (JR), Mid-level (MID), Senior (SR), Manager (MGR) |
| Nationalities | Italian (IT), Albanian (AL), British (BR), Moroccan (MO) |
| Genders | Male (M), Female (F) |
| Lexical versions | V1 (formal), V2 (action-oriented), V3 (technical) |

Total: **4 × 4 × 4 × 2 × 3 = 384 profiles**

Each profile is generated from a base CV by replacing `[NATIONALITY]` and `[GENDER]` placeholders, keeping all job-relevant content identical. This enables counterfactual comparison across demographic groups.

---

## How to Replicate

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Generate the expanded dataset** (optional, already included)
```bash
python mass_generator.py
```

**3. Run the audit pipeline**
```bash
python run_audit.py
```

This computes cosine similarity scores between each CV and its corresponding job description using `all-MiniLM-L6-v2` and saves the results to `results/final_bias_audit_results.csv`.

---

## Model

- **Model:** `all-MiniLM-L6-v2` via [sentence-transformers](https://www.sbert.net/)
- **Similarity metric:** Cosine similarity
- **Embedding size:** 384 dimensions
- **Aggregation:** Mean pooling over token embeddings

---

## Requirements

See `requirements.txt`. Main dependencies:
- `sentence-transformers`
- `pandas`
- `scipy`
- `matplotlib`
- `seaborn`
