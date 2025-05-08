import matplotlib.pyplot as plt

fonte = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
saida = [0, 0.96, 2.02, 3.0, 3.95, 4.68, 4.91, 4.99, 5.03, 5.05, 5.07]

plt.figure(figsize=(10, 6))
plt.plot(fonte, saida, 'b-o', linewidth=2, markersize=8, label='Tensão de Saída')
plt.xlabel('Tensão da Fonte (V)')
plt.ylabel('Tensão de Saída (V)')
plt.title('Circuito Limitador de Tensão')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right')
plt.xlim(0, 10)
plt.ylim(0, 6)
plt.savefig('grafico_circuito.jpeg', dpi=300, format='jpeg')
plt.show()
