import networkx as nx


def generate_trees(n):
    """
    Generate all non-isomorphic trees with n vertices.
    """

    trees = list(nx.nonisomorphic_trees(n))

    return trees