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
- Não existem usuários nem perfis: qualquer pessoa que abre o programa pode alterar tudo.
- Não há testes automatizados (planejado com `pytest`).

## Planejamento das versões v2 e v3 (ainda não implementado)

Esta seção descreve o desenho previsto. Nada disto existe no código atual.

### Usuários e hierarquia

O sistema terá usuários com perfis e uma hierarquia em árvore, em dois ramos paralelos. Cada pessoa tem **um chefe direto**:

```
Administrador geral
 ├── Supervisor de promotoria → Líder → Promotor
 └── Administrador de vendas (atua somente no ramo de vendas)
       └── Supervisor de vendas → Líder de vendas → Vendedor
```

Os dois ramos cabem em uma única tabela de usuários, com uma coluna que aponta para o chefe direto e outra que indica o ramo (promotoria ou vendas).

### Permissões: o que pode fazer × sobre quais dados

| Ramo | Perfis | Pode | Enxerga |
|---|---|---|---|
| Promotoria | Administrador, supervisor, líder e promotor | Ler e alterar | A própria subárvore e as lojas da rota |
| Vendas | Vendedor, líder e supervisor de vendas | Somente ler os dados dos promotores | As lojas da rede que atendem: alertas, promotores do dia, responsáveis e histórico |

- Supervisores e líderes cadastram e excluem as pessoas da própria equipe (no ramo de vendas, o supervisor cuida dos líderes e o líder cuida dos vendedores).
- O administrador de vendas gerencia apenas o ramo de vendas e não altera nada da promotoria.
- Quem altera dados de ruptura e validade são os responsáveis pelos promotores.

### Rotas e redes

- **Promotor**: tem uma **rota**, que liga o promotor às lojas, com dia da semana e frequência (incluindo alternância). Uma loja pode ter um ou mais promotores fixos, e a **cobertura** é temporária e não ocupa vaga fixa.
- **Vendedor**: não tem rota. Ele consulta **toda a rede** que atende, escolhe a loja que vai visitar e vê quem estará lá naquele dia.
- **Loja fora da rota**: o promotor pode sinalizar que foi a uma loja fora da rota, e o aviso chega ao líder e ao supervisor, que são encontrados subindo a árvore a partir do promotor.

### Histórico de alterações

Cada registro de ruptura, próximo da ruptura e validade guardará **quem sinalizou, em que dia e quem alterou depois**. O histórico é uma tabela própria, com uma linha por alteração, e por isso o sistema **marca como retirado em vez de apagar**.

### Entidades previstas

Usuário, rede, loja, rota do promotor, vínculo do vendedor com a rede, registro (ruptura, próximo da ruptura e validade), histórico do registro e sinalização de fora de rota. Senhas serão guardadas com hash, nunca em texto.

### Decisões em aberto

1. A alternância de visitas é por **semana** (por exemplo, toda terça de duas em duas semanas) ou por **dias seguidos** alternados?
2. O supervisor de promotoria também cadastra e exclui líderes?
3. Existe um administrador só da promotoria, ou o administrador geral cobre os dois ramos?
4. Um vendedor pode atender mais de uma rede?
5. O líder de vendas vê o histórico de todas as redes da equipe ou só das que acompanha diretamente?

## Roadmap

| Versão | O que entra | Tecnologias |
|---|---|---|
| v1.0 | Menu com consulta, cadastro e exclusão | Python, JSON |
| v1.1 | Contagem automática dos dias em ruptura (esta versão) | datetime |
| v1.2 | Controle de validade: data de vencimento, preço, rebaixa, retirada e níveis de urgência | datetime |
| v1.5 | Refatoração com classes | POO |
| v2.0 | Catálogo de produtos e banco de dados | SQL |
| v2.1 | Usuários, hierarquia e ramos | SQL |
| v2.2 | Redes, lojas e rotas | SQL |
| v3 | Páginas web para uso no celular: login, perfis, telas de leitura, painel de alertas e aviso de loja fora da rota | Flask |
| v4 | Relatórios em Excel | Pandas |

## O que estou aprendendo com o projeto

Funções, validação de entrada, listas de dicionários, separação do código em módulos, leitura e escrita de arquivos JSON, tratamento de erros, trabalho com datas e versionamento com Git.