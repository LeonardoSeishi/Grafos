import grafos as g

objeto = g.Grafo_nD_P()
objeto.ler("facebook_santiago.net")
print(objeto.haAresta(73,632))
print(objeto.peso(73, 632))