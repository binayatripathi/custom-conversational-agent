import streamlit as st

def main():
    st.title("Conversational Agent")
    st.write("Welcome to the conversational agent!")
    user_input = st.text_input("Type your message here:")
    if user_input:
        st.write(f"You said: {user_input}")

if __name__ == "__main__":
    main()
