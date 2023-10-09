import os
import openai
import toml
import streamlit as st

#secrets = toml.load("secrets.toml")
#openai.api_key = secrets["openai_api_key"]

openai.api_key = st.secrets["openai_api_key"]


def generate_test_text(test_text):
    text = f"""You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \ 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \ 
then simply write \"No steps provided.\"

\"\"\"{test_text}\"\"\"
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=0.6,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response
    print(response)
