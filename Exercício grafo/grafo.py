import networkx as nx
import matplotlib.pyplot as plt

# Definição do grafo com pesos
G = nx.Graph()
edges = [
    ('A', 'B', 3), ('A', 'C', 5), ('A', 'D', 2), ('A', 'H', 10),
    ('B', 'C', 5), ('B', 'D', 8), ('B', 'G', 6), ('B', 'E', 4), ('B', 'H', 6),
    ('C', 'G', 9), ('C', 'F', 7), ('C', 'E', 1), ('D', 'E', 12), ('D', 'H', 14),
    ('E', 'G', 15), ('F', 'H', 9), ('G', 'H', 3)
]
G.add_weighted_edges_from(edges)

# Matriz de adjacência
adjacency_matrix = nx.adjacency_matrix(G).todense()
print("Matriz de Adjacência:")
print(adjacency_matrix)

# Lista de adjacência
adjacency_list = {node: list(G.neighbors(node)) for node in G.nodes()}
print("\nLista de Adjacentências:")
for node, neighbors in adjacency_list.items():
    print(f"{node}: {neighbors}")

# Vértices e arestas
vertices = list(G.nodes())
edges = list(G.edges(data=True))
print("\nVértices:", vertices)
print("Arestas:", edges)

# Grau de um nó específico
degree_C = G.degree('C')
print("\nGrau do nó C:", degree_C)

# Busca em largura
bfs = list(nx.bfs_edges(G, source='A'))
print("\nBusca em Largura a partir do nó A:", bfs)

# Busca em profundidade
dfs = list(nx.dfs_edges(G, source='A'))
print("Busca em Profundidade a partir do nó A:", dfs)

# Caminho com custo específico
def find_path_with_cost(graph, start, end, target_cost):
    for path in nx.all_simple_paths(graph, source=start, target=end):
        path_cost = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
        if path_cost == target_cost:
            return path, path_cost
    return None, None

path_AE_24, cost_AE_24 = find_path_with_cost(G, 'A', 'E', 24)
if path_AE_24:
    print(f"\nCaminho de A até E com custo 24: {path_AE_24}, Custo: {cost_AE_24}")
else:
    print("\nNão há caminho de A até E com custo 24.")

# Caminho mais curto (Dijkstra)
shortest_path = nx.dijkstra_path(G, source='A', target='E')
shortest_path_cost = nx.dijkstra_path_length(G, source='A', target='E')
print("\nCaminho mais curto de A até E:", shortest_path, "com custo:", shortest_path_cost)

# Árvore geradora mínima
mst = nx.minimum_spanning_tree(G)
print("\nArestas da Árvore Geradora Mínima:")
print(mst.edges(data=True))

# Visualização
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()})
plt.title("Grafo Completo com Pesos")
plt.show()
