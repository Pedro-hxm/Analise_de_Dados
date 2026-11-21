# Relatório de qualidade — base integrada Ativa Solar

- Execução: 2026-11-20T21:22:27-03:00 (America/Fortaleza)
- Responsável: Equipe do projeto (identificação individual não informada)
- Municípios exportados: 12
- Chave: codigo_ibge, preservado como texto.

## Fontes e referências

- INPE/LABREN, Atlas Brasileiro de Energia Solar (2017), série histórica descrita como 1999–2015; valores de irradiação em Wh/m².dia.
- ANEEL, agregados municipais de MMGD fotovoltaica com referência em 10/11/2026; contagens e potência não representam vendas da Ativa Solar.
- IBGE, estimativa populacional de 2026, referência em 01/07/2026.
- Domicílios do Censo 2022, estabelecimentos por CNAE/CNPJ e confirmação da área de atendimento continuam pendentes.

## Granularidade e junções

Cada fonte foi conferida para uma linha por código IBGE. Não houve remoção ou agregação adicional de linhas.

| base | linhas | codigos_unicos | linhas_duplicadas | codigos_ausentes | codigos_extras |
| --- | --- | --- | --- | --- | --- |
| INPE | 12 | 12 | 0 | 0 | 0 |
| ANEEL | 12 | 12 | 0 | 0 | 0 |
| IBGE | 12 | 12 | 0 | 0 | 0 |
| Integrada | 12 | 12 | 0 | 0 | 0 |

Junções realizadas por codigo_ibge com validação um-para-um e indicador de correspondência:

| fonte | linhas_referencia | correspondencias | sem_correspondencia |
| --- | --- | --- | --- |
| IBGE | 12 | 12 | 0 |
| INPE | 12 | 12 | 0 |
| ANEEL | 12 | 12 | 0 |
| campos pendentes da base integrada atual | 12 | 12 | 0 |

## Validação de valores e ausências

Valores numéricos foram verificados quanto a ausências inesperadas, conversão numérica, valores não finitos, contagens, sinais, coordenadas e meses esperados. Os extremos de irradiação foram registrados para conferência; não foram aplicados limites arbitrários nem correções sem evidência.

| base | variaveis_numericas | ausencias | valores_nao_numericos | valores_nao_finitos |
| --- | --- | --- | --- | --- |
| ANEEL | 3 | 0 | 0 | 0 |
| IBGE | 1 | 0 | 0 | 0 |
| INPE | 30 | 0 | 0 | 0 |
| Integrada | 36 | 0 | 0 | 0 |

Auditoria numérica por variável, incluindo ausências, extremos observados e situação:

