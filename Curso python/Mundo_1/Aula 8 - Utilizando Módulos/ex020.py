import random

n1 = str(input('Digite o nome do 1° aluno: ')).title()
n2 = str(input('Digite o nome do 2° aluno: ')).title()
n3 = str(input('Digite o nome do 3° aluno: ')).title()
n4 = str(input('Digite o nome do 4° aluno: ')).title()

aluno_escolhido = random.choice([n1, n2, n3, n4])

print(f'O aluno que deve apagar o quadro é {aluno_escolhido}')