# Inteligência Comercial Geográfica para Energia Solar

Projeto acadêmico da disciplina de Análise de Dados e BI da UNIPÊ, ministrada pelo professor Daniel Brandão.

## Objetivo

Identificar oportunidades de prospecção para uma empresa de energia solar em Goiana e região, considerando municípios de Pernambuco e da Paraíba e os públicos residencial e empresarial.

## Contexto

Nossa equipe faz parte de uma empresa de desenvolvimento de software que possui um contrato para criar uma landing page para a empresa analisada.

Aproveitando esse contato, propomos um estudo com dados públicos para apoiar a escolha de municípios para futuras ações comerciais.

## Área de estudo

| Pernambuco | Paraíba |
|---|---|
| Goiana | Caaporã |
| Itambé | Pitimbu |
| Itapissuma | Alhandra |
| Igarassu | Pedras de Fogo |
| Ilha de Itamaracá | Conde |
| Abreu e Lima | João Pessoa |

A capacidade de atendimento desses municípios será confirmada com a empresa.

## Bases de dados

| Fonte | Dados | Situação |
|---|---|---|
| INPE — Atlas Brasileiro de Energia Solar | Irradiação anual e mensal e coordenadas das sedes municipais | Disponível |
| ANEEL — Geração Distribuída | Instalações fotovoltaicas, potência instalada e unidades consumidoras beneficiadas | Disponível em agregados municipais |
| IBGE — Estimativas populacionais | População estimada dos municípios em 2026 | Disponível |
| IBGE — Censo 2022 | Domicílios particulares permanentes ocupados | Coleta pendente |
| Receita Federal — CNPJ | Estabelecimentos ativos dos segmentos selecionados | Coleta pendente |
| ANEEL — Datas de conexão | Histórico de conexões fotovoltaicas por ano | Coleta pendente |

## Dashboard em Python

O dashboard será desenvolvido em Python, com a seguinte estrutura tecnológica proposta.

- **pandas** para carregar, integrar e tratar os dados.
- **Plotly** para criar gráficos e mapas interativos.
- **Streamlit** para construir a interface do dashboard.

### Funcionalidades previstas

- Filtros por município e estado.
- Indicadores de população e geração fotovoltaica.
- Mapa da distribuição geográfica dos indicadores.
- Comparação da irradiação solar entre municípios e meses.
- Comparação dos públicos residencial e empresarial após a complementação das bases.
- Apoio à definição de prioridades de prospecção.

## Organização dos arquivos

| Pasta | Conteúdo |
|---|---|
| `01_bases_recebidas` | Bases originais e documentação recebida |
| `02_base_integrada` | CSV municipal consolidado e campos preparados para complementação |
| `03_complementacao` | Cadastro de atendimento e rotina de processamento do histórico da ANEEL |
| `04_documentacao` | Fontes, orientações, limitações e dicionário dos campos adicionais |

## Importação dos dados

Os arquivos utilizam ponto e vírgula como delimitador e codificação UTF-8 com BOM.

Na base consolidada, os números decimais utilizam vírgula. Os recortes originais do INPE utilizam ponto decimal e exigem configuração correspondente na leitura.

O código IBGE deve ser tratado como texto. Campos vazios representam dados ainda não coletados e devem permanecer como valores ausentes.

## Limitações

- População, domicílios e estabelecimentos ajudam a dimensionar públicos para investigação. A demanda depende também de interesse, consumo de energia, condições financeiras e viabilidade técnica.
- Os dados do INPE representam referências históricas nas sedes municipais, com resolução aproximada de 10 km.
- Os indicadores da ANEEL mostram a presença registrada de geração distribuída.
- Instalações por mil habitantes não equivalem ao percentual de domicílios com energia solar.
- Unidades consumidoras beneficiadas não equivalem à quantidade de instalações.
- Cada indicador deverá apresentar sua fonte e seu período de referência.
- O uso da base do INPE deverá respeitar os créditos e as condições de reprodução informados pela instituição.

## Situação atual

As bases disponíveis permitem iniciar o dashboard com população, irradiação solar e geração fotovoltaica agregada por município.

### Próximas etapas

1. Coletar os dados de domicílios do Censo 2022.
2. Definir os segmentos empresariais prioritários com o cliente.
3. Coletar os estabelecimentos ativos por CNAE.
4. Obter o histórico de conexões fotovoltaicas.
5. Confirmar a área de atendimento da empresa.
6. Integrar e validar os dados.
7. Desenvolver o dashboard em Python.
