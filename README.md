# Controle de Ruptura e Validade

Ferramenta em Python para registrar produtos em ruptura e próximos da ruptura, pensada para a rotina de promotores de merchandising.

## O problema

No dia a dia da loja, os sistemas de controle costumam perguntar *se* existe produto em ruptura ou perto do vencimento, mas não guardam *qual* produto, *quanto tempo* ele está em falta ou *quantas unidades* restam. Sem esse detalhe, não existe uma lista para agir.

Este projeto nasceu dessa lacuna: registrar apenas o que está em risco e deixar uma lista clara para quem precisa tomar uma decisão.

> Projeto independente, feito para estudo e portfólio. Não tem relação com nenhum sistema oficial de empresa e usa apenas dados fictícios.

## O que já funciona (v1.1)

Programa de terminal com menu principal e submenus:

- **Consultar informações**: buscar um produto (mostra em qual lista ele está), ver uma lista ou ver tudo, em formato de tabela
- **Adicionar**: produtos **em ruptura** (nome e dias em falta) e **próximos da ruptura** (nome e quantidade em estoque), com confirmação dos dados antes de gravar
- **Excluir**: remover um produto de uma das listas, com confirmação
- **Contagem automática dos dias em ruptura**: o promotor informa há quantos dias o produto está em falta, o programa guarda a *data de início* e calcula os dias toda vez que a tabela é mostrada. No dia seguinte, o mesmo produto aparece com um dia a mais, sem ninguém digitar nada
- Validação das entradas: respostas sim/não, números inteiros e nome do produto (não pode ficar vazio, aceita apenas letras, números, espaço e hífen, e precisa de pelo menos uma letra)
- **Checagem de nome repetido** nas duas listas, informando em qual delas o produto já está
- Possibilidade de desistir de um cadastro ou de uma exclusão digitando `voltar`
- Os dados são gravados em `estoque.json` a cada cadastro ou exclusão e carregados ao abrir o programa
- Se o `estoque.json` estiver vazio ou corrompido, o programa avisa e inicia com as listas vazias, em vez de quebrar

As opções de validade aparecem nos menus, mas ainda estão em construção.

## Como rodar

Requisitos: Python 3.

```
python main.py
```

> Arquivos `estoque.json` criados por versões anteriores à v1.1 usam outro formato para a ruptura e devem ser apagados antes de rodar.

## Organização do código

Cada arquivo tem uma responsabilidade:

| Arquivo | O que faz |
|---|---|
| `main.py` | Carrega os dados e abre o menu |
| `menu.py` | Menus e submenus: fluxo de cada tela |
| `entrada.py` | Pede dados ao usuário e valida as respostas |
| `exibicao.py` | Mostra os dados na tela (tabelas, cabeçalho, pausa) |
| `estoque.py` | Regras das listas: cadastrar, remover, localizar e calcular os dias em ruptura |
| `armazenamento.py` | Lê e grava o `estoque.json` |

## Estrutura dos dados

Cada produto é um dicionário. Na ruptura, o arquivo guarda a **data de início** (formato ISO, `aaaa-mm-dd`), e os dias são calculados ao mostrar:

```json
{
    "em_ruptura": [
        {"produto": "exemplo A", "data_inicio": "2026-11-17"}
    ],
    "proximo_a_ruptura": [
        {"produto": "exemplo B", "quantidade": 8}
    ]
}
```

## Decisões de projeto

**Guardar a data, e não o número de dias.** Um número de dias fica congelado no arquivo. A data de início não muda, e os dias são calculados na hora de mostrar. O promotor continua digitando os dias, e o programa converte em data (`hoje - dias`), o que permite corrigir um erro apenas cadastrando de novo.

**Catálogo fixo de produtos (planejado).** Hoje o promotor digita o nome do produto, e cada produto vive em uma de duas listas. A evolução planejada é um catálogo fixo: cada produto existe uma única vez e tem uma **situação** (normal, próximo da ruptura ou em ruptura), e o promotor escolhe o produto numa lista em vez de digitar.

Por causa disso, **não foi implementado** o movimento de um produto entre as listas nem a edição de dias ou quantidade. Com o catálogo, isso passa a ser apenas mudar a situação do produto, e investir nisso agora seria retrabalho. O catálogo combina com a etapa do banco de dados, em que a situação vira uma coluna da tabela de produtos.

**Alerta inicial adiado.** Um aviso ao abrir o programa, mostrando apenas o que exige ação, será construído junto com a versão web, usando as datas para priorizar vencidos e itens críticos. Um alerta de terminal seria descartado nessa migração.

## Limitações conhecidas

- Para mover um produto de uma lista para outra, ou corrigir os dias ou a quantidade, é preciso excluí-lo e cadastrá-lo de novo. Será resolvido com o catálogo de produtos.
- Controle de validade ainda não implementado.
- Não há aviso ao abrir o programa (ver decisões de projeto).
- Se o `estoque.json` estiver corrompido, o programa inicia vazio e o próximo salvamento sobrescreve o arquivo; não há cópia de segurança.

## Roadmap

| Versão | O que entra | Tecnologias |
|---|---|---|
| v1.0 | Menu com consulta, cadastro e exclusão | Python, JSON |
| v1.1 | Contagem automática dos dias em ruptura (esta versão) | datetime |
| v1.2 | Controle de validade: data de vencimento, preço, rebaixa, retirada e níveis de urgência | datetime |
| v1.5 | Refatoração com classes | POO |
| v2 | Catálogo de produtos e banco de dados | SQL |
| v3 | Páginas web para uso no celular, com painel de alertas | Flask |
| v4 | Relatórios em Excel | Pandas |

## O que estou aprendendo com o projeto

Funções, validação de entrada, listas de dicionários, separação do código em módulos, leitura e escrita de arquivos JSON, tratamento de erros, trabalho com datas e versionamento com Git.