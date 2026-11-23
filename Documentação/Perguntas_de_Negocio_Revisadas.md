# Perguntas de Negócio Revisadas — Ativa Solar

Documento de referência editável para orientar as análises futuras do projeto acadêmico de **Análise de Dados e BI do UNIPÊ**.

## Intuito e escopo

Comparar os 12 municípios do recorte de Pernambuco e Paraíba, com dados públicos, para apoiar uma triagem inicial de localidades que valha a pena investigar para futuras ações de prospecção da Ativa Solar. A análise é exploratória: não comprova demanda, não identifica clientes da Ativa Solar e não estima vendas ou faturamento da empresa.

O recorte permanece fixo nos municípios abaixo. A inclusão na lista não confirma atendimento da empresa.

| Pernambuco | Paraíba |
|---|---|
| Abreu e Lima | Alhandra |
| Goiana | Caaporã |
| Igarassu | Conde |
| Ilha de Itamaracá | João Pessoa |
| Itambé | Pedras de Fogo |
| Itapissuma | Pitimbu |

O código IBGE de sete dígitos é a chave para integrar as bases.

## Perguntas, dados, métricas e status

### 1. Tamanho dos públicos por município

**Pergunta:** Entre os municípios do recorte com atendimento confirmado, onde há mais domicílios particulares permanentes ocupados e estabelecimentos ativos nos CNAEs definidos pela empresa, analisados separadamente?

**Dados necessários**

- Confirmação da Ativa Solar sobre quais dos 12 municípios são atendidos.
- Quantidade de domicílios particulares permanentes ocupados do Censo 2022, por município.
- CNAEs prioritários definidos com a empresa e quantidade de estabelecimentos ativos por município, a partir dos dados abertos do CNPJ da Receita Federal.
- Data de referência da extração de cada base; para os estabelecimentos, regra de deduplicação e tratamento de CNAE principal e secundário.

**Métricas**

- Contagem de domicílios particulares permanentes ocupados por município atendido.
- Contagem de estabelecimentos ativos por município atendido, para os CNAEs acordados.
- Comparações e ordenações independentes para o público residencial e o empresarial; não somar os dois públicos.

**Status atual:** pendente. Os domicílios do Censo 2022 ainda não foram coletados. Os CNAEs não foram definidos e as contagens de estabelecimentos ativos não foram obtidas. A confirmação de atendimento também está pendente. Os campos preparados para esses dados estão vazios nos 12 municípios.

**Limitações e cuidados:** a população estimada pelo IBGE não substitui domicílios. Municípios sem confirmação de atendimento não podem ser tratados como atendidos nem incluídos no denominador da área atendida. Campos vazios significam ausência de coleta ou confirmação, não zero. A contagem por CNAE exige explicitar a referência temporal, a correspondência do código municipal da Receita Federal com o código IBGE e como estabelecimentos com CNAE principal e secundário serão contados.

### 2. Participação municipal nos públicos atendidos

**Pergunta:** Qual é a participação de cada município nos públicos residencial e empresarial da área atendida?

**Dados necessários**

- Confirmação da lista de municípios atendidos pela Ativa Solar.
- Contagens de domicílios ocupados do Censo 2022 e de estabelecimentos ativos nos CNAEs acordados, com suas referências e regras documentadas.

**Métricas**

- Participação residencial: domicílios do município divididos pelo total de domicílios nos municípios com atendimento confirmado, multiplicado por 100.
- Participação empresarial: estabelecimentos do município divididos pelo total de estabelecimentos nos municípios com atendimento confirmado, multiplicado por 100.
- Calcular e apresentar os dois segmentos separadamente.

**Status atual:** pendente. A cobertura atendida não foi confirmada; as contagens residenciais e empresariais necessárias também estão pendentes. Portanto, ainda não há denominadores para calcular as participações.

**Limitações e cuidados:** não calcular percentuais com campos vazios tratados como zero. O denominador deve incluir somente municípios com atendimento confirmado e usar a mesma definição e referência para cada segmento. A participação descreve a distribuição do público medido, não intenção de compra nem probabilidade de contratação.

### 3. Variação do GHI entre sedes municipais

**Pergunta:** Como o GHI anual e mensal varia entre as sedes municipais?

**Dados necessários**

- Campos anuais e mensais de GHI do INPE/LABREN — Atlas Brasileiro de Energia Solar, 2ª edição (2017), disponíveis para os 12 municípios.
- Os valores representam médias diárias em **Wh/m².dia**, estimadas a partir da série histórica **1999–2015**.

**Métricas**

- Comparação e ordenação dos valores anuais de GHI entre sedes.
- Comparações mensais entre municípios e leitura da sazonalidade dentro da série histórica.
- Amplitude ou diferenças observadas, sempre mantendo a unidade original.

**Status atual:** os dados anuais e mensais estão no repositório. No Colab foi feita uma comparação exploratória preliminar do GHI anual. A comparação mensal entre as sedes ainda precisa ser concluída e documentada. O notebook `Analise_Exploratoria_Ativa_Solar.ipynb` foi criado e executado no Colab, mas não foi transferido para o GitHub; seus resultados não estão reproduzidos neste repositório.

