# this is to integrate google gemini model with langchain.

from langchain_google_genai import ChatGoogleGenerativeAI # it inherit BaseChatModel
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.7-flash')
result = model.invoke("What is the capital of India?")

print("Result:", result.content[0]['text'])