# Roteiro preliminar de apresentação — DEILAS e dashboard

**Projeto:** Inteligência Comercial Geográfica para a Ativa Solar  
**Disciplina:** Análise de Dados e BI — UNIPÊ  
**Professor:** Daniel Brandão

## Divisão combinada

| Integrante | Responsabilidade |
|---|---|
| Pedro Henrique | Abertura; demonstração da dashboard; distinção entre valor observado e interpretação; encerramento e perguntas da turma. |
| Pedro Antônio | Perguntas de negócio e explicação do que cada uma procura responder. |
| Guilherme Cavalcante (Gui) | Recorte municipal, fontes, limpeza, integração e qualidade/situação dos dados. |
| Arlan | Apresentação do fluxo DEILA e da análise exploratória; responsável pela etapa S, cujo conteúdo será preparado amanhã. |

**Tempo sugerido:** aproximadamente 8 minutos e 30 segundos de apresentação, mais 3 minutos reservados para perguntas. É uma estimativa ajustável; o tempo da etapa S deverá ser recalibrado quando o grupo preparar esse conteúdo amanhã.

A sequência combina uma abertura breve de Pedro Henrique, as perguntas de Pedro Antônio, a preparação dos dados apresentada por Gui, a análise de Arlan e, ao final, a demonstração da dashboard e o encerramento com Pedro Henrique.

## 1. Pedro Henrique — Abertura

**Tempo sugerido: 45 segundos**

> Boa noite. Nosso projeto, desenvolvido na disciplina de Análise de Dados e BI do UNIPÊ, compara dados públicos de 12 municípios de Pernambuco e da Paraíba. A ideia é apoiar uma triagem inicial de localidades que possam merecer investigação em futuras ações de prospecção da Ativa Solar.
>
> O estudo é exploratório: ele não comprova demanda, não identifica clientes da empresa e não estima vendas ou faturamento. Também não confirmamos que todos os municípios do recorte sejam atendidos pela Ativa Solar. Primeiro, Pedro Antônio vai explicar as perguntas que orientam a análise.

## 2. Pedro Antônio — Perguntas de negócio

**Tempo sugerido: 1 minuto e 35 segundos**

> As perguntas organizam o estudo em cinco frentes. A primeira compara, separadamente, os domicílios particulares permanentes ocupados e os estabelecimentos ativos nos CNAEs que a empresa definir, entre os municípios com atendimento confirmado. Para isso, precisamos dos dados do Censo 2022, da definição dos CNAEs e das contagens de estabelecimentos, além da confirmação da área atendida.
>
> A segunda pergunta mede a participação de cada município nos públicos residencial e empresarial da área atendida. Ela depende dessas mesmas informações; população não substitui domicílios.
>
> A terceira compara o GHI anual e mensal nas sedes municipais. Essa frente já pode ser descrita com os dados históricos do INPE. A quarta observa como as instalações fotovoltaicas e a potência da ANEEL se distribuem atualmente. Para avaliar evolução anual, ainda precisamos de registros com datas de conexão.
>
> Por fim, perguntamos quais municípios e segmentos podem compor uma lista preliminar para validação comercial. Essa lista ainda não pode ser recomendada como conclusão: faltam os dados de público e a confirmação do atendimento. Gui vai explicar o recorte e como as bases foram preparadas.

**Perguntas do estudo**

1. Entre os municípios do recorte com atendimento confirmado, onde há mais domicílios particulares permanentes ocupados e estabelecimentos ativos nos CNAEs definidos pela empresa, analisados separadamente?
2. Qual é a participação de cada município nos públicos residencial e empresarial da área atendida?
3. Como o GHI anual e mensal varia entre as sedes municipais?
4. Como as instalações fotovoltaicas e a potência registradas pela ANEEL se distribuem atualmente? A evolução anual será analisada se forem obtidos registros com datas de conexão.
5. Quais municípios e segmentos podem compor uma lista preliminar para validação comercial, considerando a área atendida, o tamanho dos públicos e os indicadores de GHI e ANEEL como contexto?

## 3. Guilherme Cavalcante (Gui) — Recorte, limpeza e qualidade dos dados

**Tempo sugerido: 2 minutos**

> O recorte permanece em 12 municípios: em Pernambuco, Abreu e Lima, Goiana, Igarassu, Ilha de Itamaracá, Itambé e Itapissuma; na Paraíba, Alhandra, Caaporã, Conde, João Pessoa, Pedras de Fogo e Pitimbu.
>
> As fontes têm finalidades diferentes. O Atlas Solar 2017 do INPE/LABREN fornece GHI anual e mensal como médias diárias da série histórica de 1999 a 2015, em Wh por metro quadrado por dia, para as sedes municipais. Esses valores não medem telhados específicos. A base da ANEEL é uma fotografia da geração distribuída registrada nos municípios, com referência em 10 de novembro de 2026. A população do IBGE é uma estimativa de 2026, com referência em 1º de julho, e entra como contexto, não como substituta de domicílios.
>
> Na limpeza e integração, os dados foram organizados pelo código IBGE dos municípios. O relatório de qualidade registra 12 municípios, 12 códigos únicos e junções um-para-um. A base integrada tem 44 campos. Domicílios ocupados, estabelecimentos ativos e atendimento continuam pendentes; campos vazios não foram convertidos em zero.
>
> O notebook de limpeza contém o código do processo. No arquivo versionado, porém, não há contagens de execução nem saídas salvas. Por isso, vamos explicar a lógica do script sem usar o notebook como prova de resultados executados. Arlan apresenta agora o método e as análises exploratórias que têm saídas registradas.

