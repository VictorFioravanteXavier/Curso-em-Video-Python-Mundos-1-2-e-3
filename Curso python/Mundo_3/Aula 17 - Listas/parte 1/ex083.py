''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.'''

l = list(input('Digite uma espreção matemática: '))

c = 0
for letra in l:
    if '(' == letra:
        c += 1
    elif ')' == letra:
        c -= 1

if c == 0:
    print('Essa operação está correta.')
else:
    print('Essa operação está incorreta.')