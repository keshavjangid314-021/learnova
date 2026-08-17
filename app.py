import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Learnova | CBSE Class 12 Physics AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Cleanup & Masking
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

div[class*="viewerBadge"], 
div[class*="styles_viewerBadge"],
button[title*="Streamlit Community Cloud"],
.stAppViewerBadge,
iframe[src*="accessibility"],
div[aria-label="Streamlit status"] {
    display: none !important;
    visibility: hidden !important;
}

.sim-container {
    position: relative;
    width: 100%;
    height: 480px;
    overflow: hidden;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.sim-container iframe {
    width: 100%;
    height: 530px;
    border: none;
    margin-top: -5px;
}
</style>
""", unsafe_allow_html=True)

# 3. Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Sidebar History Setup
with st.sidebar:
    st.title("💬 Chat History")
    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.caption(f"📌 {msg['content'][:25]}...")

# 5. Main UI
st.title("⚡ Learnova Physics AI Tutor")
st.caption("CBSE Class 12 Physics Assistant")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# 6. Response Logic
def generate_response(prompt):
    text = prompt.lower().strip()
    
    if "what is" in text or "define" in text or "definition" in text:
        if "solenoid" in text:
            return """
### 🧲 What is a Solenoid?

A **solenoid** is a long helical coil of insulated copper wire wound tightly around a cylindrical frame. When current flows through it, it produces a uniform magnetic field inside its core, behaving like a bar magnet.

* **Formula:** $B = \\mu_0 n I$
  * $\\mu_0$ = Permeability of free space
  * $n$ = Turns per unit length ($N/L$)
  * $I$ = Current in Amperes
* **Key Feature:** Magnetic field inside is **strong and uniform**, while outside it is close to **zero**.
"""
        elif "huygen" in text:
            return "### 🌊 Huygens' Principle\nEvery point on a primary wavefront acts as a fresh source of secondary wavelets, spreading out in all directions with the speed of light."
        elif "kirchhoff" in text:
            return "### ⚡ Kirchhoff's Laws\n* **KCL (Junction Rule):** Total current entering a junction equals total current leaving ($\\sum I = 0$).\n* **KVL (Loop Rule):** Sum of all potential differences in a closed loop is zero ($\\sum V = 0$)."

    elif "how" in text or "work" in text or "working" in text:
        if "solenoid" in text:
            return """
### ⚙️ How a Solenoid Works (Working Principle)

1. **Magnetic Field Generation:** Direct current (DC) flowing through each loop generates a magnetic field around the wire via the Right-Hand Thumb Rule.
2. **Field Alignment:** Individual circular fields sum up along the central axis of the cylinder to form a strong, directional magnetic field line.
3. **Polarity:** 
   * Clockwise current side = **South Pole**
   * Anti-clockwise current side = **North Pole**

---
### 🔬 Interactive 3D Simulation
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"></iframe>
</div>
"""
        elif "huygen" in text:
            return "### ⚙️ How Huygens' Principle Works\nBy constructing forward envelopes touching the secondary wavelets, we can predict the exact new position of a wavefront at time $t$."

    return f"I received your query: **'{prompt}'**\n\nTry asking specific questions like:\n* *'What is a solenoid?'*\n* *'How does a solenoid work?'*"

# 7. Input Handling
if user_prompt := st.chat_input("Ask Learnova AI..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    response = generate_response(user_prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True)
