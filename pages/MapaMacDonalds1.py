import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)
df_data = st.session_state["data"]

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

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")

