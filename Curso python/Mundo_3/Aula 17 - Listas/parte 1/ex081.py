'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

l = []

while True:
    l.append(int(input('Digite um núemro: ')))

    continuar = input('Deseja contiunar? [S/N] ').upper()
    if continuar == 'N':
        break

print(f'''
Foram digitados {len(l)} números.
A lista de forma decrecente: {sorted(l, reverse=True)}''')
if 5 in l:
    print('O número cinco está na lista.')
else:
    print('Não há o número cinco na lista.')