# 📘 Extremal Analysis of Graph Invariants on Trees

This project performs computational analysis of distance-based and degree-based graph invariants on trees, focusing on their **extremal behavior (maximum and minimum values)** across different graph orders.

The main goal is to study how different invariants behave structurally and whether they induce similar or contrasting extremal tree configurations.

---

#  Graph Invariants Studied

## 1. Wiener Index
Measures total distance between all pairs of vertices:

$$
W(G) = \sum_{u,v \in V(G)} d(u,v)
$$

---

## 2. Sombor Index
A degree-based topological index:

$$
SO(G) = \sum_{uv \in E(G)} \sqrt{d(u)^2 + d(v)^2}
$$

---

## 3. Zagreb Index (First/Second variants implemented)

Degree-based structural indices used in chemical graph theory.

---

# Methodology

For each number of vertices $ ( n \in \{3, \dots, 10\} ) $ :

1. Generate all non-isomorphic trees
2. Compute:
   - Wiener index
   - Sombor index
   - Zagreb index
3. Identify:
   - Maximum value tree
   - Minimum value tree
4. Store results in structured dataset
5. Visualize:
   - Extremal trees
   - Growth trends

---

#  Project Structure

```text
Sombor_Index_Calculator/
│
├── main.py
│
├── src/
│   ├── generator.py          # Tree generation
│   ├── invariants.py         # Graph invariants
│   ├── analysis.py           # Extremal analysis
│   ├── experiments.py        # Multi-n pipeline
│   ├── visualization.py      # Graph drawing
│
├── outputs/
│   ├── csv/
│   │   └── invariant_growth.csv
│   └── figures/
│       ├── wiener_*_n*.png
│       ├── sombor_*_n*.png
│       ├── zagreb_*_n*.png
```

---

#  Experimental Outputs

## 1. Numerical Results (CSV)

Stored in:

```
outputs/csv/invariant_growth.csv
```

Contains:

| n | Wiener max | Wiener min | Sombor max | Sombor min | Zagreb max | Zagreb min |

---

## 2. Tree Visualizations

For each \( n \), extremal trees are saved:

- Wiener max/min trees
- Sombor max/min trees
- Zagreb max/min trees

Saved in:

```
outputs/figures/
```

---

## 3. Growth Curves

Plots show how each invariant evolves with increasing $\( n \)$.

---

#  Key Computational Observation

Based on computed results for $\( n = 3 \)$ to $\( n = 10 \)$:

## 1. Sombor and Zagreb Indices
- Their extremal trees (maximum and minimum) are observed to coincide for all tested values of \( n \).
- This suggests strong structural similarity in how these degree-based indices optimize tree configurations.

⚠️ This is an experimental observation and may not hold for larger \( n \).

---

## 2. Wiener Index
- Displays contrasting extremal behavior compared to Sombor and Zagreb indices.
- Observed pattern:
  - Maximum Wiener index corresponds to path-like structures
  - Minimum Wiener index corresponds to star-like structures

---

#  How to Run

```bash
python main.py
```

---

#  Requirements

```bash
pip install networkx matplotlib pandas
```

---

#  Scientific Contribution

- Developed a computational framework for analyzing graph invariants on trees across varying orders \( n \).
- Studied extremal behavior (maximum and minimum values) of Wiener, Sombor, and Zagreb indices.
- Compared structural differences between distance-based (Wiener) and degree-based (Sombor, Zagreb) invariants.
- Identified consistent similarity between extremal structures of Sombor and Zagreb indices in the tested range.
- Observed contrasting extremal behavior of the Wiener index relative to degree-based indices.
- Generated reproducible pipeline for tree generation, invariant computation, extremal detection, and visualization.
- Provided empirical insights into structural patterns of extremal trees for small to moderate \( n \).
---

#  Future Work

- Extend to larger \( n \)
- Add additional indices (Randić, ABC, harmonic index)
- Automate structural isomorphism comparison of extremal trees
- Statistical correlation analysis between invariants
- Investigate asymptotic extremal behavior

---

#  Purpose

This repository is designed as a **computational graph theory research project**, suitable for:

- Chemical graph theory exploration
- Experimental combinatorics studies
- Algorithmic graph theory research