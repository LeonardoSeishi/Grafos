import modules
import grafos as g
from queue import Queue



def BFS(grafo, emparelhamento, D):
    fila = Queue()
    for i in grafo.grafo_bipartido("x"):
        if emparelhamento[i] == None:
            D[i] = 0
            fila.put(i)
        else:
            D[i] = float("inf")

    D[None] = float("inf")
    
    while not(fila.empty()):
        x = fila.get()
        if D[x] < D[None]:
            for v in grafo.vizinhos_lista(x):
                if D[emparelhamento[v]] == float('inf'):
                    D[emparelhamento[v]] = D[x] + 1
                    fila.put(emparelhamento[v])
    
    return (D[None] != float("inf"))



def DFS(grafo, emparelhamento, x, D):
    if x != None:
        for y in grafo.vizinhos_lista(x):
            if D[emparelhamento[y]] == D[x] + 1:
                if DFS(grafo, emparelhamento, emparelhamento[y], D):
                    emparelhamento[y] = x
                    emparelhamento[x] = y
                    return True
        D[y] = float('inf')
        return False
    return True
    


def Hopcroft_Karp(grafo):
    D = {}
    emparelhamento = {}
    for i in grafo.vertices_list():
        D[i] = float("inf")
        emparelhamento[i] = None
    maximo = 0
    while BFS(grafo,emparelhamento,D):
        for x in grafo.grafo_bipartido("x"):
            if emparelhamento[x] == None:
                if DFS(grafo,emparelhamento,x,D):
                    maximo = maximo + 1

    return (maximo, emparelhamento)

