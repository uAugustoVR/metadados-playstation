def get_avg_rating(df):
    return df[df['Has Score'] == 1]['Rating'].median()

def p90_sales(filtered_df):
    df_valid = filtered_df[filtered_df['Total Sales'] > 0]

    if df_valid.empty:
        return None

    return df_valid['Total Sales'].quantile(0.9)

