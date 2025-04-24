import math

# Função para verificar se um valor é NaN e demonstrar o comportamento
valor1 = float('nan')
valor2 = 10.0

print(math.isnan(valor1))  # Retorna True, pois 'valor1' é NaN
print(math.isnan(valor2))  # Retorna False, pois 'valor2' não é NaN

print()

# Função para verificar valores inválidos e substituí-los
def verificar_valores_invalidos(leituras):
    leituras_corrigidas = []

    for leitura in leituras:
        if math.isnan(leitura):  # Se o valor for NaN, substituímos por 0
            leituras_corrigidas.append(0)
        elif leitura == float('inf'):  # Se o valor for Inf positivo, substituímos por 1
            leituras_corrigidas.append(1)
        elif leitura == float('-inf'):  # Se o valor for Inf negativo, substituímos por -1
            leituras_corrigidas.append(-1)
        else:
            leituras_corrigidas.append(leitura)  # Mantemos o valor original se válido

    return leituras_corrigidas

# Função para solicitar leituras de sensores e processá-las
def solicitar_leituras():
    n = int(input("Quantas leituras de sensores você deseja inserir? "))
    leituras = []

    for i in range(n):
        valor = input(f"Digite o valor da leitura {i+1}: ").strip().lower()

        # Conversão para NaN, Inf ou -Inf, dependendo da entrada
        if valor == "nan":
            leituras.append(float('nan'))
        elif valor == "inf":
            leituras.append(float('inf'))
        elif valor == "-inf":
            leituras.append(float('-inf'))
        else:
            try:
                leituras.append(float(valor))  # Tenta converter o valor para float
            except ValueError:
                print(f"Valor '{valor}' não é válido. Por favor, insira um valor numérico válido ou 'NaN', 'Inf', '-Inf'.")
                return

    leituras_corrigidas = verificar_valores_invalidos(leituras)
    print("\nLeituras após substituição dos valores inválidos:", leituras_corrigidas)

solicitar_leituras()