## 4. Arlan — Fluxo DEILA e análise exploratória

**Tempo sugerido: 2 minutos de análise e 30 segundos reservados à etapa S**

> Organizamos o trabalho pelo fluxo DEILAS: definir objetivos, estabelecer métricas, identificar fontes, limpar e integrar, analisar e, por último, sugerir decisões. Nesta apresentação, vou retomar essa lógica e mostrar o que as análises exploratórias já permitem observar. A etapa S fica reservada para ser preparada amanhã.
>
> No GHI anual, o maior valor observado é o de Ilha de Itamaracá, 5.532 Wh por metro quadrado por dia; o menor é o de Abreu e Lima, 5.292. Na comparação mensal, a tabela dos 12 municípios mostra o menor valor em Abreu e Lima, em junho, com 4.161, e o maior em Itapissuma, em dezembro, com 6.256. São referências históricas das sedes municipais, não medições atuais de telhados.
>
> Na fotografia da ANEEL, João Pessoa tem os maiores totais absolutos do recorte: 10.448 instalações e 118.223,30 kW de potência registrada. Alhandra tem o menor número de instalações, 122; Caaporã tem a menor potência, 1.213,37 kW.
>
> As razões por mil habitantes também foram calculadas: Ilha de Itamaracá apresenta a maior razão de instalações, 36,08, e Conde a maior razão de potência, 363,88 kW por mil habitantes. A correlação de Pearson entre população estimada e instalações é 0,992 nos 12 municípios. É uma associação descritiva, não prova de causalidade.
>
> Esses são valores observados nos dados, não uma classificação comercial. João Pessoa ter os maiores totais absolutos da ANEEL não significa automaticamente que seja a melhor localidade para prospecção. A dashboard ajuda a visualizar os indicadores; Pedro Henrique vai demonstrar os filtros e retomar essa diferença entre observação e interpretação.

**Etapa S — bloco reservado para amanhã**

Responsável: **Arlan**. O grupo ainda vai preparar o conteúdo da etapa “Sugerir decisões”. Inserir aqui, amanhã, a fala e as recomendações proporcionais às evidências e às pendências. Não apresentar uma lista preliminar como decisão comercial definitiva.

## 5. Pedro Henrique — Demonstração da dashboard e encerramento

**Tempo sugerido: 1 minuto e 40 segundos, incluindo demonstração breve**

> A dashboard reúne os indicadores disponíveis. Vou mostrar rapidamente os filtros de estado, município e indicador. No mapa, os pontos representam as sedes municipais. No GHI, podemos alternar entre a visão anual e a mensal; na ANEEL, entre número de instalações e potência registrada.
>
> Por exemplo, o painel mostra João Pessoa com os maiores totais absolutos de instalações e potência registrados pela ANEEL. Essa é a observação. A interpretação precisa ser mais cuidadosa: esses totais não demonstram demanda da Ativa Solar nem tornam o município automaticamente a melhor opção para prospecção. Também não sabemos, com os dados atuais, se o município é atendido pela empresa.
>
> [Depois que Arlan preparar a etapa S amanhã, acrescentar aqui uma síntese breve das recomendações do grupo.]
>
> Para encerrar, nosso objetivo foi comparar os 12 municípios com dados públicos e apoiar uma triagem inicial. O estudo não comprova demanda, não identifica clientes nem estima vendas ou faturamento. A pergunta sobre quais localidades e segmentos merecem validação depende de completar os dados de domicílios e estabelecimentos e confirmar a área atendida. Obrigado. Agora reservamos um tempo para as perguntas.

## Perguntas prováveis da turma

**“João Pessoa é o melhor município para prospecção?”**  
Não concluímos isso. João Pessoa tem os maiores totais absolutos de instalações e potência na fotografia da ANEEL. Esses dados não medem demanda da Ativa Solar, e ainda faltam informações de atendimento e tamanho dos públicos.

**“Os registros da ANEEL são clientes da Ativa Solar?”**  
Não. São registros de geração distribuída nos municípios; não identificam clientes nem vendas da empresa.

**“O GHI representa a irradiação atual nos telhados?”**  
Não. É uma referência histórica para as sedes municipais, calculada a partir da série de 1999 a 2015. Não mede telhados ou imóveis específicos.

