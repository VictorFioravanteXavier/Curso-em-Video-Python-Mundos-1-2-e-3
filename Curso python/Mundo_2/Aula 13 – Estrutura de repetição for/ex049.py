'''Refaça o DESAFIO 10, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n1 = int(input('fale um número qualquer: '))
print(f'''{('-')*20}\nA tabuada de {n1} é:\n{('-')*20}''')
for c in range(0,11):
    print(f'{n1} x {c:2} = {n1*c}')
