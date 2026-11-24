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

1. Como os valores anuais históricos de GHI se comparam entre as sedes dos 12 municípios?
2. Como os valores médios diários mensais de GHI variam entre as sedes dos 12 municípios ao longo do ano?
3. Como se distribuem, entre os 12 municípios, as instalações fotovoltaicas e a potência agregada registradas pela ANEEL?
4. Como variam, entre os municípios, as razões de instalações e de potência fotovoltaica registradas pela ANEEL por 1.000 habitantes estimados?
5. Que associação descritiva existe entre a população municipal estimada e o número de instalações fotovoltaicas registradas pela ANEEL nos 12 municípios?

As cinco perguntas têm resultados salvos no notebook exploratório. Para cada uma, a equipe documentou a métrica, o resultado observado, a célula onde conferi-lo e os limites de interpretação em [Perguntas de Negócio Revisadas](Documentação/Perguntas_de_Negocio_Revisadas.md).

## Fontes de dados e situação

| Fonte | Dados, período e unidade | Situação no repositório |
|---|---|---|
| **INPE/LABREN — Atlas Brasileiro de Energia Solar, 2ª edição (2017)** | GHI anual e mensal das sedes municipais, com médias diárias em **Wh/m².dia**. Estimativas da série histórica **1999–2015**, com resolução de aproximadamente **0,1° (cerca de 10 km)**. | **Disponível** para os 12 municípios, nos recortes estaduais e na base consolidada. É uma referência histórica das sedes municipais, não uma medição de telhados. O repositório também contém campos identificados como GTI10; confira os metadados antes de associar o rótulo a um ângulo fixo. |
| **ANEEL — empreendimentos de MMGD fotovoltaica** | Número de instalações, potência instalada agregada (**kW**) e unidades consumidoras que recebem créditos. Arquivo `ANEEL_MMGD_fotovoltaica_12_municipios_PE_PB_2026-11-10.csv`, baixado em **10/11/2026**; a fonte oficial é atualizada diariamente. | **Disponível** como agregado municipal dos 12 municípios na data do arquivo. É uma fotografia, não uma série histórica anual de conexões. |
| **IBGE — Estimativas de População 2026** | População municipal estimada, em **habitantes**, com referência em **01/07/2026**. | **Disponível** para os 12 municípios como contexto demográfico; não substitui a contagem de domicílios. |
| **IBGE — Censo 2022** | Domicílios particulares permanentes ocupados, em domicílios. | **Não coletado; fora das perguntas atuais.** Necessário para uma futura análise do público residencial por domicílios, não para as cinco perguntas deste README. |
| **Receita Federal — dados abertos do CNPJ** | Estabelecimentos ativos por CNAEs prioritários. | **Não coletados; fora das perguntas atuais.** Os CNAEs ainda não foram definidos; esses dados seriam necessários para uma futura análise do público empresarial. |
| **Ativa Solar — área de atendimento** | Confirmação dos municípios atendidos dentro do recorte. | **Não confirmada; fora das perguntas atuais.** O arquivo `atendimento_e_publico_alvo.csv` lista os 12 municípios, mas os campos de confirmação e CNAEs estão vazios. O recorte não deve ser confundido com a cobertura da empresa. |
| **ANEEL — evolução anual** | Registros fotovoltaicos com datas de conexão para agregar instalações por município e ano. | **Não disponível; fora das perguntas atuais.** O conjunto atual analisa apenas a fotografia municipal de 10/11/2026. Há uma rotina de processamento, ainda dependente de registros com datas. |

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

## Situação atual e possíveis ampliações futuras

**Bases e qualidade disponíveis:** as bases de INPE, ANEEL e IBGE foram integradas pelo código IBGE para os 12 municípios. A base tratada, o dicionário e o relatório de qualidade (`Base de dados/05_bases_tratadas/`) registram conferências de cobertura, unicidade, junções, ausências e tipos. O relatório, executado em **20/11/2026**, documenta também o recálculo dos indicadores de instalações e potência por mil habitantes, sem divergências após arredondamento a duas casas. Os campos complementares de domicílios, estabelecimentos por CNAE e atendimento permanecem vazios para todos os municípios.

**Notebook de limpeza:** `Notebooks/Limpeza_Inicial_DEILAS_Ativa_Solar.ipynb` é dedicado à limpeza, validação e integração das bases e à exportação da base tratada, do dicionário e do relatório de qualidade.

