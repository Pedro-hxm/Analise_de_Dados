"""Dashboard exploratória municipal da Ativa Solar."""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "Base de dados" / "05_bases_tratadas" / "base_integrada_limpa.csv"
MESES = {
    "jan": "Jan", "feb": "Fev", "mar": "Mar", "apr": "Abr",
    "may": "Mai", "jun": "Jun", "jul": "Jul", "aug": "Ago",
    "sep": "Set", "oct": "Out", "nov": "Nov", "dec": "Dez",
}
COLUNAS_MES = [f"ghi_{mes}_Wh_m2_day" for mes in MESES]
COLUNAS_PUBLICO_PENDENTE = [
    "domicilios_ocupados_2022",
    "estabelecimentos_ativos_cnae_selecionados",
    "atendimento_confirmado",
]
COLUNAS_OBRIGATORIAS = [
    "uf", "codigo_ibge", "municipio", "populacao_estimada_2026",
    "ghi_latitude", "ghi_longitude",
    "ghi_annual_Wh_m2_day", *COLUNAS_MES,
    "gd_fv_instalacoes", "gd_fv_potencia_instalada_kw",
    "gd_fv_kw_por_1000_hab", "gd_fv_instalacoes_por_1000_hab",
    *COLUNAS_PUBLICO_PENDENTE,
]
INDICADORES_MAPA = {
    "GHI anual (Wh/m².dia)": "ghi_annual_Wh_m2_day",
    "Instalações fotovoltaicas ANEEL": "gd_fv_instalacoes",
    "Potência registrada pela ANEEL (kW)": "gd_fv_potencia_instalada_kw",
    "Instalações por 1.000 habitantes": "gd_fv_instalacoes_por_1000_hab",
    "Potência por 1.000 habitantes": "gd_fv_kw_por_1000_hab",
}
INDICADOR_VAZIO = "Selecione um indicador"

st.set_page_config(
    page_title="Inteligência Comercial Geográfica — Ativa Solar",
    page_icon="☀️",
    layout="wide",
)


@st.cache_data
def carregar_base() -> pd.DataFrame:
    if not BASE_PATH.is_file():
        raise FileNotFoundError(f"Base tratada não encontrada: {BASE_PATH}")

    dados = pd.read_csv(
        BASE_PATH,
        sep=";",
        decimal=",",
        encoding="utf-8-sig",
        dtype={"codigo_ibge": "string"},
    )
    faltantes = sorted(set(COLUNAS_OBRIGATORIAS) - set(dados.columns))
    if faltantes:
        raise ValueError("Colunas ausentes na base tratada: " + ", ".join(faltantes))
    if dados["codigo_ibge"].nunique(dropna=True) != 12 or len(dados) != 12:
        raise ValueError("A base deve conter exatamente os 12 municípios do recorte.")
    return dados


def formatar_numero(valor: object, casas: int = 0) -> str:
    if pd.isna(valor):
        return "—"
    return f"{float(valor):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def total_completo(dados: pd.DataFrame, coluna: str, casas: int = 0) -> str:
    valores = dados[coluna]
    if valores.empty or valores.isna().any():
        return "Pendente"
    return formatar_numero(valores.sum(), casas)


def normalizar_atendimento(valor: object) -> bool | None:
    if pd.isna(valor):
        return None
    normalizado = str(valor).strip().casefold()
    if normalizado in {"sim", "s", "true", "1", "confirmado"}:
        return True
    if normalizado in {"não", "nao", "n", "false", "0", "não atendido", "nao atendido"}:
        return False
    return None


def publico_atendido(dados: pd.DataFrame, coluna: str) -> str:
    status = dados["atendimento_confirmado"].map(normalizar_atendimento)
    if status.isna().any():
        return "Pendente"
    atendidos = dados.loc[status]
    if atendidos.empty:
        return "Sem municípios confirmados"
    return total_completo(atendidos, coluna)


def figura_barra(dados: pd.DataFrame, coluna: str, titulo: str, eixo: str, casas: int = 0):
    figura = px.bar(
        dados.sort_values(coluna, ascending=False),
        x="municipio",
        y=coluna,
        color="uf",
        hover_data={"codigo_ibge": True, "uf": True, coluna: f":,.{casas}f"},
        labels={"municipio": "Município", "uf": "UF", coluna: eixo},
        title=titulo,
        color_discrete_map={"PE": "#138A58", "PB": "#E4A11B"},
    )
    figura.update_layout(
        xaxis_title=None,
        yaxis_title=eixo,
        legend_title_text="Estado",
        separators=",.",
        margin={"l": 12, "r": 12, "t": 55, "b": 12},
    )
    figura.update_xaxes(tickangle=-25)
    return figura


