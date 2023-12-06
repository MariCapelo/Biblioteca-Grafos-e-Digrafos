from Digrafo import Digrafo
from Grafo import Grafo
import time

dig = Digrafo()
graf = Grafo()

"""Esse codigo implmenta as bibliotecas de grafos e digrafo criadas, juntamente com um menu interativo que permiite que 
    o usuario utilize todas as funções das bibliotecas. Escolha 1 se quiser trabalhar com grafos e 2 se quiser trabalhar com digrafos.
    Alem disso, foi utilizada a biblioteca times para permitir que o usuario consiga vizualizar melhor a resposta no terminal antes que
    o menu retorne"""
    
print("TRABALHAR COM GRAFOS(1) OU DIGRAFOS(2)")
escolha = int(input())

if escolha == 2:
    while True:
        print("-"*40)
        print("MENU DE DIGRAFOS :)")
        print("(1) Adicionar arestas")
        print("(2) Lista de vértices")
        print("(3) Num de N")
        print("(4) Num de M")
        print("(5) Propriedades de um vértice")
        print("(6) Grau máximo")
        print("(7) Grau mínimo")
        print("(8) Peso de uma aresta")
        print("(9) Vizualizar digrafo")
        print("(10) BFS")
        print("(11) DFS")
        print("(12) Bellman-Ford")
        print("(13) Dijkstra")
        print("(14) PARAR")
        print("-"*40)
        print("ESCOLHA UMA OPÇÃO:")
        
        a = int(input())
        if a == 1:
            print("(1) Adicionar arquivo")
            print("(2) Escrever aresta")
            b = int(input())
            if b == 1:
                arquivo = input("Digite o nome do arquivo\n")
                dig.ler_arquivo(arquivo)
            if b == 2:
                numeros = []
                dig.add_m(numeros)
                
        elif a == 2:
            dig.mostrar_N()
            
        elif a == 3:
            print(dig.countN())
            time.sleep(5)
            
        elif a == 4:
            print(dig.countM())
            time.sleep(5)

        elif a == 5:
            print("Diga um vertice")
            c = input()
            dig.prop_N(c)
        
        elif a == 6:
            dig.maior_d()
            time.sleep(8)
            
        elif a == 7:
            dig.menor_d()
            time.sleep(8)
        
        elif a == 8:
            print("Digite a aresta:")
            u = input()
            v = input()
            print("O peso da aresta (" + str(u) + ", " + str(v) + ") e:")
            dig.pesoN(u,v)
            
        elif a == 9:
            dig.ver_digrafo()
            
        elif a == 10:
            print("Escolha o nó que deseja começar o BFS:")
            init = input()
            dig.BFS(init)
            print("O menu voltara em 10 segundos")
            time.sleep(15)
            
        elif a == 11:
            print("Escolha o vertice que deseja começar o DFS:")
            init = input()
            dig.DFS(init)
            print("O menu voltara em 10 segundos")
            time.sleep(10)
            
        elif a == 12:
            print("Escolha o vertice inicial para o algoritmo de Bellman-Ford:")
            init = input()
            dig.bellman_ford(init)
            print("O menu voltara em 10 segundos")
            time.sleep(10)
            
        elif a == 13:
            print("Escolha o vertice inicial para o algoritmo de DIJKSTRA:")
            init = input()
            dig.dijkstra(init)     
            print("O menu voltara em 10 segundos")
            time.sleep(10)
            
        elif a == 14:
            break
        
        else:
            print("A opcao escolhida nao existe!")
            
elif escolha == 1:
    
    while True:
        print("-"*40)
        print("MENU DE GRAFOS :3")
        print("(1) Adicionar arestas")
        print("(2) Lista de vizinhos")
        print("(3) Num de N")
        print("(4) Num de M")
        print("(5) Grau de um N")
        print("(6) Grau máximo")
        print("(7) Grau mínimo")
        print("(8) Peso de uma aresta")
        print("(9) Vizualizar grafo")
        print("(10) BFS")
        print("(11) DFS")
        print("(12) Bellman-Ford")
        print("(13) Dijkstra")
        print("(14) PARAR")
        print("-"*40)
        print("ESCOLHA UMA OPÇÃO:")
        
        a = int(input())
        if a == 1:
            arquivo = input("Digite o nome do arquivo\n")
            graf.ler_arquivo(arquivo)
            time.sleep(2)
            
        elif a == 2:
            print("Digite um vertice: ")
            b = input()
            print("Lista de vizinhos do vertce ", b, ": ", graf.verticeVizinho(b))
            time.sleep(5)
        
        elif a == 3:
            print("O numero de vertices do grafo é: ", graf.numeroVertice())
            time.sleep(5)
            
        elif a == 4:
            print("O numero de arestas do grafo é: ", graf.numeroAresta())
            time.sleep(5)
            
        elif a == 5:
            print("Digite um vertice: ")
            b = input()
            print("O grau do vertice ", b, " é: ", graf.grau_vertice(b))
            time.sleep(5)
        
        elif a == 6:
            graf.maiorGrau()
            time.sleep(5)
        
        elif a == 7:
            graf.menorGrau()
            time.sleep(5)
            
        elif a == 8:
            print("Digite a aresta:")
            u = input()
            v = input()
            print("O peso da aresta (", str(u), ", ", str(v), ") e:", graf.pesoAresta(u,v))
            time.sleep(5)
        
        elif a == 9:
            graf.retornaGrafo()
            
        elif a == 10:
            print("Escolha o nó que deseja começar o BFS:")
            init = input()
            graf.BFS(init)
            print("O menu voltara em 10 segundos")
            time.sleep(10)
            
        elif a == 11:
            print("Escolha o nó que deseja começar o DFS:")
            init = input()
            graf.DFS(init)
            print("O menu voltara em 10 segundos")
            time.sleep(10)
            
        elif a == 12:
            print("Escolha o vertice inicial para o algoritmo de Bellman-Ford:")
            init = input()
            graf.bellman_ford(init)
            print("O menu voltara em 10 segundos")
            time.sleep(10)
            
        elif a == 13:
            print("Escolha o vertice inicial para o algoritmo de DIJKSTRA:")
            init = input()
            graf.dijkstra(init)     
            print("O menu voltara em 10 segundos")
            time.sleep(10)
            
        elif a == 14:
            break
        
        else:
            print("A opção escolhida nao existe!")
            
                
                
