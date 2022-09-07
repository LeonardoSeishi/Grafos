import sys

class Graph:
	# Por enquanto, o array de vertices está sendo inicializado
	# com None como primeiro elemento pois os vértices dos arquivos de 
	# texto iniciam pelo número 1.
	def __init__(self):
		self.__adj = [None] # array de vertices

	@property
	def adj(self):
			return self.__adj

	def ler(self, file_path):
		try:
			file = open(file_path, 'r')
		except FileNotFoundError:
			print("Arquivo nao encontrado")

		try:
			number_vertices = int(file.readline()[10:-1])
		except ValueError:
			print("Nao foi possivel obter numero de vertices")
		
		for line in range(number_vertices):
			vertice = {"label": "", "size": 0, "arestas": {}}
			line = file.readline()
			words = line.split("\"") # funciona enquanto os rotulos estiverem dentro de aspas duplas
			vertice["label"] = words[1]
			self.__adj.append(vertice)

		file.readline() # para pular a linha "*edges"

		while True:
			line = file.readline()
			if not line:
				break
			vert1, vert2, weight = line.split()
			vert1 = int(vert1)
			weight = float(weight)
			self.__adj[vert1]["arestas"][vert2] = weight


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
	# 	print(i)