with st.container():
    st.title("Inteligência Comercial Geográfica — Ativa Solar")
    st.caption("Triagem exploratória de 12 municípios de Pernambuco e Paraíba")
    st.info(
        "Esta dashboard compara indicadores públicos municipais. Ela não comprova demanda, "
        "não identifica clientes da Ativa Solar e não estima vendas ou faturamento."
    )

try:
    df = carregar_base()
except (FileNotFoundError, ValueError, OSError) as erro:
    st.error(f"Não foi possível carregar a base tratada. {erro}")
    st.stop()

ufs_disponiveis = sorted(df["uf"].dropna().unique().tolist())

if "filtro_ufs" not in st.session_state:
    st.session_state["filtro_ufs"] = ufs_disponiveis

st.subheader("Filtros do recorte")
with st.expander("Filtrar indicadores", expanded=True):
    filtros = st.columns(
        [1, 2, 2],
        gap="small",
        vertical_alignment="bottom",
        wrap=True,
    )
    with filtros[0]:
        ufs = st.multiselect(
            "Estado",
            options=ufs_disponiveis,
            key="filtro_ufs",
        )

    opcoes_municipios = sorted(
        df.loc[df["uf"].isin(ufs), "municipio"].dropna().unique().tolist()
    )
    municipios_atuais = st.session_state.get("filtro_municipios")
    if municipios_atuais is None:
        st.session_state["filtro_municipios"] = opcoes_municipios
    else:
        st.session_state["filtro_municipios"] = [
            municipio
            for municipio in municipios_atuais
            if municipio in opcoes_municipios
        ]

    with filtros[1]:
        municipios = st.multiselect(
            "Município",
            options=opcoes_municipios,
            key="filtro_municipios",
        )

    opcoes_indicador = [INDICADOR_VAZIO, *INDICADORES_MAPA]
    if st.session_state.get("indicador_mapa") not in opcoes_indicador:
        st.session_state["indicador_mapa"] = INDICADOR_VAZIO
    with filtros[2]:
        indicador_mapa = st.selectbox(
            "Indicador",
            options=opcoes_indicador,
            key="indicador_mapa",
        )

    if indicador_mapa == INDICADOR_VAZIO:
        st.caption("Sem indicador selecionado, o mapa distingue apenas os estados.")
    else:
        st.caption(f"A cor dos pontos representa: {indicador_mapa}.")

selecionados = df.loc[df["uf"].isin(ufs) & df["municipio"].isin(municipios)].copy()

if selecionados.empty:
    st.warning("Selecione ao menos um município para visualizar os indicadores.")
    st.stop()

st.subheader("Visão geral do recorte selecionado")
kpis = st.columns(4)
kpis[0].metric("Municípios", formatar_numero(len(selecionados)))
kpis[1].metric(
    "População estimada (2026)",
    total_completo(selecionados, "populacao_estimada_2026"),
)
kpis[2].metric(
    "Instalações FV registradas", total_completo(selecionados, "gd_fv_instalacoes")
)
kpis[3].metric(
    "Potência FV registrada (kW)",
    total_completo(selecionados, "gd_fv_potencia_instalada_kw", casas=2),
)
st.caption(
    "A população é apresentada como contexto demográfico e não substitui domicílios ocupados. "
    "Os totais da ANEEL descrevem geração distribuída registrada nos municípios."
)