| base | coluna | ausentes | não_numéricos | não_finitos | mínimo | máximo | situação |
| --- | --- | --- | --- | --- | --- | --- | --- |
| INPE | ghi_longitude | 0 | 0 | 0 | -35.1125 | -34.8154 | válido |
| INPE | ghi_latitude | 0 | 0 | 0 | -7.9038 | -7.1159 | válido |
| INPE | ghi_annual_Wh_m2_day | 0 | 0 | 0 | 5292.0 | 5532.0 | válido |
| INPE | ghi_jan_Wh_m2_day | 0 | 0 | 0 | 5716.0 | 5940.0 | válido |
| INPE | ghi_feb_Wh_m2_day | 0 | 0 | 0 | 5881.0 | 6127.0 | válido |
| INPE | ghi_mar_Wh_m2_day | 0 | 0 | 0 | 5834.0 | 6088.0 | válido |
| INPE | ghi_apr_Wh_m2_day | 0 | 0 | 0 | 5136.0 | 5365.0 | válido |
| INPE | ghi_may_Wh_m2_day | 0 | 0 | 0 | 4471.0 | 4823.0 | válido |
| INPE | ghi_jun_Wh_m2_day | 0 | 0 | 0 | 4161.0 | 4366.0 | válido |
| INPE | ghi_jul_Wh_m2_day | 0 | 0 | 0 | 4269.0 | 4489.0 | válido |
| INPE | ghi_aug_Wh_m2_day | 0 | 0 | 0 | 4998.0 | 5261.0 | válido |
| INPE | ghi_sep_Wh_m2_day | 0 | 0 | 0 | 5405.0 | 5758.0 | válido |
| INPE | ghi_oct_Wh_m2_day | 0 | 0 | 0 | 5686.0 | 6071.0 | válido |
| INPE | ghi_nov_Wh_m2_day | 0 | 0 | 0 | 5985.0 | 6243.0 | válido |
| INPE | ghi_dec_Wh_m2_day | 0 | 0 | 0 | 5966.0 | 6256.0 | válido |
| INPE | gti10_longitude | 0 | 0 | 0 | -35.1125 | -34.8154 | válido |
| INPE | gti10_latitude | 0 | 0 | 0 | -7.9038 | -7.1159 | válido |
| INPE | gti10_annual_Wh_m2_day | 0 | 0 | 0 | 5296.0 | 5536.0 | válido |
| INPE | gti10_jan_Wh_m2_day | 0 | 0 | 0 | 5437.0 | 5645.0 | válido |
| INPE | gti10_feb_Wh_m2_day | 0 | 0 | 0 | 5713.0 | 5953.0 | válido |
| INPE | gti10_mar_Wh_m2_day | 0 | 0 | 0 | 5832.0 | 6087.0 | válido |
| INPE | gti10_apr_Wh_m2_day | 0 | 0 | 0 | 5296.0 | 5511.0 | válido |
| INPE | gti10_may_Wh_m2_day | 0 | 0 | 0 | 4721.0 | 5068.0 | válido |
| INPE | gti10_jun_Wh_m2_day | 0 | 0 | 0 | 4440.0 | 4650.0 | válido |
| INPE | gti10_jul_Wh_m2_day | 0 | 0 | 0 | 4530.0 | 4764.0 | válido |
| INPE | gti10_aug_Wh_m2_day | 0 | 0 | 0 | 5200.0 | 5456.0 | válido |
| INPE | gti10_sep_Wh_m2_day | 0 | 0 | 0 | 5448.0 | 5798.0 | válido |
| INPE | gti10_oct_Wh_m2_day | 0 | 0 | 0 | 5568.0 | 5944.0 | válido |
| INPE | gti10_nov_Wh_m2_day | 0 | 0 | 0 | 5726.0 | 5990.0 | válido |
| INPE | gti10_dec_Wh_m2_day | 0 | 0 | 0 | 5635.0 | 5895.0 | válido |
| ANEEL | gd_fv_instalacoes | 0 | 0 | 0 | 122.0 | 10448.0 | válido |
| ANEEL | gd_fv_potencia_instalada_kw | 0 | 0 | 0 | 1213.37 | 118223.3 | válido |
| ANEEL | gd_fv_ucs_com_credito | 0 | 0 | 0 | 191.0 | 16630.0 | válido |
| IBGE | populacao_estimada_2026 | 0 | 0 | 0 | 17168.0 | 906093.0 | válido |
| Integrada | ghi_longitude | 0 | 0 | 0 | -35.1125 | -34.8154 | válido |
| Integrada | ghi_latitude | 0 | 0 | 0 | -7.9038 | -7.1159 | válido |
| Integrada | ghi_annual_Wh_m2_day | 0 | 0 | 0 | 5292.0 | 5532.0 | válido |
| Integrada | ghi_jan_Wh_m2_day | 0 | 0 | 0 | 5716.0 | 5940.0 | válido |
| Integrada | ghi_feb_Wh_m2_day | 0 | 0 | 0 | 5881.0 | 6127.0 | válido |
| Integrada | ghi_mar_Wh_m2_day | 0 | 0 | 0 | 5834.0 | 6088.0 | válido |
| Integrada | ghi_apr_Wh_m2_day | 0 | 0 | 0 | 5136.0 | 5365.0 | válido |
| Integrada | ghi_may_Wh_m2_day | 0 | 0 | 0 | 4471.0 | 4823.0 | válido |
| Integrada | ghi_jun_Wh_m2_day | 0 | 0 | 0 | 4161.0 | 4366.0 | válido |
| Integrada | ghi_jul_Wh_m2_day | 0 | 0 | 0 | 4269.0 | 4489.0 | válido |
| Integrada | ghi_aug_Wh_m2_day | 0 | 0 | 0 | 4998.0 | 5261.0 | válido |
| Integrada | ghi_sep_Wh_m2_day | 0 | 0 | 0 | 5405.0 | 5758.0 | válido |
| Integrada | ghi_oct_Wh_m2_day | 0 | 0 | 0 | 5686.0 | 6071.0 | válido |
| Integrada | ghi_nov_Wh_m2_day | 0 | 0 | 0 | 5985.0 | 6243.0 | válido |
| Integrada | ghi_dec_Wh_m2_day | 0 | 0 | 0 | 5966.0 | 6256.0 | válido |
| Integrada | gti10_longitude | 0 | 0 | 0 | -35.1125 | -34.8154 | válido |
| Integrada | gti10_latitude | 0 | 0 | 0 | -7.9038 | -7.1159 | válido |
| Integrada | gti10_annual_Wh_m2_day | 0 | 0 | 0 | 5296.0 | 5536.0 | válido |
| Integrada | gti10_jan_Wh_m2_day | 0 | 0 | 0 | 5437.0 | 5645.0 | válido |
| Integrada | gti10_feb_Wh_m2_day | 0 | 0 | 0 | 5713.0 | 5953.0 | válido |
| Integrada | gti10_mar_Wh_m2_day | 0 | 0 | 0 | 5832.0 | 6087.0 | válido |
| Integrada | gti10_apr_Wh_m2_day | 0 | 0 | 0 | 5296.0 | 5511.0 | válido |
| Integrada | gti10_may_Wh_m2_day | 0 | 0 | 0 | 4721.0 | 5068.0 | válido |
| Integrada | gti10_jun_Wh_m2_day | 0 | 0 | 0 | 4440.0 | 4650.0 | válido |
| Integrada | gti10_jul_Wh_m2_day | 0 | 0 | 0 | 4530.0 | 4764.0 | válido |
| Integrada | gti10_aug_Wh_m2_day | 0 | 0 | 0 | 5200.0 | 5456.0 | válido |
| Integrada | gti10_sep_Wh_m2_day | 0 | 0 | 0 | 5448.0 | 5798.0 | válido |
| Integrada | gti10_oct_Wh_m2_day | 0 | 0 | 0 | 5568.0 | 5944.0 | válido |
| Integrada | gti10_nov_Wh_m2_day | 0 | 0 | 0 | 5726.0 | 5990.0 | válido |
| Integrada | gti10_dec_Wh_m2_day | 0 | 0 | 0 | 5635.0 | 5895.0 | válido |
| Integrada | populacao_estimada_2026 | 0 | 0 | 0 | 17168.0 | 906093.0 | válido |
| Integrada | gd_fv_instalacoes | 0 | 0 | 0 | 122.0 | 10448.0 | válido |
| Integrada | gd_fv_potencia_instalada_kw | 0 | 0 | 0 | 1213.37 | 118223.3 | válido |
| Integrada | gd_fv_ucs_com_credito | 0 | 0 | 0 | 191.0 | 16630.0 | válido |
| Integrada | gd_fv_kw_por_1000_hab | 0 | 0 | 0 | 55.12 | 363.88 | válido |
| Integrada | gd_fv_instalacoes_por_1000_hab | 0 | 0 | 0 | 5.23 | 36.08 | válido |

