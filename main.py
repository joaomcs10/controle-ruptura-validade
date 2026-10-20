import json

def perguntar_sim_ou_nao(pergunta):
    """strip e lower: retira os espaços antes e depois, padroniza a palavra para minuscula"""
    resposta = input(pergunta).strip().lower()

    # repete o loop ate a resposta ser valida, nao quebrando o codigo caso seja digitado outra palavra
    while resposta not in ['sim', 'nao','não']:

        print('Resposta invalida! digite sim ou nao')

        resposta = input(pergunta).strip().lower()

    return resposta


def pedir_numero(pergunta):
    """Pede um numero inteiro e so aceita digitos"""
    valor = input(pergunta).strip()

    while not valor.isdigit():

        print('Resposta invalida! digite apenas numero')

        valor = input(pergunta).strip()

    return int(valor)


def pedir_nome(pergunta):
    """Impede que seja deixado em branco a entrada"""

    resposta = input(pergunta).strip()

    while resposta == '':

        print('O nome nao pode ficar vazio')

        resposta = input(pergunta).strip()

    return resposta


# lista de dicionario vazia que recebera os dados pedidos
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
print('Produtos em Ruptura')
print(em_ruptura)
print('Produtos Próximos a Ruptura')
print(proximo_a_ruptura)

dados = {
    'em_ruptura': em_ruptura,
    'proximo_a_ruptura': proximo_a_ruptura
}

with open( 'estoque.json','w', encoding='utf-8' ) as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
