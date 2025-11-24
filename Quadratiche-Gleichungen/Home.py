import streamlit as st

# Seitenkonfiguration
st.set_page_config(
    page_title="Quadratische Gleichungen",
    page_icon="⚖️",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("Quadratische Gleichungen")
    st.markdown("---")

# Titel und Einleitung
st.title("Quadratische Gleichungen")
st.markdown("---")

# Einführung
st.header("Kick-off")

st.markdown("""
Quadratische Gleichungen begegnen dir viel öfter, als du denkst: Beim Werfen eines Balls, bei Brückenbögen oder beim Berechnen von Flächen. Immer dann, wenn etwas „parabelförmig“ verläuft, steckt im Hintergrund eine quadratische Funktion – und oft führt eine Fragestellung dann zu einer quadratischen Gleichung.
            """)


# Beispiele in zwei Spalten
st.subheader("Beispiele")

col1, col2 = st.columns(2)

with col1:
    st.write("**Quadratische Gleichungen:**")
    st.latex(r"x^2 - 5x + 6 = 0")
    st.latex(r"2x^2 + 3x - 2 = 5")
    st.latex(r"x^2 - 9 = 34")
    st.latex(r"x^2 - 4x + 1 = 3x - 2")
    st.latex(r"x^2 + x + 1 = -x^2 + 5x - 3")


with col2:
    st.write("**Keine quadratischen Gleichungen:**")
    st.latex(r"3x + 5 = 0 \quad \text{(linear)}")
    st.latex(r"x^3 - 2x + 1 = 0 \quad \text{(kubisch)}")
    st.latex(r"\sin(2x)=6")
    st.latex(r"x^2 \cdot \ln(3x-1)=e^{3}")



st.markdown("---")

# Übersicht der Themen
st.header("Themenübersicht")

st.write("""
In dieser App lernst du verschiedene Methoden zum Lösen quadratischer Gleichungen kennen. 
Wähle ein Thema in der **Seitenleiste** aus:
""")

# Themen-Karten
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Grafisches Lösen")
    st.write("""
    - Visualisierung von Parabeln
    - Ablesen von Argumenten
    - Ablesen der Nullstellen
    - Anzahl der Lösungen erkennen (0, 1 oder 2)
    """)
    
    st.subheader("2. Wurzelziehen")
    st.write("""
    - Für Gleichungen der Form: x² = k
    - Einfachste Methode für spezielle Fälle
    """)
    
    st.subheader("3. Satz vom Nullprodukt")
    st.write("""
    - Faktorisierte Form nutzen
    - Wenn a·b = 0, dann a = 0 oder b = 0
    """)

with col2:
    st.subheader("4. abc- und pq-Formel")
    st.write("""
    - Universelle Lösungsformeln
    - Diskriminante: Anzahl der Lösungen bestimmen
    - Die wichtigsten Werkzeuge!
    """)
    
    st.subheader("5. Satz von Vieta")
    st.write("""
    - Zusammenhang zwischen Lösungen und Koeffizienten
    - Schnelles Überprüfen von Lösungen
    """)
    
    st.subheader("6. Quadratische Ungleichungen")
    st.write("""
    - Lösen von ax² + bx + c > 0 (oder <, ≤, ≥)
    - Lösungsmengen bestimmen
    """)

st.markdown("---")

# Footer
st.subheader("🚀 Bereit anzufangen?")
st.write("Wähle ein Thema aus der Seitenleiste und starte deine Lernreise!")