from src.experiments import run_experiment
from src.visualization import draw_graph
import os

os.makedirs("outputs/figures", exist_ok=True)

n_values = range(3, 11)

results, trees = run_experiment(n_values)

for n in n_values:

    t = trees[n]

    draw_graph(
        t["wiener_max_tree"],
        f"Wiener Max (n={n})",
        f"outputs/figures/wiener_max_n{n}.png"
    )

    draw_graph(
        t["wiener_min_tree"],
        f"Wiener Min (n={n})",
        f"outputs/figures/wiener_min_n{n}.png"
    )

    draw_graph(
        t["sombor_max_tree"],
        f"Sombor Max (n={n})",
        f"outputs/figures/sombor_max_n{n}.png"
    )

    draw_graph(
        t["sombor_min_tree"],
        f"Sombor Min (n={n})",
        f"outputs/figures/sombor_min_n{n}.png"
    )

    draw_graph(
        t["zagreb_max_tree"],
        f"Zagreb Max (n={n})",
        f"outputs/figures/zagreb_max_n{n}.png"
    )

    draw_graph(
        t["zagreb_min_tree"],
        f"Zagreb Min (n={n})",
        f"outputs/figures/zagreb_min_n{n}.png"
    )