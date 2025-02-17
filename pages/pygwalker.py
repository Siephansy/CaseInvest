from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import os

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("Use Pygwalker In Streamlit")

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> StreamlitRenderer:
    csv_path = "./bike_sharing_dc.csv"
    if not os.path.exists(csv_path):
        st.error(f"CSV file not found: {csv_path}")
        return None
    df = pd.read_csv(csv_path)
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")

renderer = get_pyg_renderer()

if renderer:
    renderer.explorer()