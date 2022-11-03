
def imprime(grafo, A):
    C = dict()
    vertices = grafo.vertices_list()
    for i in vertices:
        C[i] = {i}
    for v in vertices:
        if (A[v] != None):
            u = A[v]
            x = C[v].union(C[u])
            for i in x:
                C[i] = x
    lista = []
    for i in C.values():
        if (i not in lista):
            lista.append(i)
    stri = ""
    for element in lista:
        for j in element:
            stri += str(j)+', '
        print(stri[:-2])
        stri = ""


# Componentes Fortemente Conexas
# Ao invés de inverter a ordem dos arcos, o algoritmo
# DFS_adap irá verificar os vértices entrantes a cada
# vértice. Ao invés de inverter o sentido de todos os arcos e verificar os saintes.
def cfc(grafo):
    L = DFS(grafo)
    A = DFS_adap(grafo, L)
    imprime(grafo, A)


# Chamada pela função DFS.
# Ao invés de armazenar o tempo em uma estrutura de dados,
# cada nó que finaliza uma chamada recursiva é adicionado ao início
# da lista (L)
def DFS_visit(grafo, v, C, L):
    C[v] = True
    for u in grafo.saintes(v):
        if (C[u] == False):
            DFS_visit(grafo, u, C, L)
    L.insert(0, v)


# Primeiro DFS chamado pela cfc, o principal
# objetivo dessa função é retornar uma lista (L) com
# as primeiras arestas a serem visitadas pelo DFS_adap
def DFS(grafo):
    C = dict()
    L = list()
    vertices = grafo.vertices_list()
    for i in vertices:
        C[i] = False

    for v in vertices:
        if (C[v] == False):
            DFS_visit(grafo, v, C, L)

    return L


# Cada vez que um vértice é visitado, os vértices
# de arcos entrantes a este vértice, que ainda não foram visitados, são
# pendurados na árvore de antecessores e chamados pela função recursivamente
def DFS_visit_adap(grafo, v, C, A):
    C[v] = True
    for u in grafo.entrantes(v):
        if (C[u] == False):
            A[u] = v
            DFS_visit_adap(grafo, u, C, A)


# Essa é a versão adaptada do algoritmo DFS
# os vértices são visitados na ordem fornecida pela lista L
def DFS_adap(grafo, L):
    C = dict()
    A = dict()
    vertices = grafo.vertices_list()
    for i in vertices:
        C[i] = False
        A[i] = None

    for v in L:
        if (C[v] == False):
            DFS_visit_adap(grafo, v, C, A)

    return A
