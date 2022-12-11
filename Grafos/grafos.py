from idna import valid_string_length


class Graph:
    def __init__(self):
        self.__vertices = {}  # dicionario de vertices
        self.__arestas = []   # array de arestas

    @property
    def vertices(self):
        return self.__vertices

    @property
    def arestas(self):
        return self.__arestas

    @vertices.setter
    def vertices(self, value):
        self.__vertices = value
    
    @arestas.setter
    def arestas(self, value):
        self.__arestas.append(value)

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
            if e[0] == int(u) and e[1] == int(v):
                return True
        return False
    def haArestaNdirigido(self, u, v):
        for e in self.__arestas:
            if (e[0] == int(u) and e[1] == int(v)) or (e[0] == int(v) and e[1] == int(u)):
                return True
        return False


    # Retorna o peso de uma aresta entre o vertice u e v
    def peso_dirigido(self, u, v):
        if self.haAresta(u, v):
            for i in self.__arestas:
                if (i[0] == int(u) and i[1] == int(v)):
                    return i[2]

    # Confere as duas direcoes da aresta, usado no dijkstra
    def peso_nao_dirigido(self, u, v):
        if self.haAresta(u, v) or self.haAresta(v, u):
            for i in self.__arestas:
                if (i[0] == int(u) and i[1] == int(v)) or (i[0] == int(v) and i[1] == int(u)):
                    return i[2]

    # Ler o arquivo e cria o grafo
    def ler(self, file_path):
        try:
            file = open(file_path, 'r')
        except FileNotFoundError:
            print("Arquivo nao encontrado")

        try:
            number_vertices = int(file.readline()[10:-1])
            for line in range(number_vertices):
                line = file.readline()
                # Quando o rotulo for uma string
                try:
                    # funciona enquanto os rotulos estiverem dentro de aspas duplas
                    words = line.split("\"")
                    vertice = {"rotulo": words[1], "vizinhos": set()}
                # Quando o rotulo não estiver dentro de aspas
                except:
                    words = line.split()
                    try:
                        # quando for um inteiro (utilizado para testes)
                        vertice = {"rotulo": int(words[1]), "vizinhos": set()}
                    except:
                        # quando for uma palavra
                        vertice = {"rotulo": words[1], "vizinhos": set()}

                self.__vertices[int(words[0])] = vertice

            # Arcs or Edges?
            line = file.readline()
            connection = line.split()[0][1:]

            while True:
                line = file.readline()
                if not line:
                    break
                vert1, vert2, weight = line.split()
                vert1 = int(vert1)
                vert2 = int(vert2)
                weight = float(weight)

                self.__vertices[vert1]["vizinhos"].add(vert2)
                if (connection == "edges"):
                    self.__vertices[vert2]["vizinhos"].add(vert1)
                aresta = (vert1, vert2, weight)
                self.__arestas.append(aresta)
        except:
            #acontece quando não há rotulo para os vertices
            while True:
                try:
                    line = file.readline()
                    # Quando o rotulo for uma string
                    vertice = {"rotulo": line, "vizinhos": set()}
                    # Quando o rotulo não estiver dentro de aspas
                    self.__vertices[int(line)] = vertice
                except:
                    break

            while True:
                line = file.readline()
                if not line:
                    break
                vert1, vert2 = line.split()
                vert1 = int(vert1)
                vert2 = int(vert2)

                self.__vertices[vert1]["vizinhos"].add(vert2)
                self.__vertices[vert2]["vizinhos"].add(vert1)
                aresta = (vert1, vert2)
                self.__arestas.append(aresta)
            


    # Retorna um lista com os vertices vizinhos que saem de v
    def saintes(self, v):
        saintes = list()
        for i in self.__arestas:
            if i[0] == int(v):
                saintes.append(i[1])

        return saintes

    # Retorna uma lista com os vertices que tem arestas dirigidas para v
    def entrantes(self, v):
        entrantes = list()
        for i in self.__arestas:
            if i[1] == int(v):
                entrantes.append(i[0])

        return entrantes

    # retorna a lista de vertices em numeros
    def vertices_list(self):
        return list(self.__vertices.keys())

    # utilizado pelo algoritmo de fluxo_maximo para criacao
    # de grafo residual
    def insere_aresta(self, element):
        self.__arestas.append(element)

    # utilizado pelo algoritmo de fluxo_maximo para checar
    # a existencia de arestas u,v e v,u. Caso existam cria novo
    # vertice v' e conecta v->v' e v'->u
    def confere_e_cria_vertice_fluxo(self):
        for i in range(len(self.__arestas)):
            u = self.__arestas[i][0]
            v = self.__arestas[i][1]
            for j in range(i + 1, len(self.__arestas)):
                if (self.__arestas[j][0] == v and self.__arestas[j][1] == u):
                    # cria novo vertice
                    num = len(self.__vertices) + 1
                    vertice = {"rotulo": str(num)+"x", "vizinhos": set()}
                    self.__vertices[num] = vertice
                    # adiciona 'u' como vizinho
                    self.__vertices[num]["vizinhos"].add(u)
                    # adiciona novo vertice como vizinho de 'v'
                    self.__vertices[v]["vizinhos"].add(num)
                    # elimina 'u' como vizinho de 'v'
                    self.__vertices[v]["vizinhos"].remove(u)

                    # Atualiza lista de arestas
                    cap = self.__arestas[j][2]
                    self.__arestas.pop(j)
                    self.__arestas.append((v, num, cap))
                    self.__arestas.append((num, u, cap))
                    break

    # utilizado pelo algoritmo de fluxo_maximo para
    # atualizacao dos valores das capacidades de cada arco
    def atualiza_capacidades(self, u, v, fluxo):
        # cap(u, v) = cap(u, v) - fluxo
        for i in range(len(self.__arestas)):
            if (self.__arestas[i][0] == u and self.__arestas[i][1] == v):
                self.__arestas[i] = (u, v, self.__arestas[i][2] - fluxo)

        # cap(v, u) = cap(v, u) + fluxo
        for i in range(len(self.__arestas)):
            if (self.__arestas[i][0] == v and self.__arestas[i][1] == u):
                self.__arestas[i] = (v, u, self.__arestas[i][2] + fluxo)

    # cria duas listas de vertices
    def grafo_bipartido(self,tipo):
        x = []
        y = []
        for i in self.__arestas:
            x.append(i[0])
            y.append(i[1])
        if tipo == "x":
            return set(x)
        elif tipo == "y":
            return set(y)
