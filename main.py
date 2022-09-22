from grafos import *
import sys

class Main:
    grafo = Graph()

    # Caso queira passar o path do arquivo como argumento pela linha de comando.
    # Senao, por enquanto, é só alterar o path aqui no else
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
    else:
        file_path = "instancias/arvore_geradora_minima/agm_tiny.net"

    grafo.ler(file_path)

    # imprime o array de vertices
    # for i in grafo.adj:
    #     print(i)
    
    #print(grafo.qtdVertices())
    #print(grafo.qtdArestas())
    #print(grafo.grau(1))
    #print(grafo.rotulo(2))
    print(grafo.vizinhos(1))
    # print(grafo.haAresta())
    # print(grafo.peso())
    
