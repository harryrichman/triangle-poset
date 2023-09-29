import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define the predicate function
def predicate(x, y):
    return x % y == 0

# Add edges based on the predicate
for i in range(1, 21):
    for j in range(1, 21):
        if i != j and predicate(i, j):
            G.add_edge(i, j)

# Draw the Hasse diagram
pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, arrows=False)
plt.axis('off')
plt.show()