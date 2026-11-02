import json

def salvar_estoque(em_ruptura,proximo_a_ruptura):
    """Gravar as duas listas no estoque.json"""

    dados = {
        'em_ruptura': em_ruptura,
        'proximo_a_ruptura': proximo_a_ruptura
    }

    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)



