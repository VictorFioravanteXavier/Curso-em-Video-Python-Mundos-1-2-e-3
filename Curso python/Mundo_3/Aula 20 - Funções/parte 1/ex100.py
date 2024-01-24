'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep

def sorteia():
    print('=-'*20)
    print(f'{"Números":^40}')
    print('=-'*20)
    print('Números:', end=' ')
    l = []
    for i in range(0,5):
        n = randint(0,100)
        l.append(n)
        sleep(0.5)
        print(n, end= ' ')
    print()
    return l


def somar_par(lista):
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print (f'Soma pares: {s}')
    
somar_par(sorteia())