# Roteiro dos slides — Inteligência Comercial Geográfica para a Ativa Solar

Material de apoio para a equipe da disciplina Análise de Dados e BI do UNIPÊ. As durações são sugestões e a apresentação pode ser ajustada ao ensaio.

## 1. Abertura e objetivo — Pedro Henrique — 40 segundos — D

- Apresentar a Ativa Solar e o projeto acadêmico.
- Explicar o objetivo de comparar dados públicos de 12 municípios de Pernambuco e Paraíba para apoiar uma triagem inicial de localidades para investigação comercial.
- Situar o caráter exploratório e a ausência de confirmação de cobertura da empresa.

## 2. Perguntas de negócio — Pedro Antônio — 1 minuto — E

- Comparar o GHI anual e o mensal entre as sedes.
- Observar a distribuição municipal de instalações e potência da ANEEL.
- Comparar instalações e potência por 1.000 habitantes estimados.
- Descrever a associação entre população e instalações.
- Explicar como cada pergunta define uma métrica que será apresentada nos resultados.

## 3. Recorte e fontes — Guilherme Cavalcante — 35 segundos — I

- Apresentar os seis municípios de cada estado. Pernambuco: Abreu e Lima, Goiana, Igarassu, Ilha de Itamaracá, Itambé e Itapissuma. Paraíba: Alhandra, Caaporã, Conde, João Pessoa, Pedras de Fogo e Pitimbu.
- INPE/LABREN fornece médias diárias de GHI anuais e mensais da série histórica 1999–2015 nas sedes, em Wh/m².dia.
- ANEEL fornece a fotografia de instalações e potência em kW de 10/11/2026. IBGE fornece a população estimada com referência em 01/07/2026.

## 4. Limpeza e qualidade — Guilherme Cavalcante — 35 segundos — L

- Descrever a sequência de leitura, padronização, validação e integração pelo código IBGE.
- Apresentar os 12 municípios, as 44 colunas da base tratada, os códigos únicos e as junções um para um.
- Explicar que as ausências são preservadas como valores não coletados ou não confirmados.

## 5. Irradiação solar — Arlan — 45 segundos — A

- Comparar as médias diárias anuais históricas: 5.292 Wh/m².dia em Abreu e Lima e 5.532 Wh/m².dia em Ilha de Itamaracá.
- Apresentar a comparação mensal histórica. O menor valor da tabela é 4.161 Wh/m².dia em Abreu e Lima em junho, e o maior é 6.256 Wh/m².dia em Itapissuma em dezembro.
- Contextualizar o GHI como referência histórica das sedes municipais, sem tratá-lo como medição de telhados.

## 6. Geração distribuída — Arlan — 45 segundos — A

- João Pessoa tem os maiores totais do recorte: 10.448 instalações e 118.223,30 kW em 10/11/2026.
- Por 1.000 habitantes estimados, Ilha de Itamaracá tem 36,08 instalações e Conde tem 363,88 kW, os maiores indicadores em suas respectivas métricas.
- Diferenciar totais e razões, explicando que a ANEEL registra geração distribuída municipal e não identifica clientes ou vendas da Ativa Solar.

## 7. População e instalações — Arlan — 25 segundos — A

- O gráfico de dispersão apresenta 12 municípios e correlação de Pearson de 0,992 entre população estimada e instalações.
- A relação é descritiva, não estabelece causalidade e pode refletir diferenças de porte, inclusive de João Pessoa.

## 8. Sugestão para investigação — Arlan — 20 segundos — S

- Propor a investigação de três perfis: João Pessoa pelos maiores totais, Ilha de Itamaracá pela razão de instalações e Conde pela razão de potência.
- Sugerir a validação do atendimento, dos públicos e das condições locais antes de uma decisão comercial.
- Apresentar a seleção como hipótese inicial, sem município vencedor ou promessa de vendas.

## 9. Dashboard e encerramento — Pedro Henrique — 1 minuto e 5 segundos

1. Mostrar os 12 municípios em [dashboard-ativasolar.streamlit.app](https://dashboard-ativasolar.streamlit.app/).
2. Selecionar instalações em totais e apontar João Pessoa.
3. Mudar para instalações por 1.000 habitantes e apontar Ilha de Itamaracá.
4. Selecionar potência por 1.000 habitantes e apontar Conde.
5. Retomar o objetivo e os limites da análise. Usar “Voltar aos 12 municípios” quando necessário.

## Tempo e perguntas

| Etapa | Tempo |
|---|---:|
| Exposição | 6min10 |
| Perguntas da turma | Até 1min |
| Total sugerido | Até 7min10 |

Perguntas prováveis para estudo: os registros são clientes da Ativa Solar? O GHI mede telhados? O que muda entre totais e razões por mil habitantes? A correlação prova causalidade? Por que não há série anual da ANEEL? Por que ainda não há prioridade comercial definitiva?

## Fontes internas

- [Perguntas, métricas e limitações](Perguntas_de_Negocio_Revisadas.md)
- [Notebook exploratório com tabelas e gráficos salvos](../Notebooks/Analise_Exploratoria_Ativa_Solar.ipynb)
- [Base integrada tratada e relatório de qualidade](../Base%20de%20dados/05_bases_tratadas/)
