def mostrar_tabela(titulo, lista, chave, rotulo):
    """Mostra uma lista de produtos em formato de tabela."""
    print(titulo)

    print(f'{"PRODUTO":<20}  {rotulo}')

    print('-' * 36)

    if not lista:
        print('Nenhum produto cadastrado.')
    for item in lista:
        print(f'{item["produto"]:<20}  {item[chave]}')


def em_construcao():
    """Devolve uma mensagem sobre uma funcionalidade em construção."""

    print('Esta opçao ainda está em construção')


def mostrar_cabecalho(titulo):
    largura = 60

    print("-+" * 30)

    print(titulo.center(largura))

    print('-+' * 30)

def pausar():
    """Espera o usuario aperta Enter, para dar tempo de ler o resultado"""

    input('\n Aperte enter para continuar...')