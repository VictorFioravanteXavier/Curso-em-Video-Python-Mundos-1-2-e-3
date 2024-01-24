'''Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

d = {}

d['Nome'] = input('Digite o nome: ')
d['Media'] = float(input('Digite a media: '))

if d['Media'] <= 7:
    d['Situacao'] = 'Reprovou'
else:
    d['Situacao'] = 'Passou'

print('-'*30)
print(f'Nome: {d["Nome"]}')
print(f'Média: {d["Media"]}  ')
print(f'Situação: {d["Situacao"]}')
print('-'*30)