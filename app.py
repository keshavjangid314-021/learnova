import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Learnova | CBSE Class 12 Physics AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Styling & Elements Cleanup (Hides Crown, Blue Icons, and External Links)
st.markdown("""
<style>
/* Security & Cleanup: Hide Streamlit Default UI & External Badges */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hide Floating Red/Pink Crown Badge & Accessibility Icons */
div[class*="viewerBadge"], 
div[class*="styles_viewerBadge"],
button[title*="Streamlit Community Cloud"],
.stAppViewerBadge,
iframe[src*="accessibility"],
div[aria-label="Streamlit status"] {
    display: none !important;
    visibility: hidden !important;
}

/* Container for Simulation to Hide Bottom Links */
.sim-container {
    position: relative;
    width: 100%;
    height: 500px;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

.sim-container iframe {
    width: 100%;
    height: 540px; /* Slight overflow to crop external bottom links */
    border: none;
    margin-top: -5px;
}

/* Chat Styling Adjustments */
.stChatMessage {
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# 3. Main Header
st.title("⚡ Learnova Physics AI Tutor")
st.caption("CBSE Class 12 Physics Assistant with Live Interactive 3D Virtual Labs")

# 4. Expandable Cheat-Sheet & Topics List
with st.expander("📌 Quick Formula Cheat-Sheet & Key Topics"):
    st.markdown("""
    * **Electromagnetism:** Solenoid ($B = \mu_0 n I$), Toroid, Ampere's Circuital Law
    * **Wave Optics:** Huygens Principle, Young's Double Slit Experiment ($y = \frac{n\lambda D}{d}$)
    * **Current Electricity:** Kirchhoff's Current & Voltage Laws ($\sum I = 0$, $\sum V = 0$)
    """)

# 5. Welcome Banner
st.info("🤖 **Welcome to Learnova!** Ask me specific questions like *'What is a solenoid?'*, *'How does a solenoid work?'*, *'Explain Huygens Principle'*, or *'Kirchhoff's Laws'*. ")

# 6. Chat History Management
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# 7. Response Logic Function
def generate_response(prompt):
    text = prompt.lower().strip()
    
    # --- TOPIC: SOLENOID (Definition / Basic Info) ---
    if "what is solenoid" in text or "define solenoid" in text or "solenoid definition" in text:
        return """
### 🧲 What is a Solenoid?

A **solenoid** is a long helical coil of insulated copper wire wound tightly around a cylindrical core. When an electric current passes through it, it produces a uniform magnetic field inside its core, behaving similarly to a bar magnet.

* **Magnetic Field Inside:** $B = \mu_0 n I$
  * $\mu_0$ = Permeability of free space ($4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$)
  * $n$ = Number of turns per unit length ($n = N/L$)
  * $I$ = Current flowing through the wire
* **Properties:**
  * Field inside is **strong, uniform, and parallel** to the axis.
  * Field outside the solenoid is very weak and considered **zero**.
"""

    # --- TOPIC: SOLENOID (Working Mechanism) ---
    elif "how it works" in text or "how solenoid works" in text or "working of solenoid" in text or "working mechanism" in text:
        return """
### ⚙️ How a Solenoid Works (Working Mechanism)

1. **Current Flow & Magnetic Field Generation:** 
   When direct current (DC) flows through each circular loop of the helical coil, it creates a magnetic field around each loop (Right-Hand Thumb Rule).

2. **Vector Addition of Fields:** 
   The magnetic fields of individual circular turns combine along the central line of the cylinder to create a strong, straight, uniform magnetic field inside the coil.

3. **Polarity Formation:** 
   * The end where current flows **clockwise** acts as the **South Pole**.
   * The end where current flows **anti-clockwise** acts as the **North Pole**.

---
### 🔬 Interactive 3D Solenoid & Electromagnet Simulation
Adjust current and turns in the simulation below to observe magnetic field vectors in real time:

<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"></iframe>
</div>
"""

    # --- TOPIC: HUYGENS PRINCIPLE ---
    elif "huygen" in text or "wavefront" in text:
        return """
### 🌊 Huygens' Principle of Wavefronts

1. **Primary Wavefront:** Every point on a given primary wavefront acts as a fresh source of secondary disturbance, sending out spherical wavelets.
2. **Speed of Wavelets:** These secondary wavelets spread out in all directions with the speed of light in that medium.
3. **Secondary Wavefront:** The forward envelope or tangential surface touching these secondary wavelets gives the new position of the wavefront at a later time $t$.

> **CBSE Tip:** Use Huygens' principle to prove the **Law of Reflection** ($\theta_i = \theta_r$) and **Law of Refraction** ($\frac{\sin i}{\sin r} = \frac{v_1}{v_2}$).
"""

    # --- TOPIC: KIRCHHOFF'S LAWS ---
    elif "kirchhoff" in text or "kvl" in text or "kcl" in text:
        return """
### ⚡ Kirchhoff's Circuit Laws

1. **Kirchhoff's Current Law (KCL / Junction Rule):** 
   The algebraic sum of all electric currents entering and leaving any junction in an electrical circuit is equal to zero.
   $$\sum I = 0$$
   *(Based on the Law of Conservation of Charge)*

2. **Kirchhoff's Voltage Law (KVL / Loop Rule):** 
   The algebraic sum of all potential differences (EMF and voltage drops) around any closed loop in a circuit is zero.
   $$\sum V = 0$$
   *(Based on the Law of Conservation of Energy)*
"""

    # --- FALLBACK RESPONSE ---
    else:
        return f"""
I received your query: **"{prompt}"**

Currently, I am specialized in CBSE Class 12 Physics core concepts. Try asking:
* *"What is a solenoid?"*
* *"How does a solenoid work?"*
* *"Explain Huygens Principle"*
* *"State Kirchhoff's Laws"*
"""

# 8. User Input & Processing
if user_prompt := st.chat_input("Ask Learnova AI (e.g., 'What is solenoid?' or 'How it works?')"):
    # Display User Message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate & Display Assistant Response
    response_content = generate_response(user_prompt)
    st.session_state.messages.append({"role": "assistant", "content": response_content})
    with st.chat_message("assistant"):
        st.markdown(response_content, unsafe_allow_html=True)
