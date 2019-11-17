import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from itertools import combinations
from collections import Counter


def plot_data_dist_grid(data, col_idx, n_col=4, n_row=4, order=None):
    """
    Plot multiple columns count plot as a grid.
    :param data: The df to be analysed
    :param col_idx: the columns to be plotted
    :param n_col: Number of columns in plot grid
    :param n_row: Number of rows in plot grid
    :param order: The order for x-axes. This will only work if all the plots have the same values
    :return: Plot
    """
    # Create the subplot to host the plots.
    fig, axes = plt.subplots(nrows=n_row, ncols=n_col, figsize=[25, 20])

    n_plot = n_row * n_col
    plot_idx = [x for x in range(0, n_plot)]

    if len(col_idx) > n_plot:
        print('More columns than available plots.')

    mapping = dict(zip(col_idx[0:n_plot], plot_idx))

    for c_idx, p_idx in mapping.items():
        # doing this to avoid the error
        plot_data = data[[c_idx]].copy(deep=True)
        plot_data.fillna('NA', inplace=True)
        if order:
            g = sns.countplot(x=c_idx, data=plot_data, ax=axes.flatten()[mapping[c_idx]], order=order)
        else:
            g = sns.countplot(x=c_idx, data=plot_data, ax=axes.flatten()[mapping[c_idx]])
        _ = g.set_xticklabels(rotation=30, labels=g.get_xticklabels())


def plot_col_dist(df, col_idx, order=None, sort=True, rotation=90, fig_size=(10, 5), ax=None, title=None):
    """
    Creates a count plot of the distinct values in the column
    :param df: The data frame to analyse
    :param col_idx: The column name to analyse
    :param order: A list specifying the x-axis order
    :param sort: Should the plot be sorted in descending order?
    :param rotation: rotation of x-axis labels
    :param fig_size: Figure size
    :param ax: matplotlib Axes
    :param title: Title for the plot
    :return: Plot.
    """
    # Create the subplot to host the plots.
    fig, ax = plt.subplots(figsize=fig_size)

    if sort:
        order = df[col_idx].value_counts().index

    g = sns.countplot(data=df, x=col_idx, order=order, ax=ax)

    _ = g.set_xticklabels(rotation=rotation, labels=g.get_xticklabels())

    if title:
        g.set_title(title)


def plot_network_graph(df, col_idx, sep="; ", fig_size=(15, 15)):
    """
    Creates a network graph of the variables in multiple options response.
    These are usually stored as '; ' seperated value in each row.

    reference: Aric Hagberg (hagberg@lanl.gov)
    :param df: dataframe to analyse
    :param col_idx: The column name
    :param sep: Seperator to use to split the column value
    :param fig_size: Size of the figure
    :return:
    """
    plot_df = df[[col_idx]].dropna()
    plot_df[col_idx] = plot_df[col_idx].str.split(sep)

    # Get the nodes and node weights
    nodes = [x for l in plot_df[col_idx] for x in l]
    node_wts = Counter(nodes)
    max_wt_node = max(node_wts, key=lambda key: node_wts[key])
    max_wt_node = node_wts[max_wt_node]

    # Get the edges
    edges = plot_df[col_idx].apply(lambda x: [(*sorted(c),) for c in combinations(x, 2)])
    edges = [edge for row in edges for edge in row]

    edge_wts = Counter(edges)
    max_wt_edge = max(edge_wts, key=lambda key: edge_wts[key])
    max_wt_edge = edge_wts[max_wt_edge]

    G = nx.Graph()

    for n, w in node_wts.items():
        G.add_nodes_from([n], nodesize=w/max_wt_node)

    for e, w in edge_wts.items():
        G.add_edges_from([e], weight=w/max_wt_edge)

    pos = nx.spring_layout(G)  # Set the node dit

    plt.figure(figsize=fig_size)

    large_1 = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] < 0.1]
    large_2 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.1 <= d['weight'] < 0.2]
    large_3 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.2 <= d['weight'] < 0.3]
    large_4 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.3 <= d['weight'] < 0.4]
    large_5 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.4 <= d['weight'] < 0.5]
    large_6 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.5 <= d['weight'] < 0.6]
    large_7 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.6 <= d['weight'] < 0.7]
    large_8 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.7 <= d['weight'] < 0.8]
    large_9 = [(u, v) for (u, v, d) in G.edges(data=True) if 0.8 <= d['weight'] < 0.9]
    large_10 = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >= 0.9]

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=400)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=large_1, width=1, alpha=0.1)
    nx.draw_networkx_edges(G, pos, edgelist=large_2, width=2, alpha=0.2)
    nx.draw_networkx_edges(G, pos, edgelist=large_3, width=3, alpha=0.3)
    nx.draw_networkx_edges(G, pos, edgelist=large_4, width=4, alpha=0.4)
    nx.draw_networkx_edges(G, pos, edgelist=large_5, width=5, alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=large_6, width=6, alpha=0.6)
    nx.draw_networkx_edges(G, pos, edgelist=large_7, width=7, alpha=0.7)
    nx.draw_networkx_edges(G, pos, edgelist=large_8, width=8, alpha=0.8)
    nx.draw_networkx_edges(G, pos, edgelist=large_9, width=9, alpha=0.9)
    nx.draw_networkx_edges(G, pos, edgelist=large_10, width=10)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()
