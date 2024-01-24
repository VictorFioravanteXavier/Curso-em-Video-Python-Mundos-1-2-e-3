
n1 = str(input('digite alguma coisa: '))


print(f'o tipo dele é: {type(n1)}')

print(f'ele é um alfanúmerico: {n1.isalnum()}')
print(f'ele está no alfabeto: {n1.isalpha()}')
print(f'ele está na ASCII: {n1.isascii()}')
print(f'ele é decimal: {n1.isdecimal()}')
print(f'todos os caracteres são dígitos (0-9):  {n1.isdigit()}')
print(f'ele é um identificador válido em Python: {n1.isidentifier()}')
print(f'ele é todo minusculo: {n1.islower()}')
print(f'ele é todo maiusculo: {n1.isupper()}')
print(f'ele é numerico: {n1.isnumeric()}')
print(f'ele tem caracteres imprimíveis: {n1.isprintable()}')
print(f'ele é somente espaços em baranco: {n1.isspace()}')
print(f'ele está em formato de titulo: {n1.istitle()}')

