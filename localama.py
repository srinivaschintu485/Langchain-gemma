import numpy
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()

#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt=ChatPromptTemplate.from_messages(

[
    ("system","You are a helpful assistant. Please respond to the user queries"),
    ("user","Question:{question}")
]
)

st.title("Langchain Demo with OPENAI API")
input_text=st.text_input("Search the topic that u want")

llm=Ollama(model="gemma")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))