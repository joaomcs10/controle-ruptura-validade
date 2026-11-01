import json
import os
from entrada import perguntar_sim_ou_nao, pedir_nome, pedir_numero
from exibicao import mostrar_tabela
from estoque import remover_item

# os dois caminhos (com ou sem arquivo) terminam com as duas listas criadas
if os.path.exists('estoque.json'):

    print('Arquivo encontrado. Carregando dados..')
    print()

    with open('estoque.json','r',encoding='utf-8') as arquivo:

        dados = json.load(arquivo)

    # json.load devolve o dicionario salvo; cada chave em sua lista
    em_ruptura = dados['em_ruptura']
    proximo_a_ruptura = dados['proximo_a_ruptura']

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

    print('Ainda não existem dados salvos. Iniciando programa...')

    # primeira execução: começa com as listas vazias
    em_ruptura = []
    proximo_a_ruptura = []


resposta = perguntar_sim_ou_nao('existe algum produto em ruptura na sua loja?(sim/não) ')

# Executa a adição de dados caso a resposta seja sim
while resposta == 'sim':
    produto = pedir_nome('Digite o nome do produto: ')

    dias = pedir_numero('Digite quantos dias esta em ruptura:')

    print(f'confirme os dados: produto: {produto} em falta: {dias} dias')
    entrada = perguntar_sim_ou_nao('Esta correto?(sim/nao) ')

    if entrada == 'sim':

      # adiciona os dados a lista
      em_ruptura.append({'produto': produto, 'dias': dias})

      resposta = perguntar_sim_ou_nao('Existe mais algum produto em ruptura?(sim/nao) ')
    # caso o produto esteja incorreto não adiciona na lista e retorna para cadastrar outro produto
    else:

        print('Cadastro descartado. Digite os dados novamente')

resposta = perguntar_sim_ou_nao('Existe algum produto próximo a ruptura?(sim/nao) ')

while resposta == "sim":

    produto = pedir_nome('Digite o nome do produto: ')

    quantidade = pedir_numero('Digite a quantidade do produto no estoque: ')

    print(f'Confirme os dados :  produto: {produto} tem {quantidade} unidades em estoque')

    entrada = perguntar_sim_ou_nao('Esta correto ?(sim/nao) ')

    if entrada == 'sim':

        proximo_a_ruptura.append({'produto': produto, 'quantidade': quantidade})

        resposta = perguntar_sim_ou_nao('Existe mais algum produto próximo a ruptura?(sim/nao) ')

    else:

        print('Cadastro descartado. Digite os dados novamente')

print('Obrigado pela resposta')
mostrar_tabela('PRODUTOS EM RUPTURA', em_ruptura, 'dias', 'DIAS')
mostrar_tabela('PRODUTOS PRÓXIMOS DA RUPTURA', proximo_a_ruptura, 'quantidade', 'QUANTIDADE')

dados = {
    'em_ruptura': em_ruptura,
    'proximo_a_ruptura': proximo_a_ruptura
}

with open( 'estoque.json','w', encoding='utf-8' ) as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
