from Digrafo import Digrafo
import time

dig = Digrafo()

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
        break
    
    else:
        print("A opcao escolhida nao existe!")


