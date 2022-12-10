import modules
import grafos as g

def Lawler(grafo):
    X = list()
    X.insert(0, 0)
    A = subconjuntos(grafo.vertices.keys())
    for S in A[1:]:
        s = A.index(S)
        X.insert(s, float('inf'))
        g_ = criaGLinha(S, grafo)
        I = encontraTodosMaximais(A, g_)
        for C in I:
            conjS = montaConj(S)
            dif = conjS - set(C)
            i = A.index(montaBit(dif, grafo.vertices))
            if 1 + X[i] < X[s]:
                X[s] = 1 + X[i]
    
    return X[-1]

def montaConj(S):
    l_ = list()
    for key, value in S.items():
        if value == '1':
            l_.append(int(key))
    return set(l_)

def montaBit(conjunto, vertices):
    dicAux = dict()
    for i in vertices:
        if i in conjunto:
            dicAux[i] = '1'
        else:
            dicAux[i] = '0'
    return dicAux


def subconjuntos(vertices):
    card = len(vertices)
    pot2 = 2**card
    
    A = [None for _ in range(pot2)]
    numberOfBits = len(bin(pot2-1)[2:])
    for i in range(0, pot2):
        d = dict()
        binary = bin(i)[2:]

        while len(binary) < numberOfBits:
            binary = "0" + binary

        aux = 0
        for v in vertices:
            d[v] = binary[aux]
            aux += 1
        
        A[i] = d    
    return A

def listaTodosSubDescrescente(A, vertices):
    L = list()
    for i in A:
        sub = list()
        for key, value in i.items():
            if value == '1':
                sub.append(key)
        L.append(sub)    
    
    t = len(vertices)
    reverse = list()
    while t > -1:
        for i in L:
            if len(i) == t:
                reverse.append(i)
        t -= 1
                

    return reverse

def criaGLinha(subconjunto, grafo_original):
    novoGrafo = g.Graph()
    V_ = dict()
    for key, value in subconjunto.items():
        if value == '1':
            vertice = dict()
            vertice = {'rotulo': None, 'vizinhos': set()}
            V_[key] = vertice
            for aresta in grafo_original.arestas:
                if int(key) in aresta:
                    novoGrafo.arestas = aresta
    novoGrafo.vertices = V_
    return novoGrafo

def encontraTodosMaximais(A, G_):
    L = listaTodosSubDescrescente(A, G_.vertices)
    for i in range(0, len(L)):
        if L[i] != None:
            existe = verificaTodosPares(L[i], G_)
            if not(existe):
                eliminaTodosSubMenores(L, L[i])
            else:
                idx = L.index(L[i])
                L.remove(L[i])
                L.insert(idx, None)

    L = [x for x in L if x is not None]
    return L

def verificaTodosPares(s, G_):
    for v1 in s:
        for v2 in s:
            if G_.haArestaNdirigido(v1, v2):
                return True

    return False

def eliminaTodosSubMenores(L, s):
    for i in L:
        if i != None:
            if set(i) < set(s):
                idx = L.index(i)
                L.remove(i)
                L.insert(idx, None)

    return L    

"""V = [1, 2, 3, 4]
A = subconjuntos(V)
g_ = g.Graph()
V_ = dict()

for i in range(0, len(V)):
    vertice = {'rotulo': None, 'vizinhos': set()}
    vertice['rotulo'] = V[i]
    V_[i] = vertice
g_.vertices = V_
g_.arestas = (1, 3, 1)
g_.arestas = (2, 4, 1)
t = encontraTodosMaximais(A, g_)
print(t)"""