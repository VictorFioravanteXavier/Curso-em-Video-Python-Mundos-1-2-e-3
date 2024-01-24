'''Faça um programa que tenha uma função chamada área(), que receba as dimensões 
de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def Area(l,c):
    print(f'A área de um terreno {l}m * {c}m é de {l*c}m².')

l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))

Area(l, c)
