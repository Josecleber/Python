def soma_pares_sublistas(lista):
    if not lista:
        return 0
    else:
        soma_pares_primeira_sublista = sum(num for num in lista[0] if num % 2 == 0)
        return soma_pares_primeira_sublista + soma_pares_sublistas(lista[1:])

def obter_lista_de_listas():
    try:
        n = int(input("Quantas sublistas você deseja inserir? "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        return []

    lista_principal = []

    for i in range(n):
        try:
            sublista = list(map(int, input(f"Digite os números da sublista {i+1}, separados por espaço: ").split()))
            lista_principal.append(sublista)
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números inteiros separados por espaço.")
            return []

    return lista_principal

if __name__ == "__main__":
    lista = obter_lista_de_listas()
    resultado = soma_pares_sublistas(lista)
    print(f"\n A soma dos números pares nas sublistas é: {resultado}")
