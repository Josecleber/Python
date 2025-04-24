def crivo_eratostenes(n):
    if n <= 1:
        return []

    primo = [True] * (n + 1)
    primo[0] = primo[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if primo[p]:
            for i in range(p * p, n + 1, p):
                primo[i] = False

    primos = []
    for p in range(n + 1):
        if primo[p]:
            primos.append(p)
    return primos

n = int(input("Digite um número inteiro positivo n: "))

if n >= 0:
    primos = crivo_eratostenes(n)
    print("Números primos até", n, ":", primos)
else:
    print("Este número não é inteiro positivo.")
