import sys
from buscas import busca_largura, imprime_busca
from dijkstra import dijkstra
from buscas import busca_largura
from floyd_warshall import floyd_warshall, imprime_floyd_warshall
from grafos import *


class Main:
    grafo = Graph()

    # Caso queira passar o path do arquivo como argumento pela linha de comando.
    # Senao, por enquanto, é só alterar o path aqui no else
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
    else:
        file_path = "instancias/caminho_minimo/fln_pequena.net"
        # file_path = "instancias/teste_busca/teste_busca_largura.net"
        # file_path = "instancias/arvore_geradora_minima/agm_tiny.net"
        # file_path = "instancias/teste_locais/teste_floyd_warshall.net"
    grafo.ler(file_path)

    # dijkstra(grafo, 9)

    # imprime o array de vertices
    # for value in grafo.vertices.values():
    #     print(value)

    # print(grafo.peso(3, 2))

    # print(grafo.qtdVertices())
    # print(grafo.qtdArestas())
    # print(grafo.grau(1))
    # print(grafo.rotulo(2))
    # print(grafo.vizinhos(1))
    # print(grafo.haAresta(1, 4))
    # print(grafo.peso(1, 3))
    # print(grafo.entrantes(5))
    # print(busca_largura(grafo, 2))
    # print(grafo.entrantes(5))
    #t = busca_largura(grafo, 1)
    #imprime_busca(t[0], grafo.qtdVertices())
    mtx = floyd_warshall(grafo)
    imprime_floyd_warshall(mtx, grafo.qtdVertices())
