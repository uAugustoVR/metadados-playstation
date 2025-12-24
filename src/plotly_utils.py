import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import matplotlib.ticker as mticker

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
            'text': 'Percentual de Jogos de Alta Qualidade por Console PlayStation',
            'x': 0.5
        },
        yaxis=dict(
            range=[0, catalog_quality['pct_high_quality'].max() * 1.15],
            ticksuffix='%'
        ),
        height=500,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig