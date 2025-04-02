import openai
from langchain.chat_models import ChatOpenAI
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
# Initialize OpenAI LLM (Large Language Model)
llm = ChatOpenAI(model="gpt-4")


# Function to generate translation
def translate_text(text, target_language):
    # Construct the prompt to translate the text
    prompt = f"Translate the following text to {target_language}: {text}"

    # Generate translation using OpenAI's LLM (via LangChain)
    response = llm.invoke([{
        "role": "system",
        "content": "You are a helpful assistant providing translations."
    }, {
        "role": "user",
        "content": prompt
    }])

    # Extract the translation from the response
    translation = response.content.strip()  # Get the content of the first message

    return translation
