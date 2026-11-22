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
    """Devolve duas listas e um aviso. O aviso e None se esta tudo certo"""
    if not os.path.isfile('estoque.json'):

        return [], [], None

    try:

        with open('estoque.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

    except json.JSONDecodeError:

        return [], [], 'O estoque.jason está vazio ou corrompido. Iniciando com listas vazias'

    return dados['em_ruptura'], dados['proximo_a_ruptura'], None

