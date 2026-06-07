from src.generator import generate_trees

from src.analysis import extremal_wiener

from src.visualization import draw_graph
import pandas as pd

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

data = [
    {
        "Type": "Maximum Wiener Tree",
        "Value": result["max_value"],
        "Edges": list(result["max_tree"].edges())
    },
    {
        "Type": "Minimum Wiener Tree",
        "Value": result["min_value"],
        "Edges": list(result["min_tree"].edges())
    }
]

df = pd.DataFrame(data)
df.to_csv("outputs/csv/wiener_results.csv", index=False)