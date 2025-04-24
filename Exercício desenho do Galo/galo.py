from shapely.geometry import Point, Polygon
from shapely.affinity import translate, rotate
import matplotlib.pyplot as plt

# Função para desenhar um círculo
def draw_circle(center, radius):
    return Point(center).buffer(radius)

# Função para desenhar um triângulo
def draw_triangle(p1, p2, p3):
    return Polygon([p1, p2, p3])

# Função para desenhar um polígono com múltiplos vértices
def draw_line_loop(p1, p2, p3,p4,p5,p6):
    return Polygon([p1, p2, p3, p4, p5, p6])

# Função para desenhar um quadrado
def draw_square(center, side):
    offset = side / 2
    return Polygon([
        (center[0] - offset, center[1] - offset),
        (center[0] + offset, center[1] - offset),
        (center[0] + offset, center[1] + offset),
        (center[0] - offset, center[1] + offset)
    ])

# Função para desenhar um polígono genérico de 4 lados
def draw_polygon(p1, p2, p3, p4):
    return Polygon([p1, p2, p3, p4])

# Configurações da figura do gráfico
fig, ax = plt.subplots()

# Desenho das partes do galo
head = draw_circle((5.9087789331323, 17.6717381271323), 3)
eye_outer = draw_circle((5.4087789331323, 18.6717381271323), 0.9)
eye_inner = draw_circle((5.4087789331323, 18.6717381271323), 0.4)

crest1 = draw_circle((5.6044225289788, 21.9321341317473), 1.2)
crest2 = draw_circle((7.9044225289788, 21.4221341317473), 1.2)
crest3 = draw_circle((9.651173289788, 19.721341317473), 1.2)

body = draw_polygon((6, 14.55), (3.5, 11.55), (6, 8.65), (8.5, 11.55))

beak = draw_line_loop(
    (1.6044225289788, 20.2321341317473), 
    (3.9087789331323, 17.6717381271323), 
    (2.7005611305941, 17.3275302247094),
    (1.6044225289788, 15.2321341317473), 
    (3.9087789331323, 17.6717381271323), 
    (2.7005611305941, 17.3275302247094)
)

feather1 = draw_circle((10, 11.5), 2).difference(draw_circle((8.5, 8), 4))
feather2 = draw_circle((10, 11.5), 2).difference(draw_circle((7.5, 8), 4))
feather3 = draw_circle((10, 10.5), 2).difference(draw_circle((6.8, 8), 4))

leg = draw_triangle((4.5, 4.5), (7.5, 4.5), (6, 8.6))

# Desenhando cada parte do galo no gráfico
for part, color in [
    (head, 'none'), (eye_outer, 'none'), (eye_inner, 'black'),
    (body, 'none'), (beak, 'none'), (crest1, 'none'),
    (crest2, 'none'), (crest3, 'none'), (feather1, 'none'),
    (feather2, 'none'), (feather3, 'none'), (leg, 'none')
]:
    x, y = part.exterior.xy
    ax.plot(x, y, color='black', linewidth=1)
    if color != 'none':
        ax.fill(x, y, color=color)

# Ajustes de visualização
ax.set_aspect('equal')
plt.axis("off")
plt.show()
