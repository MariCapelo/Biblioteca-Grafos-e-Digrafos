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
            self.digrafo.add_edge(numeros[0][0], numeros[0][1], weight=numeros[0][2])
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
        #Função que retorna o verticie de de maior grau e o valor do maior grau
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
        print("Os vertices de maior grau de entrada / Valor maior grau de entrada: " + ListMEDN + " / " + str(maxD_entrada))
        
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
        print("O vertice de maior grau de saida / Valor maior grau de saida: " + ListMSDN + " / " + str(maxD_saida))
                
                    
    def menor_d(self):
        #Função que retorna o verticie de menor grau e o valor do menor grau
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
        print("O vertice de menor grau de entrada / Valor menor grau de entrada:", ListMIDE, minD_entrada)
       
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
        print("O vertice de maior grau de saida / Valor maior grau de saida:", ListMIDS, minD_saida)
        
        
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
        nx.draw_circular(self.digrafo, with_labels=True) 
        ptl.show()
