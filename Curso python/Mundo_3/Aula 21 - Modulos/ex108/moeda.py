def aumentar(moeda,por):
    return moeda + (moeda * (por/100))

def diminuir(moeda,por):
    return moeda - (moeda * (por/100))

def dobro(moeda):
    return moeda * 2

def metade(moeda):
    return moeda / 2

def moeda(moeda):
    return f'R${moeda}'