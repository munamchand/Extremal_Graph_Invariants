import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(G, title="Graph"):

    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    

    nx.draw(
        G, 
        pos,
        with_labels=True,
        node_size=700
    )

    plt.title(title)

    plt.show()