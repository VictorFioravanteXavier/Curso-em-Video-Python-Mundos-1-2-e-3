'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''

inicio = int(input('Digite o início: '))
passo = int(input('Digite o passo: '))
decimo = inicio + (10-1) * passo

for c in range(inicio, decimo + passo, passo):
    print(c, end=' -> ')

print('Acabou')