Campos sem coleta ou confirmação permanecem vazios e classificados separadamente:

| campo | ausentes | total_municípios | classificação |
| --- | --- | --- | --- |
| domicilios_ocupados_2022 | 12 | 12 | não coletado |
| estabelecimentos_ativos_cnae_selecionados | 12 | 12 | não coletado |
| atendimento_confirmado | 12 | 12 | pendente de confirmação |
| ano_referencia_domicilios | 12 | 12 | não coletado |
| data_referencia_cnpj | 12 | 12 | não coletado |

Nenhuma ausência foi convertida em zero. Zeros existentes nas fontes são mantidos como valores observados. Os campos atuais não foram classificados como “não disponível na fonte” ou “não se aplica”; essas categorias permanecem distintas de “não coletado” e “pendente”. Nenhum valor foi imputado ou corrigido sem confirmação na fonte.

## Indicadores recalculados

- gd_fv_kw_por_1000_hab = potência instalada em kW / população estimada × 1.000.
- gd_fv_instalacoes_por_1000_hab = instalações / população estimada × 1.000.
- Ambos foram arredondados a duas casas decimais e comparados aos valores existentes.

| indicador | municípios_comparados | divergências_após_arredondar_2_casas |
| --- | --- | --- |
| gd_fv_kw_por_1000_hab | 12 | 0 |
| gd_fv_instalacoes_por_1000_hab | 12 | 0 |

Essas razões descrevem a presença municipal de geração distribuída. Não medem clientes, vendas, faturamento, crescimento anual ou potencial de mercado da empresa.

## Dicionário, unidades e limitações

O arquivo dicionario_base_integrada.csv registra definição, unidade, fonte, período de referência e limitações de cada campo exportado. A irradiação representa a referência histórica nas coordenadas municipais, não a média de todos os imóveis ou o desempenho de um telhado. O rótulo GTI10 deve ser interpretado conforme os metadados do Atlas.

## Alterações e exportação

- Fontes originais mantidas intactas.
- Nenhuma linha descartada ou somada.
- Indicadores derivados recalculados; não foram encontradas divergências após arredondamento a duas casas.
- Campos pendentes preservados como ausentes.
- Saídas: base_integrada_limpa.csv, dicionario_base_integrada.csv e este relatório.
