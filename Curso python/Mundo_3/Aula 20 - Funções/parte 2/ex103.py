'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz 
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='<desconhecido>', gol='0'):
    return f'O jogador {nome} fez {gol} gol(s) no campeonato.'

nome = input('Digite o nome do jogador: ')
gol = input('Quantos gols ele fez: ')

if nome == '' and gol == '':
    print(ficha())
elif nome == '':
    print(ficha(gol = gol))
elif gol == '':
    print(ficha(nome = nome)) 
else:
    print(ficha(nome,gol))