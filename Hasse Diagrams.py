import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()


def predicate(x, y):
    return x % y == 0


for i in range(1, 21):
    for j in range(1, 21):
        if i != j and predicate(i, j):
            G.add_edge(i, j)  # Reversed the edge direction


nodesep = 50  # Adjust this value to control the spacing
args = "-Gnodesep={}".format(nodesep)
pos = nx.nx_agraph.graphviz_layout(G, prog="dot", args=args)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_size=10,
    arrows=True,
    arrowstyle="<|-",
)
plt.axis("off")
plt.show()