with st.container():
    st.subheader("Mapa das sedes municipais")
    coluna_metrica = INDICADORES_MAPA.get(indicador_mapa)
    color_mapa = coluna_metrica if coluna_metrica else "uf"
    labels_mapa = {
        "municipio": "Município",
        "uf": "UF",
        "codigo_ibge": "Código IBGE",
        "ghi_latitude": "Latitude da sede",
        "ghi_longitude": "Longitude da sede",
    }
    if coluna_metrica:
        labels_mapa[coluna_metrica] = indicador_mapa

    figura_mapa = px.scatter_map(
        selecionados,
        lat="ghi_latitude",
        lon="ghi_longitude",
        color=color_mapa,
        hover_name="municipio",
        hover_data={
            "uf": True,
            "codigo_ibge": True,
            "ghi_latitude": ":.4f",
            "ghi_longitude": ":.4f",
        },
        labels=labels_mapa,
        color_discrete_map={"PE": "#138A58", "PB": "#E4A11B"}
        if not coluna_metrica
        else None,
        color_continuous_scale="Viridis" if coluna_metrica else None,
        map_style="open-street-map",
        center={
            "lat": float(selecionados["ghi_latitude"].mean()),
            "lon": float(selecionados["ghi_longitude"].mean()),
        },
        zoom=7,
        height=390,
    )
    figura_mapa.update_layout(
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
        legend_title_text="UF" if not coluna_metrica else None,
    )
    st.plotly_chart(
        figura_mapa,
        width="stretch",
        config={"scrollZoom": False},
        key="mapa_sedes_municipais",
        alt="Mapa com pontos nas coordenadas das sedes dos municípios selecionados.",
    )
    st.caption(
        "Cada ponto usa a coordenada da sede municipal do INPE; não representa o limite do município nem mede telhados. "
        "O mapa-base do OpenStreetMap requer conexão à internet."
    )

st.subheader("Públicos e área atendida")
status_atendimento = selecionados["atendimento_confirmado"].map(normalizar_atendimento)
if status_atendimento.isna().any():
    total_atendimento = "Pendente"
else:
    total_atendimento = (
        f"{int(status_atendimento.sum())}/{len(selecionados)} confirmados"
    )
publicos = st.columns(3)
publicos[0].metric(
    "Domicílios ocupados — Censo 2022",
    publico_atendido(selecionados, "domicilios_ocupados_2022"),
)
publicos[1].metric(
    "Estabelecimentos ativos nos CNAEs",
    publico_atendido(selecionados, "estabelecimentos_ativos_cnae_selecionados"),
)
publicos[2].metric("Confirmação de atendimento", total_atendimento)
st.warning(
    "Os públicos residencial e empresarial são totalizados somente para municípios com atendimento "
    "confirmado. Se houver informação ausente, o resultado aparece como pendente; campos vazios não são zero."
)

st.subheader("Irradiação global horizontal — GHI")
col_ghi_anual, col_ghi_mensal = st.columns(2)
with col_ghi_anual:
    st.plotly_chart(
        figura_barra(
            selecionados,
            "ghi_annual_Wh_m2_day",
            "GHI médio diário anual por sede municipal",
            "Wh/m².dia",
        ),
        use_container_width=True,
    )

with col_ghi_mensal:
    mensal = selecionados[["municipio", "uf", *COLUNAS_MES]].melt(
        id_vars=["municipio", "uf"],
        var_name="mes",
        value_name="ghi_Wh_m2_day",
    )
    mensal["Mês"] = mensal["mes"].str.extract(r"ghi_(\w+)_")[0].map(MESES)
    mensal["Mês"] = pd.Categorical(
        mensal["Mês"], categories=list(MESES.values()), ordered=True
    )
    fig_mensal = px.line(
        mensal.sort_values("Mês"),
        x="Mês",
        y="ghi_Wh_m2_day",
        color="municipio",
        line_dash="uf",
        markers=True,
        labels={"ghi_Wh_m2_day": "Wh/m².dia", "municipio": "Município", "uf": "UF"},
        title="Variação mensal histórica entre as sedes",
    )
    fig_mensal.update_layout(
        separators=",.",
        legend_title_text="Município / estado",
        margin={"l": 12, "r": 12, "t": 55, "b": 12},
    )
    st.plotly_chart(fig_mensal, use_container_width=True)

st.caption(
    "GHI do Atlas Brasileiro de Energia Solar (INPE/LABREN, 2ª edição, 2017): "
    "referência histórica da série 1999–2015 para as sedes municipais, em médias diárias. "
    "Não é medição de telhados ou imóveis específicos."
)

st.subheader("Geração distribuída fotovoltaica registrada pela ANEEL")
col_instalacoes, col_potencia = st.columns(2)
with col_instalacoes:
    st.plotly_chart(
        figura_barra(
            selecionados,
            "gd_fv_instalacoes",
            "Instalações fotovoltaicas registradas",
            "Instalações",
        ),
        use_container_width=True,
    )
