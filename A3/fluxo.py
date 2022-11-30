from queue import Queue
import copy

# TODO atualizar peso das arestas dos caminhos aumentantes
# criar duas funcoes no arquivo grafos, uma para atualizar as capacidade
# residuais e outra para os arcos de retorno (ou uma que faca as duas coisas)


def cria_grafo_residual(grafo):
    arestas = grafo.arestas
    grafo_res = copy.deepcopy(grafo)
    for arco in arestas:
        u = arco[0]
        v = arco[1]
        novo_arco = (v, u, 0)  # inverte o sentido entre 'u' e 'v'
        grafo_res.insere_aresta(novo_arco)

    # print(grafo_res.arestas)
    print("fim cria_grafo_residual")
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
            cap_res = grafo_res.peso_nao_dirigido(u, v)
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

                    print("cam_aum =", cam_aum, "retornando")
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
            grafo_res.atualiza_peso(arco[0], arco[1], cap_min)

        print(grafo_res.arestas)

        break
