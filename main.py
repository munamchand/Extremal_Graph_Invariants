from src.generator import generate_trees

from src.analysis import extremal_wiener

from src.visualization import draw_graph

trees = generate_trees(10)

result = extremal_wiener(trees)

print("MAXIMUM WIENER INDEX")
print("---------------------")

print("Value:", result["max_value"])

print("Edges:", list(result["max_tree"].edges()))

print()

print("MINIMUM WIENER INDEX")
print("---------------------")

print("Value:", result["min_value"])

print("Edges:", list(result["min_tree"].edges()))

draw_graph(
    result["max_tree"],
    title="Maximum Wiener Index Tree"
)

draw_graph(
    result["min_tree"],
    title="Minimum Wiener Index Tree"
)
