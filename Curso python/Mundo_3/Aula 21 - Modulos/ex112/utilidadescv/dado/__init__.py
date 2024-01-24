

def leiadinheiro(quest):
    while True:
        p = input(quest)

        p = p.replace(',', '.')

        try:
            p = float(p)  
            break  
        except ValueError:
            print(f'ERRO "{p}" NÃO É UM VALOR NUMÉRICO VÁLIDO')

    return p