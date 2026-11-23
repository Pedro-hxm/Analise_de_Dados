# Inteligência Comercial Geográfica para Energia Solar — Ativa Solar

Projeto acadêmico da disciplina de **Análise de Dados e BI** do **UNIPÊ**, ministrada pelo professor Daniel Brandão. O estudo surgiu no contexto do contato da equipe com a Ativa Solar durante o desenvolvimento de uma landing page para a empresa.

## Objetivo do estudo

Comparar, com dados públicos, os 12 municípios do recorte de Pernambuco e Paraíba para apoiar uma triagem inicial de localidades que valha a pena investigar em futuras ações de prospecção da Ativa Solar. A análise é **exploratória**: não comprova demanda, não identifica clientes da Ativa Solar e não estima vendas ou faturamento da empresa.

## Área de estudo e municípios

O recorte se limita aos 12 municípios já definidos no projeto — seis em cada estado:

| Pernambuco | Paraíba |
|---|---|
| Abreu e Lima | Alhandra |
| Goiana | Caaporã |
| Igarassu | Conde |
| Ilha de Itamaracá | João Pessoa |
| Itambé | Pedras de Fogo |
| Itapissuma | Pitimbu |

O código IBGE de sete dígitos é a chave de integração das bases. A presença no recorte não confirma que a Ativa Solar atenda ao município; a confirmação da área atendida continua pendente.

## Perguntas de negócio

1. Entre os municípios do recorte com atendimento confirmado, onde há mais domicílios particulares permanentes ocupados e estabelecimentos ativos nos CNAEs definidos pela empresa, analisados separadamente?
2. Qual é a participação de cada município nos públicos residencial e empresarial da área atendida?
3. Como o GHI anual e mensal varia entre as sedes municipais?
4. Como as instalações fotovoltaicas e a potência registradas pela ANEEL se distribuem atualmente? A evolução anual será analisada se forem obtidos registros com datas de conexão.
5. Quais municípios e segmentos podem compor uma lista preliminar para validação comercial, considerando a área atendida, o tamanho dos públicos e os indicadores de GHI e ANEEL como contexto?

As perguntas, os dados e métricas necessários, o status e as limitações de cada análise estão organizados no documento editável [Perguntas de Negócio Revisadas](Documentação/Perguntas_de_Negocio_Revisadas.md).

## Fontes de dados e situação

| Fonte | Dados, período e unidade | Situação no repositório |
|---|---|---|
| **INPE/LABREN — Atlas Brasileiro de Energia Solar, 2ª edição (2017)** | GHI anual e mensal das sedes municipais, com médias diárias em **Wh/m².dia**. Estimativas da série histórica **1999–2015**, com resolução de aproximadamente **0,1° (cerca de 10 km)**. | **Disponível** para os 12 municípios, nos recortes estaduais e na base consolidada. É uma referência histórica das sedes municipais, não uma medição de telhados. O repositório também contém campos identificados como GTI10; confira os metadados antes de associar o rótulo a um ângulo fixo. |
| **ANEEL — empreendimentos de MMGD fotovoltaica** | Número de instalações, potência instalada agregada (**kW**) e unidades consumidoras que recebem créditos. Arquivo `ANEEL_MMGD_fotovoltaica_12_municipios_PE_PB_2026-11-10.csv`, baixado em **10/11/2026**; a fonte oficial é atualizada diariamente. | **Disponível** como agregado municipal dos 12 municípios na data do arquivo. É uma fotografia, não uma série histórica anual de conexões. |
| **IBGE — Estimativas de População 2026** | População municipal estimada, em **habitantes**, com referência em **01/07/2026**. | **Disponível** para os 12 municípios como contexto demográfico; não substitui a contagem de domicílios. |
| **IBGE — Censo 2022** | Domicílios particulares permanentes ocupados, em domicílios. | **Pendente de coleta e conferência** das categorias e unidades da tabela. A base integrada tem campos preparados, ainda vazios. |
| **Receita Federal — dados abertos do CNPJ** | Estabelecimentos ativos por CNAEs prioritários a definir com a empresa. | **Pendente**: os CNAEs ainda não foram definidos, e os estabelecimentos não foram coletados. Não há contagens nem data de referência no repositório. |
| **Ativa Solar — área de atendimento** | Confirmação dos municípios atendidos dentro do recorte. | **Pendente de confirmação da empresa**. O arquivo `atendimento_e_publico_alvo.csv` lista os 12 municípios, mas os campos de confirmação e CNAEs estão vazios. |
| **ANEEL — evolução anual** | Registros fotovoltaicos com datas de conexão para agregar instalações por município e ano. | **Pendente**: os dados de entrada com datas e a série anual não estão no repositório. Há uma rotina de processamento, ainda dependente desses registros. |

As fontes e os links consultados estão em `Base de dados/01_bases_recebidas/fontes_e_links.csv`. As decisões metodológicas, os dicionários e as limitações das fontes estão nos arquivos de metodologia e documentação da base.

## Limitações e cuidados de interpretação

