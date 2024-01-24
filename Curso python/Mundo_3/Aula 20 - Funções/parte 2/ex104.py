'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
"a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt("Digite um n: ")'''

def leiaint(quest):
    while True:
        n = input(quest)
        if n.isdigit() == True:
            return n
        else:
            print('Erro! Digite um número inteiro válido.')

n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar {n}.')