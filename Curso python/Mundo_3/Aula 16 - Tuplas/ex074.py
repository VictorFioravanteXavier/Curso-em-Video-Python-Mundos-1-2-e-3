'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
    mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

c = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print(f'a tupla é: {c}')
print(f'o maior é: {max(c)}')
print(f'o menor é: {min(c)}')


