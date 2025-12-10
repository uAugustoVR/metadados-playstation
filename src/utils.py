import pandas as pd

# Função para categorizar avaliações em faixas específicas
# As faixas são: Excelente (4.0-5.0), Bom (3.0-3.9), Regular (2.0-2.9), Ruim (0.0-1.9) e Sem Avaliação (nulo)
def rating_category(rating):
    if pd.isnull(rating):
        return 'Sem Avaliação'
    elif rating >= 4.0:
        return 'Excelente'
    elif rating >= 3.0:
        return 'Bom'
    elif rating >= 2.0:
        return 'Regular'
    else:
        return 'Ruim'
    
# Função para aplicar a categorização de avaliações a um DataFrame
def set_rating_category(df, column='Rating'):
    df['Rating Category'] = df[column].apply(rating_category)
    return df

# Função para extração do ano
def extract_year(df, column='Release Date'):
    df['Release Year'] = df[column].apply(
        lambda x: str(x).split('-')[0] if x != 'Unknown Date' else None
    )
    return df

