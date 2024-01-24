'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai 
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

escolha_pc = randint(1,10)
escolha_user = int(input('Digite um número de 1 até 10: '))
c = 1

while escolha_pc != escolha_user:
    escolha_user = int(input('Digite um número de 1 até 10: '))
    c += 1

print(f'Foram necessárias {c} tentaivas para acertar!')