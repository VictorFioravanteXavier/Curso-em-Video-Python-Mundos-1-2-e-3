n1 = int(input('digite um número de 0 a 9999: '))



print(f'''O número {n1} tem:
unidade: {n1 % 10}
dezena: {n1 // 10 %10}
centena: {n1 // 100 %10}
milhar: {n1 // 1000}
''')
