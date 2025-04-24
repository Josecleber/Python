import numpy as np
import networkx as nx

# Criação do grafo
G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 4}), 
    (0, 2, {'weight': 1}),
    (1, 2, {'weight': 2}), 
    (1, 3, {'weight': 5}),
    (2, 3, {'weight': 8})
])

# Número de nós no grafo
num_nodes = G.number_of_nodes()

# Construção da matriz de adjacência
adj_matrix = np.zeros((num_nodes, num_nodes))
for (u, v, wt) in G.edges(data=True):
    adj_matrix[u][v] = wt['weight']
    adj_matrix[v][u] = wt['weight']

print("Matriz de Adjacência:")
print(adj_matrix)

print("\n")

# Construção da lista de adjacência
adj_list = {i: [] for i in range(num_nodes)}
for (u, v, wt) in G.edges(data=True):
    adj_list[u].append((v, wt['weight']))
    adj_list[v].append((u, wt['weight']))

print("Lista de Adjacências:")
for key, value in adj_list.items():
    print(f"{key}: {value}")
