'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de 
    vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = p = 0

while True:
    usuario = input('Digite "I" para impar e "P" para par: ').upper()
    c = True
    if usuario == 'I':
        print(f'{"-"*15}\nPc = Par\nUsuário = Impar\n{"-"*15}')
    elif usuario == 'P':
        print(f'{"-"*15}\nPc = Impar\nUsuário = Par\n{"-"*15}')
    else:
        c = False

    if c == True:
        n = int(input('Digite um número inteiro: '))
        n_pc = randint(1,100)

        if (n+n_pc)%2 == 0:
            if usuario == 'P':
                v += 1
                print('Você venceu!!')
            else:
                p += 1
        else:
            if usuario == 'I':
                v+=1
                print('Você venceu!!')
            else:
                p += 1
        
        if p >= 1:
            break

print(f'Você venceu {v} vez(es) e perdeu 1 vez.')