- A estimativa populacional do IBGE não é uma medida de domicílios, consumidores elegíveis ou clientes potenciais. Não substitua os domicílios ocupados do Censo por população.
- Campos vazios de domicílios, CNAEs, atendimento e datas de referência indicam informação não coletada ou não confirmada; **não significam zero**.
- Os dados da ANEEL descrevem geração distribuída registrada nos municípios e não são clientes, instalações, vendas ou faturamento da Ativa Solar. Unidades consumidoras que recebem créditos não equivalem a instalações nem a clientes únicos.
- A presença de sistemas fotovoltaicos pode contextualizar a adoção e a concorrência, mas não mede demanda não atendida nem capacidade livre da rede. Baixa adoção solar, isoladamente, não comprova maior oportunidade comercial.
- O GHI do INPE é uma referência histórica da coordenada da sede municipal, baseada na série 1999–2015. Não mede telhados, terrenos ou imóveis específicos. As médias mensais descrevem sazonalidade histórica, não evolução entre anos.
- Indicadores por mil habitantes são razões descritivas; não correspondem ao percentual de domicílios com energia solar.
- A base não inclui, entre outros fatores, consumo e contas de energia, renda, intenção de compra, viabilidade de conexão, potencial de telhados, restrições locais, custos ou logística de atendimento. A triagem não aprova endereço, terreno ou projeto.
- Para uso do Atlas, atribua **LABREN / CCST / INPE — Brasil** e observe os metadados: a reprodução ou cópia para fins comerciais requer autorização expressa do CCST/INPE.

## Situação atual e dados pendentes

**Bases e qualidade disponíveis:** as bases de INPE, ANEEL e IBGE foram integradas pelo código IBGE para os 12 municípios. A base tratada, o dicionário e o relatório de qualidade (`Base de dados/05_bases_tratadas/`) registram conferências de cobertura, unicidade, junções, ausências e tipos. O relatório, executado em **20/11/2026**, documenta também o recálculo dos indicadores de instalações e potência por mil habitantes, sem divergências após arredondamento a duas casas. Os campos complementares de domicílios, estabelecimentos por CNAE e atendimento permanecem vazios para todos os municípios.

**Notebook de limpeza:** `Notebooks/Limpeza_Inicial_DEILAS_Ativa_Solar.ipynb` é dedicado à limpeza, validação e integração das bases e à exportação da base tratada, do dicionário e do relatório de qualidade.

**Notebook exploratório:** `Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb` é separado da limpeza. A análise permanece **parcial**, não concluída. Já inclui comparações de GHI anual e mensal entre os municípios, distribuição atual de instalações e potência da ANEEL, razões por mil habitantes e associação descritiva entre população e instalações. Essas análises são exploratórias: não demonstram causalidade, demanda ou oportunidade comercial da Ativa Solar.

### Links dos notebooks no Google Colab

Use os links abaixo para abrir cada notebook no Google Colab.

| Notebook | Link do Colab |
|---|---|
| [Limpeza e integração](Notebooks/Limpeza_Inicial_DEILAS_Ativa_Solar.ipynb) | [Abrir no Colab](https://colab.research.google.com/drive/1ZJNjEsiSUUG9xCWeeX6IvFgJl_RWmPI7?usp=sharing) |
| [Análise exploratória](Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb) | [Abrir no Colab](https://colab.research.google.com/drive/1RvH-tCXihHmVWonrlx2fSAdK0dh8fv9s#scrollTo=load-treated-base) |

**Ainda pendente:** coletar e conferir os domicílios ocupados do Censo 2022; definir os CNAEs com a empresa e obter as contagens de estabelecimentos ativos; confirmar a área atendida; e obter registros ANEEL com datas de conexão para eventual evolução anual. Sem os dados de público e atendimento, não é possível concluir as comparações residenciais e empresariais nem formular a lista preliminar da pergunta 5. O projeto também não definiu ponderação nem município vencedor.

## Dashboard planejada

A dashboard é uma etapa **planejada**, ainda não implementada no repositório. A proposta é desenvolvê-la em **Python**, com **pandas**, **Plotly** e **Streamlit**, para comparar os municípios por meio de filtros, mapas e gráficos de públicos, GHI e indicadores da ANEEL. As análises dos públicos e a lista preliminar dependem da confirmação de atendimento e da coleta dos dados pendentes. Uma evolução anual da ANEEL só poderá ser incluída se forem obtidos registros com datas de conexão.

## Organização do repositório

| Caminho | Conteúdo |
|---|---|
| `Base de dados/01_bases_recebidas/` | Bases originais, recortes, metodologia, fontes e links consultados. |
| `Base de dados/02_base_integrada/` | Base municipal integrada, com campos preparados para complementação. |
| `Base de dados/03_complementacao/` | Cadastro de atendimento e público-alvo e rotina para processar registros históricos da ANEEL quando obtidos. |
| `Base de dados/04_documentacao/` | Fontes de complementação e dicionário dos campos pendentes. |
| `Base de dados/05_bases_tratadas/` | Base integrada limpa, dicionário e relatório de qualidade. |
| `Notebooks/` | Notebooks separados de limpeza, validação, integração e exportação e de análise exploratória. |
| `Documentação/` | Entregas acadêmicas, PDF da primeira entrega, DOCX de limpeza e análise inicial e [perguntas de negócio revisadas](Documentação/Perguntas_de_Negocio_Revisadas.md). |

Os CSVs tabulares usam UTF-8 com BOM e ponto e vírgula como separador. As bases integradas e tratadas usam vírgula decimal; os recortes originais do INPE usam ponto decimal. Trate o código IBGE como texto e preserve campos vazios como ausências.
