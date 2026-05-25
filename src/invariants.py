import networkx as nx

def wiener_index(G):

    total = 0

    for u in G.nodes():

        lengths = nx.single_source_shortest_path_length(G, u)

        for v in lengths:
            total += lengths[v]

    return total // 2