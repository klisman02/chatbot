import streamlit as st
from utils import text
from streamlit_chat import message


def main():
    st.set_page_config(page_title='Converse com seus arquivos', page_icon=':books:')

    st.header('Converse com seus arquivos')
    user_question = st.text_input("Faça uma pergunta para mim.")

    if('conversation' not in st.session_state):
        st.session_state.conversation = None

    if(user_question):
        response = st.session_state.conversation(user_question)['chat_history']
        
        for i, text in enumerate(responde):

            if(i % 2 == 0):
                message(text.content, is_user=True, key=str(i) + '_user')
            else:
                message(text.content, is_user=False, key=str(i) + '_bot')

    with st.sidebar:
        st.subheader('Seus arquivos')
        pdf_docs = st.file_uploader('Carregue seus arquivos em formato PDF', accept_multiple_files=True)

        if st.button('Processar'):
            all_files_text = text.files(pdf_docs)

            chunks = text.create_text_chunks(all_files_text)

            vectorstore = chatbot.create_vectorstore(chunks)

            st.session_state.conversation = chatbot.create_conversation_chain(vectorstore)

if __name__ == '__main__':
    main()

    #pip install faiss-cpu openai langchain streamlit tiktoken streamlit-chat