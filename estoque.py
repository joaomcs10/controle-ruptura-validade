from entrada import perguntar_sim_ou_nao, pedir_nome, pedir_numero


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

def cadastrar_produto(lista,tipo,descricao):
    """Cadastra produtos no sistema"""

    while True:

        produto = pedir_nome("Digite o nome do produto: ")

        valor = pedir_numero(descricao)

        print(f'confirme os dados :\n produto: {produto}\n {tipo}: {valor}')

        confirmacao = perguntar_sim_ou_nao('Esta correto?(sim/não)\n')

        if confirmacao == 'sim':

            lista.append({'produto': produto, tipo: valor})

            print('Produto cadastrado com sucesso!')

            break

        print('Cadastro descartado. Digite os dados novamente')

