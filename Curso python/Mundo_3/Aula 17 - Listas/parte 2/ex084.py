'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

l = []
ll = []

while True:
    l.append(input('Digite o nome: '))
    l.append(int(input('Digite o peso (kg): ')))
    ll.append(l[:])
    l = []
    continuar = input('Quer continar? [S/N] ')
    if continuar in 'Nn':
        break

leves = []
pesados = []
menor = 100
maior = 0
for i in range(0,len(ll)):
    if ll[i][1] == maior:
        pesados.append(ll[0])
    elif ll[i][1] > maior:
        pesados=[]
        pesados.append(ll[i][0])
        maior=ll[i][1]

    if ll[i][1] == menor: 
        leves.append(ll[i][0])
    elif ll[i][1] < menor:
        leves = []
        leves.append(ll[i][0])
        menor = ll[i][1]


print(f'foram cadastradas {len(ll)} pessoas')
print(f'o menor peso foi de {menor} e a(s) pessoa(s) mai(s) leve(s) são/é:',end=' ')
for i in leves:
    print(i, end=' ')
print()
print(f'o maior peso foi de {maior} e a(s) pessoa(s) mai(s) pesada(s) são/é:',end=' ')
for i in pesados:
    print(i, end=' ')
print()