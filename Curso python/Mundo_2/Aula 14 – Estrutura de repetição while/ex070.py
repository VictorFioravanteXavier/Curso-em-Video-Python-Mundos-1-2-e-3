'''rie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''


total_gasto = mais_mil = preco_produto_mais_barato = cont = 0
nome_produto_mais_barato = ''
while True:
    continuar = input('Deseja continuar? (S ou N): ').upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))

        if cont == 0:
            produto_mais_barato = preco
            nome_produto_mais_barato = nome
            cont = 1
        
        total_gasto += preco
        if preco > 1000: 
            mais_mil += 1
        if preco < produto_mais_barato:
            produto_mais_barato = preco
            nome_produto_mais_barato = nome

print(f'''
Nota:
Preço total = {total_gasto}
Quantidade de produtos que custam mais de mil: {mais_mil}

Produto mais barato:
Nome: {nome_produto_mais_barato}
Preço: {produto_mais_barato}
''')