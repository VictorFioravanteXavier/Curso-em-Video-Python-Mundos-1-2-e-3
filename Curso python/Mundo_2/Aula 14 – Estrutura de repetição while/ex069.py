'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

q_18 = q_m = q_f = 0

while True:
    continuar = input('Deseja continuar: (S ou N). ').upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        idade = int(input('Digite a idade da pessoa: '))
        sexo = input('Digite o sexo da pessoa (M ou F): ').upper()

        if idade > 18:
            q_18 += 1

        if sexo == 'M':
            q_m += 1
        else:
            if idade < 20:
                q_f += 1
    else:
        print('\nOpção inválida. Tente novamente.\n')
    
print(f'''
Pessoas com mais de 18 anos {q_18}
Homens cadastrados: {q_m}
Mulheres com menos de 20 anos {q_f}''')