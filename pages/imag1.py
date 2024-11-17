import streamlit as st
import cv2
import numpy as np
from PIL import Image

def remove_background_opencv(image):
    # Converter para array do OpenCV
    img = np.array(image)
    # Criar máscara para segmentação de fundo
    mask = np.zeros(img.shape[:2], np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Retângulo de segmentação (ajustar conforme necessário)
    rect = (10, 10, img.shape[1]-10, img.shape[0]-10)
    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Criar máscara para aplicar ao primeiro plano
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    result = img * mask2[:, :, np.newaxis]

    return Image.fromarray(result)

st.title("Remoção de Fundo com OpenCV")
uploaded_file = st.file_uploader("Carregue sua imagem", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original", use_column_width=True)

    result_image = remove_background_opencv(image)
    st.image(result_image, caption="Sem Fundo", use_column_width=True)