**“Por que não mostramos domicílios e estabelecimentos?”**  
Os domicílios particulares permanentes ocupados do Censo 2022 ainda precisam ser coletados e conferidos. A empresa ainda precisa definir os CNAEs; as contagens de estabelecimentos ativos e a confirmação do atendimento também estão pendentes.

**“As instalações por mil habitantes representam o percentual de casas com painel solar?”**  
Não. É uma razão entre instalações registradas e população estimada. Não é percentual de domicílios nem uma taxa de clientes da Ativa Solar.

**“A correlação de 0,992 prova que cidades mais populosas têm mais instalações por causa da população?”**  
Não. É uma associação descritiva nos 12 municípios e não demonstra causalidade. O porte de João Pessoa também pode influenciar a associação.

**“Por que não mostramos a evolução anual da ANEEL?”**  
A base tratada disponível é uma fotografia com referência em 10/11/2026. Uma série anual depende de obter e conferir registros com datas de conexão.

**“Baixa adoção solar significa maior oportunidade?”**  
Não por si só. Os dados não medem demanda não atendida, intenção de compra ou capacidade livre da rede.

## Evidências numéricas nas saídas salvas

Os resultados abaixo aparecem em saídas salvas do notebook exploratório. A numeração indica a posição da célula no arquivo, começando em 1. Nenhuma célula foi executada para preparar este roteiro.

| Célula | Resultado observado |
|---|---|
| 5 | GHI anual: maior em Ilha de Itamaracá (5.532 Wh/m².dia); menor em Abreu e Lima (5.292 Wh/m².dia). |
| 7 | Tabela mensal dos 12 municípios; mínimo em Abreu e Lima em junho (4.161 Wh/m².dia); máximo em Itapissuma em dezembro (6.256 Wh/m².dia). |
| 9 | Instalações ANEEL: maior total em João Pessoa (10.448); menor em Alhandra (122). |
| 11 | Potência ANEEL: maior em João Pessoa (118.223,30 kW); menor em Caaporã (1.213,37 kW). |
| 13 | Instalações por 1.000 habitantes: maior em Ilha de Itamaracá (36,08); menor em Alhandra (5,23). |
| 15 | Potência por 1.000 habitantes: maior em Conde (363,88 kW); menor em Caaporã (55,12 kW). |
| 17 | Correlação de Pearson entre população estimada e instalações: 0,992; análise descritiva de 12 municípios. |

O notebook exploratório tem 18 células, 9 delas de código, com contagens de execução e saídas salvas. O notebook de limpeza tem 29 células, 13 delas de código, sem contagens de execução ou saídas salvas no arquivo versionado. A equipe pode explicar a execução que realizou no VS Code, sem atribuir essa evidência às saídas do arquivo versionado.

## O que falta fechar antes da apresentação

- Preparar amanhã o conteúdo da etapa S com Arlan e inserir a síntese aprovada na fala de encerramento.
- Confirmar que a sequência dos slides acompanha as quatro falas e que as transições estão claras.
- Abrir a dashboard antes da apresentação e deixar os filtros em um estado que facilite a demonstração.
- Conferir que a apresentação separa visualmente “valor observado” de “interpretação”, sobretudo no exemplo de João Pessoa.
- Manter visíveis as pendências de atendimento, domicílios ocupados, CNAEs e estabelecimentos ativos.
- Reservar cerca de 3 minutos para perguntas; ajustar o tempo se a turma definir outra duração.

## Arquivos consultados na preparação do roteiro

- README.md e Documentação/Perguntas_de_Negocio_Revisadas.md — objetivo, perguntas e estado dos dados.
- Base de dados/01_bases_recebidas/LEIA-ME.txt, Base de dados/01_bases_recebidas/Fontes_e_metodologia_AtivaSolar_12_municipios_PE_PB.md e Base de dados/01_bases_recebidas/fontes_e_links.csv — fontes, períodos, unidades e limites.
- Base de dados/04_documentacao/LEIA_PRIMEIRO.txt, fontes_complementacao.txt e dicionario_complementacao.csv — campos pendentes e regras de complementação.
- Base de dados/05_bases_tratadas/base_integrada_limpa.csv, dicionario_base_integrada.csv e relatorio_qualidade_base_integrada.md — base tratada e controles de qualidade.
- Notebooks/Limpeza_Inicial_DEILAS_Ativa_Solar.ipynb e Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb — etapas de tratamento e saídas exploratórias salvas.
- Base de dados/03_complementacao/atendimento_e_publico_alvo.csv e gerar_historico_aneel.py — situação do atendimento e rotina para eventual série anual.
- Dashboard/app.py — filtros, mapa, indicadores e avisos da dashboard.
- Documentação/Limpeza das Bases e Análise Exploratória Inicial - Ativa Solar.docx e Documentação/Primeira entrega DEILAS — Inteligência Comercial Geográfica.pdf — registros de entregas anteriores, preservados como documentos de entregas anteriores.
