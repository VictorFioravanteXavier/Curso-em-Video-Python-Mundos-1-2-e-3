'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Digte seu 1° número: '))
n2 = float(input('Digte seu 2° número: '))
escolha = 0

while escolha != 5:
    escolha = int(input(f'''
    {"-"*4} Escolha {"-"*4}
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair do programa
    Escolha uma opção: '''))

    if escolha == 1:
        print(f'\n{n1} + {n2} = {n1+n2}')
    elif escolha == 2:
        print(f'\n{n1} x {n2} = {n1*n2}')
    elif escolha == 3:
        print(f'\nO maior entre {n1} e {n2} é: {max(n1,n2)}')
    elif escolha == 4:
        n1 = float(input('\nNovo valor para o 1° número:'))
        n2 = float(input('Novo valor para o 2° número:'))
    elif escolha == 5:
        print('\nSaindo...\n')

