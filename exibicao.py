def mostrar_tabela(titulo, lista, chave, rotulo):
    """Mostra uma lista de produtos em formato de tabela."""
    print(titulo)

    print(f'{"PRODUTO":<20}  {rotulo}')

    print('-' * 36)

    if not lista:

        print('Nenhum produto cadastrado.')
    for item in lista:

        print(f'{item["produto"]:<20}  {item[chave]}')

