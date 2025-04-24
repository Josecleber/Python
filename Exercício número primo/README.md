# Verificador de Números Primos

Este exercício em Python implementa uma função que verifica se um número fornecido pelo usuário é primo.

## Como funciona

A função `is_prime(n)` utiliza uma abordagem eficiente para verificar se um número é primo:
- Retorna `False` se o número for menor ou igual a 1.
- Retorna `True` diretamente para 2 e 3.
- Elimina múltiplos de 2 e 3.
- Testa divisibilidade de `n` por números na forma de 6k ± 1 até a raiz quadrada de `n`.

## Exemplo de execução

```bash
$ python numero_primo.py
Digite um número: 7
7 é um número primo.

$ python numero_primo.py
Digite um número: 8
8 não é um número primo.
```

## Autor
José Cleber Alves da Cruz Mendes  
Curso: Engenharia da Computação – Uniube



**Exercício desenvolvido durante as aulas de Python.**
