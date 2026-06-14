class UnionFind:

    def __init__(self, n):
        self.pai = list(range(n))

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, a, b):
        raizA = self.find(a)
        raizB = self.find(b)
        if raizA != raizB:
            self.pai[raizB] = raizA



def kruskal(num_vertices, arestas):
    arestas.sort() #ordem crescente pelo peso
    lista_ordenada = arestas
    uf = UnionFind(num_vertices)
    mst = []
    descartadas = []
    custo = 0
    for peso, u, v in lista_ordenada:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, peso))
            custo += peso
        else:
            descartadas.append((u, v, peso))
    return mst, custo, descartadas, lista_ordenada