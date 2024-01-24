'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um 
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado 
pela função moeda(), desenvolvida no desafio 108.'''

import moeda

p = float(input('Digite o valor de uma modeda: R$'))
opc = bool(input('Digite True se quer com formatação de moeda ou False se não: '))

print(f'\ncom mais 10% no valor: {moeda.aumentar(p,10,opc)}')

print(f'com menos 13% no valor: {moeda.diminuir(p,13,opc)}')

print(f'o dobro: {moeda.dobro(p,opc)}')

print(f'a metade: {moeda.metade(p,opc)}\n')