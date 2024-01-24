'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo:  0 - 1 - 1 - 2 - 3 - 5 - 8'''

n = int(input('\nDigite quantos números quer dá Sequência de Fibonacci: '))-2
p1 = 0
p2 = 1
print(f'\n{p1} -> {p2}', end= ' -> ')

while n != 0:
    p2 = p1 + p2
    p1 = p2 - p1
    n -= 1
    if n != 0:
        print(p2, end= ' -> ')
    else:
        print(p2,'\n')