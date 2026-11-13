from entrada import perguntar_sim_ou_nao, pedir_nome, pedir_numero
from exibicao import pausar

def remover_item(lista, nome):
    for item in lista:

        if item['produto'].lower() == nome.lower():

            confirmar = perguntar_sim_ou_nao(f"Deseja realmente remover {item['produto']}(sim/não)?")

            if confirmar == 'sim':
                lista.remove(item)

                print('Item removido com sucesso.')

                return item

            print('Remoção cancelada.')

            return None

    print(f'O {nome} não consta no sistema')

    return None

def cadastrar_produto(em_ruptura,proximo_a_ruptura,tipo,descricao):
    """Cadastra produto recusando produtos que ja existem em outra lista"""

    destino = proximo_a_ruptura if tipo == 'quantidade' else em_ruptura

    while True:

        produto = pedir_nome('Digite o nome do produto ou "voltar" para sair: ')

        local = onde_esta(produto, em_ruptura, proximo_a_ruptura)

        if produto.lower() == 'voltar':

            return None

        if local is not None:

            print(f'{produto} ja existe na lista {local}.')

            continue

        valor = pedir_numero(descricao)

        print(f'confirme os dados :\n produto: {produto}\n {tipo}: {valor}')

        confirmacao = perguntar_sim_ou_nao('Esta correto?(sim/não)\n')

        if confirmacao == 'sim':

            destino.append({'produto': produto, tipo: valor})

            return produto

        print('Cadastro descartado. Digite os dados novamente')

def existe_na_lista(lista,produto):
    """Devolve True se ja existe um produto com esse nome na lista"""

    return any(item['produto'].lower() == produto.lower() for item in lista)


def onde_esta(nome,em_ruptura, proximo_a_ruptura):
    """Devolve 'Em ruptura', 'Proximo a ruptura' ou None, conforme a lista que o nome está.''"""

    if existe_na_lista(em_ruptura,nome):

        return 'Em ruptura'

    if existe_na_lista(proximo_a_ruptura,nome):

        return 'proximo a ruptura'

    return None