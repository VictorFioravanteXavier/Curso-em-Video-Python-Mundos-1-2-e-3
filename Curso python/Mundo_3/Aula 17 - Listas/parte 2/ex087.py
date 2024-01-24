'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

l = [[],[],[]]
soma_pares = soma_coluna = maior = 0

for i in range(0,3):
    for j in range (0,3):
        l[i].append(int(input(f'Digite o número da posição [{i+1}] [{j+1}]: ')))

        if l[i][j] % 2 == 0:
            soma_pares += l[i][j]

        if j == 2:
            soma_coluna += l[i][j]
        
        if i == 1:
            if j == 0:
                maior = l[i][j]
            elif maior < l[i][j]:
                maior = l[i][j]

print('=-'*19)
for i in l:
    print(f'{"     "*2}[{i[0]:^3}] [{i[1]:^3}] [{i[2]:^3}]')
print('=-'*19)
print(f'A soma de todos os pares é: {soma_pares}')
print(f'A soma da 3° coluna é: {soma_coluna}')
print(f'O maior valor da segunda linha é: {maior}')