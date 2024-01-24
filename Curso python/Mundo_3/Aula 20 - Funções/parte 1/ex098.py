'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''


from time import sleep

def contador(inicio, fim, passo=1):
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} com passo {passo}:')
    if inicio < fim:
        for i in range(inicio, fim+passo, passo):
            sleep(0.5)
            print(i, end=' ')
        print()
    else:
        for i in range(inicio, fim, -passo):
            sleep(0.5)
            print(i, end=' ')
        print()

contador(0,10)

contador(10,0,2)

print('-' * 30)
print('Agora é sua vez de personalizar a contagem: ')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio,fim,passo)