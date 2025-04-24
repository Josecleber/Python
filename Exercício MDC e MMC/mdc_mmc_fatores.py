def fatorar(n):
    fatores = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            fatores[i] = fatores.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        fatores[n] = fatores.get(n, 0) + 1
    return fatores


def mdc_mmc(a, b):
    fatores_a = fatorar(a)
    fatores_b = fatorar(b)

    mdc = 1
    mmc = 1
    for fator in set(fatores_a.keys()) | set(fatores_b.keys()):
        exp_a = fatores_a.get(fator, 0)
        exp_b = fatores_b.get(fator, 0)
        mdc *= fator ** min(exp_a, exp_b)
        mmc *= fator ** max(exp_a, exp_b)

    return mdc, mmc

a, b = map(int, input("Digite dois números inteiros: ").split())
mdc, mmc = mdc_mmc(a, b)
print(f"MDC({a}, {b}) = {mdc}")
print(f"MMC({a}, {b}) = {mmc}")
