import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# ---------------- ENV ----------------
load_dotenv()  # HF_TOKEN in .env

# ---------------- HF CLIENT ----------------
client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Gov Scheme Chatbot 2026",
    page_icon="🇮🇳",
    layout="centered"
    
)

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
<style>
/* ---- Global font & background ---- */
html, body, [class*="css"] {
    font-family: 'Segoe UI', 'Poppins', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top left, #1a1a2e 0%, #0f0f1a 60%, #0a0a12 100%);
}

/* ---- Hero header ---- */
.hero-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #FFFFFF;
    padding-top: 10px;
    margin-bottom: 0px;
    letter-spacing: 0.5px;
}

.hero-title .accent-orange {
    color: #FF9933;
}

.hero-title .accent-green {
    color: #138808;
}

.hero-subtitle {
    text-align: center;
    font-size: 17px;
    color: #b5b5c3;
    margin-top: 4px;
    margin-bottom: 25px;
}

.hero-divider {
    height: 3px;
    border: none;
    border-radius: 5px;
    margin: 10px auto 30px auto;
    width: 60%;
    background: linear-gradient(90deg, #FF9933, #FFFFFF, #138808);
}

/* ---- Sidebar ---- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #16161f 0%, #0f0f17 100%);
    border-right: 1px solid rgba(255,153,51,0.25);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #FF9933;
}

/* ---- Form fields ---- */
div[data-baseweb="select"] > div, .stNumberInput input, .stTextInput input {
    background-color: #1c1c29 !important;
    border: 1px solid rgba(255,153,51,0.35) !important;
    border-radius: 10px !important;
    color: #f0f0f0 !important;
}

/* ---- Buttons ---- */
.stButton button, .stFormSubmitButton button {
    background: linear-gradient(90deg, #FF9933, #e0701c);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
    transition: 0.25s ease-in-out;
    width: 100%;
}

.stButton button:hover, .stFormSubmitButton button:hover {
    background: linear-gradient(90deg, #138808, #0e6606);
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(19,136,8,0.35);
}

/* ---- Chat message cards ---- */
div[data-testid="stChatMessage"] {
    background: #161622;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 6px 10px;
    margin-bottom: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.35);
}

/* ---- Sidebar query history cards ---- */
section[data-testid="stSidebar"] .stMarkdown p {
    font-size: 13.5px;
}

/* ---- Divider styling ---- */
hr {
    border-color: rgba(255,255,255,0.08) !important;
}

/* ---- Caption ---- */
.stCaption, .css-1cpxqw2 {
    text-align: center;
}
</style>

<h1 class="hero-title"><span class="accent-orange">🇮🇳 Government</span> Scheme <span class="accent-green">Advisor</span></h1>
<p class="hero-subtitle">Find the best Central &amp; State Government Schemes tailored to you.</p>
<hr class="hero-divider">
""", unsafe_allow_html=True)

# Session state for history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar input
st.sidebar.header("Tell me about yourself")
st.sidebar.markdown("## 👤 User Profile")

with st.sidebar.form("user_form", clear_on_submit=False):
    age = st.number_input("Your Age", min_value=18, max_value=100, step=1)
    gender = st.selectbox(
        "Gender",
        ("Male", "Female", "Other")
    )
    occupation = st.selectbox(
        "Occupation",
        ("Student", "Farmer", "Private Job", "Government Job", "Self Employed", "Unemployed")
    )
    income = st.number_input("Monthly Income (₹)", min_value=0, step=1000)
    state = st.text_input("State (e.g. Uttar Pradesh)")
    category = st.selectbox("Category", ("General", "OBC", "SC", "ST"))
    submitted = st.form_submit_button("Find My Schemes")


# Core recommendation function
def recommend_schemes(age, gender, occupation, income, state, category):
    system_prompt = """
You are a brutal but helpful Indian Government Scheme Advisor.
STRICT RULES:
- Be honest and direct
- Clearly explain eligibility or rejection
- Recommend only REAL schemes
- Prefer State then Central
- Use bullets
- Plain text output
-If the user asks anything outside Indian government schemes, politely refuse and redirect them back to scheme-related questions.

"""
    user_prompt = f"""
User Profile:
- Age: {age}
- Gender: {gender}
- Occupation: {occupation}
- Income: ₹{income}
- State: {state}
- Category: {category}

Task:
Recommend the best government schemes with steps.
"""
    # Model that is *actually supported* via providers
    model_id = "Qwen/Qwen2.5-7B-Instruct"

    response = client.chat_completion(
        model=model_id,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


# Clear history
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.experimental_rerun()

# Sidebar history
if st.session_state.chat_history:
    st.sidebar.divider()
    st.sidebar.header("📜 Previous Queries")
    for i, chat in enumerate(reversed(st.session_state.chat_history), 1):
        st.sidebar.markdown(
            f"""
            <div style='background:#1c1c29;border:1px solid rgba(255,153,51,0.25);
            border-radius:10px;padding:10px 12px;margin-bottom:10px;'>
            <p style='color:#FF9933;font-weight:600;margin:0 0 4px 0;font-size:13px;'>Query {i}</p>
            <p style='color:#d5d5df;font-size:12.5px;margin:0 0 6px 0;'>{chat['user']}</p>
            <p style='color:#9be29b;font-size:12px;margin:0;'>{chat['assistant'][:150]}{'...' if len(chat['assistant']) > 150 else ''}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# When form submitted
if submitted:
    user_input = (
        f"Age: {age}, Gender: {gender}, Occupation: {occupation}, Income: ₹{income}, "
        f"State: {state}, Category: {category}"
    )

    with st.spinner("Finding the best government schemes for you... 🇮🇳"):
        answer = recommend_schemes(age, gender, occupation, income, state, category)

    st.session_state.chat_history.append({"user": user_input, "assistant": answer})
    st.chat_message("assistant").markdown(answer)

# Follow‑up chat
user_question = st.chat_input("Ask about a scheme...")

if user_question:
    messages = [
        {"role": "system", "content": "You are Brutal Government Scheme Advisor. Answer plainly."}
    ]
    for chat in st.session_state.chat_history:
        messages.append({"role": "user", "content": chat["user"]})
        messages.append({"role": "assistant", "content": chat["assistant"]})
    messages.append({"role": "user", "content": user_question})

    with st.spinner("Thinking... 🇮🇳"):
        response = client.chat_completion(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=messages,
            max_tokens=800,
            temperature=0.3
        )

    text = response.choices[0].message.content.strip()
    st.session_state.chat_history.append({"user": user_question, "assistant": text})
    st.chat_message("assistant").markdown(text)

st.divider()
st.markdown(
    "<p style='text-align:center;color:#9a9aa8;font-size:13px;'>"
    "⚠️ Always verify schemes from official government portals.</p>",
    unsafe_allow_html=True
)