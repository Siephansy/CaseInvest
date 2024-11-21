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


# Configuração inicial
st.set_page_config(layout="wide")
st.markdown("# 🗺️ Localização de Franquias do McDonald's")

# Criando o mapa com Folium
latitude, longitude = -23.550520, -46.633308  # São Paulo, Brasil
folium_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Adicionando um marcador
folium.Marker(
    location=[-23.563988, -46.654731],
    popup="McDonald's - Avenida Paulista",
    tooltip="Clique para mais informações",
).add_to(folium_map)

# Salvando o mapa como HTML
folium_map_html = folium_map._repr_html_()

# Configurando iframe do Google Maps
google_maps_iframe = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3656.5416344698983!2d-46.656497985021065!3d-23.561531484682776!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce58583d14c6b7%3A0x9c6fb81eb64a5bb1!2sMcDonald's%20-%20Av.%20Paulista!5e0!3m2!1spt-BR!2sbr!4v1605463652291!5m2!1spt-BR!2sbr" 
width="100%" height="100%" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
"""

# Configuração do layout do dashboard
layout = [
    dashboard.Item("folium_map", 0, 0, 6, 4, isResizable=True, isDraggable=True),
    dashboard.Item("google_map", 6, 0, 6, 4, isResizable=True, isDraggable=True),
    dashboard.Item("video", 0, 4, 6, 3, isResizable=True, isDraggable=True),
    dashboard.Item("texto", 6, 4, 6, 3, isResizable=True, isDraggable=True),
]

# Configuração do painel drag-and-drop
with elements("dashboard"):
    with dashboard.Grid(layout, draggableHandle=".draggable", style={"height": "90vh"}):
        # Renderizando o mapa do Folium
        with mui.Card(key="folium_map", sx={"padding": "1em"}):
            st.markdown(f"<div>{folium_map_html}</div>", unsafe_allow_html=True)

        # Renderizando o iframe do Google Maps
        with mui.Card(key="google_map", sx={"padding": "1em"}):
            st.markdown(google_maps_iframe, unsafe_allow_html=True)

        # Renderizando o player de vídeo
        with mui.Card(key="video", sx={"padding": "1em"}):
            media.Player(
                url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=True
            )

        # Renderizando a seção de texto adicional
        with mui.Card(key="texto", sx={"padding": "1em"}):
            st.markdown("### Informações adicionais")
            st.write(
                "Este é um exemplo de painel arrastável que combina mapas, vídeos e informações adicionais!"
            )
