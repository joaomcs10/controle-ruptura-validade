from entrada import pedir_numero, pedir_nome
from estoque import onde_esta
from exibicao import em_construcao, mostrar_cabecalho, pausa


def menu_principal(em_ruptura,proximo_a_ruptura):

    while True:

        mostrar_cabecalho('Menu Principal')

        print('\n 1 - Consultar informações')
        print('\n 2 - Adicionar ')
        print('\n 3 - Excluir ')
        print('\n 4 - sair')

        opcao = pedir_numero('Escolha uma opção: ')

        if opcao == 1:
            menu_informacoes(em_ruptura,proximo_a_ruptura)

        elif opcao == 2:
            menu_adicionar()

        elif opcao == 3:
            menu_excluir()

        elif opcao == 4:

            print('Encerrando o programa ...')

            break

        else:

            print('Entrada invalida! Escolha uma opção do menu')

def menu_informacoes(em_ruptura,proximo_a_ruptura):


    while True:

        mostrar_cabecalho('Menu Informações')

        print('\n 1 - consultar produto')
        print('\n 2 - consultar lista')
        print('\n 3 - consultar tudo ')
        print('\n 4 - voltar')

        opcao  = pedir_numero('Escolha uma opção: ')

        if opcao == 1:

            nome= pedir_nome('digite o nome do produto: ')
            local = onde_esta(nome,em_ruptura,proximo_a_ruptura)

            if local is None:

                print(f'O {nome} não está cadastrado')

            else:

                print(f'O {nome} está cadastrado em {local}')

            pausa()

        elif opcao == 2:
            em_construcao()

        elif opcao == 3:
            em_construcao()

        elif opcao == 4:

            break

        else:

            print('Entrada invalida! Escolha uma opção do menu')

def menu_adicionar(em_ruptura,proximo_a_ruptura):

    while True:

        mostrar_cabecalho('Menu Adicionar')

        print('\n 1 - adicionar em ruptura')
        print('\n 2 - adicionar proximo a ruptura ')
        print('\n 3 - adicionar proximo a validade ')
        print('\n 4 - voltar')

        opcao  = pedir_numero('Escolha uma opção: ')

        if opcao == 1:
            em_construcao()

        elif opcao == 2:
            em_construcao()

        elif opcao == 3:
            em_construcao()

        elif opcao == 4:

            break

        else:

            print('Entrada invalida! Escolha uma opção do menu')

def menu_excluir(em_ruptura,proximo_a_ruptura):

    while True:

        mostrar_cabecalho('Menu Excluir')

        print('\n 1 - excluir em ruptura')
        print('\n 2 - excluir proximo a ruptura ')
        print('\n 3 - excluir proximo a validade ')
        print('\n 4 - voltar')

        opcao  = pedir_numero('Escolha uma opção: ')

        if opcao == 1:
            em_construcao()

        elif opcao == 2:
            em_construcao()

        elif opcao == 3:
            em_construcao()

        elif opcao == 4:

            break

        else:

            print('Entrada invalida! Escolha uma opção do menu')

if __name__ == '__main__':
    from armazenamento import carregar_estoque

    em_ruptura, proximo_a_ruptura = carregar_estoque()
    menu_principal(em_ruptura, proximo_a_ruptura)
