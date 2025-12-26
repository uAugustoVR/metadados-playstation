import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from utils import utils, data_utils, plotly_utils

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

# --- Pré-processamento adicional ---
df = data_utils.load_data()
df_base = df.copy()
df_analysis = utils.extract_genre(df_base)

# --- Barra Lateral (Filtros) ---
st.sidebar.header("Filtros")
df_filtered = data_utils.render_main_filters(df_analysis)

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas Principais")
metrics = data_utils.get_main_metrics(df_filtered)
data_utils.render_main_metrics(metrics)

st.markdown('---')

# --- Análises Visuais ---
st.subheader("Gráficos")

col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    if not df_filtered.empty:
        threshold = data_utils.p90_sales(df_filtered)
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
