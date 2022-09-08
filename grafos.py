#biblioteca de grafos

from cmath import pi


class Grafo_nD_P: #grafo nao dirigido e ponderado
    def __init__(self, V=None, E=None, w=None):
        self.V = V  #conjunto de vertices
        self.E = E  #conjunto de arestas
        self.w = w  #função que mapeia o peso de cada aresta {u, v} ∈ E

    def qtdVertices(self):
        return len(self.V)

    def qtdArestas(self):
        return len(self.E)

    # Numero de vizinhos
    def grau(self, v):
        return len(self.vizinhos(v))

    def rotulo(self, v):
        return 0

    def vizinhos(self, v):
        neighbors = []
        for i in self.E:
            if i[0] == v:
                neighbors.append(i[1])
            if i[1] == v:
                neighbors.append(i[0])
        return neighbors

    def haAresta(self, u, v):
        neighbors = []
        for i in self.w:
            if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                return True

        return False

    def peso(self, u, v):

        for i in self.w:
            if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                return i[2]
             
        return False

    def ler(self, arquivo):
        file = open(arquivo,"r")
        verticeList = list()
        edgesList = list()
        weightList = list()
        # Utilizado para controle de iteração 
        # Linha 1 ate n -> vertices 
        # Linha n + 2 ate fim -> arestas
        counter = 0 
        for line in file:
            values = line.split()
            if values[0] == "*vertices":
                counter = int(values[1]) + 1 # Gambiarra
            if values[0] != "*vertices" and values[0] != "*edges" and counter > 0:
                verticeList.append(int(values[0]))
            if values[0] != "*vertices" and values[0] != "*edges" and counter < 0:
                edgesList.append((int(values[0]), int(values[1])))
                weightList.append((int(values[0]), int(values[1]), float(values[2])))
            counter -= 1
        file.close()
        self.V = verticeList
        self.E = edgesList
        self.w = weightList
        return 0

    

