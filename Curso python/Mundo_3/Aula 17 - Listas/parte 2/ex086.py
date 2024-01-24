'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

l = [[],[],[]]

for i in range(0,3):
    for j in range (0,3):
        l[i].append(int(input(f'Digite o número da posição [{i+1}] [{j+1}]: ')))

for i in l:
    print(f'[{i[0]:^3}] [{i[1]:^3}] [{i[2]:^3}]')
