'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma 
lista composta. No final, mostre um boletim contendo a média de cada um e permita que 
o usuário possa mostrar as notas de cada aluno individualmente.'''

l = []
nome = []
notas = []

while True:
    nome.append(input("Nome do aluno: "))
    for i in range(0,2):
        notas.append(float(input(f'Digite a {i+1}° nota: ')))
    nome.append(notas[:])
    l.append(nome[:])
    del (nome[:],notas[:])

    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break

print('=-'*15)
print(f'{"BOLETIM":^30}')
print('=-'*15)
print(f'N° - {"Nome":^15} - {"Média":^5}')
print('=-'*15)
for c, i in enumerate(l):
    print(f'{c}° - {i[0]:^15} - {sum(i[1]) / 2:^6}')
print('=-'*15)
while c != 999:
    c = int(input('Quer saber as notas de qual aluno? (999 para sair) '))
    if c != 999:
        print(f'Nome: {l[c][0]}\nNotas: {l[c][1][0],l[c][1][1]}')
        print('=-'*15)
