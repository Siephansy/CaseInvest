import streamlit as st
import time

# Função para exibir Snackbar
def show_snackbar(message, duration=3):
    snackbar_code = f"""
    <style>
        .snackbar {{
            visibility: visible;
            min-width: 250px;
            margin-left: -125px;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 2px;
            padding: 16px;
            position: fixed;
            z-index: 1;
            left: 50%;
            bottom: 30px;
            font-size: 17px;
        }}
        .snackbar.hide {{
            visibility: hidden;
        }}
    </style>
    <div id="snackbar" class="snackbar">{message}</div>
    <script>
        setTimeout(function() {{
            var snackbar = document.getElementById('snackbar');
            snackbar.className = snackbar.className + " hide";
        }}, {duration * 1000});
    </script>
    """
    st.markdown(snackbar_code, unsafe_allow_html=True)

# Função para exibir Modal Dialog
def show_modal(title, content):
    modal_code = f"""
    <div class="modal">
        <style>
            .modal {{
                display: block;
                position: fixed;
                z-index: 1;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                overflow: auto;
                background-color: rgb(0,0,0);
                background-color: rgba(0,0,0,0.4);
            }}
            .modal-content {{
                background-color: #fefefe;
                margin: 15% auto;
                padding: 20px;
                border: 1px solid #888;
                width: 80%;
                text-align: center;
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
                animation: slide-in 0.5s;
            }}
            @keyframes slide-in {{
                from {{ transform: translateY(-50px); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
        </style>
        <div class="modal-content">
            <h2>{title}</h2>
            <p>{content}</p>
            <button onclick="closeModal()">Close</button>
        </div>
    </div>
    <script>
        function closeModal() {{
            var modal = document.querySelector('.modal');
            modal.style.display = 'none';
        }}
    </script>
    """
    st.markdown(modal_code, unsafe_allow_html=True)

# Main Page
st.title("Streamlit Snackbar & Modal Example")

if st.button("Show Snackbar"):
    show_snackbar("This is a snackbar message!")

if st.button("Show Modal"):
    show_modal("Modal Title", "This is the modal content.")

st.write("Click the buttons above to see the Snackbar and Modal in action.")
