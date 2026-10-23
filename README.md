# Controle de Ruptura e Validade

Ferramenta em Python para registrar produtos em ruptura e próximos da ruptura, pensada para a rotina de promotores de merchandising.

## O problema

No dia a dia da loja, os sistemas de controle costumam perguntar *se* existe produto em ruptura ou perto do vencimento, mas não guardam *qual* produto, *quanto tempo* ele está em falta ou *quantas unidades* restam. Sem esse detalhe, não existe uma lista para agir.

Este projeto nasceu dessa lacuna: registrar apenas o que está em risco e deixar uma lista clara para quem precisa tomar uma decisão.

> Projeto independente, feito para estudo e portfólio. Não tem relação com nenhum sistema oficial de empresa e usa apenas dados fictícios.

## O que já funciona (v1, em andamento)

- Cadastro de produtos **em ruptura** (nome e dias em falta)
- Cadastro de produtos **próximos da ruptura** (nome e quantidade em estoque)
- Validação das entradas: respostas sim/não, números inteiros e nome não vazio
- Confirmação dos dados antes de gravar cada registro
- Salvamento dos registros em arquivo JSON (`estoque.json`)

## Como rodar

Requisitos: Python 3.

```
python main.py
```

O programa faz as perguntas no terminal e, ao final, grava os registros em `estoque.json`.

## Estrutura dos dados

Cada produto é um dicionário, e as listas guardam todos os registros:

```json
{
    "em_ruptura": [
        {"produto": "exemplo A", "dias": 5}
    ],
    "proximo_a_ruptura": [
        {"produto": "exemplo B", "quantidade": 8}
    ]
}
```

## Roadmap

| Versão | O que entra | Tecnologias |
|---|---|---|
| v1 | Terminal: carregar o JSON ao abrir, tabela de produtos, menu | Python, JSON |
| v1.5 | Refatoração com classes | POO |
| v2 | Controle de validade e banco de dados | SQL |
| v3 | Páginas web para uso no celular | Flask |
| v4 | Relatórios em Excel | Pandas |

## O que estou aprendendo com o projeto

Funções, validação de entrada, listas de dicionários, leitura e escrita de arquivos JSON e versionamento com Git.
