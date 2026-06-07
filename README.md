
# 📘 Graph Invariants and Extremal Analysis of Trees

---

## Abstract

This project implements classical and modern graph invariants on tree graphs, including the Wiener index, Zagreb indices, and Sombor index. It focuses on computational generation of trees and extremal analysis (maximum and minimum values) of these invariants. The pipeline is designed for reproducible experiments in computational graph theory.

---

## 1. Mathematical Background

Let \( G = (V, E) \) be a simple connected graph.

### Wiener Index

$$
W(G) = \sum_{u,v \in V(G)} d(u,v)
$$

---

### First Zagreb Index

$$
M_1(G) = \sum_{v \in V(G)} d(v)^2
$$

---

### Second Zagreb Index

$$
M_2(G) = \sum_{uv \in E(G)} d(u)d(v)
$$

---

### Sombor Index

$$
SO(G) = \sum_{uv \in E(G)} \sqrt{d(u)^2 + d(v)^2}
$$

---

## 2. Project Objective

- Generate tree graphs of order \( n \)
- Compute graph invariants
- Find extremal structures (max/min values)
- Visualize graph structures

---

## 3. Methodology

### 3.1 Project Structure

```text
generator.py      → Tree generation
invariants.py     → Graph invariant definitions
analysis.py       → Extremal analysis (max/min)
visualization.py  → Graph drawing utilities
main.py           → Execution pipeline
```

---

### 3.2 Workflow

1. Generate trees of order \( n \)
2. Compute invariants for each tree
3. Identify extremal cases
4. Save results (CSV)
5. Visualize graphs (PNG)

---

## 4. Experimental Results

### Maximum Wiener Index Tree
- Value: 165  
- Structure: computed extremal tree

### Minimum Wiener Index Tree
- Value: 81  
- Structure: computed extremal tree

---

## 5. How to Run

```bash
python main.py
```

---

## 6. Output Files

```text
outputs/
├── csv/
│   └── wiener_results.csv
└── figures/
    ├── max_wiener_tree.png
    └── min_wiener_tree.png
```

---

## 7. Visualization

Graphs are generated using NetworkX:

- Nodes = vertices
- Edges = connections
- Layout = spring embedding

---

## 8. Dependencies

```bash
pip install networkx matplotlib pandas
```

---

## 9. Future Work

- Chemical graph theory extensions
- Additional indices (ABC, GA, Randic)
- ML-based prediction of invariants
- Large-scale tree enumeration

---

## 10. Reproducibility

This project is fully reproducible and modular, allowing independent testing of graph invariants and structural comparison of trees.