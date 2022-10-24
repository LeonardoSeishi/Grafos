import queue
from grafos import Graph as G


def busca_largura(G, s):

    s = int(s)
    # Estrutura que armazena um booleano que indica se um determinado vértice foi visitado
    C = {}
    # Estrutura que armazena o número de arestas necessárias para ir do vértice s (fornecido) até qualquer outro vértice
    D = {}
    # Estrutura que armazena os antecessores de cada vértice
    A = {}

    for i in range(1, G.qtdVertices()+1):
        C[i] = False
        D[i] = 0
        A[i] = None

    C[s] = True
    D[s] = 0
    Q = queue.Queue()
    Q.put(s)

    while not (Q.empty()):
        u = Q.get()
        vizinhos = G.vizinhos_lista(u)

        for v in vizinhos:
            if C[v] == False:
                C[v] = True
                D[v] = D[u] + 1
                A[v] = u
                Q.put(v)

    return D, A


def imprime_busca(D, qtdV):
    maxLevel = max(D.values())
    count = 0

    while count <= maxLevel:
        level = []
        print(f"{count}: ", end='')
        for i in range(1, qtdV + 1):
            if D[i] == count:
                level.append(i)

        if len(level) > 1:
            for i in range(0, len(level)):
                if i == len(level)-1:
                    print(f"{level[i]}", end="\n")
                else:
                    print(f"{level[i]},", end=" ")
        else:
            print(f"{level[0]}", end="\n")

        count += 1
        level.clear()
