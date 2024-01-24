valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Quantos anos pretende pagar a casa: '))

valor_mensal_apagar = valor_casa / (anos*12)
print(f'O valor  mensal a pagar vai ser R${valor_mensal_apagar:.2f}')
porcentagem_salario = (salario*30)/100

if valor_mensal_apagar <= porcentagem_salario:
    print('Você podera comprar a casa!')
else:
    print('Você não podera comprar a casa.')