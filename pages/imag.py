import streamlit as st
from PIL import Image, ImageOps
from rembg import remove
import io

# Configuração da página
st.set_page_config(page_title="Remover Fundo e P&B", layout="centered")

st.title("🖼️ Remover Fundo e Converter para Preto e Branco")

# Upload da imagem
uploaded_file = st.file_uploader("Envie uma imagem (JPG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Exibe a imagem original
    st.subheader("Imagem Original")
    original_image = Image.open(uploaded_file)
    st.image(original_image, caption="Imagem Original", use_column_width=True)

    # Remover fundo
    st.subheader("Removendo Fundo...")
    with st.spinner("Processando a imagem..."):
        input_image = original_image.convert("RGB")
        output = remove(input_image)
        output_image = Image.open(io.BytesIO(output)).convert("RGB")
    st.image(output_image, caption="Imagem sem Fundo", use_column_width=True)

    # Converter para preto e branco
    st.subheader("Convertendo para Preto e Branco...")
    grayscale_image = ImageOps.grayscale(output_image)
    st.image(grayscale_image, caption="Imagem em Preto e Branco", use_column_width=True)

    # Opção para download
    st.subheader("Baixar Resultado")
    buffer = io.BytesIO()
    grayscale_image.save(buffer, format="PNG")
    buffer.seek(0)
    st.download_button(
        label="📥 Baixar Imagem P&B",
        data=buffer,
        file_name="imagem_pb.png",
        mime="image/png",
    )
else:
    st.info("Por favor, envie uma imagem para começar.")
