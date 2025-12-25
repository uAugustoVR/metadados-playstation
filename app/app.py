import streamlit as st

# Define as páginas
pg = st.navigation(
    pages=[
        st.Page("pages/overview.py", "Página Inicial"),
        st.Page("pages/market_trends.py", "Mercado & Tendências"),
        st.Page("pages/publishers.py", "Publishers")
    ]
)

pg.run()
