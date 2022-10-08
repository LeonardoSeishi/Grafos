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
    def qtdVertices(self):
        return len(self.__vertices)

    # Complexidade O(1)
    def qtdArestas(self):
        return len(self.__arestas)

    # Retorna o numero de vizinhos de um vertice v
    def grau(self, v):
        return len(self.__vertices[v]["vizinhos"])

    # Retorna o rotulo de um vertice v
    def rotulo(self, v):
        return self.__vertices[v]["rotulo"]

    # Retorna uma lista com todos os vizinhos de v
    def vizinhos(self, v):
        viz = list()
        for i in self.__vertices[v]["vizinhos"]:
            viz.append(self.__vertices[i]["rotulo"])
        return viz

    # Retorna uma lista com os vizinhos em numeros
    def vizinhos_lista(self, v):
        return list(self.__vertices[v]["vizinhos"])

    # Retorna um booleano se existe uma aresta entre o vertice u e v
    def haAresta(self, u, v):
        for e in self.__arestas:
            if e[0] == u and e[1] == v:
                return True
        return False

    # Retorna o peso de uma aresta entre o vertice u e v
    def peso(self, u, v):
        if self.haAresta(u, v):
            for i in self.__arestas:
                if (i[0] == u and i[1] == v):
                    return i[2]

    # Confere as duas direcoes da aresta, usado no dijkstra
    def peso_nao_dirigido(self, u, v):
        if self.haAresta(u, v) or self.haAresta(v, u):
            for i in self.__arestas:
                if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                    return i[2]

    # Ler o arquivo e cria o grafo
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

            # Quando o rotulo for uma string
            try:
                # funciona enquanto os rotulos estiverem dentro de aspas duplas
                words = line.split("\"")
                vertice = {"rotulo": words[1], "vizinhos": set()}
            # Quando o rotulo for um inteiro (utilizado para testes)
            except:
                words = line.split()
                vertice = {"rotulo": int(words[1]), "vizinhos": set()}

            self.__vertices[int(words[0])] = vertice

        # Pula a linha "*edges"
        file.readline()

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

    # Retorna um lista com os vertices vizinhos que saem de v
    def saintes(self, v):
        saintes = list()
        for i in self.__arestas:
            if i[0] == v:
                saintes.append(i[1])

        return saintes

    # Retorna uma lista com os vertices que tem arestas dirigidas para v
    def entrantes(self, v):
        entrantes = list()
        for i in self.__arestas:
            if i[1] == v:
                entrantes.append(i[0])

        return entrantes

    # retorna a lista de vertices em numeros
    def vertices_list(self):
        return list(self.__vertices.keys())
