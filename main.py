from src.generator import generate_trees

from src.analysis import extremal_wiener

trees = generate_trees(5)

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