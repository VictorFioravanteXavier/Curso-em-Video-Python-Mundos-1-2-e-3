'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.'''

import moeda

p = float(input('Digite o valor de uma modeda: R$'))

print(f'\ncom mais 10% no valor: {moeda.moeda(moeda.aumentar(p,10))}')

print(f'com menos 13% no valor: {moeda.moeda(moeda.diminuir(p,13))}')

print(f'o dobro: {moeda.moeda(moeda.dobro(p))}')

print(f'a metade: {moeda.moeda(moeda.metade(p))}\n')