def leia_matriz(linhas, colunas):
  matriz = []
  for i in range(linhas):
    linha = list(map(int, input(f"Digite os elementos da linha {i+1} separados por espaço: ").split()))
    matriz.append(linha)
  return matriz

def imprima_matriz(matriz):
  for linha in matriz:
    print(linha)

def eh_simetrica(matriz):
  n = len(matriz)
  for i in range(n):
    for j in range(i + 1, n):
      if matriz[i][j] != matriz[j][i]:
        return False
  return True

def soma_diagP(matriz):
  n = len(matriz)
  soma = 0
  for i in range(n):
    soma += matriz[i][i]
  return soma

def soma_diagS(matriz):
  n = len(matriz)
  soma = 0
  for i in range(n):
    soma += matriz[i][n - 1 - i]
  return soma

def encontra_negativos(matriz):
  negativos = []
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if matriz[i][j] < 0:
        negativos.append((matriz[i][j], i, j))
  return negativos

def encontra_max_min(matriz):
  maximo = float('-inf')
  minimo = float('inf')
  for linha in matriz:
    for elemento in linha:
      if elemento > maximo:
        maximo = elemento
      if elemento < minimo:
        minimo = elemento
  return maximo, minimo

def multiplica_matriz(matrizA, matrizB):
  linhasA = len(matrizA)
  colunasA = len(matrizA[0])
  linhasB = len(matrizB)
  colunasB = len(matrizB[0])

  if colunasA != linhasB:
    return None

  matrizC = [[0] * colunasB for _ in range(linhasA)]
  for i in range(linhasA):
    for j in range(colunasB):
      for k in range(colunasA):
        matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
  return matrizC

def main():
  n = int(input("Digite o tamanho da matriz A (n x n): "))
  print("Digite os elementos da matriz A:")
  matrizA = leia_matriz(n, n)

  if eh_simetrica(matrizA):
    print("A matriz A é simétrica.")
  else:
    print("A matriz A não é simétrica.")

  soma_diag_principal = soma_diagP(matrizA)
  print("Soma da diagonal principal:", soma_diag_principal)

  soma_diag_secundaria = soma_diagS(matrizA)
  print("Soma da diagonal secundária:", soma_diag_secundaria)

  negativos = encontra_negativos(matrizA)
  if negativos:
    print("Números negativos e suas localizações:")
    for negativo, linha, coluna in negativos:
      print(f"Valor: {negativo}, Linha: {linha}, Coluna: {coluna}")
  else:
    print("Não há números negativos na matriz A.")

  maximo, minimo = encontra_max_min(matrizA)
  print("Valor máximo:", maximo)
  print("Valor mínimo:", minimo)

  p = int(input("Digite o número de colunas da matriz B (n x p): "))
  print("Digite os elementos da matriz B:")
  matrizB = leia_matriz(n, p)
  matrizC = multiplica_matriz(matrizA, matrizB)

  if matrizC:
    print("Matriz C (produto de A por B):")
    imprima_matriz(matrizC)
  else:
    print("Não é possível multiplicar as matrizes A e B.")

if __name__ == "__main__":
  main()
