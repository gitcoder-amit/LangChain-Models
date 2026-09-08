from langchain_openai import ChatOpenAI # it inherit BaseChatModel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4", temperature = 0.7, max_completion_tokens = 20)
# max_completion_tokens -> this will make sure only 20 tokens are generated in the response, if the model tries to generate more than 20 tokens, it will be truncated. and it helps in reducing the cost of the API call.
# temperature -> this will make sure the response is more creative and less deterministic. if you want a more deterministic response, you can set the temperature to 0.0
result = model.invoke("What is the capital of India?")
print("Result:", result)
print("Answer:", result.content)