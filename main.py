from src.experiments import run_experiment
from src.visualition import draw_graph
import os

os.makedirs("outputs/csv", exist_ok=True)

def main():

    n_values = list(range(3, 11))  # for n = 3 to 10.

    df = run_experiment(n_values)

    print(df)

    df.to_csv("outputs/csv/invariant_growth.csv", index=False)

    print("Saved: outputs/csv/invariant_growth.csv")


if __name__ == "__main__":
    main()

# Draw Graphs
result = run_experiment(range(3, 11))

trees = generate_trees(10)

draw_graph(
    trees[0],
    "Example Tree",
    "outputs/figures/example.png"
)





