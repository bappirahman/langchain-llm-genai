from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API")


app = FastAPI(
  title='Langchain Server',
  version='1.0',
  description='A llm api server'
)

add_routes(
  app,
  ChatOpenAI(),
  path='/openai'
)

model = ChatOpenAI()

llm = Ollama(model='llama2')

prompt1 = ChatPromptTemplate.from_template('Write me an essay about {topic} with 100 words')
prompt2 = ChatPromptTemplate.from_template('Write me an poem about {topic} with 100 words')

add_routes(
  app, 
  prompt1|model,
  path='/essay'
)

add_routes(
  app,
  prompt2|model,
  path='/poem'
)

if __name__ == '__main__':
  uvicorn.run(app, host='localhost', port='8000')