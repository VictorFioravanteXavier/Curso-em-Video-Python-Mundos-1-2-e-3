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