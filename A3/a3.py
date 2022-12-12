# importa o path do diretorio "Grafos" (acho que deve estar na primeira linha)
from modules import *
from fluxo import *
from grafos import *
from coloracao import Lawler
from emparelhamento import Hopcroft_Karp

class A3:
    grafo = Graph()

    # Caso queira passar o path do arquivo como argumento pela linha de comando.
    # Senao, por enquanto, é só alterar o path aqui no else
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
    else:
        #file_path = "../instancias/emparelhamento_maximo/pequeno.net"
        file_path = "../instancias/emparelhamento_maximo/gr128_10.net"

    grafo.ler(file_path)

    # Exercício 1
    r = input("Deseja corrigir o exercício 1? [y/n] ")
    if r == 'y':
        # é necessario informar o vertice de inicio e de fim
        fluxo_maximo(grafo, 1, 7)
    
    # Execício 2
    print()
    r = input("Deseja corrigir o exercício 2? [y/n] ")
    if r == 'y':
        m,e = Hopcroft_Karp(grafo)
        i=0
        print(f"Número máximo de emparelhamentos: {m}\n\nEmparelhamentos:")
        for v1,v2 in e.items(): 
            if i >= m:
                break
            print(f'{v1}-{v2}')
            i += 1
        

    #Execício 3
    print()
    r = input("Deseja corrigir o exercício 3? [y/n] ")
    if r == 'y':
        print(Lawler(grafo))
