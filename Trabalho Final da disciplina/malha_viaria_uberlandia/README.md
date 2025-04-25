# Análise e Otimização de Malhas de Trânsito em Uberlândia/MG

Projeto final da disciplina de **Laboratório de Programação Competitiva**: 

modelagem e análise de tráfego utilizando grafos aplicados à malha viária de Uberlândia.

---

## Objetivo

Modelar e simular o comportamento do trânsito em Uberlândia usando grafos extraídos do OpenStreetMap, com o intuito de:

- Calcular o caminho mais curto em tempo.
- Visualizar trajetos e congestionamentos em mapas interativos.
- Comparar cenários de tráfego em diferentes condições.

---

## Tecnologias Utilizadas

- **Python 3.9+**
- **OSMnx** – Para baixar e estruturar dados da malha viária.
- **NetworkX** – Manipulação de grafos.
- **Matplotlib** – Gráficos e visualização.
- **Folium** – Mapas interativos.
- **GeoPandas** – Análise espacial.

---

## Como Executar

1. Instale os pacotes:

```bash
pip install -r requirements.txt
```

2. Execute o script principal:

python analise_trafego.py

Algumas funcionalidades, como visualização com Folium, funcionam melhor em notebooks (Jupyter ou Google Colab).

# Funcionalidades

Download da malha viária de Uberlândia via OpenStreetMap

Cálculo de rota mais rápida entre dois pontos

Mapa interativo com rota traçada

Simulação de volume e capacidade nas ruas

Detecção e visualização de congestionamentos

Comparação de tempo entre cenários

# Exemplo de Resultado

Rota mais curta: 8 minutos

Cenário congestionado: 9.6 minutos

Mapa interativo com rota e outro com índice de congestionamento

Gráfico de comparação de cenários



## Autores
José Cleber Alves da Cruz Mendes 

Joaquim Marcelo Zaiden

Luiz Gustavo Moreira Lima

Bryan Henrique Oliveira Evangelista

Projeto apresentado na UNIUBE, 2024.

Curso: Engenharia da Computação – Uniube


**Exercício desenvolvido durante as aulas de Python.**
