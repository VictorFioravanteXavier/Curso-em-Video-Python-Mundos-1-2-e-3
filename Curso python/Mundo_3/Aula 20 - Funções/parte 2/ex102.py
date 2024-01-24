'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor 
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo 
do fatorial.'''

def fatorial(num, show = False):
    """->Calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num."""
    if show == True:
        fat = 1
        fat_str = ''
        for i in range(num, 0, -1):
            fat *= i 
            fat_str += str(i)
            if i > 1:
                fat_str += ' x '
        return f'{fat_str} = {fat}'
    else:
        fat = 1
        for i in range(num, 0, -1):
            fat *= i 
        return f'{fat}'

print(fatorial(5))