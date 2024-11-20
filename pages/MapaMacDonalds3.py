import streamlit as st
from streamlit_folium import st_folium
import folium
from urllib.error import URLError

import pandas as pd
import pydeck as pdk

from streamlit_elements import elements, mui, html
from streamlit.hello.utils import show_code

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
# Exibindo o mapa no Streamlit
st.markdown(google_maps_iframe, unsafe_allow_html=True)


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
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)

mapping_demo()





with elements("nested_children"):

    # You can nest children using multiple 'with' statements.
    #
    # <Paper>
    #   <Typography>
    #     <p>Hello world</p>
    #     <p>Goodbye world</p>
    #   </Typography>
    # </Paper>

    with mui.Paper:
        with mui.Typography:
            html.p("Hello world")
            html.p("Goodbye world")



with elements("properties"):

    # You can add properties to elements with named parameters.
    #
    # To find all available parameters for a given element, you can
    # refer to its related documentation on mui.com for MUI widgets,
    # on https://microsoft.github.io/monaco-editor/ for Monaco editor,
    # and so on.
    #
    # <Paper elevation={3} variant="outlined" square>
    #   <TextField label="My text input" defaultValue="Type here" variant="outlined" />
    # </Paper>

    with mui.Paper(elevation=3, variant="outlined", square=True):
        mui.TextField(
            label="My text input",
            defaultValue="Type here",
            variant="outlined",
        )

    # If you must pass a parameter which is also a Python keyword, you can append an
    # underscore to avoid a syntax error.
    #
    # <Collapse in />

    mui.Collapse(in_=True)

    # mui.collapse(in=True)
    # > Syntax error: 'in' is a Python keyword:






with elements("callbacks_hotkey"):

    # Invoke a callback when a specific hotkey sequence is pressed.
    #
    # For more information regarding sequences syntax and supported keys,
    # go to Mousetrap's project page linked below.
    #
    # /!\ Hotkeys work if you don't have focus on Streamlit Elements's frame /!\
    # /!\ As with other callbacks, this reruns the whole app /!\

    from streamlit_elements import event

    def hotkey_pressed():
        print("Hotkey pressed")

    event.Hotkey("g", hotkey_pressed)

    # If you want your hotkey to work even in text fields, set bind_inputs to True.
    event.Hotkey("h", hotkey_pressed, bindInputs=True)
    mui.TextField(label="Try pressing 'h' while typing some text here.")

    # If you want to override default hotkeys (ie. ctrl+f to search in page),
    # set overrideDefault to True.
    event.Hotkey("ctrl+f", hotkey_pressed, overrideDefault=True)




with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    with dashboard.Grid(layout):
        mui.Paper("First item", key="first_item")

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("First item", key="first_item")
        with elements("media_player"):
            from streamlit_elements import media
            media.Player(url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=True)
        mui.Paper("First item2", key="first_item2")
        with elements("media_player"):
            from streamlit_elements import media
            media.Player(url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=True)


