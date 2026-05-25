from src.generator import generate_trees

from src.invariants import (
    wiener_index,
    sombor_index,
    zagreb_index
)

trees = generate_trees(5)

print("Number of non-isomorphic trees:", len(trees))

for i, tree in enumerate(trees):

    w = wiener_index(tree)
    s = sombor_index(tree)
    z = zagreb_index(tree)

    print(f"\nTree {i+1}")

    print("Edges:", list(tree.edges()))

    print("Wiener Index:", w)

    print("Sombor Index:", round(s, 4))

    print("Zagreb Index:", z)