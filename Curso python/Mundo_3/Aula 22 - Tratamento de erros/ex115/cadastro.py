def cadastro():
    print(f'{"-"*50}')
    print(f'{"Novo Cadastro":^50}')
    print(f'{"-"*50}')
    nome = input('Nome: ').title()
    while True:
        idade = int(input('Idade: '))
        try:
            break
        except ValueError:
            print('\033[31mDigite uma idade válida...\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário decidiu não digitar nada...\033[m')
            idade = "Erro"
            break
    
    arquivo = open('cadastros.txt', 'a')
    arquivo.write(f'{nome:<42}{idade:>3} anos\n')
    arquivo.close()
