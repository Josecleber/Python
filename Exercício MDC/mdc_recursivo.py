def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

a, b = map(int, input("Digite dois números separados por espaço: ").split())
print(f'mdc({a},{b}) = {mdc(a, b)}')
