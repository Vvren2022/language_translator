# language_helper.py
from langchain.chat_models import ChatOpenAI
import math

# Initialize the OpenAI LLM
llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.2, max_tokens=2000)


# Function to generate translation prompt
def get_translation_prompt(text, target_language):
    return f"""
    You are a professional translator.
    Translate the following text into {target_language} while maintaining **accuracy, fluency, and natural tone**.
    - **Simple words** should be translated **directly** without adding unnecessary complexity.
    - **Idioms, slang, and cultural references** should be translated using an **equivalent expression** in {target_language}, not word-for-word.
    - Maintain **formal grammar** where appropriate.

    Text: "{text}"
    """


# Function to chunk text if it's too long
def chunk_text(text, max_length=2000):
    # Split text into chunks that fit the model's max token limit
    words = text.split()
    chunks = []
    chunk = []

    for word in words:
        chunk.append(word)
        if len(' '.join(chunk)) > max_length:
            chunks.append(' '.join(chunk[:-1]))  # Add the previous chunk
            chunk = [word]  # Start new chunk

    if chunk:
        chunks.append(' '.join(chunk))  # Add the last chunk

    return chunks


# Function to translate text into any language with chunking for long text
def translate_text(text, target_language):
    prompt = get_translation_prompt(text, target_language)

    # If the text is too long, split it into smaller chunks
    chunks = chunk_text(text)

    translation = ""
    for chunk in chunks:
        # Generate the translation for each chunk
        response = llm.invoke([
            {"role": "user", "content": prompt + "\n" + chunk}
        ])
        translation += response.content.strip() + " "  # Combine translated chunks

    return translation.strip()  # Return full translated text after combining chunks
