n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
"""maior = n1
menor = n1
if maior < n2:
    maior = n2
if menor > n2:
    menor = n2
if maior < n3:
    maior = n3
if menor > n3:
    menor = n3

print(f'o maior é {maior}')
print(f'o menor é {menor}')"""

print(f'O maior é {max(n1,n2,n3)}')
print(f'o menor é {min(n1,n2,n3)}')
