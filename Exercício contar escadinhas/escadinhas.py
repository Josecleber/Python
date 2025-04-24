def num_escadinhas(seq):
    if len(seq) == 1:
        return 1

    num_escadinhas = 0
    j = 0
    n = len(seq) - 1

    while j < n:
        i = j
        diff = seq[i+1] - seq[i]

        while i < n and seq[i+1] - seq[i] == diff:
            print(f"seq[{i}] = {seq[i]} e seq[{i+1}] = {seq[i+1]} e diff = {diff}")
            i += 1

        num_escadinhas += 1
        j = i

    return num_escadinhas

if __name__ == "__main__":
    N = int(input("Digite o tamanho da sequência: "))
    seq = list(map(int, input("Digite a sequência de números separados por espaço: ").split()))
    print("Número de escadinhas:", num_escadinhas(seq))
