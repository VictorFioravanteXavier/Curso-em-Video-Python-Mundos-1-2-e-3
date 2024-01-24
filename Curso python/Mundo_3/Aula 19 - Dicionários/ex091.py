'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário 
em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep

d = {}

print('=-'*15)
print(f'{"Rolando":^30}')
print('-='*15)
sleep(.5)

for i in range(0,4):
    sleep(.5)
    d[i+1] = randint(0,20)
    print(f'Jogador: {i+1} / Resultado {d[i+1]}')
    sleep(.5)


print('-='*15)
print(f'{"Posições":^30}')
print('-='*15)
sleep(.5)

for j,i in enumerate(sorted(d.keys(), reverse=True)):
    sleep(.5)
    print(f'{j+1}° Posição / Jogador: {i} / Resultado {d[i]}')
    sleep(.5)