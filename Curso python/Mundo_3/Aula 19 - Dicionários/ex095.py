d = {}
gols = []
jogadores = []
maior = None
while True:
    d['Nome'] = input('Digite o nome do jogador: ')
    n = int(input('Quantas partidas ele  jogou: '))

    if maior == None:
        maior = n
    elif maior < n:
        maior = n


    print('=-'*30)
    gols = []
    for i in range (0,n):
        gols.append(int(input(f'Quantos gols ele fez na {i+1}° partida: ')))

    d['Gols'] = gols[:]
    d['Total'] = sum(d['Gols'])
    jogadores.append(d.copy())
    
    opc = input('Quer continar? [S/N] ').upper()
    if opc == 'N':
        break


print('=-' * 30)
print(f'{"cod":^3} - {"Nome":^15} - {"Gols":^{maior*(maior-1)+2}} - {"Total":^5}')
for i in range(0, len(jogadores)):
    gols_formatados = ', '.join(str(g) for g in jogadores[i]["Gols"])
    print(f'{i:^3} - {jogadores[i]["Nome"]:^15} - {gols_formatados:^{maior*(maior-1)+2}} - {jogadores[i]["Total"]:^5}')

print('=-'*30)
while True:
    cod = int(input('Mostrar dados de qual jogador? [digite 999 para acabar] ')) 
    if cod == 999:
        print('Saindo...')
        break
    print('=-'*30)
    print(f'- Dados das partidas do jogador {jogadores[cod]["Nome"]} ')
    for j, i in enumerate(jogadores[cod]['Gols']):
        print(f'Na {j+1}° partida ele marcou {i} gols')
    print('-='*30)  