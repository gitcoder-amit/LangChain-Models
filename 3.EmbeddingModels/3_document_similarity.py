from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

load_dotenv()  # Load environment variables from .env file

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=300) # dimensions involves cost as well, so choose wisely

documents = [
    'Virat Kohli is the captain of Indian cricket team, Known for his aggressive batting style and consistency, he has numerous records in international cricket.',
    'MS Dhoni, former captain of Indian cricket team, is celebrated for his calm demeanor and finishing abilities in high-pressure situations.',
    'Rohit Sharma, an Indian cricketer, is renowned for his elegant batting technique and ability to score big hundreds, holding the record for the highest individual score in ODIs.',
    'Sachin Tendulkar, often referred to as the "God of Cricket," is a legendary Indian batsman with a career spanning over two decades, known for his impeccable technique and numerous records.',
    'Jasprit Bumrah, an Indian fast bowler, is recognized for his unique bowling action and ability to deliver yorkers consistently, making him a key player in limited-overs cricket.'

]

query = "Tell me about Bumbrah"


doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)


print(cosine_similarity([query_embedding], doc_embeddings)) # [[0.62335358 0.41626087 0.42484402 0.3370099  0.41797868]]


scores = cosine_similarity([query_embedding], doc_embeddings)[0]
print(sorted(list(enumerate(scores)), key = lambda x : x[1])[-1]) # (0, 0.62335358)  # This will give the index of the document with highest similarity score along with the score itself


index, score = sorted(list(enumerate(scores)), key = lambda x : x[1])[-1]

print("Most similar document to the query:")
print(documents[index])
print("Similarity Score:", score)