**Notebook exploratório:** `Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb` é separado da limpeza. Ele contém as cinco análises correspondentes às perguntas deste README: GHI anual e mensal, distribuição atual de instalações e potência da ANEEL, razões por mil habitantes e associação descritiva entre população e instalações. As nove células de código têm contagens de execução e saídas salvas. Esses resultados descrevem os dados dos 12 municípios; não demonstram causalidade, demanda ou oportunidade comercial da Ativa Solar.

### Links dos notebooks no Google Colab

Use os links abaixo para abrir cada notebook no Google Colab.

| Notebook | Link do Colab |
|---|---|
| [Limpeza e integração](Notebooks/Limpeza_Inicial_DEILAS_Ativa_Solar.ipynb) | [Abrir no Colab](https://colab.research.google.com/drive/1ZJNjEsiSUUG9xCWeeX6IvFgJl_RWmPI7?usp=sharing) |
| [Análise exploratória](Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb) | [Abrir no Colab](https://colab.research.google.com/drive/1RvH-tCXihHmVWonrlx2fSAdK0dh8fv9s#scrollTo=load-treated-base) |

**Escopo respondível sem novas coletas:** as cinco perguntas atuais podem ser respondidas com as bases tratadas e as saídas salvas no notebook exploratório. Domicílios do Censo 2022, estabelecimentos ativos por CNAE, confirmação de atendimento e registros ANEEL com datas de conexão continuam ausentes, mas são requisitos de possíveis ampliações futuras — não dependências das perguntas atuais. Sem eles, o trabalho não mede o tamanho dos públicos residencial e empresarial da Ativa Solar, não confirma cobertura da empresa e não deve produzir uma lista ou prioridade comercial definitiva.

## Dashboard

O MVP da dashboard está implementado em `Dashboard/app.py`, com **Python**, **pandas**, **Plotly** e **Streamlit**. Ele carrega a base integrada limpa e permite filtrar por estado e município para comparar GHI anual e mensal, instalações e potência fotovoltaica registradas pela ANEEL, razões por mil habitantes e população estimada como contexto. A dashboard também exibe como não preenchidos os campos de público residencial e empresarial e de confirmação de atendimento. Esses campos representam lacunas para possíveis ampliações comerciais, não entradas das cinco perguntas atuais; valores ausentes não são convertidos em zero.

Para executar a aplicação a partir da raiz do repositório:

```powershell
python -m pip install -r Dashboard/requirements.txt
python -m streamlit run Dashboard/app.py
```

A dashboard é exploratória e não gera prioridade comercial final. Os dados da ANEEL são geração distribuída registrada nos municípios. A ausência de domicílios, CNAEs, confirmação de atendimento e registros anuais da ANEEL limita possíveis análises comerciais futuras, mas não impede os cinco comparativos definidos para o escopo atual.

## Organização do repositório

| Caminho | Conteúdo |
|---|---|
| `Base de dados/01_bases_recebidas/` | Bases originais, recortes, metodologia, fontes e links consultados. |
| `Base de dados/02_base_integrada/` | Base municipal integrada, com campos preparados para complementação. |
| `Base de dados/03_complementacao/` | Cadastro de atendimento e público-alvo e rotina para processar registros históricos da ANEEL quando obtidos. |
| `Base de dados/04_documentacao/` | Fontes de complementação e dicionário dos campos pendentes. |
| `Base de dados/05_bases_tratadas/` | Base integrada limpa, dicionário e relatório de qualidade. |
| `Notebooks/` | Notebooks separados de limpeza, validação, integração e exportação e de análise exploratória. |
| `Dashboard/` | Aplicação exploratória em Streamlit e dependências necessárias para executá-la. |
| `Documentação/` | [Guia unificado da apresentação DEILAS em Word](Documentação/Guia_Unificado_Apresentacao_DEILAS.docx) para o ensaio e [roteiro resumido](Documentação/Roteiro_Apresentacao_DEILAS_Equipe_4.md) com os tempos e a divisão das etapas entre os integrantes. O PDF da primeira entrega e o DOCX de limpeza e análise inicial registram fases anteriores do projeto. |

Os CSVs tabulares usam UTF-8 com BOM e ponto e vírgula como separador. As bases integradas e tratadas usam vírgula decimal; os recortes originais do INPE usam ponto decimal. Trate o código IBGE como texto e preserve campos vazios como ausências.
