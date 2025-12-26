import streamlit as st

page_home = st.Page(
    page='views/home.py',
    title='Página Inicial',
    icon='🏠',
    default=True
)

page_overview = st.Page(
    page='views/overviews.py',
    title='Visão Geral',
    icon='📊'
)

page_market_trends = st.Page(
    page='views/market_trends.py',
    title='Mercado & Tendências',
    icon='📈'
)

page_publishers = st.Page(
    page='views/publishers.py',
    title='Publishers',
    icon='🏢'
)

# Define as páginas
pg = st.navigation(
    {
        'Info': [page_home],
        'Projetos': [page_overview, page_market_trends, page_publishers]
    }
)

# --- Configuração da Página ---
st.set_page_config(
    page_title="Análise de Mercado PlayStation",
    layout="wide",
    page_icon="🎮"
)

# --- Conteúdo Principal ---
st.title("🎮 PlayStation Sales & Metadata")

st.markdown("""
## Visão Geral do Projeto

Esta análise explora a relação entre **qualidade**, **vendas** e **estratégia de mercado** nos consoles **PlayStation (PS3, PS4 e PS5)**, utilizando dados históricos de vendas, avaliações e metadados de jogos.

O objetivo é entender **o sucesso comercial da marca**, indo além da percepção comum de que boas avaliações garantem altas vendas.

---
""")

pg.run()
