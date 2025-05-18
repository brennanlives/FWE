Examples for *Fractal-Weighted Efficiency* (FWE)
=======
# Fractal-Weighted Efficiency (FWE) · companion repository  

<sup>Repository for **“Fractal-Weighted Efficiency: A Scale-Agnostic Metric Linking Energy and Structure”** (O’Rear et al., 2025).  
Clean code, processed tables, and lightweight toy data reproduce every figure and numerical example in the manuscript.</sup>

---

## 1 Overview  

This repo contains only:

| folder | contents |
|--------|-----------|
| **data/raw/** | small public-domain source files **or** 1-line stub files that point to large external downloads (MLPerf power logs, light-sheet image stacks, …) |
| **data/processed/** | cleaned CSVs & figures ready for plotting / statistics |
| **scripts/** | single-run CLI tools that build the paper’s tables |
| **notebooks/** | step-by-step Jupyter notebooks for each illustrative example |
| **docs/** | PDF of the paper and supplementary diagrams |

> **Large binaries** are *not* tracked in Git.  
> Run `scripts/get_large_data.sh` to fetch them on-demand.

---

## 2 Quick start

```bash
# 1 create the environment
conda env create -f environment.yml     # Python 3.10, pandas, scikit-image …
conda activate fwe

# 2 rebuild one example table
python scripts/compute_eta_edge.py      # reproduces Table 8, writes data/processed/…

# 3 interactive exploration
jupyter lab                             # open notebooks/ for walk-throughs
>>>>>>> 8ac4732 (Clean README; prune temporary folders)
