import streamlit as st
import openai

opanai.apy_key = "sk-JGftaPYrPTKm8jnXAcZgT3BlbkFJzf61UE7lsdWWmM0AZdk"

def main():
    st.title("CHAT WITH YOUR DOCUMENT")
    st.write("Welcome to the personal chatbot agent that know whats in your documents!")
    user_input = st.text_input("Ask anything about your dcouments")
    if user_input:
        st.button("Send")
        response = opanai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Answer the following based on the documents selected" + user_input, 
            max_tokens = 3000,
            temperature = 0.0,
        )

        res = response["choices"][0]["text"]
        st.write(f"You said: {user_input}")

if __name__ == "__main__":
    main()
