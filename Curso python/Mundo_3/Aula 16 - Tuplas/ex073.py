'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''
colocacao = ('BOTAFOGO','FLAMENGO','GRÊMIO','SÃO PAULO','FLUMINENSE','PALMEIRAS',
            'RED BULL BRAGANTINO','ATHLETICO-PR','FORTALEZA','CRUZEIRO','INTERNACIONAL',
            'ATLÉTICO-MG','CUIABÁ','SANTOS','CORINTHIANS','BAHIA','GOIÁS','CORITIBA','VASCO','AMÉRICA-MG')

print('Os cinco melhores colocados: ')
for i in range(0,5):
    print(f'{i+1} - {colocacao[i]}')
print("="*25)

print('Os quatro piores colocados: ')
for i in range(17,21):
    print(f'{i} - {colocacao[i-1]}')
print("="*25)

print('Colocação em ordem alfabética: ')
print(sorted(colocacao))
print("="*25)

c = 'CHAPECOENCE' in colocacao
if c == False:
    print('Capecoence não está nessa lista. :(')
else:
    print(f'Capecoence está na {colocacao.index("CHAPECOENCE")+1}° posição')
print("="*25)
