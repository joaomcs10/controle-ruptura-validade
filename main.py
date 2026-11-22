from armazenamento import carregar_estoque
from menu import menu_principal
from exibicao import pausar

def main():

    em_ruptura,proximo_a_ruptura, aviso = carregar_estoque()

    if aviso is not None:

        print(f'Aviso: {aviso}')
        pausar()

    menu_principal(em_ruptura,proximo_a_ruptura)

if __name__ == '__main__':
    main()
