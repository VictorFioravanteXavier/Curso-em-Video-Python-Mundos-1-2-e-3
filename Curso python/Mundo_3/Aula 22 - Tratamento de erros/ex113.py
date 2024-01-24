'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número de tipo inválido. Aproveite e crie também 
uma função leiaFloat() com a mesma funcionalidade.'''

def leiaint(quest):
    while True:
        try:
            p = int(input(quest))
            return p
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: Valor não é um número inteiro válido.\033[m')

def leiareal(quest):
    while True:
        try:
            p = float(input(quest).replace(',', '.'))
            return p
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        except ValueError:
            print('\033[31mERRO: Valor não é um número real válido.\033[m')

# main
n1 = leiaint('Digite um número inteiro: ')
print('Você digitou:', n1)

n2 = leiareal('Digite um número real: ')
print('Você digitou:', n2)
