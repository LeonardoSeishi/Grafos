import queue
from grafos import Graph as G

def busca_largura(G, s):

    #**  OBS Não foi utilizado listas porque seria preciso adicionar um Nonetype, ja que os vertices comecam com indice 1
    C = {}
    D = {}
    A = {}

    for i in range(1, G.qtdVertices()+1):
        C[i] = False
        D[i] = 0
        A[i] = None

    C[s] = True
    D[s] = 0
    Q = queue.Queue()
    Q.put(s)


    while not(Q.empty()):
        u = Q.get()
        saintes = G.saintes(u)


        for v in saintes:
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