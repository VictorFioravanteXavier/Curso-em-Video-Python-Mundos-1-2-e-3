km = int(input('Digite a velociadade do carro (em KM): '))

if km == 80:
    print('Não foi multado!')
else:
    print(f'Você foi multado em R${(km-80)*7:.2f}.')
