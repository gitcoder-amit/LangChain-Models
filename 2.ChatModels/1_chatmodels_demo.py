from langchain_openai import ChatOpenAI # it inherit BaseChatModel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4")

result = model.invoke("What is the capital of India?")
print("Result:", result)
print("Answer:", result.content)