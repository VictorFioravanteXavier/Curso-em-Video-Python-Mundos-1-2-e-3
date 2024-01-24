'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

print('Digite 4 números: ')
t = (int(input()), int(input()), int(input()), int(input()))

print(f'o núemro 9 apareceu {t.count(9)} vez(es)')

if 3 in t == True:
    print(f'o 3 apareceu a primeira vez na {t.index(3)+1}° posição ')
else:
    print("O número '3' não foi digitado.")

p = 0
for i in t:
    if i %2 == 0:
        print(i, end=' ')
        p = 1
if p == 0:
    print('Não tem números pares')
else:
    print('São os núemros pares da tupla.')