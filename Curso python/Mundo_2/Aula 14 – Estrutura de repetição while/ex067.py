'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
    O programa será interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input('Digite um número para saber sua tabuada (digite um valor negativo para sair.): '))
    if n < 0:
        print('Saindo...')
        break
    for i in range(0,11):
        print(f'{n} x {i:2} = {n*i}')