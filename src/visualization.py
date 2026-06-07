import matplotlib.pyplot as plt
import networkx as nx
import os

def draw_graph(G, title, filename=None):

    plt.figure(figsize=(6, 6))

    pos = nx.spring_layout(G, seed=42)  # stable layout

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=600,
        font_size=10
    )

    plt.title(title)

    if filename:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.show()
    plt.close()


    

