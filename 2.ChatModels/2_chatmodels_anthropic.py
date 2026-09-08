# This is to integrate claude model from anthropic with langchain.

from langchain_anthropic import ChatAnthropic # it inherit BaseChatModel
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = "claude-v1", temperature = 0.7)

result = model.invoke("What is the capital of India?")
print(result.content)