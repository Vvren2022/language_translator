from langchain.chat_models import ChatOpenAI
import tiktoken
import time
import os



os.environ["OPENAI_API_KEY"]=grisha_key
# Initialize the OpenAI LLM
llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.2, max_tokens=2000)

# Tokenizer for counting tokens
tokenizer = tiktoken.encoding_for_model("gpt-4-turbo")


# Function to generate a translation prompt
def get_translation_prompt(text, target_language):
    return f"""
    You are a **professional translator**.
    - **Simple words** → Translate directly without adding complexity.
    - **Idioms, slang, cultural references** → Use **equivalent expressions** in {target_language}, NOT word-for-word.
    - **Grammar & Sentence Structure** → Must be **accurate and formal**.
    - **Maintain original tone** (formal/informal).

    Translate to {target_language}:
    "{text}"
    """


# Function to chunk text based on token count
def chunk_text(text, max_tokens=2000):
    words = text.split()
    chunks = []
    chunk = []

    for word in words:
        chunk.append(word)
        token_count = len(tokenizer.encode(" ".join(chunk)))

        if token_count > max_tokens:
            chunks.append(" ".join(chunk[:-1]))  # Store last valid chunk
            chunk = [word]  # Start a new chunk

    if chunk:
        chunks.append(" ".join(chunk))  # Add the last chunk

    return chunks


# Function to translate text with chunking & error handling
def translate_text(text, target_language):
    chunks = chunk_text(text)

    translation = []
    for chunk in chunks:
        prompt = get_translation_prompt(chunk, target_language)

        try:
            response = llm.invoke([{"role": "user", "content": prompt}])
            translated_chunk = response.content.strip() if response and response.content else ""
            translation.append(translated_chunk)
        except Exception as e:
            print(f"Error during translation: {e}")
            translation.append("[Translation failed for this part]")  # Fallback text

        time.sleep(1)  # Prevent hitting API rate limits

    return " ".join(translation).strip()
