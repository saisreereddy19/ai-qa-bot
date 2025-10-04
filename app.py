import streamlit as st
import ollama

# Streamlit Page Setup
st.set_page_config(page_title="AI Q&A Bot 🤖", page_icon="💬")
st.title("💬 AI Q&A Bot (Llama 3 1B via Ollama)")
st.write("Ask me anything — powered by **Llama 3 1B** running locally through Ollama!")

# Input box for user question
question = st.text_input("Enter your question:")

# When user clicks "Ask" button
if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                # Query Ollama model
                response = ollama.chat(
                    model="llama3:1b",  # ✅ lighter model for low-RAM systems
                    messages=[
                        {"role": "system", "content": "You are a helpful AI assistant."},
                        {"role": "user", "content": question}
                    ]
                )

                # Extract the answer
                answer = response["message"]["content"]
                st.success(answer)

            except Exception as e:
                st.error(f"Error: {e}")
