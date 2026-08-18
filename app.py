import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ChitraVidya | CBSE Science & Maths AI Visualizer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Styling & Cleanup
st.markdown("""
<style>
/* Hide Default Streamlit Elements */
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

/* Modern Streamlit Chat Styling */
.stChatMessage {
    border-radius: 12px;
    padding: 12px 16px;
    margin-bottom: 10px;
}

/* Crop & Frame for 3D Simulators */
.sim-container {
    position: relative;
    width: 100%;
    height: 520px;
    overflow: hidden;
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.1);
    margin-top: 15px;
}

.sim-container iframe {
    width: 100%;
    height: 570px;
    border: none;
    margin-top: -5px;
}
</style>
""", unsafe_allow_html=True)

# Custom Avatars (AI & User Icons)
AI_AVATAR = "https://api.iconify.design/lucide:sparkles.svg?color=%2310a37f"
USER_AVATAR = "https://api.iconify.design/lucide:user.svg?color=%236b7280"

# 3. Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Sidebar Setup
with st.sidebar:
    st.markdown("### 💬 Chat History")
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.caption(f"📌 {msg['content'][:25]}...")

# 5. Main Title Section
st.title("✨ ChitraVidya AI")
st.caption("3D Interactive Science & Maths Learning Assistant for CBSE Class 12")

# 6. Welcome Banner with PCM Sample Questions
if len(st.session_state.messages) == 0:
    st.info("""
    👋 **Welcome to ChitraVidya AI!** Ask questions or explore 3D visual models across PCM topics:

    * **⚡ Physics:**
      * 🧲 **Solenoid & Electromagnetism:** *"What is solenoid?"* | *"How does a solenoid work?"*
      * ⚡ **Electromagnetic Induction:** *"Explain Electromagnetic Induction"* | *"State Faraday's Law"*
      * 🔋 **Circuit Construction:** *"Explain Electric Circuit"* | *"What is Ohm's Law?"*
      * ⚡ **Kirchhoff's Laws:** *"Explain Kirchhoff's Laws"* | *"What is KCL and KVL?"*
      * ⚛️ **Charges and Fields:** *"What is Coulomb's Law?"* | *"Explain Electric Field Lines"*
      * 🌊 **Wave Optics:** *"Explain Huygens' Principle"*
      * 📡 **EM Waves (Class 12):** *"Explain EM Waves"* | *"What is displacement current?"* | *"Show Maxwell's Equations"*

    * **🧪 Chemistry:**
      * 🧪 **pH Scale, Acids & Bases:** *"What is pH scale?"* | *"Explain Acid and Base strength"*
      * 💎 **Molecule Shapes & VSEPR:** *"What are molecule shapes?"* | *"Explain VSEPR Theory"*

    * **📐 Mathematics:**
      * 📐 **3D Geometry & Vectors (Class 12 CBSE):** *"Explain 3D Geometry"* | *"Show Vector Cross Product"* | *"Find shortest distance between skew lines"*
    """)

# 7. Render Chat History with Custom Avatars
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else AI_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"], unsafe_allow_html=True)

