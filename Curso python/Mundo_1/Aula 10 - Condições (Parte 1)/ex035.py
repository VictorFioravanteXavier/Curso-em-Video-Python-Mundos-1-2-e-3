r1 = float(input('Digite a 1° reta: '))
r2 = float(input('Digite a 2° reta: '))
r3 = float(input('Digite a 3° reta: '))

if r1+r2 >= r3 and r1+r3 >= r2 and r3+r2 >= r1:
    print('As retas podem formar um triangulo.')
else:
    print('As retas não podem formar um triangulo.')
