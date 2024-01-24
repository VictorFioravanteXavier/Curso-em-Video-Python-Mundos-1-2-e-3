'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

d = {}
l = []
m = 0

while True:
    d['Nome'] = input('Digite seu nome: ')
    d['Sexo'] = input('Digite seu sexo: [M/F] ').upper()
    while True:
        if d['Sexo'] in 'MF':
            break
        else:
            d['Sexo'] = input('Opção inválida! Digite o seu sexo: [M/F]').upper()
    d['Idade'] = int(input('Digite sua idade: '))
    l.append(d.copy())
    opc = input('Deseja continuar? [S/N] ')
    if opc in 'nN':
        break

print('=-'*25)
print(f'Foram adicionadas {len(l)} pessoas')

for i in range(0,len(l)):
    m += l[i]['Idade']
m /= len(l)
print(f'A média de idade do grupo é {m}.\n')

print('=-' * 25)
print(f'{"Lista de mulhers no grupo":^50}')
print('=-' * 25)
for i in range (0,len(l)):
    if l[i]['Sexo'] == 'F':
        print(f'Nome: {l[i]["Nome"]}\nIdade: {l[i]["Idade"]}\n')

print('=-' * 25)
print(f'{"Lista de pessoas acima da média de iadde":^50}')
print('=-' * 25)
for i in range (0,len(l)):
    if l[i]['Idade'] > m:
        print(f'Nome: {l[i]["Nome"]}\nSexo: {l[i]["Sexo"]}\nIdade: {l[i]["Idade"]}\n')