'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

passo = int(input('Digite o passo: '))
inicio = int(input('Digite o início: '))
decimo = inicio + 9 * passo
continuar = 1

while continuar != 0:
    
    while inicio != decimo + passo:
        if inicio != decimo:
            print(inicio, end=' -> ')
        else:
            print(inicio)
        inicio += passo

    continuar = int(input('Digite a quantidade a mais para adicionar na PA (0 para parar): '))
    decimo += continuar * passo

print('Acabou')
