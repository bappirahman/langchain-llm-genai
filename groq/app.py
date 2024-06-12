import streamlit as st
from langchain_groq import ChatGroq
from langchain_community import WebBasedLoader
from langchain_community import OllamaEmbeddings
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY'] 


if 'vector' not in st.session_state:
    st.session_state.embedding = OllamaEmbeddings()
    st.session_state.loader = WebBasedLoader('https://docs.smith.langchain.com')
    st.session_state.docs = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs, st.session_state.embedding)
    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embedding)

st.titile('Chat-Groq')
llm = ChatGroq(groq_api_key=groq_api_key, model='llama3-8b-8192')

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based on the provided context only.
    Please provide the most accurate response based on the context.
    <context>
    {context}
    </context>
    Question: {input}
    """
)

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = st.session_state.vector.as_retriever()
restrieval_chain = create_retrieval_chain(retriever, document_chain)

prompt = st.text_input('Input your prompt here')
os.write(prompt)
