from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))


anos = date.today().year - ano_nascimento

if anos < 10:
    print(f'Ele(a) é Mirin, pois tem {anos} anos')
elif anos < 15:
    print(f'Ele(a) é Infantil, pois tem {anos} anos')
elif anos < 20:
    print(f'Ele(a) é Junior, pois tem {anos} anos')
elif anos == 20:
    print(f'Ele(a) é Sênior, pois tem {anos} anos')
else:
    print(f'Ele(a) é Master, pois tem {anos} anos')