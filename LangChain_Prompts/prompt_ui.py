from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()  # Load environment variables from .env file

st.header("Research Tool")
user_input = st.text_input("Enter your prompt/query here:")
model = ChatOpenAI(model = "gpt-4", temperature = 0.7)


if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)
