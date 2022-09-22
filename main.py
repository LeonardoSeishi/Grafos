from grafos import *
from buscas import busca_largura
import sys

class Main:
    grafo = Graph()

    # Caso queira passar o path do arquivo como argumento pela linha de comando.
    # Senao, por enquanto, é só alterar o path aqui no else
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
    else:
        file_path = "instancias/arvore_geradora_minima/agm_tiny.net"
        # file_path = "instancias/teste_busca/teste_busca_largura.net"
    grafo.ler(file_path)

    # imprime o array de vertices
    # for i in grafo.adj:
    #     print(i)
    
    #print(grafo.qtdVertices())
    #print(grafo.qtdArestas())
    #print(grafo.grau(1))
    #print(grafo.rotulo(2))
    #print(grafo.vizinhos(1))
    #print(grafo.haAresta(1, 4))
    #print(grafo.peso(1, 3))
    #print(grafo.entrantes(5))
    print(busca_largura(grafo, 2))
    
