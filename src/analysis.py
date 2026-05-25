from src.invariants import (
    wiener_index,
    sombor_index,
    zagreb_index
)

def extremal_wiener(trees):

    max_tree = None
    min_tree = None

    max_value = float('-inf')
    min_value = float('inf')

    for tree in trees:

        w = wiener_index(tree)

        if w > max_value:
            max_value = w
            max_tree = tree

        if w < min_value:
            min_value = w
            min_tree = tree

    return {
        "max_tree": max_tree,
        "max_value": max_value,
        "min_tree": min_tree,
        "min_value": min_value
    }