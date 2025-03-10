
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
from ydata_profiling import ProfileReport
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import datetime
import json
import io
import os

# URLs para ícone da página e imagem
favicon_url = "assets/favicon.ico"
imagem_url = 'assets/logo.png'

# Configuração da página
st.set_page_config(page_icon=favicon_url, page_title="EDA Tool | Camila Braz")

# Create a Streamlit app
st.title("Exploratory Data Analysis: report generator")
st.sidebar.image(imagem_url)
# , width = 300

with st.sidebar.expander("About this app"):
    st.write(
        "EDA Analysis automatized using Streamlit and the ydata_profiling package.\n\n"
        "Source code here: [GitHub Repository](https://github.com/camilasbraz/streamlit-exploratory-analysis)\n\n"
        "Contact: [camilabraz03@gmail.com](mailto:camilabraz03@gmail.com)\n\n"
        "Application and code under the MIT License"
    )

st.sidebar.title("Upload Data")


demo_folder = "demo_files"  

with open('demo_files.zip', 'rb') as f:
    zip_file = io.BytesIO(f.read())

st.sidebar.download_button('Download Demo Files', zip_file, key='download_zip', file_name='archive.zip', mime='application/zip')


uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check the file extension
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "csv":
        # Read CSV file
        df = pd.read_csv(uploaded_file)
    elif file_extension == "xlsx":
        # Read Excel file
        df = pd.read_excel(uploaded_file)


    columns_to_analyze = st.sidebar.radio(
        'Select wheter to include all columns in the report or a subset of columns.',
        ('All columns', 'Subset columns'),
        key="custom_radio")

    
    if columns_to_analyze == 'All columns':
        df = df
    elif columns_to_analyze == 'Subset columns':
        column_list = list(df.columns)
        columns_subset = st.sidebar.multiselect(
            'Select what to include in the report.',
            column_list
        )
        df = df[columns_subset]
    
    
    mode_choice = st.sidebar.radio(
        'Select analysis mode:',
        ('Minimal Mode', 'Complete Mode')
    )

    if mode_choice == 'Minimal Mode':
        minimal = True
    elif mode_choice == 'Complete Mode':
        minimal = False
        st.sidebar.warning("The Complete Mode, which includes more detailed analysis and visualizations, can be resource-intensive and may not work efficiently on very large datasets")

    with st.sidebar.expander("Advanced Options"):
        sensitive_info = st.checkbox("Handle sensitive information?")
        schema = st.checkbox("Load JSON dataset type schema?")
        if schema:
            schema_json = st.sidebar.file_uploader("Upload JSON dataset type schema file", type=["json"])
        analyze_time_series = st.checkbox("Analyze Time Series Data?")

    
    # Display the raw data
    st.subheader("Data Content")
    max_rows = 10
    df_display = df.head(max_rows)


    grid = AgGrid(
        df_display,
        width= '100%', 
        enable_enterprise_modules=False

        )
    
    if st.button('Generate Report'):

        # grid_df = grid=['data']
        
        # df = pd.DataFrame(grid_df)
        # Create a Pandas Profiling report
        st.markdown("### EDA Report")

        # Create a dynamic progress bar
        progress_bar = st.empty()
        progress_percent = 0
        title = uploaded_file.name.split(".")[0].capitalize()  + " | EDA Report | Generated with EDA Tool by Camila Braz"

        # Get the current year
        current_year = datetime.datetime.now().year

        # Update the dataset dictionary
        dataset = {
            "description": f"This profiling report was generated with https://github.com/camilasbraz/streamlit-exploratory-analysis",
            "copyright_holder": "camilabraz03@gmail.com",
            "copyright_year": str(current_year),
            "url": "https://github.com/camilasbraz",
        }
        # Step 1: Profile the data
        # st.write("Profiling the data...")

        
        profile_parameters = {
            'df': df,
            'explorative': True,
            'title': title,
            'dataset' :dataset,
            'sensitive': sensitive_info, 
        }   

        if analyze_time_series:
            profile_parameters['tsmode'] = True 


        # Only add 'duplicates' and 'samples' if not handling sensitive info
        if sensitive_info:
            profile_parameters['duplicates'] = None
            profile_parameters['samples'] =  None
        
        # Only add 'schema' and 'descriptions' if the corresponding options are selected
        if schema: 
            if schema_json is None:
                st.warning("JSON Schema file selected but not uploaded. Generating report without it!")
            else:
                # Save the uploaded JSON file to a temporary directory
                with open('temp_schema.json', 'wb') as f:
                    f.write(schema_json.read())
                # Opening the temporary JSON file
                try:
                    json_file_name = 'temp_schema.json'
                    with open(json_file_name, 'r') as f:
                        json_data = json.load(f)
                        type_schema = {column: data_type for column, data_type in zip(json_data["columns"], json_data["data_type"])}
                        print(type_schema)
                    profile_parameters['type_schema'] = type_schema
                except FileNotFoundError:
                    st.error(f"The file '{json_file_name}' was not found. Please make sure the file exists.")
                # Remove the temporary file after use
                os.remove('temp_schema.json')
    
        
        # Create the ProfileReport instance
        profile = ProfileReport(**profile_parameters)

        # https://github.com/madelinekinnaird/Gerrymandr/blob/master/images/az1.PNG
        # https://github.com/madelinekinnaird/Gerrymandr/blob/master/images/az1.PNG?raw=true
        profile.config.html.style.logo = "https://github.com/camilasbraz/streamlit-exploratory-analysis/blob/main/assets/logo_report.png?raw=true"

        progress_percent += 15
        progress_bar.progress(progress_percent)

        # Step 2: Render the report to HTML
        # st.write("Rendering the report to HTML...")
        # st.write("This may take some time depending on the data size.")
        export_html = profile.to_html()
        progress_percent += 70
        progress_bar.progress(progress_percent)

        # Final progress update
        progress_percent = 100
        progress_bar.progress(progress_percent)

        # Step 4: Provide the option to download the HTML report
        st.markdown("##### You can now download the complete EDA report:")
        title_html = uploaded_file.name.split(".")[0].capitalize()  + "_EDA_Report" + '.html'
        st.download_button(label="Download Report", data=export_html, file_name=title_html)

        st_profile_report(profile)



else:
    st.warning("Plase upload your CSV or XLSX file.")
