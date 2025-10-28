import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Italiana','ativo':True},
                {'nome':'Cantina','categoria':'Italiana','ativo':False}]

def exibir_nome_do_programa():
    '''
    Função responsável por exibir o nome do programa na tela

    Output:
        - Nome do programa
    '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)
def exibir_menu():
    '''
    Função responsável por exibir o menu de opções do programa

    Output:
        - Menu de seleção
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Atualizar estado restaurante')
    print('4. Sair\n')

def finalizando_app():
    '''
    Função responsável por apresentar a mensagem de finalização do programa

    Output:
        - Mensagem de finalização do progroma
    '''
    exibir_mensagem_titulo('Finalizando o programa...')

def opcao_invalida():
    '''
    Função responsável por apresentar em tela uma mensagem de erro

    Output:
        - Mensagem de erro
    '''
    exibir_mensagem_titulo('Opção inválida!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''
    Função responsável por voltar ao menu principal do programa

    Input:
        - Qualquer tecla pressionada pelo usuário
    '''
    input("\nPressione qualquer tecla para continuar. ")
    main()

def exibir_mensagem_titulo(texto):
    '''
    Função responsável por limpar o texto em tela

    Input:
        - texto: Texto a ser exibido na tela

    Output:
        - Texto formatado na tela
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''
    Função responsável por cadastrar um novo restaurante

    Input:
        - Nome do restaurante
        - Categoria do restaurante

    Output:
        - Dados do restaurante cadastrado
    '''
    exibir_mensagem_titulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Informe o nome do restaurante: ')
    categoria_do_restaurante = input(f'Informe a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_do_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Função responsável por listar todos os restaurantes cadastrados

    Input:
        - Nome do restaurante

    Output:
        - Dados de todos os restaurantes cadastrados
    '''
    exibir_mensagem_titulo('Listar restaurantes:')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado')
    for restaurante in restaurantes:
        ativo = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante["categoria"].ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def main():
    '''
    Função principal do programa

    Output:
        - Menu principal
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolha_opcao()

def alternar_estado_restaurante():
    '''
    Função responsável por alterar o status do restaurante

    Input:
        - Nome do restaurante

    Output:
        - Dados do restaurante atualizados
    '''
    exibir_mensagem_titulo('Alternando estado do restaurante')
    nome_do_restaurante = input('Informe o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_do_restaurante:
            restaurante['ativo'] = not restaurante['ativo']
            restaurante_encontrado = True
            print(f'Estado do restaurante {nome_do_restaurante} alterado para {restaurante["ativo"]}')
            break
    if (not restaurante_encontrado):
        print(f'Restaurante não encontrado!')
    voltar_ao_menu_principal()

def escolha_opcao():
    '''
    Função responsável por definir o comportamento do programa conforme opção selecionado do usuário

    Input:
        - Opção selecionada pelo usuário

    Output:
        - Rotina correspondente a opção selecionada
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif (opcao_escolhida == 2):
            listar_restaurantes()
        elif (opcao_escolhida == 3):
            alternar_estado_restaurante()
        elif (opcao_escolhida == 4):
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()