import streamlit as st
# from language_helper import translate_text
# from complex_language_translator import translate_text
# from worst_case_handle_language_translator import translate_text
# from language_embedding_translator import translate_text
# from language_translator_with_vectordatabase import translate_text
from final_translator import translate_text
# Streamlit UI
# st.title("LLM Language Translator")
#
# # Text input and target language selection
# text = st.text_area("Enter text to translate:")
# target_language = st.selectbox("Select target language:", ["French", "German", "Spanish", "Chinese", "Italian","English"])
#
# # Translate button
# if st.button("Translate"):
#     if text:
#         translated_text = translate_text(text, target_language)
#         st.write(f"Translated text: {translated_text}")
#     else:
#         st.error("Please enter some text.")
#

# main.py
# import streamlit as st
# # from language_helper import translate_text  # Importing translation function
#
# # Streamlit page configuration
# st.set_page_config(page_title="Global Language Translator", layout="centered")
#
# # App title
# st.title("Global Language Translator")
#
# # Text input by the user
# text = st.text_area("Enter text to translate:", "", height=150)
#
# # Dropdown for selecting the target language
# languages = [
#     "French", "Spanish", "Chinese", "Hindi", "Arabic", "Russian", "Japanese", "Italian"
# ]
# target_language = st.selectbox("Select target language:", languages)
#
# # When the button is pressed, perform the translation
# if st.button("Translate"):
#     if text:
#         # Call the translation function
#         translation = translate_text(text, target_language)
#         st.subheader(f"Translation in {target_language}:")
#         st.write(translation)
#     else:
#         st.error("Please enter text to translate.")



# main.py
import streamlit

# main.py
# import streamlit as st
# # from language_helper import translate_text
#
# # Streamlit UI
# st.title("🌍 AI-Powered Language Translator")
#
# # Input fields
# text = st.text_area("Enter text to translate:", height=150)
# target_language = st.selectbox("Select target language:",
#                                ["French", "German", "Spanish", "Chinese", "Japanese", "Italian", "Russian", "Arabic"])
#
# # Translate button
# if st.button("Translate"):
#     if text.strip():
#         translation = translate_text(text, target_language)
#         st.success("Translation:")
#         st.write(translation)
#     else:
#         st.warning("Please enter some text for translation.")



# main.py
# import streamlit as st
#   # Importing translation function
#
# # Streamlit page configuration
# st.set_page_config(page_title="Global Language Translator", layout="centered")
#
# # App title
# st.title("Global Language Translator")
#
# # Text input by the user
# text = st.text_area("Enter text to translate:", "", height=150)
#
# # Dropdown for selecting the target language
# languages = [
#     "French", "Spanish", "Chinese", "Hindi", "Arabic", "Russian", "Japanese", "Italian"
# ]
# target_language = st.selectbox("Select target language:", languages)
#
# # When the button is pressed, perform the translation
# if st.button("Translate"):
#     if text:
#         # Call the translation function
#         translation = translate_text(text, target_language)
#         st.subheader(f"Translation in {target_language}:")
#         st.write(translation)
#     else:
#         st.error("Please enter text to translate.")


# main.py
# import streamlit as st
#  # Importing translation function
#
# # Streamlit page configuration
# st.set_page_config(page_title="Global Language Translator", layout="centered")
#
# # App title
# st.title("Global Language Translator")
#
# # Text input by the user
# text = st.text_area("Enter text to translate:", "", height=150)
#
# # Dropdown for selecting the target language
# languages = [
#     "French", "Spanish", "Chinese", "Hindi", "Arabic", "Russian", "Japanese", "Italian","German"
# ]
# target_language = st.selectbox("Select target language:", languages)
#
# # When the button is pressed, perform the translation
# if st.button("Translate"):
#     if text:
#         # Call the translation function
#         translation = translate_text(text, target_language)
#         st.subheader(f"Translation in {target_language}:")
#         st.write(translation)
#     else:
#         st.error("Please enter text to translate.")



# main.py
# import streamlit as st
#  # Importing translation function
#
# # Streamlit page configuration
# st.set_page_config(page_title="Global Language Translator", layout="centered")
#
# # App title
# st.title("Global Language Translator")
#
# # Text input by the user
# text = st.text_area("Enter text to translate:", "", height=150)
#
# # Dropdown for selecting the target language
# languages = [
#     "French", "Spanish", "Chinese", "Hindi", "Arabic", "Russian", "Japanese", "Italian"
# ]
# target_language = st.selectbox("Select target language:", languages)
#
# # When the button is pressed, perform the translation
# if st.button("Translate"):
#     if text:
#         # Call the translation function
#         translation = translate_text(text, target_language)
#         st.subheader(f"Translation in {target_language}:")
#         st.write(translation)
#     else:
#         st.error("Please enter text to translate.")



import streamlit as st
# from language_helper import translate_text

# Streamlit UI Setup
st.set_page_config(page_title="AI Translator", layout="centered")

st.title("🌍 AI-Powered Language Translator")

st.write("Translate text into any language with accurate, fluent, and context-aware translation.")

# User Input
text = st.text_area("Enter text to translate:", height=150)
target_language = st.text_input("Enter target language (e.g., German, French, Spanish)")

if st.button("Translate"):
    if text.strip() and target_language.strip():
        with st.spinner("Translating... ⏳"):
            translated_text = translate_text(text, target_language)
        st.success("Translation Complete! ✅")
        st.text_area("Translated Text:", translated_text, height=150)
    else:
        st.warning("⚠️ Please enter text and target language.")


