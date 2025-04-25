# Otimização de Custos com Restrições

Este programa utiliza **programação dinâmica com memoização** e **busca binária** para resolver um problema de otimização de custo. O objetivo é determinar o menor custo possível para se mover por uma sequência de pontos, com restrições de distância e custo fixo de transição.

## Funcionalidade

Dado:

- Uma sequência de `n` valores crescentes
- Dois custos possíveis de movimentação (`a` e `b`)
- Um custo fixo `c` ao alternar entre dois modos (ou caminhos)

A função `solve_case` calcula o menor custo para atingir o último ponto da sequência, podendo escolher entre dois caminhos com restrições diferentes de transição.

## Como funciona

- A lista `f[0]` contém os valores originais.
- A lista `f[1]` é derivada de `f[0]`, considerando a troca de caminho com custo fixo `c`.
- A função `go()` é uma abordagem recursiva com **memoização** que usa `bisect_left` para encontrar o maior índice anterior possível dentro do intervalo permitido (`a` ou `b`).
- A matriz `dp` evita recomputações.

## Como usar

Execute o arquivo com:

```bash
python otimizacao_com_custos.py
```

Insira os dados no seguinte formato:

n c a b v1 v2 v3 ... vn

Exemplo de entrada:

5 3 2 1 1 3 6 10 15

Saída esperada:

4


## Autor
José Cleber Alves da Cruz Mendes  
Curso: Engenharia da Computação – Uniube



**Exercício desenvolvido durante as aulas de Python.**
