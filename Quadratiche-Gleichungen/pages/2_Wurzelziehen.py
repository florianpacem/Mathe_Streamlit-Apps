import streamlit as st
import sympy as sp

# Seitenkonfiguration
st.set_page_config(
    page_title="Wurzelziehen",
    page_icon="⚖️",
    layout="wide"
)

st.title("Wurzelziehen - ein Tool zum Lösen quadratischer Gleichungen")
st.markdown("---")

# Einführungsbeispiel
st.header("Anwendungsfälle")

st.markdown(
    """
    Immer dann, wenn quadratische Gleichungen eine der folgenden Formen aufweisen,

    1. Typ 1: $x^2=k$
    2. Typ 2: $(x-d)^2 = k$

    kann man sie mittels "Wurzelziehen" lösen. Leider sehen nicht alle Gleichungen auf den ersten Blick genau so aus, weshalb man sie manchmal etwas umformen muss, um eine diese Formen erkennen zu können.

    Wichtig dabei ist, dass kein zusätzlicher $x$-Term (wie z.B. $+3x$) vorkommen darf.
    """)

st.divider()

st.header("Beispiele")

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("#### Eine Gleichung in der Form $x^2=k$:")
    
    st.markdown("""
                $-x^2+9=0$ → hier sieht man nicht sofort, dass es eine Typ-1 Gleichung ist. Deshalb formen wir sie zunächst um:
                
                $$
                \\begin{align*}
                -x^2+9&=0 \\qquad &&|-9 \\\\
                -x^2&=-9 \\qquad &&|\\cdot (-1)\\\\
                x^2&=9
                \\end{align*}
                $$

                Jetzt erkennt man deutlich, dass es sich um eine Gleichung vom Typ 1 handelt. D.h. wir können diese Gleichung mittels **Wurzelziehen** lösen

                $$
                \\begin{align*}
                x^2&=9 \\qquad &&|\\sqrt{\\phantom{x}}\\\\
                x=-\\sqrt{9} \\quad &\\lor \\quad x=\\sqrt{9}\\\\
                x=-3 \\quad &\\lor \\quad x=3
                \\end{align*}
                $$

                Lösungsmenge: $\mathbb{L}=\{-3,3\}$
                """)
    
with col2:
    st.markdown("#### Eine Gleichung in der Form $(x-d)^2=k$:")
    
    st.markdown("""
                $2(x-4)^2=50$ → hier sieht man nicht sofort, dass es eine Typ-2 Gleichung ist. Deshalb formen wir sie zunächst um:
                
                $$
                \\begin{align*}
                2(x-4)^2&=50 \\qquad &&|: 2 \\\\
                (x-4)^2&=25
                \\end{align*}
                $$

                Jetzt erkennt man deutlich, dass es sich um eine Gleichung vom Typ 2 handelt. D.h. wir können diese Gleichung mittels **Wurzelziehen** lösen

                $$
                \\begin{align*}
                (x-4)^2&=25 \\qquad &&|\\sqrt{\\phantom{x}}\\\\
                x-4=-\\sqrt{25} \\quad &\\lor \\quad x-4=\\sqrt{25}\\\\
                x-4=-5 \\quad &\\lor \\quad x-4=5 \\qquad &&|+4\\\\
                x=-1 \\quad &\\lor \\quad x=9
                \\end{align*}
                $$

                Lösungsmenge: $\mathbb{L}=\{-1,9\}$
                """)

st.divider()

st.header("Übungen: Lösen mittels Wurzelziehen")

st.markdown("#### Löse die folgenden Gleichungen.")

st.write("")

col1, col2 = st.columns([1,1])

