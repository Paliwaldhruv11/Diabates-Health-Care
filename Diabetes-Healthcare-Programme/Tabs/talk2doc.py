import streamlit as st
from openai import APIStatusError, RateLimitError

from groq_config import get_groq_api_key, groq_chat_completion


def ask_diabetes_assistant(query: str) -> str:
    system = (
        "You are a medical chatbot specialized in diabetes and its health implications. "
        "Answer only diabetes-related queries with medically accurate information. "
        "If a question is unrelated to diabetes, politely inform the user that you can only "
        "answer diabetes-related questions."
    )
    user = (
        f"**User's Question:** {query}\n\n"
        "Provide a clear, concise, and accurate medical response."
    )
    return groq_chat_completion(
        [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
    )


def app():
    if not get_groq_api_key():
        st.error(
            "Groq API key is missing. Add `GROQ_API_KEY=gsk_...` to `.env` next to `main.py`, "
            "or `GROQ_API_KEY` in `.streamlit/secrets.toml`. Keys: https://console.groq.com/keys"
        )
        st.warning(
            "If you already pasted the key in `.env`, **save the file (Ctrl+S)** — unsaved edits are not read — "
            "then **restart Streamlit**."
        )
        st.stop()

    st.title("🩺 Diabetes Medical Chatbot")
    st.image("./images/capsule.png", use_container_width=True)
    st.success("Please ask your queries related to diabetes and its health implications.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_query = st.text_input("Ask your question about diabetes:")

    if st.button("Get Answer"):
        if user_query:
            try:
                response = ask_diabetes_assistant(user_query)
            except RateLimitError:
                st.error(
                    "Groq rate limit reached (HTTP 429). Wait a moment and try again, "
                    "or set `GROQ_MODEL` in `.env` to another model. "
                    "See https://console.groq.com/docs/rate-limits"
                )
            except APIStatusError as e:
                st.error(f"Groq API error: {e.message}")
            else:
                st.session_state.chat_history.append(("You", user_query))
                st.session_state.chat_history.append(("Chatbot", response))

    st.subheader("Chat History:")
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑‍⚕️ {role}:** {message}")
        else:
            st.markdown(f"**🤖 {role}:** {message}")


if __name__ == "__main__":
    app()
