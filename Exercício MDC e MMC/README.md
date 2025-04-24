# Cálculo de MDC e MMC com Fatoração

Este script em Python calcula o **Máximo Divisor Comum (MDC)** e o **Mínimo Múltiplo Comum (MMC)** entre dois números inteiros utilizando fatoração em primos.

## Como funciona

- A função `fatorar(n)` decompõe o número `n` em seus fatores primos.
- A função `mdc_mmc(a, b)` usa os fatores de `a` e `b` para:
  - Calcular o **MDC** com os menores expoentes comuns.
  - Calcular o **MMC** com os maiores expoentes encontrados.

## Exemplo de execução

```bash
$ python mdc_mmc_fatores.py
Digite dois números inteiros: 18 30
MDC(18, 30) = 6
MMC(18, 30) = 90
```

## Autor
José Cleber Alves da Cruz Mendes  
Curso: Engenharia da Computação – Uniube


**Exercício desenvolvido durante as aulas de Python.**
