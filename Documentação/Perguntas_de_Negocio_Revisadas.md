# Perguntas de Negócio — escopo analítico disponível

Documento editável de referência para as análises do projeto acadêmico de **Análise de Dados e BI do UNIPÊ**.

## Intuito e escopo

Comparar, com dados públicos já disponíveis, os 12 municípios do recorte de Pernambuco e Paraíba para apoiar uma triagem exploratória de localidades que possam merecer investigação posterior para ações de prospecção da Ativa Solar. As perguntas abaixo foram delimitadas aos dados e às análises que já constam no repositório. Elas não comprovam demanda, não identificam clientes da Ativa Solar e não estimam vendas ou faturamento.

O recorte permanece fixo nos 12 municípios — seis em cada estado. A inclusão de um município no estudo não confirma que a empresa o atenda.

| Pernambuco | Paraíba |
|---|---|
| Abreu e Lima | Alhandra |
| Goiana | Caaporã |
| Igarassu | Conde |
| Ilha de Itamaracá | João Pessoa |
| Itambé | Pedras de Fogo |
| Itapissuma | Pitimbu |

O código IBGE de sete dígitos é a chave usada na integração das bases.

## Perguntas, dados, métricas e status

### 1. Comparação anual do GHI

**Pergunta:** Como os valores anuais históricos de GHI se comparam entre as sedes dos 12 municípios?

**Dados necessários**

- GHI anual do INPE/LABREN para cada sede municipal, disponível na base integrada tratada.
- Os valores são médias diárias em **Wh/m².dia**, estimadas a partir da série histórica **1999–2015**.

**Métricas**

- Tabela e ordenação descritiva dos valores anuais por município, incluindo a leitura dos maiores e menores valores observados.
- Comparação em **Wh/m².dia**, sem tratar a ordem como classificação comercial.

**Status atual:** respondível com a base `Base de dados/05_bases_tratadas/base_integrada_limpa.csv`. A comparação e a saída estão salvas no notebook `Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb`.

**Limitações:** o GHI é uma referência histórica nas coordenadas das sedes municipais, com resolução aproximada de 0,1° (cerca de 10 km). Não mede telhados ou imóveis específicos, não descreve todos os pontos do município e não é previsão das condições atuais.

### 2. Comparação mensal do GHI

**Pergunta:** Como os valores médios diários mensais de GHI variam entre as sedes dos 12 municípios ao longo do ano?

**Dados necessários**

- Os 12 campos mensais de GHI do INPE/LABREN para cada sede municipal, disponíveis na base integrada tratada.
- Médias diárias mensais em **Wh/m².dia**, referentes à série histórica **1999–2015**.

**Métricas**

- Comparação dos valores de cada mês entre municípios.
- Tabela mensal e gráfico dos perfis ao longo dos 12 meses, preservando a unidade original.

**Status atual:** respondível com os campos mensais disponíveis. A tabela comparativa e o gráfico mensal estão salvos no notebook exploratório versionado.

**Limitações:** os meses representam médias diárias históricas, não medições mensais de telhados nem uma série de mudanças entre anos. O resultado deve ser descrito como sazonalidade histórica das referências municipais.

### 3. Distribuição municipal da geração distribuída fotovoltaica registrada pela ANEEL

**Pergunta:** Como se distribuem, entre os 12 municípios, as instalações fotovoltaicas e a potência agregada registradas pela ANEEL?

**Dados necessários**

- Número de instalações fotovoltaicas e potência instalada agregada em **kW** no arquivo `ANEEL_MMGD_fotovoltaica_12_municipios_PE_PB_2026-11-10.csv`.
- Fotografia municipal com referência em **10/11/2026**.

**Métricas**

- Totais de instalações fotovoltaicas por município.
- Potência agregada registrada por município, em kW.
- Comparação descritiva dos totais entre os 12 municípios.

**Status atual:** respondível com os dados ANEEL integrados e com as tabelas e gráficos já salvos no notebook exploratório.

**Limitações:** os valores descrevem geração distribuída registrada nos municípios, não clientes, instalações vendidas, vendas ou faturamento da Ativa Solar. A fotografia não permite inferir evolução anual, demanda não atendida ou capacidade livre da rede. Baixa adoção, isoladamente, não comprova oportunidade comercial.

### 4. Indicadores da ANEEL por população estimada

