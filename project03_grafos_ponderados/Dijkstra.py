from math import inf
from Grafo import Grafo
import heapq

def dijkstra_heapq(grafo: Grafo, origem: int):
    num_vertices = grafo.num_vertices
    distancia = [inf] * num_vertices
    pais = [None] * num_vertices
    distancia[origem] = 0
    visitado = [False]*num_vertices

    fila = [(0, origem)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)
        if(visitado[vertice_atual]):
            continue 
        
        visitado[vertice_atual] = True
        
        for vizinho, peso in grafo.retorna_vizinho(vertice_atual):
            nova_distancia = distancia[vertice_atual] + peso

            if(nova_distancia < distancia[vizinho]):
                distancia[vizinho] = nova_distancia
                pais[vizinho] = vertice_atual
                heapq.heappush(fila, (nova_distancia, vizinho))
    
    return distancia, pais

def reconstruir_caminho(pais, destino):
    caminho = [destino]
    vertice_atual = destino

    while pais[vertice_atual] is not None:
        vertice_atual = pais[vertice_atual]
        caminho.append(vertice_atual)

    caminho.reverse()
    return caminho