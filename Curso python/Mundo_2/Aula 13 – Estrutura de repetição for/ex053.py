''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

palavra = input('Digite uma palavra: ').lower().split()
palavra_sem_espaco = ''.join(palavra)


print(f'O inverso de {palavra_sem_espaco} é {palavra_sem_espaco[::-1]}')

if palavra_sem_espaco == palavra_sem_espaco[::-1]:
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')
    