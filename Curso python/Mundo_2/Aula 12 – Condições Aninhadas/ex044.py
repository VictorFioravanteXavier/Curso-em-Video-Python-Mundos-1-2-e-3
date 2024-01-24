valor = float(input('Digite o valor a ser pago: '))
escolha = int(input(f'''{'-'*30}\nEscolha a forma de pagamneto:\n{'-'*30}
( 1 ) - dinheiro / cheque
( 2 ) - à vista no cartão
( 3 ) - 2x no cartão
( 4 ) - 3x ou mais no cartão
~> '''))



if escolha == 1:
    print(f'O valor que deve ser pago é R${valor-(valor*10/100):.2f}, ele recebeu um desconto de 10%.')
elif escolha == 2:
    print(f'O valor que deve ser pago é R${valor-(valor*5/100):.2f}, ele recebeu um desconto de 5%.')
elif escolha == 3:
    print(f'O valor que deve ser pago é R${valor}.')
elif escolha == 4:
    quant = int(input('Quantas parcelas: '))
    print(f'''O valor que deve ser pago é R${valor+(valor*20/100):.2f}, ele recebeu um juros de 20%.
E por mês terá que pagar R${(valor+(valor*20/100))/quant:.2f}''')