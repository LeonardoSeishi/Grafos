from ordenacao_topologica import visit_ot, print_ord
from grafos import *
from cfc import *
from prim import *
import sys
sys.path.insert(0, "../Grafos")

class A2:
    grafo = Graph()

    # Caso queira passar o path do arquivo como argumento pela linha de comando.
    # Senao, por enquanto, é só alterar o path aqui no else
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
    else:
        # file_path = "../instancias/dirigidos/dirigido2.net"
        # file_path = "../instancias/dirigidos/dirigido1.net"
        # file_path = "../instancias/dirigidos/simpsons_amizades1.net"
        # file_path = "../instancias/dirigidos/tcc_completo.net"
        # file_path = "../instancias/dirigidos/manha.net"
        # file_path = "../instancias/teste_locais/abcd.net"
        # file_path = "../instancias/teste_locais/componentes.net"
        file_path = "../instancias/arvore_geradora_minima/agm_tiny.net"

    grafo.ler(file_path)

    # Exercício 1
    r = input("Deseja corrigir o exercício 1? [y/n] ")
    if r == 'y':
        cfc(grafo)

    # Execício 2
    print()
    r = input("Deseja corrigir o exercício 2? [y/n] ")
    if r == 'y':
        l = visit_ot(grafo)
        print_ord(grafo, l)

    # Execício 3
    print()
    r = input("Deseja corrigir o exercício 3? [y/n] ")
    if r == 'y':
        ans = Prim(grafo)
        print(ans[0])
        print(ans[1])