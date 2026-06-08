import matplotlib.pyplot as plt
import networkx as nx
import os

def draw_full_page(n, trees_dict, save_path):

    """
    Creates ONE image per n containing:
    6 graphs:
    - Wiener Max / Min
    - Sombor Max / Min
    - Zagreb Max / Min
    """

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    items = [
        ("Wiener Max", trees_dict["wiener_max_tree"]),
        ("Sombor Max", trees_dict["sombor_max_tree"]),
        ("Zagreb Max", trees_dict["zagreb_max_tree"]),
        ("Wiener Min", trees_dict["wiener_min_tree"]),
        ("Sombor Min", trees_dict["sombor_min_tree"]),
        ("Zagreb Min", trees_dict["zagreb_min_tree"]),
    ]

    for ax, (title, G) in zip(axes.flatten(), items):

        pos = nx.spring_layout(G, seed=42)

        nx.draw(
            G,
            pos,
            ax=ax,
            with_labels=True,
            node_size=500,
            font_size=8
        )

        ax.set_title(title)

    fig.suptitle(f"Extremal Trees Comparison (n={n})", fontsize=16)

    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300)

    plt.close()


    

