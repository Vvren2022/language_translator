from langchain.chat_models import ChatOpenAI
import os
import openai
import faiss
import numpy as np
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import openai


os.environ["OPENAI_API_KEY"]=grisha_key
llm = ChatOpenAI(temperature=0.1)

embedding_model = OpenAIEmbeddings()

# Function to get embedding for a single text
def get_embedding(text):
    # Use embed_documents for embedding the text
    embeddings = embedding_model.embed_documents([text])
    return embeddings[0]  # Return the first embedding

d = 1536  # Dimension of the embedding vectors (text-embedding-ada-002 has 1536 dimensions)
index = faiss.IndexFlatL2(d)

# Store translations in a dictionary (for quick lookup)
db = {}

# Function to add text and its translation to FAISS and db
def add_to_db(text, translation):
    embedding = get_embedding(text)
    index.add(np.array(embedding).reshape(1, -1))  # Add embedding to FAISS
    db[index.ntotal - 1] = translation  # Store translation in dictionary


def translate_text(text, target_language):
    # Get the embedding for the input text
    embedding = get_embedding(text)

    # Search the FAISS index for similar translations
    if index.ntotal > 0:
        D, I = index.search(np.array(embedding).reshape(1, -1), 1)  # Search for nearest match
        if D[0][0] < 0.1:  # Threshold for similarity (you can adjust this)
            return db[I[0][0]]  # Return the translation if a match is found

    # Use GPT-4 to translate the text if no match is found
    prompt = f"Translate the following text to {target_language}: {text}"

    # Generate translation using OpenAI's LLM (via LangChain)
    response = llm.invoke([{
        "role": "system",
        "content": "You are a helpful assistant providing translations."
    }, {
        "role": "user",
        "content": prompt
    }])

    # Access the content of the response (message content)
    translation = response.content.strip()  # Get the content of the first message

    # Store the new translation in the FAISS index and dictionary
    index.add(np.array(embedding).reshape(1, -1))  # Add new embedding to FAISS index
    db[index.ntotal - 1] = translation  # Save translation to the dictionary

    return translation