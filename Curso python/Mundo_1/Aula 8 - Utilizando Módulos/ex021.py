import random

n1 = str(input('Digite o nome do 1° aluno: ')).title()
n2 = str(input('Digite o nome do 2° aluno: ')).title()
n3 = str(input('Digite o nome do 3° aluno: ')).title()
n4 = str(input('Digite o nome do 4° aluno: ')).title()

alunos = [n1, n2, n3, n4]
random.shuffle(alunos)

print(f'A ordem que vai ser apresentada é {alunos}')
