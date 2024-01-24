'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros 
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles 
é o maior.'''

def maior(*num):
    print('-='*25)
    print('Analizando os valores passados...')
    print(*num, f'Foram colocados ao todo {len(num)} números')
    if len(num) < 1:
        print('O maior é 0')
    else:
        m = None
        for i in num:
            if m == None:
                m=i
            else:
                if i > m :
                    m = i
        print(f'O maior é {m}')
    

maior(1,2,1,2,2,5,2,5,8,9,4,6)

maior(0,25,51,5151,151815)

maior()