'''Faça um programa que tenha uma função notas() que pode receber várias 
notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''

def notas(*notas, sit = False):
    """-> Função para analizar notas e situações de varios alunos
    :param n: um ou mais notas (aceita várias)
    :param sit: valor opcional, indicado se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma."""

    d = {'total': len(notas), 'maior' : max(notas), 'menor' : min(notas), 'media' : sum(notas)/len(notas)}

    if sit:
        if d['media'] > 7:
            d['situação'] = 'Boa'
        elif d['media'] >= 6:
            d['situação'] = 'Razoavel'
        elif d['media'] < 6:
            d['situação'] = 'Mal'
        
    return d

resp = notas(4.5, 5.5, 10, 9, 6, 4.9, 7, 6.5, sit = False)
print(resp)
help(notas)