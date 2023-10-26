import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

def predicate(x, y):
    return x % y == 0

for i in range(1, 5):
    for j in range(1, 5):
        if i != j and predicate(i, j):
            G.add_edge(i, j)

pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, arrows=False)
plt.axis('off')
plt.show()