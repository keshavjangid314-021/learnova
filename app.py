import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Learnova | CBSE Class 12 Science AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Styling & Cleanup
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

/* Crop PhET External Links at the bottom */
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

# 5. Main UI Title
st.title("⚡ Learnova Science AI Tutor")
st.caption("CBSE Class 11 & 12 Interactive Science Assistant with Virtual 3D Labs")

# 6. Welcome Banner
if len(st.session_state.messages) == 0:
    st.info("""
    👋 **Welcome to Learnova Science AI!** You can ask questions and explore interactive 3D simulations on the following topics:

    * **Physics Topics:**
      * 🧲 **Solenoid & Electromagnetism** (*"What is solenoid?"* / *"How does solenoid work?"*)
      * ⚡ **Electromagnetic Induction** (*"Explain Electromagnetic Induction"* / *"Faraday's Law"*)
      * 🔋 **Circuit Construction** (*"Explain Electric Circuit"* / *"Ohm's Law & Circuits"*)
      * ⚡ **Kirchhoff's Laws** (*"Explain Kirchhoff's Laws"* / *"KCL and KVL"*)
      * ⚛️ **Charges and Fields** (*"What is Coulomb's Law?"* / *"Electric Charges and Fields"*)
      * 🌊 **Huygens' Principle**

    * **Chemistry Topics:**
      * 🧪 **pH Scale, Acids & Bases** (*"What is pH scale?"* / *"Explain Acid and Base"*)
      * 💎 **Molecule Shapes & VSEPR** (*"What are molecule shapes?"* / *"VSEPR Theory"*)
    """)

# 7. Render Active Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# 8. Smart Intent-Based Response Generator
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
### ⚙️ How a Solenoid Works (Working Mechanism)

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
   * **Statement:** The algebraic sum of all potential differences (EMFs and voltage drops across resistors) in any closed loop of a circuit is zero.
   * **Formula:** $$\\sum V = 0 \\quad \\text{or} \\quad \\sum \\mathcal{E} = \\sum I R$$
   * **Law:** Based on the **Law of Conservation of Energy**.

---
### 🔬 Interactive Circuit Construction Lab (Test KCL & KVL)
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
  *(The negative sign represents **Lenz's Law**, which states that induced current opposes the change in flux causing it).*

---
### 🔬 Interactive 3D Lab: Electromagnetic Induction
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"></iframe>
</div>
"""

    # --- Circuit Construction Kit ---
    elif "circuit" in text or "ohm" in text or "resistor" in text:
        return """
### 🔋 Circuit Construction & Electrical Laws

* **Ohm's Law:** $V = I R$ (Potential difference is directly proportional to current).
* **Series Circuit:** Total resistance $R_{eq} = R_1 + R_2 + R_3$. Current remains same across all components.
* **Parallel Circuit:** Total resistance $\\frac{1}{R_{eq}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}$. Voltage remains same across branches.

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

* **Coulomb's Law:** The electrostatic force between two point charges is given by:
  $$F = k \\frac{|q_1 q_2|}{r^2}$$
* **Electric Field ($E$):** Force per unit charge ($E = \\frac{F}{q}$). Field lines originate from positive charges and terminate at negative charges.

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

* **pH Scale Definition:** A logarithmic scale used to measure the hydrogen ion concentration $[H^+]$ of a solution:
  $$\\text{pH} = -\\log_{10}[H^+]$$
* **Values:**
  * **pH < 7:** Acidic
  * **pH = 7:** Neutral
  * **pH > 7:** Basic / Alkaline

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

    # --- Fallback ---
    else:
        return f"""
I received your query: **"{prompt}"**

Try asking:
* *"What is a solenoid?"* or *"How does a solenoid work?"*
* *"Explain Kirchhoff's Laws"*
* *"Explain Electromagnetic Induction"*
* *"What is pH scale?"*
* *"Explain Molecule Shapes VSEPR Theory"*
"""

# 9. User Input Handling
if user_prompt := st.chat_input("Ask Learnova Science AI..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    response = generate_response(user_prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True)
