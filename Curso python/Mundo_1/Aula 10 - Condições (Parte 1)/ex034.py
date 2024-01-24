salario = float(input('Digite seu salario: '))

if salario <= 1250.00:
    print(f'''Seu salario teve um aumento de {(salario*15)/100}
no total ficou {salario+salario*0.15}''')
else:
    print(f'''Seu salario teve um aumento de {(salario*10)/100}
no total ficou {salario+salario*0.10}''')
