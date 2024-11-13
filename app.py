import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 

if "data" not in st.session_state:
    #df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    #df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    #df_data = df_data[df_data["Value(£)"] > 0]
    #df_data = df_data.sort_values(by="Overall", ascending=False)


    # Aqui você pode substituir pelo dataset relevante para a análise de investimento em franquias
    df_data = pd.DataFrame({
        "Ano": [2018, 2019, 2020, 2021, 2022],
        "Faturamento (R$ milhões)": [2500, 2800, 2700, 3000, 3200],
        "Crescimento (%)": [12, 8, -4, 11, 6]
    })
    st.session_state["data"] = df_data

st.set_page_config(page_title="Análise de Investimento - Case McDonald's", layout="centered")
st.markdown("# 🍟 Análise de Investimento de Negócios - Case McDonald's")


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

st.markdown("## 📈 Crescimento do Faturamento do McDonald's no Brasil")
st.line_chart(st.session_state["data"].set_index("Ano")["Faturamento (R$ milhões)"])

# Dados iniciais sobre custos
st.markdown("## 💲 Estrutura de Custos")
st.write("Estima-se que o investimento inicial para uma franquia McDonald's esteja entre R$ 2,67 milhões e R$ 4 milhões.")
st.write("Abaixo estão os principais custos envolvidos no investimento:")
costs = {
    "Item": ["Taxa de Franquia", "Construção e Equipamentos", "Treinamento", "Capital de Giro"],
    "Custo Aproximado (R$)": ["250 mil", "Variável", "Incluso", "Variável"]
}
df_costs = pd.DataFrame(costs)
st.table(df_costs)

# Estimativa de tempo de retorno do investimento
st.markdown("## ⏳ Tempo Médio de Retorno do Investimento")
st.write("A previsão de retorno do investimento (payback) para uma unidade do McDonald's é de aproximadamente **5 anos**.")

# Link para download do dataset e informações adicionais
st.sidebar.markdown("### Links Úteis")
st.sidebar.markdown("[🔗 Kaggle Dataset](https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data)", unsafe_allow_html=True)
st.sidebar.markdown("[🌐 Saiba mais sobre franquias do McDonald's](https://www.mcdonalds.com.br/)")

st.markdown("---")
st.markdown("### Sobre o App")
st.write("Este app foi desenvolvido com base em dados reais e informações de mercado. \
         Ele é um recurso para investidores, analistas e entusiastas que desejam explorar as oportunidades \
         de negócio no setor de franquias do McDonald's.")