**Pergunta:** Como variam, entre os municípios, as razões de instalações e de potência fotovoltaica registradas pela ANEEL por 1.000 habitantes estimados?

**Dados necessários**

- Instalações e potência da ANEEL, com referência em **10/11/2026**.
- População municipal estimada pelo IBGE para **2026**, com referência em **01/07/2026**, medida em habitantes.
- Os dois indicadores derivados já constam da base integrada tratada e foram recalculados e conferidos no relatório de qualidade.

**Métricas**

- Instalações por 1.000 habitantes = instalações fotovoltaicas ÷ população estimada × 1.000.
- Potência em kW por 1.000 habitantes = potência agregada em kW ÷ população estimada × 1.000.

**Status atual:** respondível. As duas razões foram recalculadas para os 12 municípios, conferidas sem divergências após arredondamento a duas casas decimais e comparadas no notebook exploratório, com saídas salvas.

**Limitações:** são razões descritivas com referências temporais distintas. Não são percentuais de domicílios com energia solar, taxas de clientes da empresa nem medidas de potencial de mercado. População é usada somente como denominador desses indicadores e não substitui domicílios ocupados.

### 5. Associação descritiva entre população e instalações

**Pergunta:** Que associação descritiva existe entre a população municipal estimada e o número de instalações fotovoltaicas registradas pela ANEEL nos 12 municípios?

**Dados necessários**

- População estimada pelo IBGE para 2026, referência em **01/07/2026**.
- Número de instalações fotovoltaicas da ANEEL, referência em **10/11/2026**.
- Os dois campos estão disponíveis para os 12 municípios na base integrada tratada.

**Métricas**

- Gráfico de dispersão entre população e instalações.
- Correlação de Pearson para descrever a associação linear na amostra municipal, acompanhada da leitura dos valores absolutos e das diferenças de escala.

**Status atual:** respondível. O notebook exploratório tem o gráfico, a saída numérica e a interpretação salvos. A correlação registrada é **0,992** para os 12 municípios.

**Limitações:** a correlação descreve somente esta amostra de 12 municípios; não demonstra causalidade, não é previsão e pode refletir diferenças de porte populacional. Não deve ser interpretada como relação entre população e clientes ou vendas da Ativa Solar.

## Dados fora do escopo destas perguntas

As cinco perguntas acima não dependem de novas coletas: os campos necessários e as respectivas análises estão disponíveis na base tratada e no notebook exploratório com execuções e saídas salvas. As lacunas abaixo continuam reais no repositório, mas são requisitos de possíveis ampliações futuras — não impedem responder ao conjunto atual:

- **Domicílios particulares permanentes ocupados do Censo 2022:** não coletados. Seriam necessários para estudar o público residencial por domicílios; a população não pode substituí-los.
- **CNAEs e estabelecimentos ativos:** os CNAEs não foram definidos e as contagens não foram coletadas. Seriam necessários para estudar o público empresarial.
- **Área de atendimento da Ativa Solar:** não confirmada. O recorte de 12 municípios é geográfico e não deve ser apresentado como cobertura da empresa.
- **Histórico anual da ANEEL:** não há registros com datas de conexão disponíveis no repositório. A pergunta atual se limita à fotografia municipal de 10/11/2026; não se deve descrever evolução anual.

## Regras de interpretação

- Não converter campos vazios em zero; eles continuam indicando ausência de coleta ou confirmação.
- Não usar população estimada como substituta de domicílios particulares permanentes ocupados.
- Descrever os dados da ANEEL como geração distribuída registrada nos municípios, nunca como clientes ou vendas da Ativa Solar.
- Tratar o GHI do INPE como referência histórica das sedes municipais, não como medição de telhados específicos.
- Não interpretar baixa adoção solar, isoladamente, como evidência de oportunidade comercial.
- Diferenciar valores observados, interpretações descritivas e hipóteses para investigação posterior. Não declarar município vencedor, prioridade comercial definitiva ou recomendação final.

## Artefatos de referência

- Base integrada tratada, dicionário e relatório de qualidade: `Base de dados/05_bases_tratadas/`.
- Notebook exploratório com análises executadas e saídas salvas: `Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb`.
- Dashboard exploratória: `Dashboard/app.py`.

Este documento delimita perguntas compatíveis com os dados e análises disponíveis; não substitui os metadados das fontes, os dicionários ou a metodologia de tratamento.
