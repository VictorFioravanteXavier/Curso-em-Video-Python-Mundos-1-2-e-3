'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(nasc):
    from datetime import date
    atual =  date.today().year
    global r
    r = atual - nasc
    if r < 16:
        return f'Com {r} anos: VOTO NEGADO.'
    elif r >= 18 and r < 65:
        return f'Com {r} anos: VOTO OBRIGATORIO.'
    else:
        return f'Com {r} anos: VOTO OPCIONAL.'


nasc = int(input('Ano de nascimento: '))

print(voto(nasc))