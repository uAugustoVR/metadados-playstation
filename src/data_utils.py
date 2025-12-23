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

