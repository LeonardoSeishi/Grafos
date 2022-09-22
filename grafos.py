class Graph:
	# Por enquanto, o array de vertices está sendo inicializado
	# com None como primeiro elemento pois os vértices dos arquivos de 
	# texto iniciam pelo número 1.
	def __init__(self):
		self.__vertices = {} # array de vertices
		self.__arestas = [] # array de arestas

	@property
	def adj(self):
			return self.__vertices
	@property
	def ver(self):
			return self.__arestas


	# Complexidade O(1)
	# TODO: Retirar o menos um se nao tiver o NoneType como primeiro elemento
	def qtdVertices(self):
		return len(self.__vertices) - 1

    # Complexidade O(1)
	# TODO: Mudar o começo do for de 1 para zero se nao tiver o NoneType como primeiro elemento
	def qtdArestas(self):
		return len(self.__arestas)

    # # Numero de vizinhos
	def grau(self, v):
		return len(self.__vertices[v]["vizinhos"])

	def rotulo(self, v):
		return self.__vertices[v]["rotulo"]

	# TODO : printar o nome dos usuários
	# ! esta saindo um none no final
	def vizinhos(self, v):
		for i in self.__vertices[v]["vizinhos"]:
			print(self.__vertices[i]["rotulo"])

	def haAresta(self, u, v):
		return v in self.__[u]["arestas"]
		
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
			# ? O que vai ser o size
			vertice = {"rotulo": words[1], "size": 0, "vizinhos": set()}
			self.__vertices[int(words[0])] = vertice

		file.readline() # Pula a linha "*edges"

		while True:
			line = file.readline()
			if not line:
				break
			vert1, vert2, weight = line.split()
			vert1 = int(vert1)
			vert2 = int(vert2)
			weight = float(weight)
			

			self.__vertices[vert1]["vizinhos"].add(vert2)
			self.__vertices[vert2]["vizinhos"].add(vert1)
			aresta = {(vert1, vert2): weight}
			self.__arestas.append(aresta)



