import networkx as nx

def generate_trees(n):
    """
    Generate all non-isomorphic trees on n vertices.
    """

    trees = list(nx.nonisomorphic_trees(n))

    return trees