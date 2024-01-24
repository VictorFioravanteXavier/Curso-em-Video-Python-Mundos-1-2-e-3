import random
while True:
    escolha = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).title()
    escolha_pc = random.choice(['Pedra', 'Papel', 'Tesoura'])

    print('Calculando...')

    if escolha not in ('Pedra', 'Papel', 'Tesoura'):
        print('Erro! Tente novamente.')
    else:
        print(f'Você escolheu {escolha} e o pc escolheu {escolha_pc} então você', end=' ')
        if escolha == 'Papel' and escolha_pc == 'Pedra':
            print('\033[1;32mVENCEU!\033[m')
        elif escolha == 'Papel' and escolha_pc == 'Tesoura':
            print('\033[1;31mPERDEU!\033[m')
        elif escolha == 'Pedra' and escolha_pc == 'Papel':
            print('\033[1;31mPERDEU!\033[m')
        elif escolha == 'Pedra' and escolha_pc == 'Tesoura':
            print('\033[1;32mVENCEU!\033[m')
        elif escolha == 'Tesoura' and escolha_pc == 'Pedra':
            print('\033[1;31mPERDEU!\033[m')
        elif escolha == 'Tesoura' and escolha_pc == 'Papel':
            print('\033[1;32mVENCEU!\033[m')
        else:
            print('\033[1;33mEMPATE!\033[m')
