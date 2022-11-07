from grafos import Graph
 
def Prim(G):
    r = G.vertices_list()[0]
    A = {}
    K = {}
    for v in (G.vertices_list()):
        A[v] = None
        K[v] = float('inf')
 
    K[r] = 0
 
    while len(K) != 0:
        u_ = min(K.values())
        for u in (K):
            if K[u] == u_:
                break
 

        K.pop(u)
        for v in (G.vizinhos_lista(u)):
            for key in (K.keys()):
                if (v == key) and (G.peso_nao_dirigido(u, v) < K[v]):
                    A[v] = u
                    K[v] = G.peso_nao_dirigido(u, v)

    peso = 0
    resposta = ""
    for key, value in A.items():
        if value == None:
            peso = peso
        else:
            peso += G.peso_nao_dirigido(key, value)
            resposta += f"{key}-{value}, "

    return peso, resposta