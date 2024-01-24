from datetime import date
n1 = int(input('Dogite seu ano de nascimento: '))
data = date.today().year
idade =  data - n1

if idade < 18:
    print(f'Ainda vai se alistar faltam {18 - idade} anos.')
elif idade == 18:
    print('Hora de se alistar.')
else:
    print(f'passou do tempo de alistamento. Já passou {idade - 18} anos.')
