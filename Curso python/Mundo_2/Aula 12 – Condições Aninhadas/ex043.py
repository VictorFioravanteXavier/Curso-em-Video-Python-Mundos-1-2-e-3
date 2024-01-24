peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

IMC = peso/(pow(altura,2))

if IMC <= 18.5:
    print('Você está abaixo de peso.')
elif IMC <= 25:
    print('Você está no peso ideal.')
elif IMC <= 30:
    print('Você está com sobrepeso.')
elif IMC <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')