**Limitações e cuidados:** o GHI do INPE é uma referência histórica para as coordenadas das sedes municipais, com resolução aproximada de 0,1° (cerca de 10 km); não é medição de telhados, imóveis ou de todo o território municipal. A série 1999–2015 não deve ser apresentada como condição atual ou previsão. As médias mensais indicam sazonalidade histórica, não evolução entre anos. O projeto também possui campos identificados como GTI10; confira os metadados antes de atribuir um ângulo fixo ao rótulo.

### 4. Distribuição da geração distribuída fotovoltaica registrada pela ANEEL

**Pergunta:** Como as instalações fotovoltaicas e a potência registradas pela ANEEL se distribuem atualmente? A evolução anual será analisada se forem obtidos registros com datas de conexão.

**Dados necessários**

- Arquivo municipal de MMGD fotovoltaica da ANEEL para os 12 municípios, com referência de **10/11/2026**.
- Número de instalações, potência instalada agregada em **kW** e unidades consumidoras que recebem créditos.
- Para calcular evolução anual: registros de empreendimentos com município e data de conexão, suficientes para agregação por ano.

**Métricas**

- Distribuição municipal do número de instalações fotovoltaicas e da potência instalada total em kW.
- Como contexto descritivo, instalações e potência por mil habitantes, já recalculadas na base tratada com a estimativa populacional de 2026.
- Se a série com datas de conexão for obtida, contagem e potência por município e ano, com regras de inclusão documentadas.

**Status atual:** o arquivo da ANEEL está disponível como fotografia municipal baixada em 10/11/2026. No Colab foram feitas comparações exploratórias preliminares do número de instalações e da potência, além dos indicadores por mil habitantes. As análises ainda não estão reproduzidas neste repositório. A série histórica anual não está disponível; depende da obtenção de registros com datas de conexão.

**Limitações e cuidados:** os dados descrevem geração distribuída registrada nos municípios; não identificam clientes, vendas ou faturamento da Ativa Solar. Unidades consumidoras que recebem créditos não são equivalentes a instalações ou clientes únicos. A fotografia de 10/11/2026 não demonstra evolução temporal. Baixa adoção solar, isoladamente, não prova oportunidade comercial, demanda não atendida ou capacidade livre da rede.

### 5. Lista preliminar para validação comercial

**Pergunta:** Quais municípios e segmentos podem compor uma lista preliminar para validação comercial, considerando a área atendida, o tamanho dos públicos e os indicadores de GHI e ANEEL como contexto?

**Dados necessários**

- Municípios do recorte com atendimento confirmado pela Ativa Solar.
- Contagens comparáveis de domicílios ocupados e estabelecimentos ativos nos CNAEs acordados.
- Indicadores de GHI anual e mensal e fotografia municipal da ANEEL, com períodos e unidades preservados.
- Critérios explícitos para organizar a lista, documentando eventuais decisões de ponderação antes de aplicá-las.

**Métricas e critérios de leitura**

- Tamanho e participação de cada público por município atendido, mantendo residencial e empresarial separados.
- GHI anual e mensal e instalações/potência da ANEEL como indicadores de contexto para comparar os municípios.
- Lista preliminar de municípios e segmentos acompanhada dos critérios e das limitações; não produzir uma pontuação ou vencedor sem regra justificada.

**Status atual:** não permite uma recomendação final nem uma lista fundamentada enquanto faltarem as contagens de público e a confirmação da área atendida. Os indicadores ambientais e de geração distribuída existentes, sozinhos, não suprem essas lacunas. O projeto não definiu município vencedor nem ponderação.

**Limitações e cuidados:** esta pergunta orienta uma triagem para validação comercial posterior, não uma decisão de prospecção ou previsão de vendas. GHI histórico e geração distribuída registrada pela ANEEL são contexto, não prova de demanda da Ativa Solar. Baixa adoção não deve ser tratada isoladamente como oportunidade. A base também não contém consumo, renda, intenção de compra, potencial de telhados, viabilidade de conexão, custos, restrições locais ou logística de atendimento.

## Pendências transversais e regras de interpretação

- Coletar e conferir os domicílios particulares permanentes ocupados do Censo 2022.
- Definir com a empresa os CNAEs e coletar os estabelecimentos ativos, documentando data de referência, chave municipal e deduplicação.
- Confirmar quais municípios do recorte são atendidos pela Ativa Solar.
- Obter registros da ANEEL com datas de conexão para avaliar a evolução anual, caso estejam disponíveis.
- Concluir e documentar a comparação mensal do GHI.
- Preservar ausências como valores pendentes, sem convertê-las em zero; não usar população como substituta de domicílios.
- Descrever os dados da ANEEL como geração distribuída registrada nos municípios, nunca como clientes da Ativa Solar, vendas ou faturamento.
- Tratar o GHI do INPE como referência histórica das sedes municipais, não como medição de telhados específicos.
- Não interpretar baixa adoção solar, isoladamente, como evidência de oportunidade comercial.

## Estado dos artefatos

O repositório contém o notebook de limpeza `Notebooks/Limpeza_Inicial_DEILAS_Ativa_Solar.ipynb`, a base integrada limpa, seu dicionário e o relatório de qualidade. O notebook exploratório separado `Analise_Exploratoria_Ativa_Solar.ipynb` foi criado e executado no Colab, mas ainda não foi transferido ao GitHub. Assim, os cálculos exploratórios mencionados acima não podem ser reproduzidos a partir do conteúdo atualmente versionado.

Este documento registra as perguntas e necessidades analíticas; não substitui a metodologia da base, os dicionários nem os metadados das fontes.
