
from Grafo import Grafo
from Dijkstra import dijkstra_heapq, reconstruir_caminho
from Prim import prim
from Kruskal import kruskal 

if __name__ == "__main__":
    grafo = Grafo(9)
    grafo.adicionar_aresta(0, 1, 4)
    grafo.adicionar_aresta(0, 2, 2)
    grafo.adicionar_aresta(1, 2, 1) 
    grafo.adicionar_aresta(1, 3, 5)
    grafo.adicionar_aresta(2, 3, 8)
    grafo.adicionar_aresta(2, 4, 10)
    grafo.adicionar_aresta(3, 4, 2)
    grafo.adicionar_aresta(3, 5, 6)
    grafo.adicionar_aresta(4, 5, 3)
    grafo.adicionar_aresta(4, 6, 7)
    grafo.adicionar_aresta(5, 6, 1)
    grafo.adicionar_aresta(5, 7, 9)
    grafo.adicionar_aresta(6, 7, 4)
    grafo.adicionar_aresta(6, 8, 6)
    grafo.adicionar_aresta(7, 8, 2)

    print("==== Grafo ====")
    grafo.exibir_grafo()

    print("\n==== Dijkstra ====")
    distancia, pais = dijkstra_heapq(grafo, 0)
    print(f"Distancias: {distancia}")
    print(f"Pais: {pais}")
    destinos = [5,8]
    for destino in destinos:
        caminho = reconstruir_caminho(pais, destino)
        print(f"Caminho 0 -> {destino}: {caminho}")
        print(f"Custo: {distancia[destino]}")

    print("\n==== Prim ====")
    print("Partindo do vértice 0:")
    mst_prim, custo_prim, ordem = prim(grafo, 0)
    print(f"Arestas escolhidas: {mst_prim}")
    print(f"Custo total: {custo_prim}")
    print(f"Ordem de inclusão: {ordem}")
    print("\nPartindo do vértice 5:")
    mst_prim, custo_prim, ordem = prim(grafo, 5)
    print(f"Arestas escolhidas: {mst_prim}")
    print(f"Custo total: {custo_prim}")
    print(f"Ordem de inclusão: {ordem}")
    

    print("\n=== Kruskal ====")
    arestas = grafo.obter_arestas()
    mst_kruskal, custo_kruskal, descartadas, ordenadas = kruskal(9, arestas)
    print(f"Arestas selecionadas: {mst_kruskal}")
    print(f"Arestas descartadas: {descartadas}")
    print(f"Custo total: {custo_kruskal}")
    print(f"Arestas ordenadas por ordem crecente: {ordenadas}")
    