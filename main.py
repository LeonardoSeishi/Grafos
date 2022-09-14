import grafos as g

objeto = g.Grafo_nD_P()
objeto.ler("instancias/facebook/facebook_santiago.net")

print(objeto.rotulo(1))
print(objeto.rotulo(688))
print(objeto.haAresta(73, 632))
print(objeto.peso(73, 632))
