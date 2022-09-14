# biblioteca de grafos

class Grafo_nD_P:  # grafo nao dirigido e ponderado
    def __init__(self, V=None, E=None, w=None):
        # conjunto de vertices [(1, "rotulo 1"), (2, "rotulo 2"), ...]
        self.V = V
        self.E = E  # conjunto de arestas [(1, 2), (1, 3), ..., (5, 6)]
        self.w = w  # função que mapeia o peso de cada aresta {u, v} ∈ E
        # [(1, 2, 1.0), (1, 3, 4.3), ...]

    # Complexidade O(1)
    def qtdVertices(self):
        return len(self.V)

    # Complexidade O(1)
    def qtdArestas(self):
        return len(self.E)

    # Numero de vizinhos
    # Complexidade O(n)
    def grau(self, v):
        return len(self.vizinhos(v))

    # Complexidade O(n)
    def rotulo(self, v):
        for i in self.V:
            if (i[0] == v):
                return i[1]
        return 0

    # Complexidade O(n)
    def vizinhos(self, v):
        neighbors = []
        for i in self.E:
            if i[0] == v:
                neighbors.append(i[1])
            if i[1] == v:
                neighbors.append(i[0])
        return neighbors

    # Complexidade O(n)
    def haAresta(self, u, v):
        for i in self.w:
            if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                return True

        return False

    # Complexidade O(n)
    def peso(self, u, v):
        for i in self.w:
            if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                return i[2]

        return False

    def ler(self, arquivo):
        file = open(arquivo, "r")
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
                counter = int(values[1]) + 1  # Gambiarra
            if values[0] != "*vertices" and values[0] != "*edges" and counter > 0:
                verticeList.append((int(values[0]), line.split("\"")[1]))
            if values[0] != "*vertices" and values[0] != "*edges" and counter < 0:
                edgesList.append((int(values[0]), int(values[1])))
                weightList.append(
                    (int(values[0]), int(values[1]), float(values[2])))
            counter -= 1
        file.close()
        self.V = verticeList
        self.E = edgesList
        self.w = weightList
        return 0
