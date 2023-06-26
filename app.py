import streamlit as st

def main():
    st.title("CHAT WITH YOUR DOCUMENT")
    st.write("Welcome to the personal chatbot agent that know whats in your documents!")
    user_input = st.text_input("Ask abything about your dcouments")
    if user_input:
        st.write(f"You said: {user_input}")

if __name__ == "__main__":
    main()
