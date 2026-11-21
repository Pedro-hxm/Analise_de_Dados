# Fontes e metodologia — Base da Ativa Solar (12 municípios de PE e PB)

**Montagem:** 10/11/2026  
**Escopo:** exclusivamente os 12 municípios indicados para o projeto.

## Municípios incluídos

- **Pernambuco:** Abreu e Lima, Goiana, Igarassu, Itamaracá, Itambé e Itapissuma.
- **Paraíba:** Alhandra, Caaporã, Conde, João Pessoa, Pedras de Fogo e Pitimbu.

## Objetivo

Preparar uma base inicial para comparar o potencial de prospecção e instalação de sistemas fotovoltaicos da Ativa Solar nestas localidades. A empresa apresenta atendimento a residências, empresas e propriedades rurais.

## Três conjuntos de dados selecionados

1. **INPE/LABREN — Atlas Brasileiro de Energia Solar, 2ª edição (2017).** Irradiação Global Horizontal (GHI) e irradiação no Plano Inclinado a 10° (GTI10), valores anuais e mensais, e coordenadas das sedes. Os valores são estimativas baseadas em imagens de satélite de 1999–2015, resolução 0,1° (cerca de 10 km), e representam o ponto da sede municipal, não a média de toda a cidade nem um telhado/terreno específico. Unidade: Wh/m².dia; dividir por 1.000 para kWh/m².dia.
2. **ANEEL — empreendimentos de MMGD.** Registros fotovoltaicos (UFV) dos 12 municípios, agregados por código IBGE: número de instalações, potência total em kW e UCs que recebem créditos. O arquivo de origem foi baixado em 10/11/2026; os dados são atualizados diariamente. O pacote não contém nomes ou documentos de titulares. A presença atual de sistemas pode sinalizar adoção ou concorrência, mas não mede demanda não atendida nem capacidade livre da rede.
3. **IBGE — estimativas de população 2026.** População estimada com referência em 1º de julho de 2026. Usada como aproximação do tamanho do mercado local; não substitui consumo, renda ou intenção de compra.

## Preparação e uso

- A cobertura é somente a lista acima: seis municípios de PE e seis da PB.
- As tabelas foram unidas pelo código IBGE de sete dígitos. No Atlas, “Itamaracá” corresponde à denominação oficial **Ilha de Itamaracá**.
- `base_municipal_AtivaSolar_12_municipios_PE_PB.csv` tem uma linha por município e junta irradiação, população e métricas ANEEL por 1.000 habitantes.
- Os CSVs usam UTF-8 com BOM e ponto e vírgula. As tabelas tratadas usam vírgula decimal. Os quatro CSVs estaduais do INPE foram filtrados para os municípios selecionados.
- Nenhuma ponderação ou município vencedor foi definido nesta etapa. Adoção fotovoltaica existente deve ser interpretada como possível procura consolidada ou concorrência.

## Limitações e uso do Atlas

A base apoia uma primeira triagem municipal, não aprova um endereço ou terreno. Não inclui disponibilidade de conexão, subestações, custo/uso do solo, zoneamento, restrições ambientais, potencial de telhados, tarifas, contas de energia, renda ou logística de atendimento.

Os metadados do INPE informam que a base do Atlas não pode ser reproduzida ou copiada, integral ou parcialmente, para fins comerciais sem autorização expressa do CCST/INPE. Para o trabalho acadêmico, atribua “LABREN / CCST / INPE – Brasil”.

## Arquivos do pacote

- `base_municipal_AtivaSolar_12_municipios_PE_PB.csv` — base consolidada, 12 linhas.
- `dados/01_INPE/` — quatro CSVs do Atlas filtrados e o master de GHI/GTI10.
- `dados/02_ANEEL/` — indicadores fotovoltaicos agregados para os 12 municípios.
- `dados/03_IBGE/` — estimativas populacionais para os 12 municípios.
- `fontes_e_links.csv` — inventário dos links consultados e usados.

## Links consultados e downloads

- **Ativa Solar — Site institucional:** https://ativasolar.com/
  - Contexto da empresa e serviços.
- **INPE/LABREN — Atlas Brasileiro de Energia Solar 2017:** https://labren.ccst.inpe.br/atlas_2017.html
  - Página oficial e acesso às bases.
- **INPE/LABREN — Página de Pernambuco:** https://labren.ccst.inpe.br/atlas_2017_PE.html
  - Consulta e arquivos de PE.
- **INPE/LABREN — Página da Paraíba:** https://labren.ccst.inpe.br/atlas_2017_PB.html
  - Consulta e arquivos de PB.
- **INPE/LABREN — GHI — sedes selecionadas de PE:** https://labren.ccst.inpe.br/projetos/atlas_2017/GLOBAL_HORIZONTAL_PE_sedes-munic_(csv).zip
  - Arquivo de origem; filtrado para os seis municípios de PE.
- **INPE/LABREN — GTI10 — sedes selecionadas de PE:** https://labren.ccst.inpe.br/projetos/atlas_2017/TILTED_LATITUDE_PE_sedes-munic_(csv).zip
  - Arquivo de origem; filtrado para os seis municípios de PE.
- **INPE/LABREN — GHI — sedes selecionadas de PB:** https://labren.ccst.inpe.br/projetos/atlas_2017/GLOBAL_HORIZONTAL_PB_sedes-munic_(csv).zip
  - Arquivo de origem; filtrado para os seis municípios de PB.
- **INPE/LABREN — GTI10 — sedes selecionadas de PB:** https://labren.ccst.inpe.br/projetos/atlas_2017/TILTED_LATITUDE_PB_sedes-munic_(csv).zip
  - Arquivo de origem; filtrado para os seis municípios de PB.
- **INPE/LABREN — Ajuda de leitura do Atlas:** https://labren.ccst.inpe.br/atlas_2017_ajuda.html
  - Leitura e formato das bases.
- **INPE/LABREN — Metadados do Atlas (PDF):** https://labren.ccst.inpe.br/projetos/atlas_2017/atlas_solar_2017_metadados.pdf
  - Unidades, resolução, período e restrição comercial.
- **ANEEL — Relação de empreendimentos MMGD:** https://dadosabertos.aneel.gov.br/dataset/relacao-de-empreendimentos-de-geracao-distribuida
  - Página oficial do conjunto atualizado diariamente.
- **ANEEL — Download dos registros MMGD:** https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/b1bd71e7-d0ad-4214-9053-cbd58e9564a7/download/empreendimento-geracao-distribuida.zip
  - Arquivo baixado em 10/11/2026; filtrado para UFV nos 12 municípios e agregado por código IBGE.
- **IBGE — Estimativas municipais de população 2026:** https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao
  - Página oficial; referência populacional em 01/07/2026.
- **IBGE — POP2026_20261029.xlsx:** https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2026/POP2026_20261029.xlsx
  - Planilha oficial convertida para CSV e filtrada para os 12 municípios.
