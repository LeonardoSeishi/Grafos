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
        file_path = "../instancias/fluxo_maximo/fluxo.net"

    grafo.ler(file_path)

    fluxo_maximo(grafo, 1, 4)

    # grafo.atualiza_peso(1, 2, 3)

    print("deu")
