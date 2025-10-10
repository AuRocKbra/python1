import os

restaurantes = ['Pizza','Suchi']

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)
def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizando_app():
    exibir_mensagem_titulo('Finalizando o programa...')

def opcao_invalida():
    exibir_mensagem_titulo('Opção inválida!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input("\nPressione qualquer tecla para continuar. ")
    main()

def exibir_mensagem_titulo(texto):
    os.system('cls')
    print(f'{texto}')
    print()

def cadastrar_novo_restaurante():
    exibir_mensagem_titulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Informe o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_mensagem_titulo('Listar restaurantes:')
    for restaurante in restaurantes:
        print(f'-{restaurante}')
    voltar_ao_menu_principal()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolha_opcao()

def escolha_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif (opcao_escolhida == 2):
            listar_restaurantes()
        elif (opcao_escolhida == 3):
            print('Ativando restaurante')
        elif (opcao_escolhida == 4):
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()