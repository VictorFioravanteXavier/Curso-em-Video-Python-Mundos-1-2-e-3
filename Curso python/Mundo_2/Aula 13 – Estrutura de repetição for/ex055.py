'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''


peso = []
for i in range(0,5):
    peso.append(float(input('digite seu peso: ')))

print(f'O maior peso é {max(peso)} e o mneor é {min(peso)}.')
