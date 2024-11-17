import streamlit as st
import streamlit.components.v1 as components

# Função para exibir Snackbar
def show_snackbar(message, duration=3):
    snackbar_code = f"""
    <style>
        .snackbar {{
            visibility: visible;
            min-width: 300px;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            border-radius: 4px;
            padding: 16px;
            position: fixed;
            z-index: 1;
            left: 50%;
            bottom: 30px;
            transform: translateX(-50%);
            font-size: 16px;
        }}
        .snackbar.hide {{
            visibility: hidden;
        }}
    </style>
    <div id="snackbar" class="snackbar">
        {message}
        <div style="font-size: 12px; margin-top: 5px;">This message will disappear in {duration} seconds.</div>
    </div>
    <script>
        setTimeout(function() {{
            var snackbar = document.getElementById('snackbar');
            snackbar.className = snackbar.className + " hide";
        }}, {duration * 1000});
    </script>
    """
    components.html(snackbar_code, height=100)

# Função para exibir Modal Dialog
def show_modal(title, content, footer):
    modal_code = f"""
    <div id="customModal" style="display: block; position: fixed; z-index: 2; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.4);">
        <div style="background-color: #fefefe; margin: 15% auto; padding: 20px; border: 1px solid #888; width: 60%; border-radius: 8px; text-align: center; animation: slide-in 0.5s;">
            <h2>{title}</h2>
            <p>{content}</p>
            <div style="margin-top: 20px; color: gray; font-size: 14px;">{footer}</div>
            <button onclick="document.getElementById('customModal').style.display='none'" style="margin-top: 20px; padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 4px; cursor: pointer;">Close</button>
        </div>
    </div>
    <style>
        @keyframes slide-in {{
            from {{ transform: translateY(-50px); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}
    </style>
    """
    components.html(modal_code, height=400)

# Página Principal
st.title("Streamlit Snackbar & Modal Example")
st.write("Explore exemplos de **Snackbar** e **Dialog Modal** com conteúdos aprimorados.")

# Exemplo de Snackbar
if st.button("Show Snackbar"):
    show_snackbar("This is a snackbar with more detailed content!", duration=4)

# Exemplo de Modal Dialog
if st.button("Show Modal"):
    show_modal(
        title="Welcome to the Modal Dialog 🎉",
        content=(
            "This is a detailed modal dialog box. "
            "You can use this space to display important information, alerts, or collect user input."
        ),
        footer="Tip: Modals are great for drawing user attention!",
    )
