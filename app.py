import streamlit as st
import streamlit.components.v1 as components

# Streamlit Page Config & Title Update
st.set_page_config(page_title="ChitraVidya AI - 3D Interactive Tutor", layout="wide")

st.title("🎨 ChitraVidya AI — 3D Interactive Science & Maths Tutor")
st.caption("Visual, Interactive & Real-time 3D Simulations for CBSE Class 11 & 12")

# Sidebar Menu (Purane Topics + Naye Topics)
selected_topic = st.sidebar.selectbox(
    "Choose Chapter / Module",
    [
        "Physics: Solenoid & Electromagnetism",
        "Physics: Faraday's Law of Induction",
        "Physics: Kirchhoff's Laws (KCL & KVL)",
        "Physics: Electromagnetic Waves (Class 12)",
        "Chemistry: pH Scale & Solutions",
        "Chemistry: VSEPR Theory & Molecular Geometry",
        "Maths: 3D Geometry & Vectors (Class 12 CBSE)"
    ]
)

# ====================================================================
# 1. PURANI SAVED TOPICS (SAVED AS IT IS)
# ====================================================================

if selected_topic == "Physics: Solenoid & Electromagnetism":
    st.header("🧲 Physics: Solenoid & Magnetic Field")
    st.write("Solenoid ke 3D magnetic field pattern aur current flow ko interactive feel karein.")
    components.html(
        '<iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html" width="100%" height="600" allowfullscreen style="border:none; border-radius:10px;"></iframe>',
        height=620
    )

elif selected_topic == "Physics: Faraday's Law of Induction":
    st.header("⚡ Physics: Faraday's Law of Electromagnetic Induction")
    st.write("Magnet movement aur induced emf/current ko live experiment karke dekhein.")
    components.html(
        '<iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html" width="100%" height="600" allowfullscreen style="border:none; border-radius:10px;"></iframe>',
        height=620
    )

elif selected_topic == "Physics: Kirchhoff's Laws (KCL & KVL)":
    st.header("🔌 Physics: Kirchhoff's Current & Voltage Laws")
    st.write("DC Circuit Virtual Lab: Resistors, Battery, aur Wires laga kar KCL aur KVL verify karein.")
    components.html(
        '<iframe src="https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html" width="100%" height="600" allowfullscreen style="border:none; border-radius:10px;"></iframe>',
        height=620
    )

elif selected_topic == "Chemistry: pH Scale & Solutions":
    st.header("🧪 Chemistry: pH Scale & Solutions")
    st.write("Acids, bases aur neutral liquids ke pH value ko measure aur test karein.")
    components.html(
        '<iframe src="https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_en.html" width="100%" height="600" allowfullscreen style="border:none; border-radius:10px;"></iframe>',
        height=620
    )

elif selected_topic == "Chemistry: VSEPR Theory & Molecular Geometry":
    st.header("⚛️ Chemistry: VSEPR Theory & Molecular Shapes")
    st.write("Molecules ke 3D bond angles, lone pairs, aur molecular shapes ko rotate karke dekhein.")
    components.html(
        '<iframe src="https://phet.colorado.edu/sims/html/molecule-shapes/latest/molecule-shapes_en.html" width="100%" height="600" allowfullscreen style="border:none; border-radius:10px;"></iframe>',
        height=620
    )

# ====================================================================
# 2. NAYA TOPIC: PHYSICS CLASS 12 - ELECTROMAGNETIC WAVES
# ====================================================================

elif selected_topic == "Physics: Electromagnetic Waves (Class 12)":
    st.header("📡 Class 12 Physics: Electromagnetic Waves")
    
    with st.expander("📌 Topic Index & Sawal Kaise Puchein (Interactive Guide)", expanded=True):
        st.markdown("""
        * **1. Transverse Nature of EM Waves (Electric $\\vec{E}$ & Magnetic $\\vec{B}$ Vectors):**
          * *Simulation:* 3D Oscillating Electric and Magnetic fields perpendicular to each other.
          * *Sawal Kaise Puchein:* *"Show the phase difference and angle between electric and magnetic field vectors in EM waves."*
        * **2. Electromagnetic Spectrum Visualization:**
          * *Simulation:* Interactive band slider showing Radio waves, Microwaves, Infrared, Visible, UV, X-rays & Gamma rays.
          * *Sawal Kaise Puchein:* *"Compare the frequency, wavelength, and energy of Microwaves vs X-rays visually."*
        * **3. Displacement Current & Maxwell's Equations:**
          * *Simulation:* 3D Capacitor charging circuit showing magnetic field lines generated between plates due to $I_d$.
          * *Sawal Kaise Puchein:* *"Demonstrate displacement current density during capacitor charging using Maxwell's 4th equation."*
        """)

    st.subheader("🖥️ Interactive EM Waves 3D Simulation")
    components.html(
        '<iframe src="https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_en.html" width="100%" height="600" allowfullscreen style="border:none; border-radius:10px;"></iframe>',
        height=620
    )

# ====================================================================
# 3. NAYA TOPIC: MATHEMATICS CLASS 12 CBSE (3D & VECTORS)
# ====================================================================

elif selected_topic == "Maths: 3D Geometry & Vectors (Class 12 CBSE)":
    st.header("📐 Class 12 CBSE Maths: 3D Geometry & Visualizer")
    
    with st.expander("📌 Topic Index & Sawal Kaise Puchein (Interactive Guide)", expanded=True):
        st.markdown("""
        * **1. 3D Geometry (Lines, Skew Lines & Planes in Space):**
          * *Simulation:* 3D coordinate space showing shortest distance vector between two skew lines and intersection of planes.
          * *Sawal Kaise Puchein:* *"Show the shortest distance line vector between two skew lines in 3D space."*
        * **2. Vectors & Cross Product Direction:**
          * *Simulation:* Interactive 3D vectors with Right-Hand Thumb Rule for $\\vec{a} \\times \\vec{b}$.
          * *Sawal Kaise Puchein:* *"Demonstrate dot product projection of vector $\\vec{A}$ on $\\vec{B}$ in 3D."*
        * **3. Application of Integrals (3D Solids of Revolution):**
          * *Simulation:* 2D bounded region rotating in 3D space to form a paraboloid/cone solid.
          * *Sawal Kaise Puchein:* *"Rotate curve $y = \\sqrt{x}$ about X-axis to generate a 3D paraboloid solid."*
        * **4. Linear Programming Problem (3D Feasible Region):**
          * *Simulation:* Bounded 3D convex polygon formed by multiple plane constraint equations.
          * *Sawal Kaise Puchein:* *"Highlight the corner points of the feasible region for optimizing objective function Z."*
        """)

    st.subheader("🖥️ Interactive 3D Math & Geometry Canvas")
    components.html(
        '<iframe src="https://www.geogebra.org/3d?embed" width="100%" height="600" allowfullscreen style="border:none; border-radius:10px;"></iframe>',
        height=620
    )
