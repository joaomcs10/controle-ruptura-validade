from armazenamento import carregar_estoque
from menu import menu_principal

def main():

    em_ruptura,proximo_a_ruptura = carregar_estoque()
    menu_principal(em_ruptura,proximo_a_ruptura)

if __name__ == '__main__':
    main()