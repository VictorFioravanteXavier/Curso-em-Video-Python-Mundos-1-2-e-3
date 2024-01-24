n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))

media = (n1+n2)/2

print(f'Com a de {media} você ficou', end=' ')

if media < 5:
    print('REPROVADO!')
elif media < 7:
    print('DE RECUPERAÇÃO!')
else:
    print('APROVADO!')
