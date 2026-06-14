import heapq 
from Grafo import Grafo

def prim(grafo, origem):
    visitado = set([origem])
    ordem = [] 
    arestas = [] #fila de prioridade
    for v, peso in grafo.retorna_vizinho(origem):
        heapq.heappush(arestas, (peso, origem, v))
    mst = [] #arvore geradora minima
    custo = 0
    while arestas:
        peso, u, v = heapq.heappop(arestas)
        if v in visitado:
            continue
        visitado.add(v)
        mst.append((u, v, peso))
        ordem.append(v)
        custo += peso
        for prox, p in grafo.retorna_vizinho(v):
            if prox not in visitado:
                heapq.heappush(arestas, (p, v, prox))
    return mst, custo, ordem