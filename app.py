"""
This script prompts the user for a question on the terminal and hits openai API to get a response from the model.

    Example Usage:
    (Note: The response to the above question will differ based on whether the chosen model is 3.5 or 4.)
    ```sh
    docker run -it --rm \
        --env OPENAI_API_KEY=<your-api-key> \
        -p 5000:5000 \
        babajikifauj/gpt-4:latest
    ```
        User: I'm in my house. On the top of my chair in the living room is a coffee cup. Inside the coffee cup is a thimble. Inside the thimble is a single diamond. I move the chair to my bedroom. Then I put the coffee cup on the bed. Then I turn the the cup upside down. Then I return it to rightside-up, and place the coffee cup on the kitchen counter. Where is my diamond?

        Bot (gpt-3.5-turbo): The diamond is inside the thimble, which is inside the coffee cup, which is on the kitchen counter.

        Bot (gpt-4): Your diamond is most likely on the bed since you turned the coffee cup upside down while it was on the bed, causing the diamond to fall out of the thimble and onto the bed.
"""

import os
from math import ceil
import openai
import logging
import streamlit as st

logger = logging.getLogger()
logging.basicConfig(level=logging.WARN)

# Hard-code which model to use
MODEL_ID = 'gpt-4'


def add_message(message_type, content):
    conversation = st.session_state.get("conversation", [])
    conversation.append({"role": message_type, "content": content})
    st.session_state.conversation = conversation

def chatgpt_convo():
    conversation = st.session_state.get("conversation", [])
    cost = st.session_state.get("cost", 0)

    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=conversation
    )
    cost += ceil(response['usage']['prompt_tokens'] / 1000) * 0.03 + \
        ceil(response['usage']['completion_tokens'] / 1000) * 0.06
    content = response['choices'][0]['message']['content']
    conversation.append(
        {
            "role": "assistant",
            "content": content
        }
    )

    st.session_state.conversation = conversation
    st.session_state.cost = cost

    return {
        "conversation": conversation,
        "cost": cost
    }

def main():
    st.set_page_config(page_title="Chat with OpenAI GPT", page_icon=":speech_balloon:")

    st.title("Chat with OpenAI GPT")

    if "OPENAI_API_KEY" in os.environ:
        API_KEY = os.environ["OPENAI_API_KEY"]
    else:
        # Read it from local
        with open('.key', 'r') as f:
            API_KEY = f.read()

    openai.api_key = API_KEY

    if "conversation" not in st.session_state:
        st.session_state.conversation = []
        st.session_state.cost = 0

    input_placeholder = "Type your message here (press Shift+Enter for a newline)"
    with st.form(key='input-form'):
        content = st.text_area("You:", value='', key='input', help=input_placeholder)

        if st.form_submit_button(label='Send'):
            add_message('user', content)
            response = chatgpt_convo()['conversation'][-1]['content']
            st.write("OpenAI GPT:", response, unsafe_allow_html=True)
            st.write("")
        elif st.form_submit_button(label='Reset'):
            st.session_state.conversation = []
            st.session_state.cost = 0
            st.write("Conversation reset.")
            st.write("")

    if not content:
        st.stop()

    st.write("Chat History:")
    for item in st.session_state.conversation:
        if item['role'] == 'user':
            st.write("You: " + item['content'])
        elif item['role'] == 'assistant':
            st.write("OpenAI GPT: " + item['content'], unsafe_allow_html=True)

    st.write("")
    st.write("Cost: ${:.2f}".format(st.session_state.cost))


if __name__ == '__main__':
    main()
