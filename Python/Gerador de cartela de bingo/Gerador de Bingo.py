#Cartela de Bingo para o Tio.
from random import randint
print('*'*30)
print(f'{"GERADOR DE CARTELAS":^30}')
print('*'*30)
quant = int(input("Gerar quantas cartelas? "))
for y in range(1, quant+1):
    k = 0
    matriz = [[], [], [], [], []]
    for linha in range(0, 5): #linha
        for coluna in range(0, 5): #coluna
            k = 0
            while k != 1:
                if coluna == 0:
                    n = randint(1, 15)
                elif coluna == 1:
                    n = randint(16, 30)
                elif coluna == 2:
                    n = randint(31, 45)
                elif coluna == 3:
                    n = randint(46, 60)
                else:
                    n = randint(61, 75)
                if n not in matriz[coluna]:
                    matriz[coluna].append(n)
                    k += 1
            matriz[coluna].sort()
    print('-=' * 30)
    print()
    print(f'Cartela {y}')
    for linha in range(0, 5):
        for coluna in range(0, 5):
            print(f'[{matriz[coluna][linha]:^5}]', end='')
        print() #Quebra de linha para poder montar a matriz
    print()
    print(matriz)
