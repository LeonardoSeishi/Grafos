import sys

sys.path.insert(0, "../Grafos/Grafos")

from grafos import *

def visit_ot(G):

    C = {}
    T = {}
    F = {}
    O = []
    tempo = 0
    
    # Configurando todos os vértices
    for i in range(1, G.qtdVertices()+1):
        C[i] = False
        T[i] = float('inf')
        F[i] = float('inf')


    for u in G.vertices:    
        if not(C[u]):
            dfs_visit_ot(G, u, C, T, F, tempo, O)   


    return O


def dfs_visit_ot(G, v, C, T, F, tempo, O):
    
    C[v]  = True
    tempo = tempo + 1
    T[v]  = tempo

    # TODO: mudar para não ponderado
    vizinhos = G.saintes(v)
    for i in vizinhos:
        if not(C[i]):
            dfs_visit_ot(G, i, C, T, F, tempo, O )

    tempo = tempo + 1
    F[v]  = tempo
    O.insert(0, v)

def print_ord(grafo, lista):
    for i in range(0, len(lista)):
        if i == len(lista)-1:
            print(grafo.vertices[lista[i]]["rotulo"])    
        else:
            print(grafo.vertices[lista[i]]["rotulo"], "->", end=" ")    
