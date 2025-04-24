def le_vetor(v):
    valor = float(input("Digite um número (0 para encerrar): "))
    while valor != 0:
        v.append(valor)
        valor = float(input("Digite um número (0 para encerrar): "))

def calc_media(v):
    if len(v) == 0:
        return 0
    return sum(v) / len(v)

def det_qts_impares(v):
    cont_impar = 0
    for i in range(0, len(v)):
        if int(v[i]) % 2 != 0:
            cont_impar += 1
    return cont_impar

if __name__ == "__main__":
    vet = []
    le_vetor(vet)
    media = calc_media(vet)
    qtd_impar = det_qts_impares(vet)
    print(f'Média aritmética = {media:.2f}')
    print(f'Quantidade de números ímpares = {qtd_impar}')
