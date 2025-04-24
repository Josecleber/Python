import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Criando o quadro da paisagem
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')

# Adicionando o contorno da imagem
frame = patches.Rectangle((0, 0), 10, 8, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(frame)

# Definindo as cores
colors = {1: 'yellow', 2: 'red', 3: 'green', 4: 'blue', 5: 'orange'}

# Desenhando o sol
sun = patches.Circle((1.5, 6.5), 0.7, edgecolor='yellow', facecolor=colors[1], linewidth=1.5)
ax.add_patch(sun)

# Desenhando os raios do sol
ax.plot([1, 0.5], [6, 5.3], color='red', linewidth=1.5)
ax.plot([1.45, 1.45], [5.75, 5], color='red', linewidth=1.5)
ax.plot([2, 2.5], [6, 5.3], color='red', linewidth=1.5)
ax.plot([2.23, 3.23], [6.55, 6.55], color='red', linewidth=1.5)
ax.plot([0.77, 0.3], [6.55, 6.55], color='red', linewidth=1.5)
ax.plot([0.8, 0.3], [6.2, 6], color='red', linewidth=1.5)
ax.plot([2.2, 3.1], [6.25, 5.9], color='red', linewidth=1.5)
ax.plot([1.45, 1.45], [7.2, 7.5], color='red', linewidth=1.5)
ax.plot([2.1, 2.5], [6.96, 7.3], color='red', linewidth=1.5)
ax.plot([0.9, 0.7], [6.96, 7.17], color='red', linewidth=1.5)

# Função para criar ondas no mar
def create_wave(amplitude, frequency, phase, x_start, x_end, num_points):
    x = np.linspace(x_start, x_end, num_points)
    y = amplitude * np.sin(2 * np.pi * frequency * x + phase)
    return x, y

# Criando o mar (ondas)
amplitude = 0.5
frequency = 0.1
phase = np.pi
x, y = create_wave(amplitude, frequency, phase, 0, 10, 200)
ax.fill_between(x, y + 1, facecolor='skyblue', linewidth=0)
ax.plot(x, y + 1, color='skyblue', linewidth=2)

# Desenhando o barco
boat_base = patches.Polygon([[5.6, 2.5], [9.2, 2.5], [8.8, 1.5], [6, 1.5]], closed=True, edgecolor='black', facecolor=colors[5], linewidth=1.5)
ax.add_patch(boat_base)

# Mastros do barco
ax.plot([7.5, 7.5], [2.5, 5], color='black', linewidth=2)

# Velas do barco
sail_left = patches.Polygon([[5.7, 3.3], [7.4, 5.5], [7.4, 3.3]], closed=True, edgecolor='black', facecolor='white', linewidth=1.5)
sail_right = patches.Polygon([[7.6, 3], [7.6, 5], [9.4, 3]], closed=True, edgecolor='black', facecolor=colors[1], linewidth=1.5)
ax.add_patch(sail_left)
ax.add_patch(sail_right)

# Janelas do barco
window_left = patches.Circle((6.9, 2), 0.2, edgecolor='black', facecolor=colors[4], linewidth=1.5)
window_right = patches.Circle((8, 2), 0.2, edgecolor='black', facecolor=colors[4], linewidth=1.5)
ax.add_patch(window_left)
ax.add_patch(window_right)

# Desenhando a bola
ball = patches.Circle((8.5, 6.5), 0.5, edgecolor='black', facecolor="white", linewidth=1.5)
ax.add_patch(ball)

# Desenhando os detalhes da bola
ax.plot([8.3, 8.4], [6.1, 6.75], color='red', linewidth=1.5)
ax.plot([8.7, 8.6], [6.1, 6.75], color='green', linewidth=1.5)
bolaz = patches.Arc((8.5, 6.9), 0.55, 0.35, angle=0, theta1=180, theta2=360, edgecolor='blue', linewidth=1.5)
ax.add_patch(bolaz)

# Desenhando o peixe
fish_bodyx = patches.Arc((1.5, 1), 1.5, 0.5, angle=0, theta1=0, theta2=180, edgecolor='black', facecolor="green", linewidth=1.5)
fish_bodyy = patches.Arc((1.5, 1), 1.5, 0.5, angle=0, theta1=180, theta2=360, edgecolor='black', facecolor="green", linewidth=1.5)
fish_bodyz = patches.Arc((2, 1), 0.6, 0.4, angle=0, theta1=90, theta2=270, edgecolor='black', facecolor="green", linewidth=1.5)
ax.add_patch(fish_bodyx)
ax.add_patch(fish_bodyy)
ax.add_patch(fish_bodyz)

# Desenhando a cauda do peixe
fish_tail = patches.Polygon([[0.28, 1.3], [0.28, 0.7], [0.77, 1]], closed=True, edgecolor='black', facecolor="green", linewidth=1.5)
ax.add_patch(fish_tail)

# Desenhando a barbatana do peixe
fish_t = patches.Polygon([[1.15, 1.8], [1.1, 1.18], [1.6, 1.28]], closed=True, edgecolor='black', facecolor="green", linewidth=1.5)
ax.add_patch(fish_t)

# Desenhando o olho do peixe
fish_eye = patches.Circle((2, 1), 0.07, edgecolor='black', facecolor='black')
ax.add_patch(fish_eye)

# Exibindo o gráfico final
plt.show()
