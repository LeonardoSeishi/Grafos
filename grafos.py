class Graph:
	# Por enquanto, o array de vertices está sendo inicializado
	# com None como primeiro elemento pois os vértices dos arquivos de 
	# texto iniciam pelo número 1.
	def __init__(self):
		self.__adj = [] # array de vertices
		self.__are = [] # array de arestas

	@property
	def adj(self):
			return self.__adj
	@property
	def ver(self):
			return self.__are


	# Complexidade O(1)
	# TODO: Retirar o menos um se nao tiver o NoneType como primeiro elemento
	def qtdVertices(self):
		return len(self.__adj) - 1

    # Complexidade O(1)
	# TODO: Mudar o começo do for de 1 para zero se nao tiver o NoneType como primeiro elemento
	def qtdArestas(self):
		return len(self.__are) 

    # # Numero de vizinhos
	def grau(self, v):
		return len(self.__adj[v]["vizinhos"])

	def rotulo(self, v):
		return self.__adj[v]

	# TODO : printar o nome dos usuários
	def vizinhos(self, v):
		for i in self.__are:
			if self.haAresta(v, i[])

	def haAresta(self, u, v):
		return v in self.__[u]["vizinhos"]
		
	def peso(self, u, v):
		if self.haAresta(u, v):
			return self.__are[(u, v)]

	# ? O primeiro elemento a ser inserido na lista é NoneType. está correto?
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
			line = file.readline()
			words = line.split("\"") # funciona enquanto os rotulos estiverem dentro de aspas duplas
			vertice = {int(words[0]): "", "size": 0, "vizinhos": []}
			vertice[int(words[0])] = words[1]
			self.__adj.append(vertice)

		file.readline() # para pular a linha "*edges"

		while True:
			line = file.readline()
			if not line:
				break
			vert1, vert2, weight = line.split()
			vert1 = int(vert1)
			vert2 = int(vert2)
			weight = float(weight)
			aresta = {(vert1, vert2): weight}
			self.__are.append(aresta)



