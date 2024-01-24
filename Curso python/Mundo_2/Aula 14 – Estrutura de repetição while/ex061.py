'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

passo = int(input('Digite o passo: '))
inicio = int(input('Digite o inicio: '))
decimo = inicio + 9 * passo

while inicio != decimo+passo:
    print(inicio, end=' -> ')
    inicio+=passo

print('Acabou')