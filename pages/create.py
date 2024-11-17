import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from PIL import Image, ImageDraw
import random
import time

# Configuração da página
st.set_page_config(page_title="Sinfonia Visual e Interativa", layout="wide")

# Funções auxiliares
def generate_art():
    """Gera uma arte aleatória usando Pillow."""
    img_size = 500
    img = Image.new("RGB", (img_size, img_size), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)

    for _ in range(50):
        shape_type = random.choice(["circle", "line", "rectangle"])
        color = tuple(random.choices(range(256), k=3))
        
        # Coordenadas válidas
        x1, x2 = sorted([random.randint(0, img_size) for _ in range(2)])
        y1, y2 = sorted([random.randint(0, img_size) for _ in range(2)])

        if shape_type == "circle":
            draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
        elif shape_type == "line":
            draw.line([x1, y1, x2, y2], fill=color, width=3)
        elif shape_type == "rectangle":
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)

    return img

def generate_3d_plot():
    """Gera um gráfico 3D aleatório usando Plotly."""
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2) * 5) + np.cos(Y * 5)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale="Viridis")])
    fig.update_layout(scene=dict(zaxis=dict(range=[-2, 2])), margin=dict(l=0, r=0, t=0, b=0))
    return fig

# Layout principal
st.title("🎨 Sinfonia Visual e Interativa 🎶")
st.markdown("Bem-vindo a uma experiência única de cores, formas e música! 🚀")

# Colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎵 Música Ambiente")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    st.subheader("🖌️ Arte Generativa")
    if st.button("Gerar Arte"):
        img = generate_art()
        st.image(img, caption="Arte Generativa Aleatória", use_column_width=True)

with col2:
    st.subheader("📊 Gráfico 3D Interativo")
    if st.button("Gerar Gráfico 3D"):
        fig = generate_3d_plot()
        st.plotly_chart(fig, use_container_width=True)

# Rodapé interativo
st.markdown("---")
st.subheader("🎉 Desafio Interativo")
colors = st.multiselect(
    "Escolha suas cores favoritas:",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"],
    default=["Blue", "Green"],
)
if colors:
    st.write(f"Você escolheu: {', '.join(colors)}")

# Efeito surpresa
if st.button("✨ Surpresa Final"):
    st.balloons()
    for _ in range(3):
        st.snow()
        st.confetti()
        time.sleep(0.5)

progress_bar = st.progress(0)

for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i + 1)


st.image("https://www.example.com/success_image.png", caption="Sucesso!", use_column_width=True)


st.success("Parabéns! Você completou o quiz!")

st.warning("Parabéns quiz!")
st.error("Parabou o quiz!")
st.success("Paracompleto")
st.info("Pariz!")


st.toast('Your edited image was saved!', icon='😍')


if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')



def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()



with st.spinner('Wait for it...'):
    time.sleep(5)
st.success("Done!")



with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button("Rerun")




with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(
        label="Download complete!", state="complete", expanded=False
    )

st.button("Rerun2")




# Escolha de efeito
effect = st.radio(
    "Escolha um efeito para visualizar 🎉",
    options=["🎈 Balões", "❄️ Neve", "📊 Barra de Progresso", "🔔 Alertas"],
)

# Botão para ativar o efeito
if st.button("Ativar Efeito"):
    if effect == "🎈 Balões":
        st.balloons()
    elif effect == "❄️ Neve":
        st.snow()
    elif effect == "📊 Barra de Progresso":
        st.write("Carregando progresso...")
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.05)  # Pequena pausa para simular carregamento
            progress_bar.progress(i + 1)
        st.success("Progresso concluído! 🎉")
    elif effect == "🔔 Alertas":
        st.warning("Este é um alerta de aviso! ⚠️")
        st.error("Ocorreu um erro! ❌")
        st.success("Tudo está funcionando perfeitamente! ✅")
        st.info("Aqui está uma informação adicional. ℹ️")

# Mensagem de rodapé
st.markdown("✨ Explore os efeitos interativos no Streamlit para deixar sua aplicação mais divertida e dinâmica!")