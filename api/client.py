import requests
import streamlit as st


url = 'http://localhost:8000'
def get_openai_response(input_text1):
  response = requests.post(f'{url}/essay/invoke', json={'input': {'topic': input_text1}})
  return response.json()['output']['content']

def get_llama_response(input_text2):
  response = requests.post(f'{url}/poem/invoke', json={'input': {'topic': input_text2}})
  return response.json()['output']['content']

st.title('Langchain client')
input_text1=st.text_input('Write an essay on')
input_text2=st.text_input('Write an poem on')

if input_text1:
  st.write(get_openai_response(input_text1))

if input_text2:
  st.write(get_llama_response(input_text2))
