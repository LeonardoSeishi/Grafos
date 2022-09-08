#biblioteca de grafos

class Grafo_nD_P: #grafo nao dirigido e ponderado
    def __init__(self, V, E, w ):
        self.V = V  #conjunto de vertices
        self.E = E  #conjunto de arestas
        self.w = w  #função que mapeia o peso de cada aresta {u, v} ∈ E

    def qtdVertices(self):
        return len(self.V)

    def qtdArestas(self):
        return len(self.E)

    def grau(self, v):
        return 0

    def rotulo(self, v):
        return 0

    def vizinhos(self, v):
        return []

    def haAresta(self, u, v):
        return False

    def peso(self, u, v):
        return 999999999999999

    def ler(self, arquivo):
        return 0

    

