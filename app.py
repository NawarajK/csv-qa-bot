import streamlit as st
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

def setup_environment():
    """Loads environment variables from .env file."""
    load_dotenv()

def get_api_key():
    """Retrieves the OpenAI API key from environment variables."""
    return os.getenv("OPENAI_API_KEY")

def display_header():
    """Displays the main header and informational message for the app."""
    st.title("CSV Q&A Bot")
    st.info("This app allows you to upload a CSV file and ask questions about its content using natural language.")

def handle_file_upload():
    """Handles the file upload and returns the uploaded file."""
    return st.file_uploader("Choose a CSV file", type="csv")

def get_answer(data, question, api_key):
    """Gets the answer from the AI model."""
    with st.spinner("Thinking..."):
        try:
            llm = OpenAI(api_key=api_key)
            agent = create_pandas_dataframe_agent(llm, data, verbose=True, allow_dangerous_code=True)
            return agent.run(question)
        except Exception as e:
            st.error(f"An error occurred with the AI model: {e}")
            return None

def display_history():
    """Displays the conversation history."""
    if "history" in st.session_state and st.session_state.history:
        st.subheader("Conversation History")
        for i, chat in enumerate(reversed(st.session_state.history)):
            st.markdown(f"**Q{len(st.session_state.history) - i}:** {chat['question']}")
            st.markdown(f"**A{len(st.session_state.history) - i}:** {chat['answer']}")
            st.markdown("---")

def main():
    """Main function to run the Streamlit app."""
    setup_environment()
    api_key = get_api_key()

    display_header()

    if "history" not in st.session_state:
        st.session_state.history = []

    uploaded_file = handle_file_upload()

    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            st.write("Here is the data from your CSV file:")
            st.dataframe(data)

            question = st.text_input("Ask a question about your data:")

            if question:
                if api_key:
                    answer = get_answer(data, question, api_key)
                    if answer:
                        st.session_state.history.append({"question": question, "answer": answer})
                        st.write("Answer:")
                        st.write(answer)
                else:
                    st.warning("OpenAI API Key not found. Please create a .env file with your key.")
            
            display_history()

        except Exception as e:
            st.error(f"An error occurred while reading the CSV file: {e}")

if __name__ == "__main__":
    main()