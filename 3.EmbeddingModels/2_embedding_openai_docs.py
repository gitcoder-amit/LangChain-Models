from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

embeding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=32) # dimensions involves cost as well, so choose wisely
# 

documents = [
    'Delhi is the capital of India',
    'Kolkata is the capital of West Bengal',
    "Paris is the capital of France",
]
result = embeding.embed_documents(documents)
print(str(result)) # this will give 32 dimension vector
