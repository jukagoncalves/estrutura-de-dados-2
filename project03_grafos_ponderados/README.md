# GCT153 – Estruturas de Dados II
## Atividade 01 – Grafos: Rotas, Conectividade e Redes de Menor Custo

**Prof. Dr. Alysson Naves**  
**Aluno:** Juka Francis

---

## Descrição

Implementação de um grafo ponderado não direcionado e três algoritmos clássicos de grafos:

- **Dijkstra** — caminhos mínimos a partir de uma origem
- **Prim** — Árvore Geradora Mínima (MST) por expansão de vértices
- **Kruskal** — Árvore Geradora Mínima (MST) por ordenação de arestas

O grafo utilizado representa uma rede de 9 cidades (vértices 0–8) conectadas por 15 estradas ponderadas, simulando um cenário de logística e distribuição.

---

## Estrutura do Projeto

```
projeto_grafos/
│
├── Grafo.py        ← Classe GrafoPonderado (lista de adjacência)
├── Dijkstra.py     ← Algoritmo de Dijkstra + reconstrução de caminho
├── Prim.py         ← Algoritmo de Prim (MST)
├── Kruskal.py      ← Algoritmo de Kruskal + estrutura Union-Find
├── main.py         ← Ponto de entrada: monta o grafo e executa os experimentos
└── README.md       ← Este arquivo
```

---

## Pré-requisitos

- **Python 3.8 ou superior**
- Nenhuma biblioteca externa é necessária
- Módulos utilizados: `heapq` e `math` (ambos da biblioteca padrão do Python)

Para verificar sua versão do Python:

```bash
python --version
# ou
python3 --version
```

---

## Como Executar

### 1. Clone ou baixe o projeto

```bash
git clone <url-do-repositorio>
cd projeto_grafos
```

Ou, se recebeu os arquivos compactados:

```bash
unzip projeto_grafos.zip
cd projeto_grafos
```

### 2. Execute o programa principal

```bash
python main.py
```

> Em sistemas Linux/macOS, pode ser necessário usar `python3`:
> ```bash
> python3 main.py
> ```

### 3. Saída esperada

O programa exibirá no terminal, em sequência:

```
==== Grafo ====
0 : [(1, 4), (2, 2)]
1 : [(0, 4), (2, 1), (3, 5)]
...

==== Dijkstra ====
Distancias: [0, 3, 2, 8, 10, 13, 14, 18, 20]
Pais: [None, 2, 0, 1, 3, 4, 5, 6, 6]
Caminho 0 -> 5: [0, 2, 1, 3, 4, 5]
Custo: 13
Caminho 0 -> 8: [0, 2, 1, 3, 4, 5, 6, 8]
Custo: 20

==== Prim ====
Partindo do vértice 0:
Arestas escolhidas: [(0, 2, 2), (2, 1, 1), ...]
Custo total: 20
Ordem de inclusão: [2, 1, 3, 4, 5, 6, 7, 8]

Partindo do vértice 5:
Arestas escolhidas: [(5, 6, 1), (5, 4, 3), ...]
Custo total: 20
Ordem de inclusão: [6, 4, 3, 7, 8, 1, 2, 0]

=== Kruskal ====
Arestas selecionadas: [(1, 2, 1), (5, 6, 1), ...]
Arestas descartadas: [(0, 1, 4), (3, 5, 6), ...]
Custo total: 20
Arestas ordenadas por ordem crescente: [...]
```

---

## Experimentos Executados

| # | Experimento | Resultado |
|---|---|---|
| 1 | Dijkstra a partir do vértice 0 | Distâncias mínimas para todos os vértices |
| 2 | Reconstrução do caminho 0 → 5 | `[0, 2, 1, 3, 4, 5]`, custo 13 |
| 3 | Reconstrução do caminho 0 → 8 | `[0, 2, 1, 3, 4, 5, 6, 8]`, custo 20 |
| 4 | Prim a partir do vértice 0 | MST com custo total 20 |
| 5 | Prim a partir do vértice 5 | MST com custo total 20 (mesmo resultado) |
| 6 | Kruskal no mesmo grafo | MST com custo total 20 |
| 7 | Comparação Prim vs Kruskal | Mesmo custo (20) e mesmo conjunto de arestas |

---

## Restrições respeitadas

- Nenhuma biblioteca pronta de grafos foi utilizada (ex: NetworkX)
- Toda a estrutura do grafo e os algoritmos foram implementados do zero
- Módulos auxiliares permitidos utilizados: `heapq` (fila de prioridade) e `math.inf` (infinito)

---

## Observações

- O grafo é **não direcionado**: cada aresta `(u, v, peso)` é armazenada nos dois sentidos na lista de adjacência
- O formato interno das arestas no Kruskal é `(peso, u, v)` — com o peso primeiro, para compatibilidade com a ordenação e com o `heapq`
- A estrutura **Union-Find** implementada usa compressão de caminho (*path compression*), garantindo eficiência nas operações de `find` e `union`