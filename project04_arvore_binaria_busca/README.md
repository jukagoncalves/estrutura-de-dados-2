# Árvore Binária de Busca (BST)

**GCT153 – Estruturas de Dados II**
Prof. Dr. Alysson Naves 

---

## Descrição

Implementação de uma Árvore Binária de Busca em Python, desenvolvida manualmente sem o uso de bibliotecas prontas. O projeto inclui todas as operações fundamentais da BST e uma interface interativa no terminal.

---

## Estrutura do Projeto

```
.
├── bst.py       # Implementação das classes No e ArvoreBinariaBusca
├── main.py      # Interface interativa com menu de 13 opções
├── README.md    # Este arquivo
└── Relatório_Tabela_Hash.pdf/  # PDF do relatório
```

---

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa é necessária

Para verificar sua versão do Python:

```bash
python3 --version
```

---

## Como Executar

### Interface interativa (menu)

```bash
python3 main.py
```

Isso abrirá o menu com todas as operações disponíveis:

```
╔══════════════════════════════════════╗
║     ÁRVORE BINÁRIA DE BUSCA (BST)    ║
╠══════════════════════════════════════╣
║  1. Inserir valor                    ║
║  2. Buscar valor                     ║
║  3. Remover valor                    ║
║  4. Menor valor                      ║
║  5. Maior valor                      ║
║  6. Percurso pré-ordem               ║
║  7. Percurso em-ordem                ║
║  8. Percurso pós-ordem               ║
║  9. Contar nós                       ║
║ 10. Contar folhas                    ║
║ 11. Altura da árvore                 ║
║ 12. Verificar se está vazia          ║
║ 13. Visualizar árvore                ║
║  0. Sair                             ║
╚══════════════════════════════════════╝
```

### Usar a BST como módulo em outro arquivo

```python
from bst import ArvoreBinariaBusca

arvore = ArvoreBinariaBusca()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)

print(arvore.em_ordem())   # [5, 10, 15]
print(arvore.altura())     # 1
print(arvore.buscar(5))    # True
```

---

## Exemplo de Uso

A seguir, um exemplo de sessão interativa inserindo os valores `10 5 15 2 7 12 20` e visualizando a árvore:

```
Escolha uma opção: 1
Valores para inserir (separados por espaço): 10 5 15 2 7 12 20
✔ Inserido(s): [10, 5, 15, 2, 7, 12, 20]
Árvore atual:

  [10]
  ├── [5]
  │   ├── [2]
  │   └── [7]
  └── [15]
      ├── [12]
      └── [20]
```

> **Dica:** na opção 1, é possível inserir vários valores de uma vez, separados por espaço.

---

## Operações e Complexidade

| Operação       | Caso médio  | Pior caso (degenerada) |
|----------------|-------------|------------------------|
| Inserir        | O(log n)    | O(n)                   |
| Buscar         | O(log n)    | O(n)                   |
| Remover        | O(log n)    | O(n)                   |
| Mínimo/Máximo  | O(log n)    | O(n)                   |
| Percursos      | O(n)        | O(n)                   |
| Altura         | O(n)        | O(n)                   |

O pior caso ocorre quando os valores são inseridos em ordem crescente ou decrescente, degenerando a árvore em uma lista encadeada.

---

## Decisões de Implementação

- **Valores repetidos:** são ignorados silenciosamente. Se um valor já presente for inserido novamente, nenhuma modificação é feita na árvore.
- **Remoção com dois filhos:** utiliza o sucessor em-ordem (menor valor da subárvore direita) para substituir o nó removido, preservando a propriedade da BST.
- **Convenção de altura:** árvore vazia retorna `-1`; árvore com apenas a raiz retorna `0`.
