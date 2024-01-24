'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date

data = date.today().year()
menores = 0
maiores = 0

for i in range(0,7):
    ano = int(input('digite a seu ano de nascimento: '))
    idade = data - ano
    if idade < 21:
        menores += 1
    else:
        maiores += 1

print(f'{menores} são menores de idade e {maiores} são maiores.')
