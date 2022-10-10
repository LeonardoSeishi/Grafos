from grafos import Graph as G

#vertices
#{rotulo: "", vizinhos: [v1,v2,...]}

#arestas
#("v1","v2")


def buscaCiclo(G,v,C):
    ciclo = [v]
    t = v
    while True:
        condicao = 0
        for u in G.vizinhos_lista(v): #u = vertice vizinho de v
            for e in (G.arestas):
                if ((e[0] == v and e[1] == u) or (e[0] == u and e[1] == v)):
                    if not(C[e]):
                        condicao += 1  #existe u pertencente a N(v): C{u,v} = false
                        break
            
        if (condicao == 0): #nao existe u pertencente a N(v): C{u,v} = false
            return (False, None)

        for u in G.vizinhos_lista(v):
            for e in (G.arestas):
                if ((e[0] == v and e[1] == u) or (e[0] == u and e[1] == v)) and not(C[e]): #selecionar aresta "e" na qual Ce = False, conectada a "v" 
                    C[e] = True  
                    v = u
                    ciclo.append(v) #adicionar a lista do ciclo 
                    break
                
        if v == t: #until v=t
            break
    

    #procurar no ciclo se há algum vertice que tenha uma aresta nao percorrida
    for u in ciclo:
        for e in (G.arestas):
            if not(C[e]):
                if e[0] == u:
                    x = e[1]
                elif e[1] == u:
                    x = e[0]
                (r, ciclo_) = buscaCiclo(G, x, C)
                if not r:
                    return (False, None)

                for i in range(len(ciclo)):
                    if ciclo[i] == ciclo_[0]:
                        for j in range(1, len(ciclo_)):
                            ciclo.insert(i+j, ciclo_[j])
                        

    return (True, ciclo)


def arestas_visitadas(G):
    C = {}
    for e in G.arestas:
        C[e] = False
    return C


def Hierholzer(G):

    C = arestas_visitadas(G)

    for v in G.vertices:
        if G.vizinhos(v) != []:
            break
    (r, ciclo) = buscaCiclo(G,v,C)
    
    if not r:
        return (False, None)
    else:
        aresta_sobrando = False
        for e in C:
            if e == False:
                aresta_sobrando = True
        if aresta_sobrando:
            return (False, None)
        else:
            return (True, ciclo)
