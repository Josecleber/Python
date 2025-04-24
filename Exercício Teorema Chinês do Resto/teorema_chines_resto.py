import math

def euclid_estendido(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        mdc, x, y = euclid_estendido(b % a, a)
        return (mdc, y - (b // a) * x, x)

def teorema_chines_do_resto(restos, mod):
    n = len(restos)
    M = math.prod(mod)
    Mi = [M // m for m in mod]
    inversos = [euclid_estendido(Mi[i], mod[i])[1] for i in range(n)]
    print("Inversos Modulares:", inversos)

    resultado = sum(restos[i] * Mi[i] * inversos[i] for i in range(n)) % M
    return resultado

# Exemplo fixo:
restos = [2, 3, 2]
mod = [3, 5, 7]
print("Solução:", teorema_chines_do_resto(restos, mod))
