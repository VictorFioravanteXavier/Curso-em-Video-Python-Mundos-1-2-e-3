n1 = int(input('Digite um valor inteiro qualquer: '))
escolha = int(input('Digite (1 para binário), (2 para octal), (3 para hexadecimal): '))
cont = 0

if escolha == 1:
    print(f'O número {n1} em binário fica {bin(n1)}')
elif escolha == 2:
    print(f'O número {n1} em octal fica {oct(n1)}')
elif escolha == 3:
    print(f'O número {n1} em hexadecimal fica {hex(n1)}')
else:
    print(f'Erro!!\nA opção {escolha} não está listada.\nTente novamnete! ')