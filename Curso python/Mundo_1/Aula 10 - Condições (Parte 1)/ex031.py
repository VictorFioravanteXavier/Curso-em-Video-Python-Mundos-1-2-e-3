dis = float(input('Digite a distancia que você vai percorrer (em KM): '))

if dis <= 200:
    print(f'Você tera que pagar R${dis*0.5} pois sua viagem é menor ou igual a 200Km')
elif dis > 200:
    print(f'Você tera que pagar R${dis*0.45} pois sua viagem é maior que 200Km')
