import pandas as pd
import plotly.express as px

# Função para criar o gráfico de dispersão Metascore vs Vendas Totais
def graph_metascore_sales(df, threshold):
    df_corr = df[
        (df['Has Score'] == 1) &
        (df['Total Sales'] > 0)
    ]

    fig = px.scatter(
        df_corr,
        x="Rating",
        y="Total Sales",
        opacity=0.6,
        template="plotly_dark",
        labels={
            "Rating": "Avaliação Média (Rating)",
            "Total Sales": "Vendas Totais (Milhões)"
        },
        title="Metascore vs Vendas com Threshold de Alto Desempenho"
    )

    # 🔴 Linha do percentil 90
    fig.add_hline(
        y=threshold,
        line_dash="dash",
        line_color="red",
        annotation_text=f"P90: {threshold/1e6:.2f}M",
        annotation_position="top left"
    )

    # 🎯 AJUSTE CRÍTICO DO EIXO Y
    fig.update_yaxes(
        tickformat=".2s",     # 1.5M, 2M, etc
        title="Vendas Totais (Milhões)",
        rangemode="tozero"
    )

    fig.update_xaxes(
        tickmode="linear",
        dtick=0.5
    )

    fig.update_layout(
        height=500,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig

# Função para criar o gráfico de percentual de jogos de alta qualidade
def graph_pct_high_quality(df_filtered):
    df_valid = df_filtered[df_filtered['Has Score'] == 1]

    if df_valid.empty:
        return None

    catalog_quality = (
        df_valid
        .groupby('Console')
        .apply(lambda x: (x['Rating'] >= 4.0).mean() * 100)
        .to_frame('pct_high_quality')
        .reset_index()
    )

    fig = px.bar(
        catalog_quality,
        x='Console',
        y='pct_high_quality',
        text='pct_high_quality',
        template='plotly_dark',
        labels={
            'Console': 'Console PlayStation',
            'pct_high_quality': 'Percentual de Jogos com Rating ≥ 4.0'
        }
    )

    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='outside'
    )

    fig.update_layout(
        title={
            'text': 'Percentual de Jogos de Alta Qualidade por Console PlayStation'
        },
        yaxis=dict(
            range=[0, catalog_quality['pct_high_quality'].max() * 1.15],
            ticksuffix='%'
        ),
        height=500,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig

# Função para criar o gráfico de evolução das vendas por gênero
def graph_genres_sales_evolution(df, top_n=5):
    year_genre_valid = (
        df
        .dropna(subset=['Release Year', 'Genre List'])
    )

    year_genre_valid = year_genre_valid[year_genre_valid['Sales Fraction'] > 0]

    evolution_genres_by_sales = (
        year_genre_valid
        .groupby(['Release Year', 'Genre List'])['Sales Fraction']
        .sum()
        .reset_index(name='Sales')
    )

    # Top N gêneros por vendas totais
    top_genres = (
        evolution_genres_by_sales
        .groupby('Genre List')['Sales']
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .index
    )

    df_top = evolution_genres_by_sales[
        evolution_genres_by_sales['Genre List'].isin(top_genres)
    ].copy()

    # Converte vendas para milhões (melhor controle do eixo)
    df_top['Sales (M)'] = df_top['Sales'] / 1e6

    fig = px.line(
        df_top,
        x='Release Year',
        y='Sales (M)',
        color='Genre List',
        markers=True,
        title=f'Evolução dos Top {top_n} Gêneros de Jogos PlayStation ao Longo dos Anos (por Vendas)',
        labels={
            'Release Year': 'Ano de Lançamento',
            'Sales (M)': 'Vendas Totais (em milhões)',
            'Genre List': 'Gênero'
        }
    )

    fig.update_layout(
        height=500,
        legend_title_text='Gênero',
        xaxis=dict(
            tickmode='linear'
        ),
        yaxis=dict(
            ticksuffix='M'
        ),
        margin=dict(l=40, r=40, t=80, b=40)
    )

    return fig

# Função para criar o gráfico de lançamentos por trimestre
def graph_quarterly_releases(df):
    # --- Pré-processamento ---
    df_time = df[df['Release Date'] != 'Unknown Date'].copy()

    df_time['Release Date'] = pd.to_datetime(
        df_time['Release Date'],
        errors='coerce'
    )
    df_time = df_time.dropna(subset=['Release Date'])

    # Extrai trimestre
    df_time['Quarter Num'] = df_time['Release Date'].dt.quarter

    # Agregação
    quarterly_releases = (
        df_time
        .groupby('Quarter Num')
        .size()
        .reset_index(name='Num Games')
    )

    # Labels amigáveis
    quarter_labels = {
        1: 'Q1 (Jan–Mar)',
        2: 'Q2 (Abr–Jun)',
        3: 'Q3 (Jul–Set)',
        4: 'Q4 (Out–Dez)'
    }

    quarterly_releases['Quarter'] = quarterly_releases['Quarter Num'].map(quarter_labels)

    # --- Gráfico ---
    fig = px.bar(
        quarterly_releases,
        x='Quarter',
        y='Num Games',
        title='Distribuição de Lançamentos por Trimestre',
        labels={
            'Quarter': 'Trimestre',
            'Num Games': 'Número de Jogos Lançados'
        },
        text='Num Games'
    )

    fig.update_layout(
        uniformtext_minsize=10,
        uniformtext_mode='hide',
        xaxis={'categoryorder': 'array', 'categoryarray': list(quarter_labels.values())},
        height=500,
        margin=dict(l=40, r=40, t=80, b=40)
    )

    return fig

# Função para criar o gráfico de avaliações por publisher
def graph_publisher_score(df):
    # --- Base consistente ---
    df_pub = df[
        (df['Has Score'] == 1) &
        (df['Publisher'] != 'Unknown')
    ].copy()

    # --- Conta jogos por publisher ---
    publisher_counts = df_pub.groupby('Publisher').size()

    # ⚠️ Mesmo threshold do notebook (ex: >= 20 ou >= 30)
    valid_publishers = publisher_counts[publisher_counts >= 20].index
    df_pub = df_pub[df_pub['Publisher'].isin(valid_publishers)]

    # --- Top 10 por mediana ---
    top_publishers = (
        df_pub
        .groupby('Publisher')['Rating']
        .median()
        .sort_values(ascending=False)
        .head(10)
        .index
    )

    df_pub = df_pub[df_pub['Publisher'].isin(top_publishers)]

    fig = px.box(
        df_pub,
        x='Publisher',
        y='Rating',
        category_orders={'Publisher': list(top_publishers)},
        points='outliers',
        title='Distribuição das Avaliações por Publisher (Top 10)'
    )

    # --- Ajustes visuais ---
    fig.update_layout(
        xaxis_title='Publisher',
        yaxis_title='Avaliação Média (Rating)',
        height=500,
        xaxis_tickangle=-45,
        margin=dict(l=40, r=40, t=80, b=40)
    )

    return fig

def graph_publishers_by_generation(df):
    # --- Base consistente ---
    publisher_generation_counts = (
        df[df['Publisher'] != 'Unknown']
        .groupby(['Console', 'Publisher'])
        .size()
        .reset_index(name='Num Published')
    )

    # Publisher com mais lançamentos por console
    top_publisher_by_generation = (
        publisher_generation_counts.loc[
            publisher_generation_counts
            .groupby('Console')['Num Published']
            .idxmax()
        ]
    )

    # --- Gráfico ---
    fig = px.bar(
        top_publisher_by_generation,
        x='Console',
        y='Num Published',
        text='Publisher',
        title='Publisher com Maior Número de Lançamentos por Geração PlayStation'
    )

    # --- Ajustes visuais ---
    fig.update_traces(
        textposition='outside'
    )

    fig.update_layout(
        xaxis_title='Console PlayStation',
        yaxis_title='Número de Jogos Lançados',
        height=500,
        margin=dict(l=40, r=40, t=80, b=40)
    )

    return fig