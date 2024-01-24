'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

t = ("GATO", "LIVRO", "PRAIA","FLORESTA", "MONTANHA", "AVIÃO", "SOL", "PLANETA", 
    "FOGUEIRA", "CACHOEIRA")

for i in t:
    print(f'As vogais de {i} são:', end=(' '))
    for letra in i:
        if letra in 'AEIOU':
            print(letra.lower(), end= (' '))
    print()