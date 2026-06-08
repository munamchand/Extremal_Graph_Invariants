from src.experiments import run_experiment
from src.visualization import draw_full_page
import os

os.makedirs("outputs/figures", exist_ok=True)

n_values = range(4, 11)

results, trees = run_experiment(n_values)


for n in n_values:

    draw_full_page(
        n,
        trees[n],
        f"outputs/figures/summary_n{n}.png"
    )