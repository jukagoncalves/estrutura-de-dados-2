# Projeto 02 — Grafos com Lista de Adjacência

> **GCT153 — Estruturas de Dados II**  
> Prof. Dr. Alysson Naves

---

## Descrição

Implementação de um **grafo não direcionado** utilizando **lista de adjacência** em Java, com os seguintes algoritmos clássicos de percurso:

-  **DFS** — Busca em Profundidade (*Depth-First Search*)
-  **BFS** — Busca em Largura (*Breadth-First Search*)
-  **Componentes Conexas** — Identificação e contagem

---

## Estrutura do Projeto

```
projeto-grafos/
├── src/
│   ├── Grafos.java       # Classe principal com toda a lógica do grafo
│   └── App.java          # Classe de execução e testes
├── relatorio/
│   └── relatorio.pdf     # Relatório técnico do projeto
└── README.md
```

---

## Tecnologias

| Tecnologia | Versão |
|------------|--------|
| Java       | 17+    |
| Paradigma  | POO    |

---

## Como Executar

### Pré-requisitos
- Java JDK 17 ou superior instalado
- Terminal ou IDE de sua preferência (VS Code, IntelliJ, Eclipse)

### Compilar e rodar pelo terminal

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta do projeto
cd projeto-grafos/src

# Compile
javac Grafos.java App.java

# Execute
java App
```

---

## Grafo de Teste

O grafo utilizado possui **10 vértices** (0 a 9) e **7 arestas**:

```
Arestas: 0-1  1-2  2-3  4-5  6-7  7-8  8-6
Vértice 9: isolado
```

Representação visual:

```
0 — 1 — 2 — 3       4 — 5       6 — 7
                                 \  /
                                  8
                    9 (isolado)
```

---

## Saída Esperada

```
Vertice 0-> [1]
Vertice 1-> [0, 2]
Vertice 2-> [1, 3]
Vertice 3-> [2]
Vertice 4-> [5]
Vertice 5-> [4]
Vertice 6-> [7, 8]
Vertice 7-> [6, 8]
Vertice 8-> [7, 6]
Vertice 9-> []

Ordem DFS: 0 1 2 3
Ordem DFS: 4 5
Ordem DFS: 6 7 8
Ordem DFS: 9

Ordem do BFS: 0 1 2 3
Ordem do BFS: 4 5
Ordem do BFS: 6 7 8
Ordem do BFS: 9

Componente 1: 0 1 2 3
Componente 2: 4 5
Componente 3: 6 7 8
Componente 4: 9
Total de componentes conexas: 4
```

---

## Conceitos Aplicados

### DFS — Busca em Profundidade
Explora cada caminho até o fim antes de retroceder (*backtracking*). Utiliza recursão (pilha implícita). Implementado com padrão público/privado para isolamento do estado.

### BFS — Busca em Largura
Explora o grafo nível por nível utilizando uma fila. Garante o menor caminho em grafos não ponderados.

### Componentes Conexas
Subconjuntos de vértices onde qualquer par possui caminho entre si. Identificadas percorrendo todos os vértices e executando DFS em cada vértice não visitado.

---

## Complexidade

| Algoritmo           | Tempo      | Espaço  |
|---------------------|------------|---------|
| Inserção de aresta  | O(1)       | O(1)    |
| Exibir grafo        | O(V + E)   | O(1)    |
| DFS                 | O(V + E)   | O(V)    |
| BFS                 | O(V + E)   | O(V)    |
| Componentes Conexas | O(V + E)   | O(V)    |

---

## Arquitetura

```
Classe Grafos
├── Atributos
│   ├── int qtdVertices
│   └── ArrayList<Integer>[] listaAdj
├── Métodos Públicos
│   ├── inserirAresta(int origem, int destino)
│   ├── exibirGrafo()
│   ├── dfs(int origem)
│   ├── bfs(int origem)
│   └── componentesConexas()
└── Métodos Privados
    └── dfsAuxiliar(int v, boolean[] visitado)
```

---

## Autor

**Juka Francis Pereira Gonçalves**  
Engenharia de Software — Universidade Federal de Lavras (UFLA)  
Matrícula: 202415040

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos na disciplina GCT153 — Estruturas de Dados II.