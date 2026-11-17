# Controle de Ruptura e Validade

Ferramenta em Python para registrar produtos em ruptura e próximos da ruptura, pensada para a rotina de promotores de merchandising.

## O problema

No dia a dia da loja, os sistemas de controle costumam perguntar *se* existe produto em ruptura ou perto do vencimento, mas não guardam *qual* produto, *quanto tempo* ele está em falta ou *quantas unidades* restam. Sem esse detalhe, não existe uma lista para agir.

Este projeto nasceu dessa lacuna: registrar apenas o que está em risco e deixar uma lista clara para quem precisa tomar uma decisão.

> Projeto independente, feito para estudo e portfólio. Não tem relação com nenhum sistema oficial de empresa e usa apenas dados fictícios.

## O que já funciona (v1)

Programa de terminal com menu principal e submenus:

- **Consultar informações**: buscar um produto (mostra em qual lista ele está), ver uma lista ou ver tudo, em formato de tabela
- **Adicionar**: produtos **em ruptura** (nome e dias em falta) e **próximos da ruptura** (nome e quantidade em estoque), com confirmação dos dados antes de gravar
- **Excluir**: remover um produto de uma das listas, com confirmação
- Validação das entradas: respostas sim/não, números inteiros e nome do produto (não pode ficar vazio, aceita apenas letras, números, espaço e hífen, e precisa de pelo menos uma letra)
- **Checagem de nome repetido** nas duas listas, informando em qual delas o produto já está
- Possibilidade de desistir de um cadastro ou de uma exclusão digitando `voltar`
- Os dados são gravados em `estoque.json` a cada cadastro ou exclusão e carregados ao abrir o programa

As opções de validade aparecem nos menus, mas ainda estão em construção.

## Como rodar

Requisitos: Python 3.

```
python main.py
```

## Organização do código

Cada arquivo tem uma responsabilidade:

| Arquivo | O que faz |
|---|---|
| `main.py` | Carrega os dados e abre o menu |
| `menu.py` | Menus e submenus: fluxo de cada tela |
| `entrada.py` | Pede dados ao usuário e valida as respostas |
| `exibicao.py` | Mostra os dados na tela (tabelas, cabeçalho, pausa) |
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

## Decisões de projeto

**Catálogo fixo de produtos (planejado).** Hoje o promotor digita o nome do produto, e cada produto vive em uma de duas listas. A evolução planejada é um catálogo fixo: cada produto existe uma única vez e tem uma **situação** (normal, próximo da ruptura ou em ruptura), e o promotor escolhe o produto numa lista em vez de digitar.

Por causa disso, **não foi implementado** o movimento de um produto entre as listas nem a edição de dias ou quantidade. Com o catálogo, isso passa a ser apenas mudar a situação do produto, e investir nisso agora seria retrabalho. O catálogo combina com a etapa do banco de dados, em que a situação vira uma coluna da tabela de produtos.

**Alerta inicial adiado.** Um aviso ao abrir o programa, mostrando apenas o que exige ação, será construído junto com a versão web, usando as datas para priorizar vencidos e itens críticos. Um alerta de terminal seria descartado nessa migração.

## Limitações conhecidas

- Para mover um produto de uma lista para outra, é preciso excluí-lo e cadastrá-lo de novo. Será resolvido com o catálogo de produtos.
- Os dias em ruptura são digitados e ficam fixos no arquivo; ainda não são contados automaticamente.
- Controle de validade ainda não implementado.
- Não há aviso ao abrir o programa (ver decisões de projeto).

## Roadmap

| Versão | O que entra | Tecnologias |
|---|---|---|
| v1 | Menu com consulta, cadastro e exclusão (esta versão) | Python, JSON |
| v1.5 | Refatoração com classes | POO |
| v2 | Datas com contagem automática de dias, controle de validade, catálogo de produtos e banco de dados | datetime, SQL |
| v3 | Páginas web para uso no celular, com painel de alertas | Flask |
| v4 | Relatórios em Excel | Pandas |

## O que estou aprendendo com o projeto

Funções, validação de entrada, listas de dicionários, separação do código em módulos, leitura e escrita de arquivos JSON e versionamento com Git.