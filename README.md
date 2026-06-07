# Graph Invariants and Extremal Analysis of Trees

## Overview
This project implements classical and modern graph invariants (Wiener index, Zagreb indices, and Sombor index) and performs extremal analysis on tree graphs.

We study how different tree structures affect these indices and identify trees that maximize or minimize specific invariants.

---

## Features
- Generation of tree graphs (order n)
- Implementation of graph invariants:
  - Wiener Index
  - Zagreb Index (First & Second)
  - Sombor Index
- Extremal analysis (max/min Wiener index trees)
- Visualization of graphs

---

## Project Structure

- generator.py        → Tree generation
- invariants.py       → Graph invariant definitions
- analysis.py         → Extremal analysis (max/min)
- visualization.py    → Graph drawing utilities
- main.py             → Main execution pipeline

---

## Mathematical Background
For a graph \(G\):

- Wiener Index:
  \( W(G) = \sum d(u,v) \)

- First Zagreb Index:
  \( M_1(G) = \sum d(v)^2 \)

- Second Zagreb Index:
  \( M_2(G) = \sum d(u)d(v) \)

- Sombor Index:
  \( SO(G) = \sum \sqrt{d(u)^2 + d(v)^2} \)

---

## How to Run
```bash
python main.py
