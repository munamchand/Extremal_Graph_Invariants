import pandas as pd
from src.generator import generate_trees
from src.analysis import extremal_invariant
from src.invariants import wiener_index, sombor_index, zagreb_index


def run_experiment(n_values):

    results = []
    tree_store = {}

    for n in n_values:
    
        trees = generate_trees(n)

        w = extremal_invariant(trees, wiener_index)
        s = extremal_invariant(trees, sombor_index)
        z = extremal_invariant(trees, zagreb_index)

        results.append({
            "n": n,
            "wiener_max": w["max_value"],
            "wiener_min": w["min_value"],
            "sombor_max": s["max_value"],
            "sombor_min": s["min_value"],
            "zagreb_max": z["max_value"],
            "zagreb_min": z["min_value"],
        })

        tree_store[n] = {
            "wiener_max_tree": w["max_tree"],
            "wiener_min_tree": w["min_tree"],
            "sombor_max_tree": s["max_tree"],
            "sombor_min_tree": s["min_tree"],
            "zagreb_max_tree": z["max_tree"],
            "zagreb_min_tree": z["min_tree"],
        }

    return results, tree_store