import math

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

raiz = math.hypot(cateto_adjacente, cateto_oposto)

print(f'A hipotenusa é: {raiz:.2f}')
