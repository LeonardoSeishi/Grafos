from queue import Queue
import copy


def cria_grafo_residual(grafo):
    grafo_res = copy.deepcopy(grafo)
    grafo_res.confere_e_cria_vertice_fluxo()  # caso exista (u,v) e (v,u)
    for i in range(len(grafo_res.arestas)):
        u = grafo_res.arestas[i][0]
        v = grafo_res.arestas[i][1]
        novo_arco = (v, u, 0)  # inverte o sentido entre 'u' e 'v'
        grafo_res.insere_aresta(novo_arco)

    return grafo_res


def encontra_caminho_aumentante(grafo_res, s, t):
    C = {}
    A = {}
    for v in grafo_res.vertices:
        C[v] = False
        A[v] = None
    C[s] = True
    fila = Queue()
    fila.put(s)
    while not fila.empty():
        u = fila.get()
        # print("u =", u)
        for v in grafo_res.saintes(u):
            cap_res = grafo_res.peso_dirigido(u, v)
            # print("peso (u,v): ", u, v, cap_res)
            if (C[v] == False and cap_res > 0):
                # print("v =", v)
                C[v] = True
                A[v] = u
                if v == t:
                    cam_aum = []
                    w = t
                    while (w != s):
                        arco = (A[w], w, grafo_res.peso_nao_dirigido(A[w], w))
                        cam_aum.append(arco)
                        w = A[w]

                    # print("cam_aum =", cam_aum, "retornando")
                    return cam_aum
                fila.put(v)
    return None


def fluxo_maximo(grafo, s, t):
    grafo_res = cria_grafo_residual(grafo)
    F = 0  # fluxo maximo

    while True:
        cam_aum = encontra_caminho_aumentante(grafo_res, s, t)
        if (cam_aum == None):
            break

        # encontra capacidade minima
        cap_min = float('inf')
        for arco in cam_aum:
            if (arco[2] < cap_min):
                cap_min = arco[2]

        # atualiza capacidades residuais e arcos de retorno
        for arco in cam_aum:
            grafo_res.atualiza_capacidades(arco[0], arco[1], cap_min)

        # Incrementa capacidade residual do caminho
        F = F + cap_min

    print("F =", F)
