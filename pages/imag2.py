import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
from PIL import Image

def remove_background_mediapipe(image):
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
        img = np.array(image)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = selfie_segmentation.process(img_rgb)
        mask = results.segmentation_mask > 0.5
        img[~mask] = [255, 255, 255]  # Fundo branco
        return Image.fromarray(img)

st.title("Remoção de Fundo com MediaPipe")
uploaded_file = st.file_uploader("Carregue sua imagem", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original", use_column_width=True)

    result_image = remove_background_mediapipe(image)
    st.image(result_image, caption="Sem Fundo", use_column_width=True)
