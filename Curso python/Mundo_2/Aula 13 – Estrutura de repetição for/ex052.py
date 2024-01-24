'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n1 = int(input('Digite um número: '))
cont = 0
for i in range(1,n1+1):
    if n1 % i == 0:
        print(f'\033[33m {i} \033[m', end='')
        cont += 1
    else:
        print(f'\033[31m {i} \033[m', end='')

if cont == 2:
    print('\nEle é Primo!')
else:
    print('\nEle não é Primo!')
