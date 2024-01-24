'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

p = float(input('Digite o valor de uma modeda: R$'))

print(f'\ncom mais 10% no valor: {moeda.aumentar(p,10)}')

print(f'com menos 13% no valor: {moeda.diminuir(p,13)}')

print(f'o dobro: {moeda.dobro(p)}')

print(f'a metade: {moeda.metade(p)}\n')