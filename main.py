import json
import os


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
