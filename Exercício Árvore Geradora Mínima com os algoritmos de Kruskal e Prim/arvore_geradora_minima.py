import networkx as nx
import matplotlib.pyplot as plt

# Criação do grafo com pesos
G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 4}),
    (0, 2, {'weight': 1}),
    (1, 2, {'weight': 2}),
    (1, 3, {'weight': 5}),
    (2, 3, {'weight': 8}),
    (2, 4, {'weight': 10}),
    (3, 4, {'weight': 3})
])

# Árvore Geradora Mínima com Kruskal
mst_kruskal = nx.minimum_spanning_tree(G, algorithm='kruskal')
print("Arestas da Árvore Geradora Mínima (Kruskal):")
print(mst_kruskal.edges(data=True))

pos = nx.spring_layout(mst_kruskal)
nx.draw(mst_kruskal, pos, with_labels=True, node_color='lightblue', edge_color='black')
edge_labels = nx.get_edge_attributes(mst_kruskal, 'weight')
nx.draw_networkx_edge_labels(mst_kruskal, pos, edge_labels=edge_labels)
plt.title("Árvore Geradora Mínima (Kruskal)")
plt.show()

print("\n")

# Árvore Geradora Mínima com Prim (default do NetworkX)
mst_prim = nx.minimum_spanning_tree(G)
print("Arestas da Árvore Geradora Mínima (Prim):")
print(mst_prim.edges(data=True))

pos = nx.spring_layout(mst_prim)
nx.draw(mst_prim, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
edge_labels = nx.get_edge_attributes(mst_prim, 'weight')
nx.draw_networkx_edge_labels(mst_prim, pos, edge_labels=edge_labels)
plt.title("Árvore Geradora Mínima (Prim)")
plt.show()
