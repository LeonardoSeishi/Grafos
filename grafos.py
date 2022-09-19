class Graph:
	# Por enquanto, o array de vertices está sendo inicializado
	# com None como primeiro elemento pois os vértices dos arquivos de 
	# texto iniciam pelo número 1.
	def __init__(self):
		self.__adj = [None] # array de vertices

	@property
	def adj(self):
			return self.__adj

	# Complexidade O(1)
	# TODO: Retirar o menos um se nao tiver o NoneType como primeiro elemento
	def qtdVertices(self):
		return len(self.__adj) - 1

    # Complexidade O(1)
	# TODO: Mudar o começo do for de 1 para zero se nao tiver o NoneType como primeiro elemento
	def qtdArestas(self):
		qnt = 0
		for v in range (1, len(self.__adj)):	
			qnt += len(self.__adj[v]["arestas"])
		return qnt / 2

    # # Numero de vizinhos
	def grau(self, v):
		return len(self.__adj[v]["arestas"])

	def rotulo(self, v):
		return self.__adj[v]["label"]

	# TODO : printar o nome dos usuários
	def vizinhos(self, v):
		return self.__adj[v]["arestas"]

	def haAresta(self, u, v):
		for vv in self.__adj:
			if vv["arestas"] == v:
				return True
		return False
		
	def peso(self, u, v):
		return self.__adj[u]["arestas"][v]

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


