import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("Use Pygwalker In Streamlit")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    try:
        from pygwalker.api.streamlit import StreamlitRenderer
        renderer = StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")
        
        if renderer:
            renderer.explorer()
    except ModuleNotFoundError:
        st.error("The pygwalker module is not found. Please ensure it is installed.")
else:
    st.info("Please upload a CSV file to proceed.")