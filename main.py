import streamlit as st
from huggingface_hub import InferenceClient

# ==========================
# Paste your NEW Hugging Face Token here
# ==========================


HF_TOKEN = st.secrets["HF_TOKEN"]
client = InferenceClient(
    api_key=HF_TOKEN,
)

SYSTEM_PROMPT = """
You are Dhinesh AI.

You are a friendly, intelligent and supportive AI assistant created by Dhinesh.

Your job is to help students and everyone with:

- College Life
- Semester Preparation
- Placements
- Resume Building
- Coding
- Career Guidance
- Productivity
- Time Management
- Communication Skills
- Personal Development
- Motivation
- General Life Advice

Rules:
- Be friendly.
- Keep answers simple.
- Explain clearly.
- Encourage users.
- Never answer illegal or harmful requests.
- For medical/legal advice, recommend consulting a professional.
"""

st.set_page_config(
    page_title="Dhinesh AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Dhinesh AI")
st.caption("Your Personal AI Mentor")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome Message
if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.markdown("""
# 👋 Hello! I'm **Dhinesh AI**

Welcome! 😊

I'm your personal AI mentor created by **Dhinesh**.

### I can help you with:

🎓 College & Campus Life

📚 Study Plans & Semester Preparation

💻 Programming & Coding

📄 Resume Building & ATS Tips

💼 Placements & Career Guidance

🧠 Interview Preparation

⏰ Productivity & Time Management

🗣️ Communication Skills

🌱 Personal Development & Motivation

❤️ General Life Advice

---

💬 **Ask me anything! I'm here to help you.**
""")

# Show previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Type your question here...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.chat.completions.create(
                    
                    model="Qwen/Qwen2.5-7B-Instruct",
                    messages=messages,
                    max_tokens=500,
                    temperature=0.7
                )

                answer = response.choices[0].message.content

            except Exception as e:

                answer = f"❌ Error:\n\n{e}"

            st.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )