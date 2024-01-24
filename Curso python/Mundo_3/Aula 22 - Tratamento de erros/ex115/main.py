from cadastro import cadastro
from ler_cadastros import ler_cadastros


def main():
    while True:
        print("-"*50)
        print(f"{'MENU PRINCIPAL':^50}")
        print("-"*50)

        print('''\033[33m[ 1 ]\033[m - \033[34mVer Pessoas Cadastradas\033[m
\033[33m[ 2 ]\033[m - \033[34mCadastar nova Pessoa\033[m
\033[33m[ 3 ]\033[m - \033[34mSair do Sistema\033[m''')
        escolha = input('\033[33mSua escolha: \033[m')
        
        

        try:    
            if escolha[0] in '123':
                escolha = int(escolha)
            else:
                print('\033[31mErro! Digite uma opção válida...\033[m')
        except ValueError:
            print('\033[31mErro! Valor digitado inválido...\033[m')
        except KeyboardInterrupt:
            print('\033[31mSaindo do Sistema...\033[m')
            break
    
        if escolha == 1:
            ler_cadastros()
        elif escolha == 2:
            cadastro()
        elif escolha == 3:
            print('\033[31mSaindo do Sistema...\033[m')
            break

if __name__ == '__main__':
    main()