km = float(input('digite a quantidade de kms percorridos: '))
dias = int(input('digite a quantide de dias que o carro foi alugado: '))

print(f'O carro percorreu {km}KMs que dão R${km*0.15:.2f} e foi alugado {dias} dia(s) que dá R${dias*60:2.2f} no total tem que pagar R${dias*60+km*0.15:.2f}.')