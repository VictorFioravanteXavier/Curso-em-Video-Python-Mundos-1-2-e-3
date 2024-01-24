'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa
 vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para 
 cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

l = []
ll = []
p = int(input('Quantos jogos: '))
for i in range(0,p):
    for j in range(0,6):
        n = randint(1,60)   
        if n not in l:
            l.append(n)
        else:
            j -= 1
    ll.append(l[:])
    del l[:]


for j, i in enumerate(ll):
    sleep(0.5)
    print(f'Jogo {j+1}: {i}')
    sleep(0.5)
    