'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
print(f'''{('-')*5} 1° pessoa {('-')*5}''')

nome = input('Digite seu nome: ').title()
idade = int(input('Digite sua idade: '))
sexo = input('Digite sua idade (M ou F): ').upper()
media_idade = idade
cont = None
maior_nome = None
maior_idade = 0

if sexo == 'M':
    maior_idade = idade
    maior_nome = nome
elif sexo == 'F':
    if idade < 20:
        cont = 1

for i in range(2, 5):
    print(f'''{('-')*5} {i}° pessoa {('-')*5}''')
    nome = input('Digite seu nome: ').title()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite sua idade (M ou F): ').upper()
    media_idade += idade

    if sexo == 'M':
        if maior_idade < idade:
            maior_idade = idade
            maior_nome = nome
    elif sexo == 'F':
        if idade < 20:
            cont += 1

print(f'A media de idade do grupo é {media_idade/4:.1f}')
if maior_nome:
    print(f'O nome do homem mais velho é {maior_nome}')
else:
    print('Não há homens no grupo.')

if cont:
    print(f'Tem {cont} mulhere(s) com menos de 20 anos')
else:
    print('Não há mulhers com menos de 20 anos no grupo.')
