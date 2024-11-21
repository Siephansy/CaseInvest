import streamlit as st
from streamlit_folium import st_folium
import folium
from urllib.error import URLError
import pandas as pd
import pydeck as pdk
from streamlit_elements import elements, mui, dashboard, media

st.set_page_config(layout="wide")

st.markdown("# 🗺️ Localização de Franquias do McDonald's")

latitude, longitude = -23.550520, -46.633308  # São Paulo, Brasil
map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Adicionando um marcador
folium.Marker(
    location=[-23.563988, -46.654731],  # Exemplo: localização no centro de SP
    popup="McDonald's - Avenida Paulista",
    tooltip="Clique para mais informações",
).add_to(map)

google_maps_iframe = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3656.5416344698983!2d-46.656497985021065!3d-23.561531484682776!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce58583d14c6b7%3A0x9c6fb81eb64a5bb1!2sMcDonald's%20-%20Av.%20Paulista!5e0!3m2!1spt-BR!2sbr!4v1605463652291!5m2!1spt-BR!2sbr" width="700" height="500" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
"""

def mapping_demo():
    @st.cache_data
    def from_data_file(filename):
        url = (
            "https://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=10,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            return pdk.Deck(
                map_style=None,
                initial_view_state={
                    "latitude": 37.76,
                    "longitude": -122.4,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        else:
            st.error("Please choose at least one layer above.")
            return None
    except URLError as e:
        st.error(f"Connection error: {e.reason}")
        return None

# Layout inicial
layout = [
    dashboard.Item("map_component", 0, 0, 3, 3),
    dashboard.Item("google_maps", 3, 0, 3, 3),
    dashboard.Item("deck_gl", 0, 3, 6, 3),
    dashboard.Item("video_player", 6, 0, 2, 2),
]

with elements("dashboard"):
    with dashboard.Grid(layout):
        # Mapa Folium
        with mui.Paper(key="map_component"):
            st_folium(map, width=700, height=500)

        # Google Maps Iframe
        with mui.Paper(key="google_maps"):
            st.markdown(google_maps_iframe, unsafe_allow_html=True)

        # Deck.GL Visualization
        deck_gl_chart = mapping_demo()
        if deck_gl_chart:
            with mui.Paper(key="deck_gl"):
                st.pydeck_chart(deck_gl_chart)

        # Video Player
        with mui.Paper(key="video_player"):
            media.Player(
                url="https://www.youtube.com/watch?v=iik25wqIuFo",
                controls=True,
            )
