'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = ''

while sexo not in ('MF'):
    sexo = input('Digite seu sexo: ').upper()
    if sexo not in ('M','F'):
        print('\033[1;31mOpção inválida!\033[m')
    else:
        break

print(f'Seu sexo é {"Feminino" if sexo == "F" else "Masculino"}!')
    