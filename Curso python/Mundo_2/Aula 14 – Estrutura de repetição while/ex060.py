'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

n1 = int(input('Digite um número: '))
r = 1
print(f'{n1}! = ', end='')

while n1 != 0:
    r *= n1
    if n1 != 1 and n1 > 0:
        print(f'{n1} x ', end= '')
    elif n1 == 1:
        print(f'{n1} = ', end= '')
    n1 -= 1

print(f'{r}')

'''from math import factorial

n1 = int(input('Digite um número: '))
f = factorial(n1)

print(f'O fatorial de {n1} = {f}')'''