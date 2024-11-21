import streamlit as st
from streamlit_folium import st_folium
import folium
from streamlit_elements import elements, mui, dashboard, media

# Configuração inicial
st.set_page_config(layout="wide")
st.markdown("# 🗺️ Localização de Franquias do McDonald's")

# Criando o mapa com Folium
latitude, longitude = -23.550520, -46.633308  # São Paulo, Brasil
map = folium.Map(location=[latitude, longitude], zoom_start=12)



# Configurando iframe do Google Maps
google_maps_iframe = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3656.5416344698983!2d-46.656497985021065!3d-23.561531484682776!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce58583d14c6b7%3A0x9c6fb81eb64a5bb1!2sMcDonald's%20-%20Av.%20Paulista!5e0!3m2!1spt-BR!2sbr!4v1605463652291!5m2!1spt-BR!2sbr" width="100%" height="100%" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
"""

# Criando layout do painel
layout = [
    dashboard.Item("mapa", 0, 0, 6, 4),
    dashboard.Item("iframe", 6, 0, 6, 4),
    dashboard.Item("video", 0, 4, 6, 3),
    dashboard.Item("texto", 6, 4, 6, 3),
]

with elements("dashboard"):
    with dashboard.Grid(layout):
        # Mapa do Folium
        with mui.Card(key="mapa"):
            st_folium(map, width=700, height=500)
            # Adicionando um marcador
            folium.Marker(
                location=[-23.563988, -46.654731],
                popup="McDonald's - Avenida Paulista",
                tooltip="Clique para mais informações",
            ).add_to(map)

        # Iframe do Google Maps
        with mui.Card(key="iframe"):
            st.markdown(google_maps_iframe, unsafe_allow_html=True)

        # Player de vídeo
        with mui.Card(key="video"):
            media.Player(
                url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=True
            )

        # Texto ou informações adicionais
        with mui.Card(key="texto"):
            st.markdown("### Informações adicionais")
            st.write(
                "Este é um exemplo de painel arrastável que combina mapas, vídeos e informações adicionais!"
            )