with col_potencia:
    st.plotly_chart(
        figura_barra(
            selecionados,
            "gd_fv_potencia_instalada_kw",
            "Potência fotovoltaica instalada registrada",
            "Potência (kW)",
            casas=2,
        ),
        use_container_width=True,
    )

razoes = st.columns(2)
with razoes[0]:
    st.plotly_chart(
        figura_barra(
            selecionados,
            "gd_fv_instalacoes_por_1000_hab",
            "Instalações por 1.000 habitantes",
            "Instalações por 1.000 habitantes",
            casas=2,
        ),
        use_container_width=True,
    )
with razoes[1]:
    st.plotly_chart(
        figura_barra(
            selecionados,
            "gd_fv_kw_por_1000_hab",
            "Potência por 1.000 habitantes",
            "kW por 1.000 habitantes",
            casas=2,
        ),
        use_container_width=True,
    )

fig_associacao = px.scatter(
    selecionados,
    x="populacao_estimada_2026",
    y="gd_fv_instalacoes",
    color="uf",
    hover_name="municipio",
    hover_data={"codigo_ibge": True, "gd_fv_potencia_instalada_kw": ":,.2f"},
    labels={
        "populacao_estimada_2026": "População estimada (habitantes)",
        "gd_fv_instalacoes": "Instalações fotovoltaicas registradas",
        "uf": "Estado",
    },
    title="População estimada e instalações registradas",
    color_discrete_map={"PE": "#138A58", "PB": "#E4A11B"},
)
fig_associacao.update_layout(
    separators=",.", margin={"l": 12, "r": 12, "t": 55, "b": 12}
)
st.plotly_chart(fig_associacao, use_container_width=True)
st.caption(
    "Associação descritiva entre municípios; pode refletir diferenças de escala e não indica causalidade. "
    "Os indicadores por mil habitantes são razões, não percentuais de domicílios com energia solar."
)
st.caption(
    "ANEEL: fotografia municipal com referência em 10/11/2026. A evolução anual não está disponível "
    "e depende de registros com datas de conexão. Os dados não representam clientes ou vendas da Ativa Solar."
)

st.subheader("Dados do recorte selecionado")
colunas_tabela = [
    "uf", "codigo_ibge", "municipio", "populacao_estimada_2026",
    "ghi_annual_Wh_m2_day", "gd_fv_instalacoes", "gd_fv_potencia_instalada_kw",
    "domicilios_ocupados_2022", "estabelecimentos_ativos_cnae_selecionados",
    "atendimento_confirmado",
]
tabela = selecionados[colunas_tabela].rename(
    columns={
        "uf": "UF",
        "codigo_ibge": "Código IBGE",
        "municipio": "Município",
        "populacao_estimada_2026": "População estimada (2026)",
        "ghi_annual_Wh_m2_day": "GHI anual (Wh/m².dia)",
        "gd_fv_instalacoes": "Instalações ANEEL",
        "gd_fv_potencia_instalada_kw": "Potência ANEEL (kW)",
        "domicilios_ocupados_2022": "Domicílios ocupados (Censo 2022)",
        "estabelecimentos_ativos_cnae_selecionados": "Estabelecimentos ativos (CNAEs)",
        "atendimento_confirmado": "Atendimento confirmado",
    }
).copy()
for coluna in [
    "Domicílios ocupados (Censo 2022)",
    "Estabelecimentos ativos (CNAEs)",
    "Atendimento confirmado",
]:
    tabela[coluna] = tabela[coluna].where(tabela[coluna].notna(), "Pendente")
st.dataframe(tabela, hide_index=True, use_container_width=True)

st.subheader("Como interpretar")
st.markdown(
    "- A dashboard organiza indicadores públicos para uma **triagem exploratória**, não uma decisão comercial.\n"
    "- GHI é uma referência histórica das sedes; não estima a geração de telhados específicos.\n"
    "- ANEEL descreve geração distribuída registrada nos municípios, sem identificar clientes da Ativa Solar.\n"
    "- Baixa adoção solar, isoladamente, não comprova oportunidade.\n"
    "- Uma lista para validação comercial depende da confirmação da área atendida e dos dados de público residencial e empresarial."
)
