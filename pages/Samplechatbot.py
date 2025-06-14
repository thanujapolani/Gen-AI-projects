import streamlit as st
from langchain_openai import OpenAI

# Streamlit Page Configuration
st.set_page_config(page_title="LangChain LLM Explorer", layout="centered")

# Title and description
st.title("🔤 LangChain LLM Explorer")
st.markdown("""
This app uses **LangChain** and **OpenAI GPT-3.5** to demonstrate how large language models work using text input/output.
""")

# Sidebar - API Key Input
st.sidebar.header("🔐 API Key")
openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# User input prompt
st.subheader("💬 Ask a Question")
user_query = st.text_input("Type a question or prompt to send to the LLM:")

# Model settings (could also be sliders or inputs)
temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=2.0)
top_p = st.slider("Top-p", min_value=0.0, max_value=1.0, value=1.0)

# Submit button
if st.button("Run LLM"):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif not user_query:
        st.warning("Please enter a prompt before running the model.")
    else:
        try:
            # Initialize the OpenAI model
            llm = OpenAI(
                temperature=temperature,
                top_p=top_p,
                model_name="gpt-3.5-turbo-instruct",
                openai_api_key=openai_api_key
            )

            # Invoke the model
            with st.spinner("Generating response..."):
                response = llm.invoke(user_query)
            st.success("Response generated successfully!")
            st.markdown("### 🧠 Model Output")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built using [LangChain](https://python.langchain.com) and [Streamlit](https://streamlit.io).")
