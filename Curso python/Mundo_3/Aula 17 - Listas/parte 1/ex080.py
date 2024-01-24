'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a 
lista ordenada na tela.'''

l = []
for i in range(0,5):
    n = int(input('Digite um valor: '))

    if len(l) == 0 or n >= l[-1]:
        l.append(n)
    else:
        for i in range(len(l)):
            if n <= l[i]:
                l.insert(i, n)
                break
    

print('a lita ordenada é: ',l)