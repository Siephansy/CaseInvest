import streamlit as st
import time
import random

# Dados do quiz
quiz_data = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Berlim", "Madri", "Paris", "Lisboa"],
        "resposta_correta": "Paris"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opcoes": ["Miguel de Cervantes", "Gabriel Garcia Marquez", "William Shakespeare", "Victor Hugo"],
        "resposta_correta": "Miguel de Cervantes"
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "opcoes": ["Terra", "Marte", "Júpiter", "Saturno"],
        "resposta_correta": "Júpiter"
    }
]

# Função principal do app
def main():
    st.title("Quiz com Temporizador")

    # Configuração inicial da pontuação
    if "pontuacao" not in st.session_state:
        st.session_state.pontuacao = 0

    # Loop por cada pergunta
    for idx, questao in enumerate(quiz_data):
        st.subheader(f"Pergunta {idx + 1}")
        st.write(questao["pergunta"])

        # Embaralha as opções de resposta
        opcoes = questao["opcoes"][:]
        random.shuffle(opcoes)

        # Exibe opções e espera resposta
        resposta = st.radio("Escolha uma opção:", opcoes, key=idx)

        # Temporizador de 5 segundos antes de mostrar o feedback
        if st.button("Responder", key=f"responder_{idx}"):
            st.write("Processando resposta...")

            # Inicia o temporizador de 5 segundos
            for seg in range(5, 0, -1):
                st.write(f"Tempo restante para feedback: {seg} segundos")
                time.sleep(1)

            # Feedback visual após 5 segundos
            if resposta == questao["resposta_correta"]:
                st.success("Correto! 🎉")
                st.session_state.pontuacao += 1
            else:
                st.error("Incorreto! ❌")

            st.write("---")

    # Exibir pontuação final
    if st.button("Ver Resultado"):
        st.write(f"Você acertou {st.session_state.pontuacao} de {len(quiz_data)} perguntas!")

if __name__ == "__main__":
    main()
