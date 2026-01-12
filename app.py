import time
import datetime
import streamlit as st

from llm_client import generate_response
from prompt import SYSTEM_PROMPT

# ------------------- Demo Protection Settings -------------------
HUMAN_CODE = "TAMIRA"          # simple human check gate
MAX_CALLS_PER_MIN = 6          # per browser session
DAILY_SESSION_LIMIT = 30       # per browser session per day
MAX_INPUT_CHARS = 1500         # prevent huge prompts (cost control)

# Optional: remote kill switch via Streamlit Secrets
# In Streamlit Cloud -> Manage app -> Settings -> Secrets:
# DEMO_DISABLED="false"
DEMO_DISABLED = str(st.secrets.get("DEMO_DISABLED", "false")).lower() == "true"
# ---------------------------------------------------------------

st.title("Tamira AI")
st.caption(
    "🇩🇪 Hinweis: Um mein Budget nicht zu sprengen, ist diese Demo limitiert (Anzahl Anfragen pro Minute/Tag). "
    "🇬🇧 Note: To avoid exceeding my budget, this demo is rate-limited (number of requests per minute/day)."
)


# ----- Admin kill switch -----
if DEMO_DISABLED:
    st.error("Demo is temporarily disabled.")
    st.stop()

# ----- Human check gate -----
st.session_state.setdefault("human_ok", False)

if not st.session_state["human_ok"]:
    code = st.text_input("Type TAMIRA to start (demo protection):").strip().upper()
    if code == HUMAN_CODE:
        st.session_state["human_ok"] = True
        st.rerun()
    else:
        st.info("Enter the code to use the demo.")
        st.stop()

# ----- Rate limit per minute (session) -----
now = time.time()
st.session_state.setdefault("calls", [])
st.session_state["calls"] = [t for t in st.session_state["calls"] if now - t < 60]

if len(st.session_state["calls"]) >= MAX_CALLS_PER_MIN:
    st.warning("Too many requests. Please wait a minute and try again.")
    st.stop()

# ----- Daily session kill switch -----
today = datetime.date.today().isoformat()
st.session_state.setdefault("day", today)
st.session_state.setdefault("daily_count", 0)

if st.session_state["day"] != today:
    st.session_state["day"] = today
    st.session_state["daily_count"] = 0

if st.session_state["daily_count"] >= DAILY_SESSION_LIMIT:
    st.error("Daily demo limit reached for this session. Please come back tomorrow.")
    st.stop()

# ----- Chat state -----
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Render chat history (excluding system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ----- User input -----
prompt = st.chat_input("Say something")

if prompt:
    prompt = prompt.strip()

    # Input size guard (cost control)
    if len(prompt) > MAX_INPUT_CHARS:
        st.warning(f"Please keep messages under {MAX_INPUT_CHARS} characters for the demo.")
        st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    # ✅ Count the call right before we trigger the LLM (cost point)
    st.session_state["calls"].append(time.time())
    st.session_state["daily_count"] += 1

    # ----- Assistant streaming response -----
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            for chunk in generate_response(st.session_state.messages):
                delta = chunk.choices[0].delta
                if delta and getattr(delta, "content", None):
                    full_response += delta.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        except Exception:
            # Don't leak internal details to users
            st.error("Something went wrong while generating a response. Please try again.")
            st.stop()

    st.session_state.messages.append({"role": "assistant", "content": full_response})
