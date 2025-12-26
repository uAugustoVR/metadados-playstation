import pandas as pd
import streamlit as st
from pathlib import Path

# Funções para cálculo de métricas a partir do DataFrame filtrado
def total_games(filtered_df):
    return filtered_df['Name'].nunique()

def avg_rating(filtered_df):
    filtered_df[filtered_df['Has Score'] == 1].groupby('Console')

    return filtered_df['Rating'].median()

def p90_sales(filtered_df):
    df_valid = filtered_df[filtered_df['Total Sales'] > 0]

    if df_valid.empty:
        return None

    return df_valid['Total Sales'].quantile(0.9)

def total_sales(filtered_df):
    df_valid = filtered_df[filtered_df['Total Sales'] > 0]

    if df_valid.empty:
        return None

    return df_valid['Total Sales'].sum()


def load_data():
    """
    Carrega e prepara o dataset principal do projeto.
    Retorna o DataFrame base (df_all).
    """

    # --- Caminhos ---
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data" / "cleaned"
    DATA_FILE = DATA_DIR / "PlayStation_Metadata_treated.csv"

    # --- Leitura ---
    df = pd.read_csv(DATA_FILE)

    # --- Tipagem básica ---
    if 'Release Year' in df.columns:
        df['Release Year'] = pd.to_numeric(df['Release Year'], errors='coerce')

    if 'Rating' in df.columns:
        df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

    if 'Total Sales' in df.columns:
        df['Total Sales'] = pd.to_numeric(df['Total Sales'], errors='coerce')

    # --- Garantias mínimas ---
    if 'Has Score' not in df.columns:
        df['Has Score'] = df['Rating'].notna().astype(int)

    # --- Normalização leve de strings ---
    for col in ['Console', 'Publisher', 'Developer', 'Genres']:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    return df

def get_main_metrics(df: pd.DataFrame) -> dict:
    """
    Calcula as métricas principais do dashboard.
    Retorna um dicionário pronto para uso no Streamlit.
    """

    metrics = {
        "total_games": total_games(df),
        "avg_score": avg_rating(df) if "Rating" in df.columns else None,
        "total_sales": total_sales(df) if "Total Sales" in df.columns else None,
        "p90_sales": p90_sales(df) if "Total Sales" in df.columns else None
    }

    return metrics

def render_main_metrics(metrics: dict):
    avg_score = metrics["avg_score"]
    total_sales = metrics["total_sales"]
    p90_sales = metrics["p90_sales"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🎮 Jogos", metrics["total_games"])
    col2.metric("⭐ Avaliação Média", f"{avg_score:.2f}" if avg_score is not None else "N/A")
    col3.metric("💰 Vendas (B)", f"{total_sales/1e9:.2f}B" if total_sales is not None else "N/A")
    col4.metric("💰 P90 de Vendas (M)", f"{p90_sales/1e6:g}M" if p90_sales is not None else "N/A")

def render_main_filters(df: pd.DataFrame) -> dict:
    console_filter = st.sidebar.multiselect(
    "Console",
    options=df["Console"].unique(),
    default=df["Console"].unique()
    )

    year_filter = st.sidebar.multiselect(
        'Ano',
        options=sorted(df['Release Year'].dropna().astype(int).unique()),
        default=sorted(df['Release Year'].dropna().astype(int).unique())
    )

    genre_filter = st.sidebar.multiselect(
        'Gênero',
        options=df['Genre List'].unique(),
        default=df['Genre List'].unique()
    )

    # --- Filtragem do DataFrame ---
    df_filtered = df[
        (df['Console'].isin(console_filter)) &
        (
            df['Release Year'].isin(year_filter) |
            df['Release Year'].isna()
        ) &
        (df['Genre List'].isin(genre_filter))
    ]

    return df_filtered