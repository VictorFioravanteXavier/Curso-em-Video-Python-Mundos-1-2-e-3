'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados
em forma tabular.'''

t = ('Caneta', 1.50,
    'Livro', 5,
    'Mochila', 20, 
    'Lapis', 1, 
    'Casa', 200)

print('='*30)
print(f'{"LISTA DE PREÇOS":^30}')
print('='*30)
for i in range(0,len(t),2):
    print(f'{t[i]:.<{18}} R$ {t[i+1]:>7.2f}')
print('='*30)