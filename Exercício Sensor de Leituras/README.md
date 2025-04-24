# Sensor de Leituras - Tratamento de Valores Inválidos (NaN e Inf)

Este projeto simula o comportamento de um sensor que pode gerar leituras inválidas, como `NaN` (Not a Number) ou `Inf` (infinito). O código trata esses valores e substitui por valores específicos para garantir que o sistema não falhe devido a entradas inesperadas.

## Objetivos

- **NaN (Not a Number)**: Representa um valor indefinido ou inválido em cálculos, como o resultado de uma operação de divisão por zero.
- **Inf (Infinito)**: Um valor numérico representando o infinito positivo ou negativo.

## Pré-requisitos

Certifique-se de que a biblioteca `math` está disponível no seu ambiente Python.

## Como Executar

Execute o código Python para simular o processamento das leituras dos sensores:

```bash
python sensor_leituras.py
```

# Funcionamento

O programa solicita a quantidade de leituras de sensores que você deseja inserir.

O usuário pode inserir valores numéricos ou as palavras-chave 'nan', 'inf', ou '-inf'.

Após inserir os dados, o código processa as leituras e substitui:

NaN por 0

Inf positivo por 1

Inf negativo por -1

O programa imprime as leituras corrigidas.

# Explicação do Código

Função verificar_valores_invalidos(): Esta função recebe uma lista de leituras e substitui qualquer valor NaN por 0, Inf por 1 (se positivo) ou -1 (se negativo).

Função solicitar_leituras(): Solicita as leituras ao usuário, permitindo a entrada de valores como 'nan', 'inf', '-inf' e números válidos. Após as entradas, a função chama verificar_valores_invalidos() para tratar os valores inválidos.

# Alterações Possíveis

Você pode modificar o valor de substituição para NaN e Inf conforme a necessidade de sua aplicação.

Caso seja necessário, adicione outras verificações para tratar outros valores inválidos.

# Exemplo de Execução

Se o usuário inserir os seguintes valores:

Quantas leituras de sensores você deseja inserir? 5

Digite o valor da leitura 1: 10

Digite o valor da leitura 2: NaN

Digite o valor da leitura 3: Inf

Digite o valor da leitura 4: -Inf

Digite o valor da leitura 5: 5

A saída será:

Leituras após substituição dos valores inválidos: [10.0, 0, 1, -1, 5.0]

## Autor
José Cleber Alves da Cruz Mendes  
Curso: Engenharia da Computação – Uniube



**Exercício desenvolvido durante as aulas de Python.**
