# importa o path do diretorio "Grafos" (acho que deve estar na primeira linha)
from modules import *
from fluxo import *
from grafos import *


class A3:
    grafo = Graph()

    # Caso queira passar o path do arquivo como argumento pela linha de comando.
    # Senao, por enquanto, é só alterar o path aqui no else
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
    else:
        file_path = "../instancias/fluxo_maximo/wiki.net"

    grafo.ler(file_path)

    # Exercício 1
    r = input("Deseja corrigir o exercício 1? [y/n] ")
    if r == 'y':
        # é necessario informar o vertice de inicio e de fim
        fluxo_maximo(grafo, 1, 7)

    # Execício 2
    # print()
    # r = input("Deseja corrigir o exercício 2? [y/n] ")
    # if r == 'y':

    # Execício 3
    # print()
    # r = input("Deseja corrigir o exercício 3? [y/n] ")
    # if r == 'y':
