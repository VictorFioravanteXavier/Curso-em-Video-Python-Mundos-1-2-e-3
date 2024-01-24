'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de 
ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e 
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''


from datetime import date

ano_atual = date.today().year

d = {}
d['Nome'] = input('Digte seu nome: ')
d['Idade'] = ano_atual - int(input('Digite o seu ano de nascimento: '))
d['Carteira de Trabalho'] = int(input('Digite sua carteira de trabalho: [0 se não tiver] '))

if d['Carteira de Trabalho'] != 0:
    d['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    d['Salário'] = float(input('Digite seu salário: '))

if ano_atual-d['Ano de Contratação'] >= 35:
    d['Aposentadoria'] = 'Você já pode se aposentar!'
else:
    d['Aposentadoria'] = 35 - (ano_atual-d['Ano de Contratação'])


print(f'''
Nome: {d["Nome"]}
Idade: {d["Idade"]}
Carteira de Trabalho: {"Não tem carteira de trabalho" if d["Carteira de Trabalho"] == 0 else f"""{d['Carteira de Trabalho']}
Ano de Contratação: {d['Ano de Contratação']}
Salário: R$ {d['Salário']:.2f}"""}
{d['Aposentadoria'] if 'Você já pode se aposentar!' == d["Aposentadoria"] else f"Falta {d['Aposentadoria']} anos para você se aposentar"}
''')