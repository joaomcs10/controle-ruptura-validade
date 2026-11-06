from entrada import perguntar_sim_ou_nao, pedir_nome
from exibicao import mostrar_tabela
from estoque import remover_item, cadastrar_produto
from armazenamento import salvar_estoque,carregar_estoque

em_ruptura, proximo_a_ruptura = carregar_estoque()

if em_ruptura or proximo_a_ruptura:

    print('Dados carregando...')
    print()

    # Mostra o que ja estava registrado antes de pedir produtos novos
    mostrar_tabela('PRODUTOS EM RUPTURA', em_ruptura, 'dias', 'DIAS')
    print()
    mostrar_tabela('PRODUTOS PRÓXIMOS DA RUPTURA', proximo_a_ruptura, 'quantidade', 'QUANTIDADE')
    print()

    checagem = perguntar_sim_ou_nao('Algum Produto da lista Em ruptura ja chegou na loja?(sim/não): ')

    while checagem == 'sim':

        nome = pedir_nome('Digite o nome do produto: ')

        remover_item(em_ruptura,nome)

        checagem = perguntar_sim_ou_nao('Mais algum produto saiu?(sim/não): ')

    checagem_2 = perguntar_sim_ou_nao('Algum Produto da lista Proximo a Ruptura entrou em ruptura?(sim/não): ')

    while checagem_2 == 'sim':

        nome = pedir_nome('Digite o nome do produto: ')

        removido = remover_item(proximo_a_ruptura,nome)

        if removido:

            em_ruptura.append({'produto':removido['produto'], 'dias': 1})

            print(f'{removido["produto"]} foi transferido para a lista de ruptura.')

        checagem_2 = perguntar_sim_ou_nao('Mais algum produto que entrou em ruptura?(sim/não)')

else:

    print('Nenhum produto registrado. Iniciando programa...')


resposta = perguntar_sim_ou_nao('Existe algum produto próximo a ruptura?(sim/nao) ')

while resposta == "sim":

    cadastrar_produto(proximo_a_ruptura,em_ruptura,'quantidade','Digite a quantidade no estoque: ' )

    resposta = perguntar_sim_ou_nao('Existe mais algum produto proximo a ruptura?(sim/nao): ')

resposta_2 = perguntar_sim_ou_nao('Exite  algum produto em ruptura?(sim/nao): ')

while resposta_2 == "sim":

    cadastrar_produto(em_ruptura,proximo_a_ruptura,'dias','Quantos dias esta em falta?: ')

    resposta_2 = perguntar_sim_ou_nao('Existe mais algum produto em ruptura?(sim/nao): ')


print('Obrigado pela resposta')
mostrar_tabela('PRODUTOS EM RUPTURA', em_ruptura, 'dias', 'DIAS')
mostrar_tabela('PRODUTOS PRÓXIMOS DA RUPTURA', proximo_a_ruptura, 'quantidade', 'QUANTIDADE')

salvar_estoque(em_ruptura,proximo_a_ruptura)