'''Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o 
usuário digitar a palavra 'FIM', o programa se encerrará. 
Importante: use cores.'''

from time import sleep

def sistema():
    while True:
        sleep(1)
        print(f'''\033[1;32;42m{'~'*35}\n{'Sistema de Ajuda PyHELP':^35}\n{'~'*35}\033[m''')
        n = input('Função ou Biblioteca: ')
        if n == 'fim':
            print(f"\033[1;31;41m{'~'*10}\n{'Até logo':^10}\n{'~'*10}\033[m")
            break
        sleep(1)
        print(f'''\033[1;36;46m{'~'*35}\n{f'Acessando o manual "{n}"':^35}\n{'~'*35}\033[m''')
        sleep(1)
        print(f'\033[1;30;40m{help(n)}\033[m')

sistema()