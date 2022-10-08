
def haVerticeNaoPercorrido(C):
    for value in C.values():
        if (not value):
            return True
    return False


def verticeMenorDistancia(D, C):
    D_ = dict()
    # monta um novo dict com os vertices nao percorridos
    for k, v in D.items():
        if (not C[k]):
            D_[k] = v

    v_min = min(list(D_.values()))  # vertice de menor distancia
    for k, v in D_.items():
        if (v == v_min):
            return k  # chave cujo valor corresponde a menor distancia


def gera_caminho(A, v):
    caminho = []
    caminho.append(v)
    u = A[v]
    while (u != None):
        caminho.insert(0, u)
        u = A[u]

    str_caminho = ""
    for i in caminho:
        str_caminho += str(i) + ","

    str_caminho = str_caminho[0:-1]  # remove a ultima virgula
    return str_caminho


def dijkstra(grafo, s):
    # Inicializacao variaveis
    vertices = grafo.vertices_list()
    D = dict()
    A = dict()
    C = dict()
    for i in vertices:
        D[i] = float('inf')
        A[i] = None
        C[i] = False

    D[s] = 0
    while (haVerticeNaoPercorrido(C)):
        u = verticeMenorDistancia(D, C)
        C[u] = True
        for v in grafo.vizinhos_lista(u):
            if (C[v]):  # vertices ja percorridos nao entram no laco
                continue
            if (D[v] > D[u] + grafo.peso(u, v)):
                D[v] = D[u] + grafo.peso(u, v)
                A[v] = u

    # print solicitado pela atividade
    for i in grafo.vertices_list():
        print(f'{i}: {gera_caminho(A, i)}; d={D[i]}')
