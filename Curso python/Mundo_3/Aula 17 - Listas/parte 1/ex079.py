'''Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

l = []
while True:
    n = int(input('Digite um número: '))
    if n not in l:
        print(f'{n} foi adicionado!')
        l.append(n)
    else:
        print('Você já colocou esse número.')
    

    continuar = input("Deseja continuar? [S/N] ").upper()
    if continuar == 'N':
        break

print('Você digitou: ',sorted(l))