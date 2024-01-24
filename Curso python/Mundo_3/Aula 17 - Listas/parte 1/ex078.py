'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

l = []
for i in range(0,5):
    l.append(int(input(f'Digite o {i+1}° número: ')))
print(f'Você digitou: {l}')
print(f'O maior valor encontrado na lista é {max(l)} que está na {l.index(max(l))+1}° posição.')
print(f'O menor valor encontrado na lista é {min(l)} que está na {l.index(min(l))+1}° posição.')
