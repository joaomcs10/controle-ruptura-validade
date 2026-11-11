# Controle de Ruptura e Validade

Ferramenta em Python para registrar produtos em ruptura e próximos da ruptura, pensada para a rotina de promotores de merchandising.

## O problema

No dia a dia da loja, os sistemas de controle costumam perguntar *se* existe produto em ruptura ou perto do vencimento, mas não guardam *qual* produto, *quanto tempo* ele está em falta ou *quantas unidades* restam. Sem esse detalhe, não existe uma lista para agir.

Este projeto nasceu dessa lacuna: registrar apenas o que está em risco e deixar uma lista clara para quem precisa tomar uma decisão.

> Projeto independente, feito para estudo e portfólio. Não tem relação com nenhum sistema oficial de empresa e usa apenas dados fictícios.

## O que já funciona (v1, em andamento)

- Cadastro de produtos **em ruptura** (nome e dias em falta)
- Cadastro de produtos **próximos da ruptura** (nome e quantidade em estoque)
- Validação das entradas: respostas sim/não, números inteiros e nome do produto (letras, números, espaço e hífen, com pelo menos uma letra)
- Confirmação dos dados antes de gravar cada registro
- **Checagem de nome repetido** nas duas listas, informando em qual delas o produto já está
- Salvamento dos registros em arquivo JSON (`estoque.json`)
- Carregamento do `estoque.json` ao abrir, mostrando o que já estava registrado
- **Conferência ao abrir**: remover da ruptura o produto que chegou na loja e transferir para a ruptura o produto que deixou de estar "próximo"
- Exibição dos produtos em formato de tabela

## Como rodar

Requisitos: Python 3.

```
python main.py
```

O programa carrega o `estoque.json` (se existir), mostra as duas tabelas, faz a conferência, pede novos cadastros e grava tudo ao final.

## Organização do código

Cada arquivo tem uma responsabilidade:

| Arquivo | O que faz |
|---|---|
| `main.py` | Define a ordem do fluxo do programa |
| `entrada.py` | Pede dados ao usuário e valida as respostas |
| `exibicao.py` | Mostra os dados na tela (tabelas) |
| `estoque.py` | Regras das listas: cadastrar, remover e localizar produtos |
| `armazenamento.py` | Lê e grava o `estoque.json` |

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

## Limitações conhecidas

- Os dias em ruptura são digitados e ficam fixos no arquivo; ainda não são contados automaticamente.
- Os dados são gravados apenas ao final da execução.
- O fluxo é uma sequência fixa de perguntas, sem menu.
- Controle de validade ainda não implementado.

## Roadmap

| Versão | O que entra | Tecnologias |
|---|---|---|
| v1 | Perguntar se quer editar ou transferir um produto já registrado, e menu principal | Python, JSON |
| v1.5 | Refatoração com classes | POO |
| v2 | Datas com contagem automática de dias, controle de validade e banco de dados | datetime, SQL |
| v3 | Páginas web para uso no celular | Flask |
| v4 | Relatórios em Excel | Pandas |

## O que estou aprendendo com o projeto

Funções, validação de entrada, listas de dicionários, separação do código em módulos, leitura e escrita de arquivos JSON e versionamento com Git.