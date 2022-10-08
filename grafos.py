class Graph:
    def __init__(self):
        self.__vertices = {}  # dicionario de vertices
        self.__arestas = []  # array de arestas

    @property
    def vertices(self):
        return self.__vertices

    @property
    def arestas(self):
        return self.__arestas

    # Complexidade O(1)
    # TODO: Retirar o menos um se nao tiver o NoneType como primeiro elemento

    def qtdVertices(self):
        return len(self.__vertices)

    # Complexidade O(1)
    # TODO: Mudar o começo do for de 1 para zero se nao tiver o NoneType como primeiro elemento
    def qtdArestas(self):
        return len(self.__arestas)

    # # Numero de vizinhos
    def grau(self, v):
        return len(self.__vertices[v]["vizinhos"])

    def rotulo(self, v):
        return self.__vertices[v]["rotulo"]

    # TODO : printar o nome dos usuários
    # ! esta saindo um none no final
    def vizinhos(self, v):
        for i in self.__vertices[v]["vizinhos"]:
            print(self.__vertices[i]["rotulo"])

    def vizinhos_lista(self, v):
        return list(self.__vertices[v]["vizinhos"])

    def haAresta(self, u, v):
        return u in self.__vertices[v]["vizinhos"]

    def peso(self, u, v):
        if self.haAresta(u, v):
            for i in self.__arestas:
                if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                    return i[2]

    # ? O primeiro elemento a ser inserido na lista é NoneType. está correto?
    def ler(self, file_path):
        try:
            file = open(file_path, 'r')
        except FileNotFoundError:
            print("Arquivo nao encontrado")

        try:
            number_vertices = int(file.readline()[10:-1])
        except ValueError:
            print("Nao foi possivel obter numero de vertices")

        for line in range(number_vertices):
            line = file.readline()
            # funciona enquanto os rotulos estiverem dentro de aspas duplas
            words = line.split("\"")
            # ? O que vai ser o size
            vertice = {"rotulo": words[1], "vizinhos": set()}
            self.__vertices[int(words[0])] = vertice

        file.readline()  # Pula a linha "*edges"

        while True:
            line = file.readline()
            if not line:
                break
            vert1, vert2, weight = line.split()
            vert1 = int(vert1)
            vert2 = int(vert2)
            weight = float(weight)

            self.__vertices[vert1]["vizinhos"].add(vert2)
            self.__vertices[vert2]["vizinhos"].add(vert1)
            aresta = (vert1, vert2, weight)
            self.__arestas.append(aresta)

    def saintes(self, v):
        saintes = list()
        for i in self.__arestas:
            if i[0] == v:
                saintes.append(i[1])

        return saintes

    def entrantes(self, v):
        entrantes = list()
        for i in self.__arestas:
            if i[1] == v:
                entrantes.append(i[0])

        return entrantes

    def vertices_list(self):
        return list(self.__vertices.keys())
