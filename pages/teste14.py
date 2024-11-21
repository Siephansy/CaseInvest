import streamlit as st
from streamlit_folium import st_folium
import folium
from streamlit_elements import elements, dashboard, mui, media
from PIL import Image

# URL da imagem
image_url = "https://via.placeholder.com/300"  # Substitua pela URL da sua imagem
image = Image.open("sua_imagem.jpg")  # Substitua pelo caminho da sua imagem

# Exibir a imagem no sidebar
st.sidebar.image(image_url, caption="Minha Imagem Online", use_column_width=True)


st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #f0f0f0;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
