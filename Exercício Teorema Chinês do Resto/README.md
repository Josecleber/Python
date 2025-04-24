# Teorema Chinês do Resto

Este exercício implementa o Teorema Chinês do Resto usando o Algoritmo de Euclides Estendido.

## Objetivo

Resolver um sistema de congruências:
x ≡ r1 (mod m1) x ≡ r2 (mod m2) x ≡ r3 (mod m3) ...

## Componentes do código

- `euclid_estendido(a, b)`: Retorna o MDC de `a` e `b` e os coeficientes da identidade de Bézout.
- `teorema_chines_do_resto(restos, mod)`: Aplica o Teorema Chinês do Resto e retorna a menor solução possível para o sistema de congruências.

## Exemplo

```bash
$ python teorema_chines_resto.py
Inversos Modulares: [2, 3, 2]
Solução: 23
```

## Autor
José Cleber Alves da Cruz Mendes  
Curso: Engenharia da Computação – Uniube



**Exercício desenvolvido durante as aulas de Python.**
