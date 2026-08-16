import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Learnova | CBSE Class 12 Physics AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. UI Security & Dark/Light Mode Contrast Fix
st.markdown("""
<style>
    /* Security: Hide Edit/Deploy Toolbar & Main Menu from Users */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none;}
    div[data-testid="stToolbar"] {visibility: hidden !important;}

    /* Adaptive High Contrast Theme Fix */
    .stApp {
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    
    .stChatMessage {
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
        border: 1px solid rgba(128, 128, 128, 0.3);
    }

    /* Force text visibility across both Dark & Light system themes */
    p, h1, h2, h3, h4, span, div {
        color: var(--text-color);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.title("⚡ Learnova AI")
    st.subheader("Class 12 CBSE Physics Tutor")
    st.markdown("---")
    st.markdown("### 🎓 Supported Topics")
    st.write("1. 🧲 **Solenoid & Electromagnetism**")
    st.write("2. 🌊 **Huygens Wave Optics**")
    st.write("3. ⚡ **Kirchhoff's Circuit Laws**")
    st.markdown("---")
    st.info("💡 **Tip:** Ask questions in any way (e.g., 'how solenoid works', 'formula of kirchhoff', 'wavefront definition').")

# 4. App Header
st.title("⚡ Learnova Physics AI Tutor")
st.caption("CBSE Class 12 Physics Assistant with Live Interactive 3D Virtual Labs")

# 5. Formula Cheat-Sheet
with st.expander("📌 Quick Formula Cheat-Sheet & Key Concepts", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Solenoid Magnetic Field:** $B = \\mu_0 n I$")
        st.markdown("**Wavefront Speed:** $v = f \\lambda$")
    with col2:
        st.markdown("**Kirchhoff Junction Rule (KCL):** $\\sum I = 0$ *(Charge Conservation)*")
        st.markdown("**Kirchhoff Loop Rule (KVL):** $\\sum \\Delta V = 0$ *(Energy Conservation)*")

# 6. Knowledge Base with Flexible Query Keywords & Exact Simulations
KNOWLEDGE_BASE = {
    "solenoid": {
        "keywords": ["solenoid", "electromagnet", "coil field", "magnetic field of coil", "how solenoid work", "use of solenoid", "formula of solenoid"],
        "title": "🧲 Solenoid & Magnetic Field (Class 12 CBSE)",
        "content": """
**NCERT Definition:** A solenoid is a long helical coil of insulated copper wire wound tightly in the shape of a cylinder.

**Working & Core Concepts:**
- When an electric current passes through the coil, it generates a uniform magnetic field along its axis.
- **Inside Field:** Strong, uniform, and parallel magnetic field lines.
- **Outside Field:** Extremely weak/negligible field.
- **Behavior:** Acts as a cylindrical **Bar Magnet** with distinct North and South magnetic poles.

**Formula:**
$$B = \\mu_0 n I$$
*(where $\\mu_0 = 4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A}$, $n = N/L$ turns per unit length, $I$ is current)*
        """,
        "phet": "https://phet.colorado.edu/sims/html/magnets-and-electromagnets/latest/magnets-and-electromagnets_all.html"
    },
    "huygens": {
        "keywords": ["huygens", "wavefront", "wave optics", "secondary wavelet", "reflection wave", "refraction wave"],
        "title": "🌊 Huygens' Wave Principle & Wavefronts (Class 12 CBSE)",
        "content": """
**NCERT Definition:** A **wavefront** is defined as the locus of all points vibrating in the same phase.

**Core Postulates:**
1. Every point on a primary wavefront acts as a fresh source of secondary wavelets.
2. These wavelets spread out in all directions with the speed of light in that medium.
3. The new wavefront is the forward envelope touching these secondary wavelets.
        """,
        "phet": "https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_all.html"
    },
    "kirchhoff": {
        "keywords": ["kirchhoff", "kcl", "kvl", "junction rule", "loop rule", "circuit rule", "current law", "voltage law"],
        "title": "⚡ Kirchhoff's Circuit Rules (Class 12 CBSE)",
        "content": """
**1. Junction Rule (KCL):** The algebraic sum of currents meeting at any junction in a closed circuit is zero ($\\sum I = 0$). Based on **Conservation of Charge**.

**2. Loop Rule (KVL):** The algebraic sum of changes in potential around any closed circuit loop is zero ($\\sum \\Delta V = 0$). Based on **Conservation of Energy**.
        """,
        "phet": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_all.html"
    }
}

# 7. Chat History Logic
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "type": "text", "text": "👋 Welcome to **Learnova**! Ask me any question on **Solenoid**, **Huygens Principle**, or **Kirchhoff's Laws** in your own words to get CBSE notes and live 3D PhET simulations."}
    ]

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        if msg["type"] == "text":
            st.markdown(msg["text"])
        elif msg["type"] == "phet":
            st.components.v1.iframe(msg["url"], height=450)

# 8. Flexible Input Processing
user_input = st.chat_input("Ask Learnova AI (e.g., 'How does a solenoid work?')")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "type": "text", "text": user_input})
    
    query = user_input.lower()
    matched = None
    
    # Keyword-based flexible matching
    for key, data in KNOWLEDGE_BASE.items():
        if any(kw in query for kw in data["keywords"]):
            matched = data
            break

    with st.chat_message("assistant"):
        if matched:
            response = f"### {matched['title']}\n\n{matched['content']}"
            st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "type": "text", "text": response})
            
            st.markdown("🎮 **Interactive 3D Physics Simulation:**")
            st.components.v1.iframe(matched["phet"], height=450)
            st.session_state.chat_history.append({"role": "assistant", "type": "phet", "url": matched["phet"]})
        else:
            fallback = "I am trained on CBSE Class 12 Physics core topics. Please ask about **Solenoid / Electromagnets**, **Huygens Principle / Wavefronts**, or **Kirchhoff's Circuit Laws**!"
            st.markdown(fallback)
            st.session_state.chat_history.append({"role": "assistant", "type": "text", "text": fallback})
