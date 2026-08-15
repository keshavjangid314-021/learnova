import streamlit as st

# 1. Page Configuration (Dark Theme)
st.set_page_config(page_title="Learnova | CBSE Physics AI", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    h1, h2, h3, h4 { color: #58A6FF !important; }
    .stChatMessage { background-color: #161B22; border-radius: 10px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Learnova AI")
st.caption("Class 12 CBSE Physics Mini-ChatGPT Tutor")

# 2. About Learnova & Quick Formulas Header
with st.expander("ℹ️ About Learnova & Formula Cheat-Sheet", expanded=False):
    st.write("""
    **Learnova** provides instant CBSE Class 12 NCERT physics answers paired with live 3D PhET simulations directly in the chat!
    
    * **Solenoid Magnetic Field:** $B = \\mu_0 n I$
    * **Huygens' Wave Velocity:** $v = f \\lambda$
    * **Kirchhoff's Junction Rule (KCL):** $\\sum I = 0$ *(Charge Conservation)*
    * **Kirchhoff's Loop Rule (KVL):** $\\sum \\Delta V = 0$ *(Energy Conservation)*
    """)

# 3. Comprehensive CBSE Topic Knowledge Base
KNOWLEDGE_BASE = {
    "solenoid": {
        "title": "🧲 Solenoid & Magnetic Field (Class 12 CBSE)",
        "content": """
**NCERT Definition:** A solenoid is a long helical coil of insulated copper wire tightly wound around a cylindrical frame.

**Key CBSE Theory Points:**
* **Internal Field:** Magnetic field lines inside a long, tightly wound solenoid are straight, parallel, and uniform.
* **External Field:** Outside the solenoid, magnetic field lines are weak and spread out, effectively considered zero.
* **Magnetic Equivalence:** A current-carrying solenoid produces a magnetic field pattern identical to a **Bar Magnet** with North and South poles.

**NCERT Formula:**
$$B = \\mu_0 n I$$
*(where $B$ = magnetic field strength, $\\mu_0 = 4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A}$, $n = N/L$ turns per unit length, $I$ = electric current)*
        """,
        "phet": "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"
    },
    "huygens": {
        "title": "🌊 Huygens' Principle & Wavefronts (Class 12 CBSE)",
        "content": """
**NCERT Definition:** A **wavefront** is defined as the locus of all points in a medium vibrating in the exact same phase.

**Core Postulates of Huygens' Principle:**
1. Every point on a given primary wavefront acts as a fresh source of new disturbance, emitting secondary wavelets.
2. Secondary wavelets spread out in all directions with the speed of light in that specific medium.
3. The new wavefront at any later time is formed by taking the forward envelope (common tangential surface) touching all these secondary wavelets.

**Types of Wavefronts:**
* **Spherical:** Emitted by a point source at a finite distance.
* **Cylindrical:** Emitted by a line source (narrow slit).
* **Plane:** Formed when a source is located at infinity (e.g., sunlight entering Earth).
        """,
        "phet": "https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_all.html"
    },
    "kirchhoff": {
        "title": "⚡ Kirchhoff's Circuit Rules (Class 12 CBSE)",
        "content": """
**1. Kirchhoff's First Rule / Junction Rule (KCL):**
* **Statement:** The algebraic sum of currents meeting at any electric junction in a closed circuit is zero ($\sum I = 0$).
* **Conservation Law:** Based strictly on the **Law of Conservation of Electric Charge**.

**2. Kirchhoff's Second Rule / Loop Rule (KVL):**
* **Statement:** The algebraic sum of potential differences (emfs and $IR$ products) around any closed loop is zero ($\sum \\Delta V = 0$).
* **Conservation Law:** Based strictly on the **Law of Conservation of Energy**.
        """,
        "phet": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_all.html"
    }
}

# 4. Chat Session History Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "type": "text", "text": "👋 Hi! I am **Learnova**. Ask me questions about **Solenoid**, **Huygens Principle**, or **Kirchhoff Laws** to get CBSE theory answers along with 3D PhET interactive simulations!"}
    ]

# Render past chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.markdown(message["text"])
        elif message["type"] == "phet":
            st.components.v1.iframe(message["url"], height=420)

# 5. Handle User Chat Input
user_input = st.chat_input("Ask Learnova (e.g., 'What is Solenoid?')")

if user_input:
    # Display user input
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "type": "text", "text": user_input})
    
    query = user_input.lower()
    matched_topic = None
    
    # Check matching topic
    if "solenoid" in query or "magnetic field" in query:
        matched_topic = KNOWLEDGE_BASE["solenoid"]
    elif "huygens" in query or "wavefront" in query or "wave optics" in query:
        matched_topic = KNOWLEDGE_BASE["huygens"]
    elif "kirchhoff" in query or "kcl" in query or "kvl" in query or "junction" in query or "loop rule" in query:
        matched_topic = KNOWLEDGE_BASE["kirchhoff"]

    with st.chat_message("assistant"):
        if matched_topic:
            # Output text theory response
            response_text = f"### {matched_topic['title']}\n\n{matched_topic['content']}"
            st.markdown(response_text)
            st.session_state.chat_history.append({"role": "assistant", "type": "text", "text": response_text})
            
            # Output PhET 3D Embed directly inside chat
            st.write("🎮 **Interactive 3D Simulation:**")
            st.components.v1.iframe(matched_topic["phet"], height=420)
            st.session_state.chat_history.append({"role": "assistant", "type": "phet", "url": matched_topic["phet"]})
        else:
            fallback = "I focus on Class 12 CBSE Physics topics! Try asking me about **Solenoid**, **Huygens Wavefronts**, or **Kirchhoff Circuit Rules**."
            st.markdown(fallback)
            st.session_state.chat_history.append({"role": "assistant", "type": "text", "text": fallback})
