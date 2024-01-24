def ler_cadastros():
    arquivo = open('cadastros.txt', 'r')
    print('-'*50)
    print(f'{"PESSOAS CADASTRADAS":^50}')
    print('-'*50)
    for linha in arquivo:
        print(linha,end='')
    arquivo.close()
