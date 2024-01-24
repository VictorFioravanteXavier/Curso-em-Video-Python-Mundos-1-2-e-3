from datetime import date

ano = int(input('Digite o ano (Digite 0 para saber o ano atual): '))

if ano == 0:
    ano = date.today().year
print(ano)

if ano%4 == 0 and ano%100 != 0:
    print('Ele é bisesto!')
elif ano%4 == 0 and ano%100 == 0:
    if ano % 400 == 0:
        print('Ele é bissexto!')
    else:
        print('Ele não é bissexto!')
else:
    print('Ele não é bissexto!')
