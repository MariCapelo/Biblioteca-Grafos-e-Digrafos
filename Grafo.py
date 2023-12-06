#bibliotecas nescessárias
import networkx as nx
import matplotlib.pyplot as ptl
import heapq
import collections

class Grafo:
    #inicializando o grafo
    def __init__(self):
       #defaultdict pode automaticamente atribuir um valor padrao ao vertice
       self.g = nx.Graph()
       self.num_m = 0
        # self.g = collections.defaultdict(dict)

    #função que adiciona aresta
    def adicionaAresta(self, numeros):  
        if len(numeros) == 2: 
            self.g.add_edge(numeros[0][0], numeros[0][1], numeros[0][2])
            self.num_m += 1
            
            
        else:
            self.g.add_edge(numeros[0][0], numeros[0][1], weight = int(1))
            self.num_m += 1
            

    #função que retorna o grafo
    def retornaGrafo(self):
        G = nx.Graph(self.g)
        nx.draw_circular(G, with_labels=True)
        ptl.show()
    
    #função que retorna o numero de aresta do grafo
    def numeroAresta(self):
        return self.num_m
    
    #função que retorna o numero de vertices do grafo
    def numeroVertice(self):
        return self.g.number_of_nodes()
    
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

        # Printa o vértice com o menor grau e o valor do menor grau 
        print("O vertice de menor grau é: ", menor_vertice)
        print("O valor de menor grau é: ", menor_grau)
    
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

        # Printa o vértice com o maior grau
        print("O vertice de maior grau é: ", maior_vertice)
        print("O valor do maior grau é: ", maior_grau)
    
    def BFS(self, origem):
        #A função realiza busca em largura no digrafo a partir de uma origem selecionada
        fila = [origem]
    
        # Inicializa o dicionário de níveis com o nó de origem
        niveis = {origem:0}

        # Vai armazenar 
        pais = {origem: None}
        
        # Enquanto a fila não estiver vazia
        while fila:
            # Remove o primeiro nó da fila
            atual = fila.pop(0)
            
            # Visita todos os vizinhos do nó atual
            for vizinho in self.g[atual]:
                # Se o vizinho ainda não foi visitado
                if vizinho not in niveis:
                    # Adiciona o vizinho na fila
                    fila.append(vizinho)
                    
                    # Define o nível do vizinho
                    niveis[vizinho] = niveis[atual] + 1
                    
                    # Define o pai do vizinho
                    pais[vizinho] = atual
                    
        # Constrói a árvore a partir do dicionário de pais
        arvore = nx.DiGraph()
        for filho, pai in pais.items():
            if pai is not None:
                arvore.add_edge(pai, filho)
        
        #Percorre o dicionario niveis
        for chave, valor in niveis.items():
            print("A Distancia de ", origem, " ate ", chave, " é: ", valor)
        
        nx.draw_spectral(arvore, with_labels=True)
        ptl.show()
    

    def DFS(self, vertice_inicial):
        # Cria um conjunto para os vértices já visitados
        visitados = set()
        inicio = None
        fim = None
        tempo = None

        # Chama a função auxiliar de busca em profundidade
        print("Ordem em que os vertices foram visitados:")
        self.DFSAux(vertice_inicial, inicio, fim, tempo, visitados)

    def DFSAux(self, vertice, inicio, fim, tempo, visitados):
         #setando cada um dos componentes que sera usado para a busca em profundidade
        
        if inicio is None:
            #Vai guardar os tempos iniciais em que cada vertice foi visitado
            inicio = {}
            
        if fim is None:
            #Vai guardar os tempos em que os vertices acabaram de serem visitados
            fim = {}
            
        if tempo is None:
            #Lista que ira fazer o controle do tempo 
            tempo = [0]
            
        # Marca o vértice atual como visitado
        visitados.add(vertice)

        inicio[vertice] = tempo[0]
        tempo[0] += 1
        
        # Imprime o vértice atual
        print("O vertice ", vertice, " começou a ser visitado no tempo ", tempo[0])

        # Visita recursivamente todos os vizinhos não visitados do vértice atual
        for vizinho in self.verticeVizinho(vertice):
            if vizinho not in visitados:
                self.DFSAux(vizinho, inicio, fim, tempo, visitados)
                
        #Adiciona o tempo que o vertice terminou de ser visitado e conta mais um no tempo
        fim[vertice] = tempo[0]
        tempo[0] += 1
        
        print("O vertice ", vertice, " terminou de ser visitado no tempo ", tempo[0])
        return inicio, fim

    def bellman_ford(self, vertice_inicial):
        # Inicializa as distâncias de todos os vértices como infinito, exceto o vértice inicial
        distancia = {vertice: float('inf') for vertice in self.g}
        distancia[vertice_inicial] = 0

        # Relaxa todas as arestas V-1 vezes
        for _ in range(len(self.g) - 1):
            for s, d, w in self.g.edges(data='weight'):
                if distancia[s] != float("Inf") and distancia[s] + w < distancia[d]:
                    distancia[d] = int(distancia[s]) + int(w)

        # Verifica se existem ciclos de peso negativo
        for s, d, w in self.g.edges(data='weight'):
            if distancia[s] != float("Inf") and distancia[s] + w < distancia[d]:
                print("O digrafo contem ciclos negativos")
                return
            
        # Retorna as distâncias mínimas de todos os vértices ao vértice inicial
        #Percorre o dicionario distancia
        for chave, valor in distancia.items():
            print("A Distancia minima de ", vertice_inicial, " ate ", chave, " é: ", valor)
        
        predecessor = list(nx.bellman_ford_predecessor_and_distance(self.g, vertice_inicial)[0].values())
        print("\nLista de predecessores de cada um dos vertices seguindo a ordem de cima:")
        print(predecessor)
    
    def dijkstra(self, vertice_inicial):
       # Inicializa as distâncias de todos os vértices como infinito, exceto o vértice inicial
            distancias = {vertice: float('inf') for vertice in self.g}
            distancias[vertice_inicial] = 0

            # Inicializa o dicionário de predecessores
            predecessor = {vertice: None for vertice in self.g}

            # Relaxa todas as arestas V-1 vezes
            for _ in range(len(self.g) - 1):
                for s, d, w in self.g.edges(data='weight'):
                    if distancias[s] != float("Inf") and distancias[s] + w < distancias[d]:
                        distancias[d] = distancias[s] + w
                        predecessor[d] = s

            # Verifica se existem ciclos de peso negativo
            for s, d, w in self.g.edges(data='weight'):
                if distancias[s] != float("Inf") and distancias[s] + w < distancias[d]:
                    print("O digrafo contem ciclos negativos")
                    break

            # Retorna as distâncias mínimas de todos os vértices ao vértice inicial e o vértice predecessor no caminho mínimo de v até cada vértice
            for chave, valor in distancias.items():
                print("A Distancia minima de ", vertice_inicial, " ate ", chave, " é: ", valor)
        
            
            predecessor = list(predecessor.values())
            print("\nLista de predecessores de cada um dos vertices seguindo a ordem de cima:")
            print(predecessor)


    def ler_arquivo(self, nome_do_arquivo):
        # Abre o arquivo e lê linha por linha
        try:
            with open(nome_do_arquivo, 'r') as arquivo:
                A = arquivo.readlines()
                for linha in A:
                    # Divide a linha em origem, destino e peso
                    numeros = []
                    numeros.append([str(num) for num in linha.strip().split()[1:]])
                    # Adiciona o arco ao grafo
                    self.adicionaAresta(numeros)
            print("Arquivo lido com sucesso :)")

        except:
            print("Erro ao ler o arquivo :(")






