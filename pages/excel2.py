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
st.set_page_config(page_title='Enhanced Excel Plotter', layout='wide', initial_sidebar_state='expanded')

# Sidebar
st.sidebar.title("About 📘")
st.sidebar.info("This app allows you to upload an Excel file, visualize its data, and download the visualized data. 🚀")

# Main content
st.title('Enhanced Excel Plotter 📈')
st.subheader('Upload your Excel file and let the magic happen! ✨')

uploaded_file = st.file_uploader('Choose a XLSX file 📁', type='xlsx')

if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df.style.highlight_max(axis=0))  # Highlight max values for better visualization

    # Verificar colunas disponíveis
    available_columns = df.columns.tolist()
    st.write("### Available Columns in Your Data")
    st.write(available_columns)

    st.markdown('### Data Analysis 🔍')
    expected_columns = ['Ship Mode', 'Segment', 'Category', 'Sub-Category']
    valid_columns = [col for col in expected_columns if col in available_columns]

    if not valid_columns:
        st.error("The uploaded file does not contain any of the expected columns for analysis.")
    else:
        groupby_column = st.selectbox(
            'Select a column for analysis 📊:',
            valid_columns
        )

        # Group DataFrame
        output_columns = ['Sales', 'Profit']
        if all(col in df.columns for col in output_columns):
            df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()

            # Plot DataFrame
            fig = px.bar(
                df_grouped,
                x=groupby_column,
                y='Sales',
                color='Profit',
                color_continuous_scale=['red', 'yellow', 'green'],
                template='plotly_dark',  # Dark theme for the plot
                title=f'Sales & Profit by {groupby_column}'
            )
            st.plotly_chart(fig, use_container_width=True)

            # Download Section
            st.markdown('### Downloads 📥')
            generate_excel_download_link(df_grouped)
            generate_html_download_link(fig)
        else:
            st.error("The data does not contain the required columns: 'Sales' and 'Profit'.")
