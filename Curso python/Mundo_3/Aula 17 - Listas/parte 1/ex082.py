'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares 
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

l = []
pares = []
impares = []
while True:
    l.append(int(input('Digite um número: ')))
    c = input('Quer continuar? [S/N] ').upper()
    if c == 'N':
        break

for i in l:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'A lista inteira: {l}')
print(f'apenas pares: {pares}')
print(f'apenas ímpares: {impares}')