import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches


G = nx.DiGraph()

def predicate(x, y):
    return x % y == 0

for i in range(1, 5):
    for j in range(1, 5):
        if i != j and predicate(i, j):
            G.add_edge(i, j)

fig, ax = plt.subplots()

node_size = 800  
node_color = 'black'  
pos = nx.spring_layout(G, seed=42)  

nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray')


for node in G.nodes():
    x, y = pos[node]
    ax.add_patch(patches.FancyArrowPatch((x, y), (x, y), arrowstyle='->', mutation_scale=node_size, color=node_color))

ax.set_xticks([])
ax.set_yticks([])

plt.axis('off')
plt.show()
