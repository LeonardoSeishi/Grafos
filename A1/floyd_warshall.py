from Grafos.grafos import Graph

def floyd_warshall(G):
    qtdV = G.qtdVertices()
    Dold = cria_mtx_w(G, qtdV)

    for k in range (1, qtdV + 1):
        Dnew = {}
        for t in range (1, qtdV + 1):
            Dnew[t] = {}
        
        for i in range (1, qtdV + 1):
            for j in range(1, qtdV + 1):
                Dnew[i][j] = min(Dold[i][j], Dold[i][k] + Dold[k][j])
    
        Dold = Dnew

    return Dnew

def cria_mtx_w(G, qtdV):
    W = {}
    for i in range (1, qtdV + 1):
        W[i] = {}
    
    for i in range(1, qtdV + 1):
        for j in range(1, qtdV + 1):
            if i == j:
                W[i][j] = 0
                
            elif G.haAresta(i, j):
                W[i][j] = G.peso_nao_dirigido(i, j)

            else: 
                W[i][j] = float('inf')
    
    return W

def imprime_floyd_warshall(mtx, qtdV):
    for i in range(1, qtdV + 1):
        print(f"{i}:", end='')
        for j in range(1, qtdV + 1):
            if j != qtdV:
                print(f"{mtx[i][j]}", end=",")
            else:
                print(f"{mtx[i][j]}", end="\n")
                




