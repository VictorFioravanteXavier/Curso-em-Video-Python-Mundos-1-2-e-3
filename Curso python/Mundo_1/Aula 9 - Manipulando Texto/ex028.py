import random

nc = random.randint(0,5)
np = int(input('digite um número de 0 a 5: '))

if nc == np:
    print('Você consegui ganhar!')
else:
    print('Que pena. Tente novamente')