# 8. Smart Intent Response Generator
def generate_response(prompt):
    text = prompt.lower().strip()
    
    # --- Solenoid ---
    if "solenoid" in text:
        if "what" in text or "define" in text or "definition" in text:
            return """
### 🧲 What is a Solenoid?

A **solenoid** is a long helical coil of insulated copper wire wound tightly around a cylindrical frame. When current flows through it, it produces a uniform magnetic field inside its core, behaving like a bar magnet.

* **Formula:** $B = \\mu_0 n I$
  * $\\mu_0$ = Permeability of free space ($4\\pi \\times 10^{-7} \\text{ T}\\cdot\\text{m/A}$)
  * $n$ = Turns per unit length ($N/L$)
  * $I$ = Current in Amperes
* **Key Feature:** Magnetic field inside is **strong and uniform**, while outside it is nearly **zero**.
"""
        else:
            return """
### ⚙️ How a Solenoid Works

1. **Magnetic Field Generation:** Direct current (DC) flowing through each loop generates a magnetic field around the wire via the Right-Hand Thumb Rule.
2. **Field Alignment:** Individual circular fields sum up along the central axis of the cylinder to form a strong, directional magnetic field line.
3. **Polarity:** Clockwise current side = **South Pole** | Anti-clockwise current side = **North Pole**

---
### 🔬 Interactive 3D Magnets & Electromagnet Simulation
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/magnets-and-electromagnets/latest/magnets-and-electromagnets_all.html"></iframe>
</div>
"""

    # --- Kirchhoff's Laws ---
    elif "kirchhoff" in text or "kcl" in text or "kvl" in text or "junction rule" in text or "loop rule" in text:
        return """
### ⚡ Kirchhoff's Circuit Laws

Kirchhoff's laws are fundamental rules used to analyze complex electrical circuits:

1. **Kirchhoff's Current Law (KCL / Junction Rule):**
   * **Statement:** The algebraic sum of all electric currents meeting at any junction in an electrical circuit is zero.
   * **Formula:** $$\\sum I = 0$$
   * **Law:** Based on the **Law of Conservation of Charge**.

2. **Kirchhoff's Voltage Law (KVL / Loop Rule):**
   * **Statement:** The algebraic sum of all potential differences in any closed loop is zero.
   * **Formula:** $$\\sum V = 0 \\quad \\text{or} \\quad \\sum \\mathcal{E} = \\sum I R$$
   * **Law:** Based on the **Law of Conservation of Energy**.

---
### 🔬 Interactive Circuit Construction Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_all.html"></iframe>
</div>
"""

    # --- Electromagnetic Induction ---
    elif "induction" in text or "faraday" in text or "emi" in text:
        return """
### ⚡ Electromagnetic Induction (Faraday's Law)

**Electromagnetic Induction** is the process of generating an electromotive force (EMF) or current in a conductor by changing the magnetic flux linked with the circuit.

* **Faraday's Law Formula:** 
  $$\\mathcal{E} = -N \\frac{d\\Phi_B}{dt}$$
  *(The negative sign represents **Lenz's Law**).*

---
### 🔬 Interactive 3D Faraday's Law Simulation
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"></iframe>
</div>
"""

    # --- Circuit Construction Kit ---
    elif "circuit" in text or "ohm" in text or "resistor" in text:
        return """
### 🔋 Circuit Construction & Electrical Laws

* **Ohm's Law:** $V = I R$
* **Series Circuit:** Total resistance $R_{eq} = R_1 + R_2 + R_3$.
* **Parallel Circuit:** Total resistance $\\frac{1}{R_{eq}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}$.

---
### 🔬 Interactive Virtual Circuit Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_all.html"></iframe>
</div>
"""

    # --- Charges and Fields ---
    elif "charge" in text or "coulomb" in text or "electric field" in text:
        return """
### ⚛️ Electric Charges and Fields

* **Coulomb's Law:** Electrostatic force between two point charges:
  $$F = k \\frac{|q_1 q_2|}{r^2}$$
* **Electric Field ($E$):** Force per unit charge ($E = \\frac{F}{q}$).

---
### 🔬 Interactive Charges & Field Simulation
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_all.html"></iframe>
</div>
"""

    # --- Huygens Principle ---
    elif "huygen" in text or "wavefront" in text:
        return """
### 🌊 Huygens' Principle
Every point on a primary wavefront acts as a fresh source of secondary wavelets, spreading out in all directions with the speed of light in that medium.
"""

    # --- pH Scale, Acid & Base ---
    elif "ph" in text or "acid" in text or "base" in text:
        return """
### 🧪 pH Scale, Acids & Bases

* **pH Scale Definition:** Measure of hydrogen ion concentration $[H^+]$:
  $$\\text{pH} = -\\log_{10}[H^+]$$
* **Values:**
  * **pH < 7:** Acidic | **pH = 7:** Neutral | **pH > 7:** Basic

---
### 🔬 Interactive pH Scale Virtual Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_all.html"></iframe>
</div>
"""

    # --- Molecule Shapes & VSEPR ---
    elif "molecule" in text or "vsepr" in text or "shape" in text or "geometry" in text:
        return """
### 💎 Molecule Shapes & VSEPR Theory

**VSEPR Theory** predicts 3D molecular geometry based on electron pair repulsion:
* **Linear:** $180^\\circ$ (e.g., $\\text{CO}_2$)
* **Trigonal Planar:** $120^\\circ$ (e.g., $\\text{BF}_3$)
* **Tetrahedral:** $109.5^\\circ$ (e.g., $\\text{CH}_4$)

---
### 🔬 Interactive 3D Molecule Shapes Simulator
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/molecule-shapes/latest/molecule-shapes_all.html"></iframe>
</div>
"""

    # --- EM Waves (Physics Class 12) ---
    elif "em wave" in text or "electromagnetic wave" in text or "spectrum" in text or "displacement current" in text or "maxwell" in text:
        return """
### 📡 Physics Class 12: Electromagnetic Waves (3D Visualizer)

Electromagnetic waves consist of sinusoidal oscillating electric ($\vec{E}$) and magnetic ($\vec{B}$) fields perpendicular to each other and to wave propagation direction.

#### 📌 Topic Index & Sample Questions Guide:
* **Topic 1: Transverse Nature of EM Waves**
  * *Sawal Kaise Puchein:* *"Show phase difference between $\vec{E}$ and $\vec{B}$ vectors."*
* **Topic 2: Displacement Current ($I_d$) & Maxwell's Equations**
  * *Sawal Kaise Puchein:* *"Explain displacement current during capacitor charging."*
* **Topic 3: Electromagnetic Spectrum**
  * *Sawal Kaise Puchein:* *"Compare frequency of Microwaves vs X-rays."*

---
### 🔬 Interactive 3D Wave Interference Simulation
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_en.html"></iframe>
</div>
"""

    # --- Mathematics Class 12 CBSE (3D & Vectors) ---
    elif "math" in text or "3d" in text or "vector" in text or "skew line" in text or "plane" in text or "integral" in text:
        return """
### 📐 Mathematics Class 12 CBSE: 3D Geometry & Vector Visualizer

Visualize vectors, 3D line equations, planes, and solids interactively.

#### 📌 Topic Index & Sample Questions Guide:
* **Topic 1: 3D Geometry (Lines & Planes)**
  * *Sawal Kaise Puchein:* *"Show shortest distance vector between skew lines in 3D."*
* **Topic 2: Vectors & Cross Product Direction**
  * *Sawal Kaise Puchein:* *"Demonstrate dot product projection of vector $\\vec{A}$ on $\\vec{B}$."*
* **Topic 3: Application of Integrals (3D Solids)**
  * *Sawal Kaise Puchein:* *"Rotate curve $y = \\sqrt{x}$ about X-axis to form a 3D paraboloid."*

---
### 🔬 Interactive 3D Math Canvas (GeoGebra 3D Engine)
<div class="sim-container">
    <iframe src="https://www.geogebra.org/3d?embed"></iframe>
</div>
"""

    # --- Fallback ---
    else:
        return f"""
I received your query: **"{prompt}"**

Try asking:
* *"What is a solenoid?"*
* *"Explain Kirchhoff's Laws"*
* *"Explain EM Waves Class 12"*
* *"Show 3D Geometry and Vectors"*
"""

# 9. User Input Handling
if user_prompt := st.chat_input("Ask ChitraVidya AI..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(user_prompt)

    response = generate_response(user_prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar=AI_AVATAR):
        st.markdown(response, unsafe_allow_html=True)
