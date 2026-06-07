import pandas as pd
from generator import generate_trees
from analysis import extremal_invariant
from invariants import (
    wiener_index,
    sombor_index,
    zagreb_index
)

def run_experiment(n_values):

    results = []

    for n in n_values:

        trees = generate_trees(n)

        # Wiener
        w = extremal_invariant(trees, wiener_index)

        # Sombor
        s = extremal_invariant(trees, sombor_index)

        # Zagreb
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

    df = pd.DataFrame(results)
    return df