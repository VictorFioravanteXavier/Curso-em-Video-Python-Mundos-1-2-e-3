'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre 
os valores pares e ímpares em ordem crescente.'''

l=[[],[]]
for i in range(0,7):
    n = int(input(f'digite o {i+1}° número: '))
    if n %2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
    
print(f'os valores pares digitados foram {sorted(l[0])}')
print(f'os valores ímpares digitados foram {sorted(l[1])}')