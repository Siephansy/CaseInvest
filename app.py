import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.set_page_config(page_title="Análise de Investimento - Case McDonald's", layout="centered")
st.markdown("# 🍟 Análise de Investimento de Negócios - Case McDonald's")
st.sidebar.markdown("Desenvolvido por [Asimov Academy](https://asimov.academy)")


btn = st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    ### Explorando o Mercado de Franquias McDonald's no Brasil
Este app foi desenvolvido para analisar o potencial de investimento no mercado de franquias do McDonald's, abordando os principais fatores envolvidos, como:
- **Investimento inicial** necessário
- **Custos operacionais**
- **Retorno sobre o investimento** (ROI) esperado

Utilizamos dados reais para fornecer uma análise prática e visual sobre o cenário de franquias do McDonald's.
"""
)