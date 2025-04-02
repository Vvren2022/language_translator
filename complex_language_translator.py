# language_helper.py
from langchain.chat_models import ChatOpenAI

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


# Function to translate text into any language
def translate_text(text, target_language):
    prompt = get_translation_prompt(text, target_language)

    response = llm.invoke([
        {"role": "user", "content": prompt}
    ])

    return response.content.strip()  # Extract only the translated text
