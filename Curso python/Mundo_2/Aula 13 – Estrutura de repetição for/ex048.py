'''Faça um programa que calcule a soma entre todos os números que são 
múltiplos de três e que se encontram no intervalo de 1 até 500'''
soma = 0
for c in range(3,500,6):
    soma += c

print(soma)
