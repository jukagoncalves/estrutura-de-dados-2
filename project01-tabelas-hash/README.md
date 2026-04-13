# Projeto 01 – Tabelas Hash em Textos Reais
**GCT153 – Estruturas de Dados II**  
Prof. Dr. Alysson Naves

---

## Descrição

Este projeto implementa e compara tabelas hash com diferentes funções de hashing
aplicadas a textos reais em português e inglês. O desempenho da tabela hash é
comparado com uma estrutura linear (lista) como linha de base.

---

## Arquivos do projeto

```
projeto/
├── orientacao_projeto01.pdf    # PDF de orientação
├── tabela_hash.py              # código principal
├── tale.txt                    # texto em inglês (Tale of Two Cities)
├── quincas_borba.txt           # texto em português (Machado de Assis)
├── resultados.csv              # gerado automaticamente ao rodar
├── histogramas                 # pasta gerada automaticamente com os gráficos
└── Relatório_Tabela_Hash.pdf/  # PDF do relatório
```

---

## Requisitos

- Python 3.8 ou superior
- Biblioteca `matplotlib`

Para instalar o matplotlib, execute no terminal:

```bash
pip install matplotlib
```

---

## Como rodar

1. Coloque os arquivos `tale.txt` e `quincas_borba.txt` na mesma pasta que `tabela_hash.py`

2. No terminal, navegue até a pasta do projeto:

```bash
cd caminho/para/a/pasta
```

3. Execute o programa:

```bash
python tabela_hash.py
```

---

## O que o programa faz

Ao rodar, o programa executa automaticamente todos os experimentos:

- Lê e normaliza os dois arquivos de texto (minúsculas + tokenização por regex)
- Para cada combinação de arquivo × função hash × tamanho M:
  - Insere todas as palavras distintas na tabela hash e na lista linear
  - Calcula fator de carga (α), max_bucket, média e variância dos buckets
  - Mede comparações de busca por sucesso (palavras que existem) e falha (palavras ausentes)
  - Gera e salva o histograma de distribuição dos buckets
- Exporta todos os resultados no arquivo `resultados.csv`

---

## Funções hash implementadas

| Nome | Descrição |
|------|-----------|
| `hash_soma` | H1 – soma simples dos valores Unicode dos caracteres |
| `hash_ponderada` | H2 – soma ponderada pela posição do caractere |
| `hash_polinomial` | H3 – método de Horner com R=31 |
| `hash_xor` | H4 – mistura com XOR e deslocamento de bits |
| `hash_prefixo` | Ruim proposital – usa só os 3 primeiros caracteres |
| `hash_sufixo` | Ruim proposital – usa só os 3 últimos caracteres |

---

## Tamanhos de tabela testados

| M | Tipo |
|---|------|
| 97 | Primo |
| 100 | Não primo |
| 997 | Primo maior |

---

## Saída gerada

**Terminal:** métricas de cada experimento impressas com separador visual.

**`resultados.csv`:** uma linha por experimento com as colunas:
`texto, M, hash_name, n, alpha, max_bucket, avg_bucket, total_comp_success, avg_comp_success, total_comp_fail, avg_comp_fail`

**Pasta `histogramas/`:** um arquivo `.png` por experimento com o gráfico de
distribuição dos buckets, nomeado como `arquivo_MMM_hash_nome.png`.

---

## Regra de tokenização

Regex utilizada: `[a-záàâãéêíóôõúùüçñ]+`

Extrai sequências de letras incluindo caracteres acentuados do português e espanhol,
ignorando números, pontuação e espaços. Todo o texto é convertido para minúsculas
antes da tokenização.
