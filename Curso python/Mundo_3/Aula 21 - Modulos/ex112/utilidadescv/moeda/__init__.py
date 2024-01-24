def aumentar(m,por,opc):
    if opc:
        return moeda(m + (m * (por / 100)))
    else:
        return m + (m * (por / 100))

def diminuir(m,por,opc):
    if opc:
        return moeda(m - (m * (por / 100)))
    else:
        return m - (m * (por * 100))
    
def dobro(m,opc):
    if opc:
        return moeda(m * 2)
    else:
        return m * 2

def metade(m,opc):
    if opc:
        return moeda(m/2)
    else:
        return m / 2

def moeda(m):
    return f'R${m}'

def resumo(m,a,d):
    return f'''
{'-'*30}\n{'RESUMO DO VALOR':^30}\n{'-'*30}
{'Preço analisado:':<18} {moeda(m)}
{'Dobro do preço:':<18} {dobro(m,True)}
{'Metade do preço:':<18} {metade(m,True)}
{f'{a}% de aumento:':<18} {aumentar(m,a,True)}
{f'{d}% de redução:':<18} {diminuir(m,d,True)}
{'-'*30}'''

