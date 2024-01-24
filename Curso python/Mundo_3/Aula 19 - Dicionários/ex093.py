'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai 
ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado 
em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

d = {}
l = []
d['Nome'] = input('Digite o nome do jogador: ')

n = int(input('Quantas partidas ele  jogou: '))
for i in range (0,n):
    l.append(int(input(f'Qunatas gols ele fez na {i+1}° partida: ')))

d['Gols'] = l[:]
d['Total'] = sum(d['Gols'])
print('-='*25)
for i in d.keys():
    print(f'{i}: {d[i]}')
print('-='*25)
for j, i in enumerate(d['Gols']):
    print(f'Na {j+1}° partida ele marcou {i} gols')
print('-='*25)