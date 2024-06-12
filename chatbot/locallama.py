from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages([
  ('system', 'You are a helpful assistant who answer all question in a presize manner and easy to understand'),
  ('user', 'Question: {question}')
])

st.title('Ollama llama2 model')
input_text = st.text_input('Write your question here')

model = Ollama(model='llama2')
output_parser = StrOutputParser()
chain = prompt|model|output_parser

if input_text:
    response = chain.invoke(input_text)
    st.write(response)
