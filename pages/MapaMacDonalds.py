import streamlit as st
from streamlit_folium import st_folium
import folium


st.markdown("# 🗺️ Localização de Franquias do McDonald's")

# Criando um mapa com Folium
# Você pode ajustar a latitude e longitude para uma localização inicial
latitude, longitude = -23.550520, -46.633308  # São Paulo, Brasil

# Inicializando o mapa
map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Adicionando um marcador de exemplo para uma localização McDonald's
folium.Marker(
    location=[-23.563988, -46.654731],  # Exemplo: localização no centro de SP
    popup="McDonald's - Avenida Paulista",
    tooltip="Clique para mais informações"
).add_to(map)

# Exibindo o mapa no app Streamlit
st_folium(map, width=700, height=500)

google_maps_iframe = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3656.5416344698983!2d-46.656497985021065!3d-23.561531484682776!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce58583d14c6b7%3A0x9c6fb81eb64a5bb1!2sMcDonald's%20-%20Av.%20Paulista!5e0!3m2!1spt-BR!2sbr!4v1605463652291!5m2!1spt-BR!2sbr" width="700" height="500" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
"""
