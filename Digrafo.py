import networkx as nx 
import matplotlib.pyplot as ptl
import time

class Digrafo:
    def __init__(self):
        #Aqui estamos iniciando um Digrafo com 0 verticies e arestas. Eles ainda serão adicionados.
        #Perceba que um objeto digrafo será criado. Ou seja quando há uma aresta indo de um vertice u para um v, nao necessariamente a uma mesma voltando de v para u.
        #A networkx já faz esse trabalho para a gente de armazenar a direção da aresta.
        self.digrafo = nx.DiGraph()
        self.num_m = 0
        self.vertices = []
        
    def add_m(self, numeros):
        #Nesta função será criada as arestas do nosso digrafo a partir do metodo add_edge 
        #As arestas podem ser adicionadas tanto por inserção direta, ou seja digitando quais serão os verticies e o peso da aresta, 
        # quanto pela leitura de um arquivo dado.
        if numeros:
            if len(numeros) == 2:
                self.digrafo.add_edge(numeros[0][0], numeros[0][1], weight=int(numeros[0][2]))
                self.num_m += 1
                if numeros[0][0] not in self.vertices:
                    self.vertices.append(numeros[0][0])
                if numeros[0][1] not in self.vertices:
                    self.vertices.append(numeros[0][1])
            else:
                self.digrafo.add_edge(numeros[0][0], numeros[0][1], weight=int(1))
                self.num_m += 1
                if numeros[0][0] not in self.vertices:
                    self.vertices.append(numeros[0][0])
                if numeros[0][1] not in self.vertices:
                    self.vertices.append(numeros[0][1])
                
        else:
            print("Digite respectivamente quem será o v1, v2 e o peso:")
            v1 = input()
            v2 = input()
            w = int(input())
            numeros.append([v1, v2, w])
            self.digrafo.add_edge(numeros[0][0], numeros[0][1], weight=numeros[0][2])
            self.num_m += 1
            if v1 not in self.vertices:
                self.vertices.append(v1)
            if v2 not in self.vertices:
                self.vertices.append(v2)
            
            print("Aresta adicionada com sucesso!")
            time.sleep(1)
        
    def ler_arquivo(self, data):
        #Função para ler um arquivo de arestas e adiciona-las ao digrafo 
        try:
            with open(data, "r") as arquivo:
                A = arquivo.readlines()
                for linha in A:
                    numeros = []
                    numeros.append([str(num) for num in linha.strip().split()[1:]])
                    self.add_m(numeros)
            print("A leitura do arquivo foi bem sucedida!")
            time.sleep(1)        
        except:
            print("Erro ao ler o arquivo")
            time.sleep(1)
            
    def mostrar_N(self):
        #Essa função vai printar a lista de todos os vertices existentes no digrafo 
        print("Lista de vertices:")
        print(self.vertices)
        time.sleep(5)
               
    def countN(self):
        #Retorna o numero de vertices do digrafo criado
        print("O numero de vertices é:")
        return self.digrafo.number_of_nodes()
        
    def countM(self):    
        #Retorna o numero de arestas do digrafo
        print("O numero de arestas é:")
        return self.num_m

    def prop_N(self, u):
        #Essa função irá mostrar, a partir de uma entrada, que é um vertice qualquer, a lista de vizinhos do n selecionado,
        #o grau normal e os graus de entrada e saida. Além disso antes ele fará uma pequena busca para saber se o n que queremos acessar realmente existe,
        #se nao ele irá avisar ao usuario
        if u: 
            print("O verticie visitado é" + str(u))
            print("-"*40)
            print("Lista de vizinhos de " + str(u))
            print(list(self.digrafo.neighbors(u)))
            print("-"*40)
            print("O grau d de " + str(u) + " é: ", self.digrafo.degree(u))
            print("-"*40)
            print("A quantidade de arestas que saem é: ", self.digrafo.out_degree(u))
            print("A quantidade de arestas que entram é: ", self.digrafo.in_degree(u))
            time.sleep(5)
        else:
            print("O vertice selecionado nao existe")
            time.sleep(2)
            
            
    def maior_d(self):
        #Função que retorna os verticies de de maior grau e o valor do maior grau tanto de entrada como de saida
        maxD_entradaN = None
        maxD_entrada = -1

        for node in self.digrafo.nodes:
            degree = self.digrafo.in_degree(node)
            if degree > maxD_entrada:
                maxD_entrada = degree
                maxD_entradaN = node
        ListMEDN = []
        ListMEDN.append(maxD_entradaN)
        for node in self.digrafo.nodes:
            degree = self.digrafo.in_degree(node)
            if degree == maxD_entrada:
                ListMEDN.append(node)
        print("Valor maior grau de entrada: ", maxD_entrada)
        print("Os vertices de maior grau de entrada: ", ListMEDN)
        
        maxD_saidaN = None
        maxD_saida = -1
        for node in self.digrafo.nodes:
            degree = self.digrafo.out_degree(node)
            if degree > maxD_saida:
                maxD_saida = degree
                maxD_saidaN = node
        ListMSDN = []
        ListMSDN.append(maxD_saidaN)
        for node in self.digrafo.nodes:
            degree = self.digrafo.out_degree(node)
            if degree == maxD_saida:
                ListMSDN.append(node)
        print("Valor maior grau de saida: ", maxD_saida)
        print("Os vertices de maior grau de saida: ", ListMSDN)
                
                    
    def menor_d(self):
        #Função que retorna os verticies de menor grau e o valor do menor grau tanto de entrada como de saida
        minD_entradaN = None
        minD_entrada = self.digrafo.in_degree(self.vertices[0])

        for node in self.digrafo.nodes:
            degree = self.digrafo.in_degree(node)
            if degree < minD_entrada:
                minD_entrada = degree
                minD_entradaN = node
        ListMIDE = []
        ListMIDE.append(minD_entradaN)
        for node in self.digrafo.nodes:
            degree = self.digrafo.in_degree(node)
            if degree == minD_entrada:
                ListMIDE.append(node)
        print("Valor menor grau de entrada:", minD_entrada)
        print("O vertice de menor grau de entrada: ", ListMIDE)
       
        minD_saidaN = None
        minD_saida = self.digrafo.out_degree(self.vertices[0])
        for node in self.digrafo.nodes:
            degree = self.digrafo.out_degree(node)
            if degree < minD_saida:
                minD_saida = degree
                minD_saidaN = node
        ListMIDS = []
        ListMIDS.append(minD_saidaN)
        for node in self.digrafo.nodes:
            degree = self.digrafo.out_degree(node)
            if degree == minD_saida:
                ListMIDS.append(node)
        print("Valor menor grau de saida: ",minD_saida)
        print("Os vertices de menor grau de saida: ", ListMIDS)
        
        
    def pesoN(self, u, v):
        #Função que printa o valor do peso de uma certa aresta dada 
        #Ela itera todas as arestas do digrafo ate achar a que procuramos e depois printa seu peso
        try:
            for v1, v2, w in self.digrafo.edges(data=True):
                if (v1, v2) == (u, v):
                    print(w['weight'])
        except:
            print("A aresta nao existe")
        time.sleep(5)
        
    
    def ver_digrafo(self):
        #FUnção que mostra o grafo desenhado pelo biblioteca matplotlib
        nx.draw_circular(self.digrafo, with_labels=True) 
        ptl.show()
        
        
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
            for vizinho in self.digrafo[atual]:
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
        
        # Se algum vertice nao tiver sido acessado no BFS essa função ira dizer quem foi que nao deu pra ser acessado
        for n in self.vertices:
            if n not in niveis.keys():
                print("Foi foi possivel acessar ", n, " a partir de ", origem)
        
        nx.draw_spectral(arvore, with_labels=True)
        ptl.show()
             
          
    def DFS(self, origem):
        #Inicio da função de busca em profundidade
        visitados = set()
        inicio = None
        fim = None
        tempo = None
        print("A ordem de visitação foi:")
        self.DFSaux(origem, visitados, inicio, fim, tempo)
        
    def DFSaux(self ,atual, visitados, inicio, fim, tempo): 
        
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
            
        #adiciona os vizinhos visitados na Lista de visitados
        visitados.add(atual)
        
        #adiciona o tempo de começo de visitação de um vertice e conta mais um no tempo 
        inicio[atual] = tempo[0]
        tempo[0] += 1
        
        #Mostra qual vertice esta sendo visitado agora 
        print("O vertice ", atual, " começou a ser visitado no tempo ", tempo[0])

        
        for vizinho in self.digrafo[atual]:
            if vizinho not in visitados:
                self.DFSaux(vizinho, visitados, inicio, fim, tempo)
                
        #Adiciona o tempo que o vertice terminou de ser visitado e conta mais um no tempo
        fim[atual] = tempo[0]
        tempo[0] += 1
        
        
        print("O vertice ", atual, " terminou de ser visitado no tempo ", tempo[0])
        return inicio, fim
    
    
    def bellman_ford(self, origem):
        # Inicializa as distâncias de todos os vértices como infinito, exceto o vértice inicial
        distancia = {vertice: float('inf') for vertice in self.digrafo}
        distancia[origem] = 0

        # Relaxa todas as arestas V-1 vezes
        for _ in range(len(self.digrafo) - 1):
            for s, d, w in self.digrafo.edges(data='weight'):
                if distancia[s] != float("Inf") and distancia[s] + w < distancia[d]:
                    distancia[d] = int(distancia[s]) + int(w)

        # Verifica se existem ciclos de peso negativo
        for s, d, w in self.digrafo.edges(data='weight'):
            if distancia[s] != float("Inf") and distancia[s] + w < distancia[d]:
                print("O digrafo contem ciclos negativos")
                return
            
        # Retorna as distâncias mínimas de todos os vértices ao vértice inicial
        #Percorre o dicionario distancia
        for chave, valor in distancia.items():
            print("A Distancia minima de ", origem, " ate ", chave, " é: ", valor)
        
        predecessor = list(nx.bellman_ford_predecessor_and_distance(self.digrafo, origem)[0].values())
        print("\nLista de predecessores de cada um dos vertices seguindo a ordem de cima:")
        print(predecessor)
        
        
    def dijkstra(self, vertice_inicial):
            
            # Inicializa as distâncias de todos os vértices como infinito, exceto o vértice inicial
            distancias = {vertice: float('inf') for vertice in self.digrafo}
            distancias[vertice_inicial] = 0

            # Inicializa o dicionário de predecessores
            predecessor = {vertice: None for vertice in self.digrafo}

            # Relaxa todas as arestas V-1 vezes
            for _ in range(len(self.digrafo) - 1):
                for s, d, w in self.digrafo.edges(data='weight'):
                    if distancias[s] != float("Inf") and distancias[s] + w < distancias[d]:
                        distancias[d] = distancias[s] + w
                        predecessor[d] = s

            # Verifica se existem ciclos de peso negativo
            for s, d, w in self.digrafo.edges(data='weight'):
                if distancias[s] != float("Inf") and distancias[s] + w < distancias[d]:
                    print("O digrafo contem ciclos negativos")
                    break

            # Retorna as distâncias mínimas de todos os vértices ao vértice inicial e o vértice predecessor no caminho mínimo de v até cada vértice
            for chave, valor in distancias.items():
                print("A Distancia minima de ", vertice_inicial, " ate ", chave, " é: ", valor)
        
            
            predecessor = list(predecessor.values())
            print("\nLista de predecessores de cada um dos vertices seguindo a ordem de cima:")
            print(predecessor)

        
