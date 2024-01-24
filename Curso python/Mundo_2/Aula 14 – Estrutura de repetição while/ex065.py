'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi 
o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


continuar = ''
n1 = float(input(f'Digite um número, foi colocado nenhum número: '))
c = 1
maior = n1 
menor = n1
soma = n1

while continuar != 'N':
    continuar = input('Deseja continuar? (S ou N): ').upper()
    if continuar == 'S':
        n1 = float(input(f'Digite um número, foram colocados {c} números: '))
        c += 1
        soma += n1
        maior = max(maior,n1) 
        menor = min(menor,n1)
    elif continuar == 'N':
        print(f'A média foi: {soma/c}\nMaior: {maior}\nMenor: {menor}')
    else:
        print('Erro!')