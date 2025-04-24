# Árvore Geradora Mínima (MST)

Este exercício mostra como gerar a **Árvore Geradora Mínima** de um grafo ponderado usando dois algoritmos clássicos:

- Kruskal
- Prim

# Funcionamento

O grafo é criado com pesos definidos nas arestas.

O algoritmo de Kruskal é usado para encontrar a árvore geradora mínima.

O algoritmo de Prim (padrão do networkx.minimum_spanning_tree) também é usado.

Ambas as árvores são desenhadas usando o matplotlib.

# Objetivo

Visualizar e comparar as árvores geradoras mínimas obtidas por diferentes algoritmos.

# Exemplo de Saída

Arestas da Árvore Geradora Mínima (Kruskal):
[(0, 2, {'weight': 1}), (1, 2, {'weight': 2}), (3, 4, {'weight': 3}), (1, 3, {'weight': 5})]

Arestas da Árvore Geradora Mínima (Prim):
[(0, 2, {'weight': 1}), (1, 2, {'weight': 2}), (3, 4, {'weight': 3}), (1, 3, {'weight': 5})]

Nota: Ambas as árvores resultam na mesma estrutura, pois são soluções mínimas, mas os caminhos podem variar em grafos maiores.

## Autor
José Cleber Alves da Cruz Mendes  
Curso: Engenharia da Computação – Uniube



**Exercício desenvolvido durante as aulas de Python.**
