class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adj = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, origem: int, destino: int, peso: int):
        #Adiciona uma aresta nao-direcionada entre origem e destino
        self.lista_adj[origem].append((destino, peso))
        self.lista_adj[destino].append((origem, peso))

    def exibir_grafo(self):
        for vertice in range(self.num_vertices):
            print(f"{vertice} : {self.lista_adj[vertice]}")
        
    def retorna_vizinho(self, origem):
        return self.lista_adj[origem]
    
    def obter_arestas(self):
        arestas = []
        for u in range(self.num_vertices):
            for v, peso in self.lista_adj[u]:
                if u < v:  # evita duplicar (grafo não direcionado)
                    arestas.append((peso, u, v))
        return arestas
        
        





        