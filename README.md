# 📘 Extremal Graph Invariants on Trees

A computational research project for studying **Wiener, Sombor, and Zagreb indices** on tree graphs across different orders \( n \).  
The project performs **systematic extremal analysis (maximum and minimum values)** and generates both numerical and visual results.

---

# 📌 Research Objective

For each tree order \( n \in [3, 10] \), the system:

- Generates all non-isomorphic trees
- Computes graph invariants:
  - Wiener index
  - Sombor index
  - Zagreb index
- Finds:
  - Maximum invariant tree
  - Minimum invariant tree
- Stores results in structured datasets
- Visualizes both:
  - Growth trends (line plots)
  - Tree structures (NetworkX graphs)

---

# 📐 Mathematical Definitions

## Wiener Index

$$
W(G) = \sum_{u,v \in V(G)} d(u,v)
$$

---

## First Zagreb Index

$$
M_1(G) = \sum_{v \in V(G)} d(v)^2
$$

---

## Sombor Index

$$
SO(G) = \sum_{uv \in E(G)} \sqrt{d(u)^2 + d(v)^2}
$$

---

## Second Zagreb Index

$$
M_2(G) = \sum_{uv \in E(G)} d(u)d(v)
$$

---

# 🏗️ Project Structure

```text
Sombor_Index_calculator/
│
├── main.py
├── src/
│   ├── generator.py
│   ├── invariants.py
│   ├── analysis.py
│   ├── experiments.py
│   ├── visualization.py
│
├── outputs/
│   ├── csv/
│   │   └── invariant_growth.csv
│   └── figures/
│       ├── wiener_growth.png
│       ├── sombor_growth.png
│       ├── zagreb_growth.png
│       ├── wiener_max_n*.png
│       ├── wiener_min_n*.png
│       ├── sombor_max_n*.png
│       ├── sombor_min_n*.png
│       ├── zagreb_max_n*.png
│       └── zagreb_min_n*.png
```

---

# ⚙️ Workflow Pipeline

1. Generate trees for each \( n \)
2. Compute invariants for all trees
3. Extract extremal (max/min) trees
4. Store numerical results in CSV
5. Plot growth curves (n vs invariant values)
6. Visualize extremal tree structures

---

# 📊 Outputs

## 1. CSV Table

File:
```text
outputs/csv/invariant_growth.csv
```

Contains:

| n | Wiener max | Wiener min | Sombor max | Sombor min | Zagreb max | Zagreb min |

---

## 2. Growth Curves

Generated plots:

- Wiener index vs n
- Sombor index vs n
- Zagreb index vs n

Saved in:

```text
outputs/figures/
```

---

## 3. Tree Visualizations

For each \( n \):

- Maximum and minimum trees for each invariant

Saved as:

```text
outputs/figures/*_n*.png
```

---

# 🚀 How to Run

```bash
python main.py
```

---

# 📦 Dependencies

```bash
pip install networkx matplotlib pandas
```

---

# 📈 Research Contribution

This project enables:

- Comparative study of graph invariants
- Extremal tree structure identification
- Growth behavior analysis over increasing graph order
- Visualization of structural differences across invariants

---

# 🔭 Future Work

- Add ABC, Randic, Harary indices
- Study asymptotic extremal behavior
- Detect structural phase transitions
- Apply ML models to predict invariants
- Extend to chemical graph theory datasets

---

# 👨‍💻 Purpose

This repository is designed as a **computational graph theory framework** suitable for:

- Research exploration
- PhD applications
- Experimental combinatorics
- Chemical graph theory modeling