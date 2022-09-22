import queue
from grafos import Graph as G

def busca_largura(G, s):

    C = []
    D = []
    A = []
    print(G.qtdVertices())
    for i in range(1, G.qtdVertices()):
        C.insert(i, False)
        D.insert(i, 0)
        A.insert(i, None)

        

    Q = queue.Queue()
    Q.put(s)


    while not(Q.empty()):
        u = Q.get()
        saintes = G.saintes(u)
        for v in saintes:
            print(saintes, v)
            print(C)
            if C[v] == False:
                C[v] = True
                D[v] = D[u] + 1
                A[v] = u
                Q.put(v)
    
    return (D, A)


