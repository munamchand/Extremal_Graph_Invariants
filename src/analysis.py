from src.invariants import wiener_index, sombor_index, zagreb_index
def extremal_invariant(trees, invariant_fn):
    max_tree = None
    min_tree = None

    max_value = float("-inf")
    min_value = float("inf")

    for T in trees:
        value = invariant_fn(T)

        if value > max_value:
            max_value = value
            max_tree = T

        if value < min_value:
            min_value = value
            min_tree = T

    return {
        "max_tree": max_tree,
        "min_tree": min_tree,
        "max_value": max_value,
        "min_value": min_value
    }