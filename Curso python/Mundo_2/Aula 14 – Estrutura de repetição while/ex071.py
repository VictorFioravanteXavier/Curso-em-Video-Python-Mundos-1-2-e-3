'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o 
valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor_saque = int(input('Digite o valor para ser sacado: '))
notas50 = notas20 = notas10 = notas1 = 0

while True:
    while valor_saque >= 50:
        notas50 = valor_saque // 50
        valor_saque %= 50
        print(f'Notas de R$50: {notas50}')
    
    while valor_saque >= 20:
        notas20 = valor_saque // 20
        valor_saque %= 20
        print(f'Notas de R$20: {notas20}')
    
    while valor_saque >= 10:
        notas10 = valor_saque // 10
        valor_saque %= 10
        print(f'Notas de R$10: {notas10}')
    
    while valor_saque >= 1:
        notas1 = valor_saque // 1
        valor_saque %= 1 
        print(f'Notas de R$1: {notas1}\n')
        
    break