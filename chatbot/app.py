from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages([
  ('system', 'You are a helpful assistant who answer all question in a presize manner and easy to understand'),
  ('user', 'Question: {question}'),
])
st.title("Chatbot")

text_input = st.text_input("Ask a question about the chatbot")

model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|model|output_parser
if text_input:
    response = chain.invoke(text_input)
    st.write(response)