with col1:
    # Aufgabe a)
    st.markdown("**a)** $-x^2+5=0$")

    with st.expander("✅ Lösung anzeigen"):
        st.markdown("""
        $$
        \\begin{align*}
        -x^2+5&=0 &&|-5 \\\\
        -x^2&=-5 &&|:(-1) \\\\
        x^2&=5 &&|\\sqrt{\\phantom{x}} \\\\
        x_1&=\\sqrt{5} \\approx 2{,}24 \\\\
        x_2&=-\\sqrt{5} \\approx -2{,}24
        \\end{align*}
        $$
        """)
        st.success("**Lösungsmenge:** $\\mathbb{L} = \\{-\\sqrt{5}; \\sqrt{5}\\}$")

    st.markdown("<br>", unsafe_allow_html=True)

    # Aufgabe b)
    st.markdown("**b)** $3x^2-6=0$")

    with st.expander("✅ Lösung anzeigen"):
        st.markdown("""
        $$
        \\begin{align*}
        3x^2-6&=0 &&|+6 \\\\
        3x^2&=6 &&|:3 \\\\
        x^2&=2 &&|\\sqrt{\\phantom{x}} \\\\
        x_1&=\\sqrt{2} \\approx 1{,}41 \\\\
        x_2&=-\\sqrt{2} \\approx -1{,}41
        \\end{align*}
        $$
        """)
        st.success("**Lösungsmenge:** $\\mathbb{L} = \\{-\\sqrt{2}; \\sqrt{2}\\}$")

    st.markdown("<br>", unsafe_allow_html=True)

    # Aufgabe c)
    st.markdown("**c)** $x^2+1=0$")

    with st.expander("✅ Lösung anzeigen"):
        st.markdown("""
        $$
        \\begin{align*}
        x^2+1&=0 &&|-1 \\\\
        x^2&=-1 &&|\\sqrt{\\phantom{x}}
        \\end{align*}
        $$
        """)
        st.error("**Keine Lösung!** Es gibt keine reelle Zahl, deren Quadrat negativ ist.")
        st.info("**Lösungsmenge:** $\\mathbb{L} = \\{\\}$ (leere Menge)")

    st.markdown("<br>", unsafe_allow_html=True)

with col2:
    # Aufgabe d)
    st.markdown("**d)** $6x^2-27=0$")

    with st.expander("✅ Lösung anzeigen"):
        st.markdown("""
        $$
        \\begin{align*}
        6x^2-27&=0 &&|+27 \\\\
        6x^2&=27 &&|:6 \\\\
        x^2&=4{,}5 &&|\\sqrt{\\phantom{x}} \\\\
        x_1&=\\sqrt{4{,}5} \\approx 2{,}12 \\\\
        x_2&=-\\sqrt{4{,}5} \\approx -2{,}12
        \\end{align*}
        $$
        """)
        st.success("**Lösungsmenge:** $\\mathbb{L} = \\{-\\sqrt{4{,}5}; \\sqrt{4{,}5}\\}$")

    st.markdown("<br>", unsafe_allow_html=True)

    # Aufgabe e)
    st.markdown("**e)** $(x-4)^2=25$")

    with st.expander("✅ Lösung anzeigen"):
        st.markdown("""
        $$
        \\begin{align*}
        (x-4)^2&=25 &&|\\sqrt{\\phantom{x}} \\\\
        x-4&=\\pm 5 &&|+4 \\\\
        \\\\
        x_1&=4+5=9 \\\\
        x_2&=4-5=-1
        \\end{align*}
        $$
        """)
        st.success("**Lösungsmenge:** $\\mathbb{L} = \\{-1; 9\\}$")

    st.markdown("<br>", unsafe_allow_html=True)

    # Aufgabe f)
    st.markdown("**f)** $3(x+1)^2=21$")

    with st.expander("✅ Lösung anzeigen"):
        st.markdown("""
        $$
        \\begin{align*}
        3(x+1)^2&=21 &&|:3 \\\\
        (x+1)^2&=7 &&|\\sqrt{\\phantom{x}} \\\\
        x+1&=\\pm\\sqrt{7} &&|-1 \\\\
        \\\\
        x_1&=-1+\\sqrt{7} \\approx 1{,}65 \\\\
        x_2&=-1-\\sqrt{7} \\approx -3{,}65
        \\end{align*}
        $$
        """)
        st.success("**Lösungsmenge:** $\\mathbb{L} = \\{-1-\\sqrt{7}; -1+\\sqrt{7}\\}$")