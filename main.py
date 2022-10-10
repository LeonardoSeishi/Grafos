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
        # file_path = "instancias/facebook/facebook_santiago.net"
        file_path = "instancias/caminho_minimo/fln_pequena.net"
        # file_path = "instancias/arvore_geradora_minima/agm_tiny.net"
        # file_path = "instancias/caminho_minimo/fln_pequena.net"
        # file_path = "instancias/teste_locais/teste_floyd_warshall.net"

    grafo.ler(file_path)

    # Exercício 1
    r = input("Deseja corrigir o exercício 1? [y/n] ")
    if r == 'y':
        print(f"Quantidade de vertice: {grafo.qtdVertices()}")
        print(f"Quantidade de arestas: {grafo.qtdArestas()}")
        print()
        t = input(
            "Qual vértice deseja verificar o número de vizinhos, rótulo, vizinhos? ")
        print("Grau: ", grafo.grau(int(t)))
        print("Rotulo: ", grafo.rotulo(int(t)))
        print()
        print("Coloque os vértices que deseja verificar a existencia de arestas e seu peso")
        u = input("u = ")
        v = input("v = ")
        print()
        print("A aresta existe? ", grafo.haAresta(u, v))
        print("Peso: ", grafo.peso_nao_dirigido(u, v))

    # Execício 2
    print()
    r = input("Deseja corrigir o exercício 2? [y/n] ")
    if r == 'y':
        print("Coloque o vertice s")
        s = input("s = ")
        t = busca_largura(grafo, s)
        imprime_busca(t[0], grafo.qtdVertices())

     # Execício 3
    print()
    r = input("Deseja corrigir o exercício 3? [y/n] ")
    # if r == 'y':

    # Execício 4
    print()
    r = input("Deseja corrigir o exercício 4? [y/n] ")
    if r == 'y':
        print("Informe o vertice s")
        s = input("s = ")
        dijkstra(grafo, int(s))

    # Exercício 5
    print()
    r = input("Deseja corrigir o exercício 5? [y/n] ")
    if r == 'y':
        mtx = floyd_warshall(grafo)
        imprime_floyd_warshall(mtx, grafo.qtdVertices())

    # Instruções execução Dijkstra
    # Chamar a função dijkstra(G, vertice) passando como parâmetros
    # Um grafo G e um vértice pertencente ao grafo. A função não retorna
    # nada e imprime na tela as distancias a partir do vértice informado
    # exemplo:
    # dijkstra(grafo, 6)
