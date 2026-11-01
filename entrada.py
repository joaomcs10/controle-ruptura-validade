def perguntar_sim_ou_nao(pergunta):
    """Pergunta ao usuário e só aceita sim, nao ou não. Devolve a resposta em minúsculas."""
    digitado = input(pergunta).strip().lower()

    # repete o loop ate a resposta ser valida, nao quebrando o codigo caso seja digitado outra palavra
    while digitado not in ['sim', 'nao','não']:

        print('Resposta invalida! digite sim ou nao')

        digitado = input(pergunta).strip().lower()

    return digitado

def pedir_numero(pergunta):
    """Pede um numero inteiro e so aceita digitos"""
    valor = input(pergunta).strip()

    while not valor.isdigit():

        print('Resposta invalida! digite apenas numero')

        valor = input(pergunta).strip()

    return int(valor)


def pedir_nome(pergunta):
    """Impede que seja deixado em branco a entrada"""

    nome = input(pergunta).strip()

    while nome == '':

        print('O nome nao pode ficar vazio')

        nome = input(pergunta).strip()

    return nome


def mostrar_tabela(titulo, lista, chave, rotulo):
    """Mostra uma lista de produtos em formato de tabela."""
    print(titulo)

    print(f'{"PRODUTO":<20}  {rotulo}')

    print('-' * 36)

    if not lista:

        print('Nenhum produto cadastrado.')
    for item in lista:

        print(f'{item["produto"]:<20}  {item[chave]}')

