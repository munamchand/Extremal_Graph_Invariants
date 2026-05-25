import networkx as nx
import math


def wiener_index(G):

    total = 0

    for u in G.nodes():

        lengths = nx.single_source_shortest_path_length(G, u)

        for v in lengths:
            total += lengths[v]

    return total // 2


def sombor_index(G):

    total = 0

    for u, v in G.edges():

        du = G.degree(u)
        dv = G.degree(v)

        total += math.sqrt(du**2 + dv**2)

    return total


def zagreb_index(G):

    return sum(deg**2 for node, deg in G.degree())