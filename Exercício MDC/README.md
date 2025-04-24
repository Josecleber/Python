# Cálculo do MDC (Máximo Divisor Comum)

Este exercício em Python implementa uma função recursiva para calcular o MDC (Máximo Divisor Comum) entre dois números inteiros.

## Como funciona

A função `mdc(a, b)` utiliza o Algoritmo de Euclides:
- Se `b` for 0, retorna `a`.
- Caso contrário, chama a função recursivamente com os valores `b` e `a % b`.

## Exemplo de execução

```bash
$ python mdc_recursivo.py
Digite dois números separados por espaço: 30 45
mdc(30,45) = 15
```


## Autor
José Cleber Alves da Cruz Mendes  
Curso: Engenharia da Computação – Uniube


**Exercício desenvolvido durante as aulas de Python.**
