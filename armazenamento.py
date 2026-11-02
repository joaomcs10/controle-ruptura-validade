import os
import json

def salvar_estoque(em_ruptura,proximo_a_ruptura):
    """Gravar as duas listas no estoque.json"""

    dados = {
        'em_ruptura': em_ruptura,
        'proximo_a_ruptura': proximo_a_ruptura
    }

    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def carregar_estoque():
    """Lê estoque.json e devolve as duas listas. Sem arquivo. devolve as duas listas vazias"""
    if not os.path.isfile('estoque.json'):

        return [], []

    with open('estoque.json', 'r', encoding='utf-8') as arquivo:

        dados = json.load(arquivo)

    return dados['em_ruptura'], dados['proximo_a_ruptura']

