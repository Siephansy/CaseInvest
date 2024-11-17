import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from io import StringIO, BytesIO

# Function to generate Excel download link
def generate_excel_download_link(df):
    towrite = BytesIO()
    df.to_excel(towrite, index=False, header=True, engine='openpyxl')
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">📥 Download Excel File 📊</a>'
    return st.markdown(href, unsafe_allow_html=True)

# Function to generate HTML download link for the plot
def generate_html_download_link(fig):
    towrite = StringIO()
    fig.write_html(towrite, include_plotlyjs="cdn")
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64,{b64}" download="plot.html">📥 Download Plot 📉</a>'
    return st.markdown(href, unsafe_allow_html=True)

# Set page configuration
st.set_page_config(page_title='Dynamic Excel Plotter', layout='wide', initial_sidebar_state='expanded')

# Sidebar
st.sidebar.title("About 📘")
st.sidebar.info("This app allows you to upload an Excel file, visualize its data, and download the visualized data. 🚀")

# Main content
st.title('Dynamic Excel Plotter 📈')
st.subheader('Upload your Excel file and let the magic happen! ✨')

uploaded_file = st.file_uploader('Choose a XLSX file 📁', type='xlsx')

if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df.style.highlight_max(axis=0))  # Highlight max values for better visualization

    st.markdown('### Data Analysis 🔍')
    all_columns = df.columns.tolist()  # Dynamic array of all columns
    st.write("### Available Columns in Your Data")
    st.write(all_columns)

    # User selects a column for grouping
    groupby_column = st.selectbox(
        'Select a column for grouping 📊:',
        all_columns
    )

    # User selects numerical columns for analysis
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    st.write("### Numeric Columns Available for Analysis")
    st.write(numeric_columns)

    if not numeric_columns:
        st.error("No numeric columns available in the data for analysis.")
    else:
        analysis_columns = st.multiselect(
            'Select numerical columns for analysis:',
            numeric_columns,
            default=numeric_columns[:2]  # Pre-select the first two if available
        )

        if not analysis_columns:
            st.warning("Please select at least one numerical column for analysis.")
        else:
            # Group DataFrame
            df_grouped = df.groupby(by=[groupby_column], as_index=False)[analysis_columns].sum()

            # Plot DataFrame
            fig = px.bar(
                df_grouped,
                x=groupby_column,
                y=analysis_columns[0],  # Default to the first selected column for plotting
                color=analysis_columns[0],
                color_continuous_scale='Viridis',
                template='plotly_dark',
                title=f'{analysis_columns[0]} by {groupby_column}'
            )
            st.plotly_chart(fig, use_container_width=True)

            # Download Section
            st.markdown('### Downloads 📥')
            generate_excel_download_link(df_grouped)
            generate_html_download_link(fig)
