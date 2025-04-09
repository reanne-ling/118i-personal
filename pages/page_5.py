import openai
import os
import openai
import streamlit as st
import requests
from openai import OpenAI

# using openai api key to access 
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# for it to pop up on the sidebar
st.sidebar.markdown("# Translator 🌍")

# page title
st.header('Translator 🌍', divider= 'blue')
st.write('Access real-time language support to help you understand forms, ' \
'instructions, and key information—available in multiple languages.')

# Create two selectbox buttons
# these languages are based on local demogrpahic data within San Jose (Santa Clara County)
source_language = st.selectbox('Select Source language', [
    'English', 'Spanish', 'French', 'Vietnamese', 
    'Mandarin', 'Cantonese', 'Tagalog', 'Korean', 'Hindi', 
    'Arabic', 'Russian', 'Farsi', 'Punjabi', 'Japanese', 
    'Portuguese', 'Thai'
    ])
target_language = st.selectbox('Select Target language', [
    'English', 'Spanish', 'French', 'Vietnamese', 
    'Mandarin', 'Cantonese', 'Tagalog', 'Korean', 'Hindi', 
    'Arabic', 'Russian', 'Farsi', 'Punjabi', 'Japanese', 
    'Portuguese', 'Thai'
    ])

# Create a text input field
text = st.text_input('Enter the text you want to translate: ')

# Create a button
if st.button('Submit'):
    # Print the input from the text field and radio buttons
    st.write(f'You entered: {text}')
    st.write(f'Source language: {source_language}')
    st.write(f'Target language: {target_language}')

# function to translate the text
def translate(text, source_language = "English", target_language = "French"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a sentence in "+ source_language
                +", and your task is to translate it into " + target_language 
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    return response.choices[0].message.content
st.write(translate(text, source_language, target_language))

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎")