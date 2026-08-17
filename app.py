import streamlit as st
import streamlit.components.v1 as components

# ... baaki code same rahega ...

# Response Function ke andar Solenoid Working block:
elif "how" in text or "work" in text or "working" in text:
    if "solenoid" in text:
        st.markdown("""
### ⚙️ How a Solenoid Works (Working Principle)

1. **Magnetic Field Generation:** Direct current (DC) flowing through each loop generates a magnetic field around the wire via the Right-Hand Thumb Rule.
2. **Field Alignment:** Individual circular fields sum up along the central axis of the cylinder to form a strong, directional magnetic field line.
3. **Polarity:** 
   * Clockwise current side = **South Pole**
   * Anti-clockwise current side = **North Pole**

---
### 🔬 Interactive 3D Simulation
""")
        # Stable Embed Method for PhET
        components.iframe(
            "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html",
            height=500,
            scrolling=False
        )
        return ""
