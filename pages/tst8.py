import streamlit as st

# Perguntas e respostas
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
st.title("Quiz de Conhecimentos Gerais")

# Armazenar respostas e pontuação
respostas = []
pontuacao = 0

# Loop pelo quiz
for idx, questao in enumerate(quiz_data):
    st.subheader(f"Pergunta {idx + 1}")
    st.write(questao["pergunta"])

    # Opções de resposta como botões de rádio
    resposta = st.radio("Escolha uma opção:", questao["opcoes"], key=idx)
    respostas.append(resposta)

    # Verificar resposta
    if resposta == questao["resposta_correta"]:
        pontuacao += 1

# Botão para exibir pontuação final
if st.button("Ver Resultado"):
    st.write(f"Você acertou {pontuacao} de {len(quiz_data)} perguntas!")
    for idx, questao in enumerate(quiz_data):
        st.write(f"**Pergunta {idx + 1}:** {questao['pergunta']}")
        st.write(f"Sua resposta: {respostas[idx]}")
        st.write(f"Resposta correta: {questao['resposta_correta']}")
        st.write("---")

