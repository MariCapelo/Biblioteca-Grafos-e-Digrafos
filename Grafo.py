#bibliotecas nescessárias
import heapq
import collections

class Grafo:
    #inicializando o grafo
    def __init__(self):
       #defaultdict pode automaticamente atribuir um valor padrao ao vertice
        self.g = collections.defaultdict(dict)

    #função que adiciona aresta
    def adicionaAresta(self, origem, fim, peso):    
        self.g[origem][fim] = int(peso)

    #função que retorna o grafo
    def retornaGrafo(self):
     return dict(self.g)
    
    #função que retorna o numero de aresta do grafo
    def numeroAresta(self):
        return sum(len(aresta) for aresta in self.g.values())
    
    #função que retorna o numero de vertices do grafo
    def numeroVertice(self):
        return len(self.g)
    
    #função que retorna os vertices vizinhos
    def verticeVizinho(self, vertice):    
        return list(self.g[vertice].keys()) if vertice in self.g else []
    
    #função que retorna o grau do vertice
    def grau_vertice(self, vertice):
        return len(self.g[vertice]) if vertice in self.g else 0
    
    # função que retorna o peso da aresta
    def pesoAresta(self, origem, fim):
        # Verifica se a aresta existe
        if origem in self.g and fim in self.g[origem]:
            # Retorna o peso da aresta
            return self.g[origem][fim]
        else:
            # Retorna None se a aresta não existir
            return None
        

    #função que retorna o menor grau
    def menorGrau(self):
        # Verifica se o grafo está vazio
        if not self.g:
            return None

        # Inicializa o menor grau como infinito e o vértice correspondente como None
        menor_grau = float('inf')
        menor_vertice = None

        # Percorre todos os vértices do grafo
        for vertice in self.g:
            # Calcula o grau do vértice
            grau = self.grau_vertice(vertice)

            # Atualiza o menor grau e o vértice correspondente, se necessário
            if grau < menor_grau:
                menor_grau = grau
                menor_vertice = vertice

        # Retorna o vértice com o menor grau
        return menor_vertice
    
    # função que retorna o vértice com o maior grau do grafo
    def maiorGrau(self):
        # Verifica se o grafo está vazio
        if not self.g:
            return None

        # Inicializa o maior grau como -infinito e o vértice correspondente como None
        maior_grau = float('-inf')
        maior_vertice = None

        # Percorre todos os vértices do grafo
        for vertice in self.g:
            # Calcula o grau do vértice
            grau = self.grau_vertice(vertice)

            # Atualiza o maior grau e o vértice correspondente, se necessário
            if grau > maior_grau:
                maior_grau = grau
                maior_vertice = vertice

        # Retorna o vértice com o maior grau
        return maior_vertice
    
    def busca_em_largura(self, vertice_inicial):
        # Cria uma fila para os vértices a serem visitados
        fila = collections.deque([vertice_inicial])

        # Cria um conjunto para os vértices já visitados
        visitados = set([vertice_inicial])

        while fila:
            # Remove o próximo vértice da fila
            vertice = fila.popleft()

            # Imprime o vértice atual
            print(vertice)

            # Adiciona todos os vizinhos não visitados do vértice atual à fila
            for vizinho in self.verticeVizinho(vertice):
                if vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)
    

    def BuscaProfundidade(self, vertice_inicial):
        # Cria um conjunto para os vértices já visitados
        visitados = set()

        # Chama a função auxiliar de busca em profundidade
        self.BuscaProfundidadeAux(vertice_inicial, visitados)

    def BuscaProfundidadeAux(self, vertice, visitados):
        # Marca o vértice atual como visitado
        visitados.add(vertice)

        # Imprime o vértice atual
        print(vertice)

        # Visita recursivamente todos os vizinhos não visitados do vértice atual
        for vizinho in self.verticeVizinho(vertice):
            if vizinho not in visitados:
                self.BuscaProfundidadeAux(vizinho, visitados)

    def bellman_ford(self, vertice_inicial):
        # Inicializa as distâncias de todos os vértices como infinito, exceto o vértice inicial
        distancia = {vertice: float('inf') for vertice in self.g}
        distancia[vertice_inicial] = 0

        # Relaxa todas as arestas V-1 vezes
        for _ in range(len(self.g) - 1):
            for vertice in self.g:
                for vizinho in self.g[vertice]:
                    if distancia[vertice] + self.g[vertice][vizinho] < distancia[vizinho]:
                        distancia[vizinho] = distancia[vertice] + self.g[vertice][vizinho]

        # Verifica se existem ciclos de peso negativo
        for vertice in self.g:
            for vizinho in self.g[vertice]:
                if distancia[vertice] + self.g[vertice][vizinho] < distancia[vizinho]:
                    raise ValueError('Grafo contém um ciclo de peso negativo')

        # Retorna as distâncias mínimas de todos os vértices ao vértice inicial
        return distancia
    
    def dijkstra(self, vertice_inicial):
        # Inicializa as distâncias de todos os vértices como infinito, exceto o vértice inicial
        distancia = {vertice: float('inf') for vertice in self.g}
        distancia[vertice_inicial] = 0

        # Cria uma fila de prioridade para os vértices a serem visitados
        fila_prioridade = [(0, vertice_inicial)]

        while fila_prioridade:
            # Remove o vértice com a menor distância da fila de prioridade
            dist, vertice = heapq.heappop(fila_prioridade)

            # Verifica se a distância atual é a menor distância para o vértice
            if dist == distancia[vertice]:
                # Atualiza as distâncias dos vizinhos
                for vizinho, peso in self.g[vertice].items():
                    dist_vizinho = dist + peso
                    if dist_vizinho < distancia[vizinho]:
                        distancia[vizinho] = dist_vizinho
                        heapq.heappush(fila_prioridade, (dist_vizinho, vizinho))

        # Retorna as distâncias mínimas de todos os vértices ao vértice inicial
        return distancia

    
    # isso aqui pode tá mt errado
    def adicionar_arcos_do_arquivo_ao_grafo(grafo, nome_do_arquivo):
        # Abre o arquivo e lê linha por linha
        with open(nome_do_arquivo, 'r') as arquivo:
            for linha in arquivo:
                # Divide a linha em origem, destino e peso
                origem, destino, peso = linha.strip().split()

                # Adiciona o arco ao grafo
                grafo.adicionaAresta(origem, destino, int(peso))





