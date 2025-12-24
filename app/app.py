import pandas as pd
import seaborn as sns
import streamlit as st
from pathlib import Path
import matplotlib.pyplot as plt
from src import utils, data_utils, plotly_utils

sns.set_theme(
    style="dark",
    context="notebook",
    palette="viridis"
)

plt.rcParams.update({
    "figure.facecolor": "#0E1117",
    "axes.facecolor": "#0E1117",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "text.color": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "#333333"
})


# --- Configuração do path ---
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data/cleaned"

# --- Carregamento dos dados ---
df = pd.read_csv(DATA_DIR / "PlayStation_Metadata_treated.csv")

# --- Configuração da Página ---
st.set_page_config(
    page_title="Análise de Mercado PlayStation",
    layout="wide",
    page_icon="🎮"
)

# --- Pré-processamento adicional ---
df_base = df.copy()
df_analysis = utils.extract_genre(df_base)

# --- Barra Lateral (Filtros) ---
st.sidebar.header("Filtros")

console_filter = st.sidebar.multiselect(
    "Console",
    options=df_analysis["Console"].unique(),
    default=df_analysis["Console"].unique()
)

year_filter = st.sidebar.multiselect(
    'Ano',
    options=sorted(df_analysis['Release Year'].dropna().astype(int).unique()),
    default=sorted(df_analysis['Release Year'].dropna().astype(int).unique())
)

genre_filter = st.sidebar.multiselect(
    'Gênero',
    options=df_analysis['Genre List'].unique(),
    default=df_analysis['Genre List'].unique()
)

# --- Filtragem do DataFrame ---
df_filtered = df_analysis[
    (df_analysis['Console'].isin(console_filter)) &
    (
        df_analysis['Release Year'].isin(year_filter) |
        df_analysis['Release Year'].isna()
    ) &
    (df_analysis['Genre List'].isin(genre_filter))
]

# --- Conteúdo Principal ---
st.title("🎮 Análise de Mercado PlayStation")

st.markdown("""
### Sumário executivo
Análise do desempenho comercial e crítico dos jogos PlayStation (PS3, PS4 e PS5),
explorando a relação entre avaliações, vendas, gêneros e estratégias de mercado.
""")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas Principais")

if not df_filtered.empty:
    total_games = data_utils.total_games(df_filtered)
    average_rating = data_utils.avg_rating(df_filtered)
    threshold = data_utils.p90_sales(df_filtered)
else:
    total_games, average_rating, threshold = 0, 0.0, 0

col1, col2, col3 = st.columns(3)
col1.metric("Total de Jogos", total_games)
col2.metric("Avaliação Média", f"{average_rating:.2f}")
col3.metric("P90 de Vendas (milhões)", f"{threshold/1e6:g}M" if threshold else None)

st.markdown('---')

# --- Análises Visuais ---
st.subheader("Gráficos")

col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    if not df_filtered.empty:
        fig = plotly_utils.graph_metascore_sales(df_filtered, threshold)
        if fig:
            st.plotly_chart(fig, width="stretch")
    else:
        st.info("Nenhum dado disponível para o gráfico.")

with col_graph2:
    if not df_filtered.empty:
        fig = plotly_utils.graph_pct_high_quality(df_filtered)
        if fig:
            st.plotly_chart(fig, width="stretch")
    else:
        st.info("Nenhum dado disponível para o gráfico.")