from langchain.embeddings import openai
from langchain.vectorstores import FAISS 
from langchain.chat_models import ChatOpenAI 
from langchain.memory import ConversationBufferMemory 
from langchain.chains import ConversationRetrievalChain 
#plataform.openai.com

def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embeddings=embeddings)

    return vectorstore

def create_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

return conversation_chain