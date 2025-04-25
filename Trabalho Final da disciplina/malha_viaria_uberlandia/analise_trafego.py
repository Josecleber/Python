import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
from IPython.display import display

# Baixar a malha viária
cidade = "Uberlândia, Minas Gerais, Brasil"
grafo = ox.graph_from_place(cidade, network_type='drive')

# Adicionar velocidades e tempos de viagem
grafo = ox.add_edge_speeds(grafo)
grafo = ox.add_edge_travel_times(grafo)

# Exibir o grafo
ox.plot_graph(grafo, node_size=0, edge_color='blue', edge_linewidth=0.5)

# Definir origem e destino
origem = list(grafo.nodes())[0]
destino = list(grafo.nodes())[-1]

# Calcular menor caminho em tempo
rota_caminho_minimo = nx.shortest_path(grafo, origem, destino, weight="travel_time")
tempo_caminho_minimo = nx.shortest_path_length(grafo, origem, destino, weight="travel_time")

print(f"Caminho mais curto entre {origem} e {destino}:")
print(rota_caminho_minimo)
print(f"Tempo estimado: {tempo_caminho_minimo / 60:.2f} minutos")

# Mapa com a rota
rota_coords = [(grafo.nodes[n]['y'], grafo.nodes[n]['x']) for n in rota_caminho_minimo]
mapa = folium.Map(location=rota_coords[0], zoom_start=13)
folium.PolyLine(rota_coords, color='red', weight=5, opacity=0.7, tooltip="Caminho Mais Curto").add_to(mapa)
display(mapa)

# Adicionar capacidade e volume simulados
for u, v, data in grafo.edges(data=True):
    data['capacity'] = data.get('length', 50) * 0.1
    data['volume'] = data.get('length', 50) * 0.05

# Identificar congestionamentos
for u, v, data in grafo.edges(data=True):
    if data['volume'] > data['capacity']:
        print(f"Rua entre {u} e {v} está congestionada.")

# Visualização do congestionamento
edges = ox.graph_to_gdfs(grafo, nodes=False)
edges['congestion'] = edges['volume'] / edges['capacity']
edges.plot(column='congestion', cmap='Reds', legend=True, figsize=(12, 8), legend_kwds={'label': "Índice de Congestionamento"})
plt.title("Análise de Congestionamento")
plt.show()

# Comparação de cenários
tempos = [tempo_caminho_minimo, tempo_caminho_minimo * 1.2]
cenarios = ["Original", "Congestionado"]
plt.bar(cenarios, [t / 60 for t in tempos], color=['blue', 'red'])
plt.title("Comparação de Tempos de Viagem")
plt.ylabel("Tempo (minutos)")
plt.show()
