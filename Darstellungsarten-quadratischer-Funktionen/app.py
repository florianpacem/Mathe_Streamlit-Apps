import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Seitenkonfiguration
st.set_page_config(
    page_title="Quadratische Funktionen",
    page_icon="📊",
    layout="wide"
)

# Custom CSS für bessere Darstellung
st.markdown("""
<style>
    .stExpander {
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .math-text {
        font-size: 1.1em;
    }
</style>
""", unsafe_allow_html=True)

# Titel
st.title("📐 Quadratische Funktionen - Die drei Darstellungsformen")

# Einführung
st.markdown("""
## Einführung

In diesem interaktiven Tool lernst du die drei verschiedenen Darstellungsformen einer quadratischen Funktion kennen:

1. **Scheitelpunktform**: $f(x)=a\\cdot(x−d)^2+e$
2. **Faktorisierte Form** - auch Nullstellenform genannt: $f(x)=a\\cdot(x−x_1)\\cdot(x−x_2)$
3. **Polynomform** - auch allgemeine Form genannt: $f(x)=ax^2+bx+c$

Jede Form hat ihre eigenen Stärken und zeigt unterschiedliche Eigenschaften der Parabel!

### Am Ende dieses Kapitels solltest du folgendes gelernt haben:

1. Ich kann die drei Darstellungsarten quadratischer Funktionen aufschreiben.
2. Ich kann die Bedeutung der Parameter in jeder Darstellungsform erklären.
3. Ich kann die Eigenschaften einer Parabel aus jeder Darstellungsform ablesen.
4. Ich kann den Scheitelpunkt aus jeder Darstellungsform bestimmen.
""")

st.divider()

# ==================================================
# 1. SCHEITELPUNKTFORM
# ==================================================

st.header("1. Die Scheitelpunktform")
st.latex(r"f(x)=a\cdot(x−d)^2+e")

st.markdown("**Aufgabe:** Verändere die Funktionsgleichung durch Bewegen der Slider. Welches Muster erkennst du in der Funktionsgleichung?")

col1, col2 = st.columns([1, 2])

with col1:
    a_sp = st.slider("Parameter a:", -3.0, 3.0, 1.0, 0.1, key="a_sp")
    d_sp = st.slider("Parameter d:", -5.0, 5.0, 0.0, 0.5, key="d_sp")
    e_sp = st.slider("Parameter e:", -5.0, 5.0, 0.0, 0.5, key="e_sp")

with col2:
    x = np.linspace(-10, 10, 400)
    y = a_sp * (x - d_sp)**2 + e_sp
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-', linewidth=2, label=f'$f(x) = {a_sp}(x-({d_sp}))^2 + ({e_sp})$')
    ax.plot(d_sp, e_sp, 'ro', markersize=10, label=f'Scheitelpunkt S({d_sp}|{e_sp})')
    
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(range(-10, 11, 1))
    ax.set_yticks(range(-10, 11, 1))
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.legend(fontsize=10)
    ax.set_title('Scheitelpunktform', fontsize=14, fontweight='bold')
    
    # Eigenschaften anzeigen
    oeffnung = "nach oben" if a_sp > 0 else "nach unten"
    if abs(a_sp) > 1:
        streckung = "gestreckt"
    elif abs(a_sp) < 1:
        streckung = "gestaucht"
    else:
        streckung = "keine Streckung"
    
    ax.text(0.02, 0.98, f'Öffnung: {oeffnung}\nStreckung: {streckung}', 
            transform=ax.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5), fontsize=10)
    
    st.pyplot(fig)
    plt.close()

with st.expander("✅ Lösung anzeigen: Was kann man aus der Scheitelpunktform direkt ablesen?"):
    st.markdown(r"""
**Lösung:**

- **Scheitelpunkt**: $S(d|e)$
- **Öffnung**:
    - $a>0$ → nach oben
    - $a<0$ → nach unten
- **Streckung**: 
    - $|a|>1$ → gestreckt
    - $|a|<1$ → gestaucht
    """)

st.divider()

# ==================================================
# 2. FAKTORISIERTE FORM (NULLSTELLENFORM)
# ==================================================

st.header("2. Die faktorisierte Form (Nullstellenform)")
st.latex(r"f(x) = a\cdot(x-x_1)\cdot(x-x_2)")

# 2.1 Wiederholung: Nullstellen
st.subheader("2.1 Wiederholung des Begriffs **Nullstelle**")

fig2, ax2 = plt.subplots(figsize=(12, 8))
x = np.linspace(-5, 5, 400)

# Drei Parabeln
y1 = (x + 3) * (x - 2)
y2 = (x - 1)**2
y3 = x**2 - 4*x + 6

ax2.plot(x, y1, 'b-', linewidth=2.5, label='Zwei Nullstellen: $f(x) = (x+3)(x-2)$')
ax2.plot(x, y2, 'g-', linewidth=2.5, label='Eine Nullstelle: $f(x) = (x-1)^2$')
ax2.plot(x, y3, 'r-', linewidth=2.5, label='Keine Nullstellen: $f(x) = x^2 - 4x + 6$')

ax2.plot([-3, 2], [0, 0], 'bo', markersize=10)
ax2.plot(1, 0, 'go', markersize=10)

ax2.axhline(y=0, color='k', linewidth=0.8)
ax2.axvline(x=0, color='k', linewidth=0.8)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-5, 5)
ax2.set_ylim(-7, 10)
ax2.set_xticks(range(-5, 6, 1))
ax2.set_yticks(range(-7, 11, 1))
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('f(x)', fontsize=12)
ax2.legend(fontsize=11, loc='upper left')
ax2.set_title('Nullstellen quadratischer Funktionen', fontsize=14, fontweight='bold')

st.pyplot(fig2)
plt.close()

with st.expander("💡 Frage: Was versteht man unter den Nullstellen einer Parabel?"):
    st.markdown("""
**Lösung:**

Die *Nullstellen* einer Parabel sind die Stellen, an denen die Parabel die **x-Achse schneidet oder berührt**.
    """)

with st.expander("💡 Frage: Wie viele Nullstellen kann eine Parabel haben?"):
    st.markdown("""
**Lösung:**

Eine Parabel hat entweder
- **keine Nullstellen**, wenn die Parabel vollständig ober- oder unterhalb der x-Achse verläuft.
- **eine Nullstelle**, wenn der Scheitelpunkt auf der x-Achse liegt.
- **zwei Nullstellen**, sonst.
    """)

with st.expander("💡 Frage: Wie berechnet man die Nullstellen einer Parabel?"):
    st.markdown(r"""
**Lösung:**

Man setzt $f(x)=0$ und löst die daraus entstehende Gleichung (man setzt die *Funktionsgleichung* $=0$ und löst diese Gleichung dann nach x auf).

D.h. die Nullstellen sind diejenigen x-Werte, für die die Funktionsgleichung $0$ ergibt.
    """)

st.divider()

# 2.2 Ablesbare Eigenschaften
st.subheader("2.2 Ablesbare Eigenschaften der Parabel")

st.markdown("**Aufgabe:** Verändere die Funktionsgleichung durch Bewegen der Slider. Welches Muster erkennst du in der Funktionsgleichung?")

col3, col4 = st.columns([1, 2])

with col3:
    a_fak = st.slider("Parameter a:", -3.0, 3.0, 1.0, 0.1, key="a_fak")
    x1_fak = st.slider("Nullstelle x₁:", -8.0, 8.0, -2.0, 0.5, key="x1_fak")
    x2_fak = st.slider("Nullstelle x₂:", -8.0, 8.0, 2.0, 0.5, key="x2_fak")

with col4:
    x = np.linspace(-10, 10, 400)
    y = a_fak * (x - x1_fak) * (x - x2_fak)
    
    # Scheitelpunkt berechnen
    d_fak = (x1_fak + x2_fak) / 2
    e_fak = a_fak * (d_fak - x1_fak) * (d_fak - x2_fak)
    
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.plot(x, y, 'g-', linewidth=2, label=f'$f(x) = {a_fak} · (x-({x1_fak})) · (x-({x2_fak}))$')
    ax3.plot([x1_fak, x2_fak], [0, 0], 'ro', markersize=10, label=f'Nullstellen: x₁={x1_fak}, x₂={x2_fak}')
    
    ax3.axhline(y=0, color='k', linewidth=0.5)
    ax3.axvline(x=0, color='k', linewidth=0.5)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(-10, 10)
    ax3.set_ylim(-10, 10)
    ax3.set_xticks(range(-10, 11, 1))
    ax3.set_yticks(range(-10, 11, 1))
    ax3.set_xlabel('x', fontsize=12)
    ax3.set_ylabel('f(x)', fontsize=12)
    ax3.legend(fontsize=10)
    ax3.set_title('Faktorisierte Form - Nullstellenform', fontsize=14, fontweight='bold')
    
    # Eigenschaften
    oeffnung = "nach oben" if a_fak > 0 else "nach unten"
    if abs(a_fak) > 1:
        streckung = "gestreckt"
    elif abs(a_fak) < 1:
        streckung = "gestaucht"
    else:
        streckung = "keine Streckung"
    
    ax3.text(0.02, 0.98, f'Öffnung: {oeffnung}\nStreckung: {streckung}', 
            transform=ax3.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5), fontsize=10)
    
    st.pyplot(fig3)
    plt.close()

with st.expander("✅ Frage: Was kann man aus der faktorisierten Form (Nullstellenform) direkt ablesen?"):
    st.markdown(r"""
**Lösung:**

- **Nullstellen**: $x_1$ und $x_2$
- **Öffnung**:
    - $a>0$ → nach oben
    - $a<0$ → nach unten
- **Streckung**: 
    - $|a|>1$ → gestreckt
    - $|a|<1$ → gestaucht
    """)

st.divider()

# Spezialfall: Eine Nullstelle
st.markdown("### Spezialfall: Eine Nullstelle")

with st.expander("💡 Frage: Wie sieht die faktorisierte Form aus, wenn es nur **eine Nullstelle** gibt?"):
    st.markdown(r"""
$x_0$ ist die Nullstelle. Bewege den Slider und achte auf die Funktionsgleichung.
""")
    
    col_help1, col_help2 = st.columns([1, 2])
    
    with col_help1:
        a_eine = st.slider("Parameter a:", -3.0, 3.0, 1.0, 0.1, key="a_eine")
        x0_eine = st.slider("Nullstelle x₀:", -8.0, 8.0, 2.0, 0.5, key="x0_eine")
    
    with col_help2:
        x = np.linspace(-10, 10, 400)
        y = a_eine * (x - x0_eine) * (x - x0_eine)
        
        fig_eine, ax_eine = plt.subplots(figsize=(10, 6))
        ax_eine.plot(x, y, 'g-', linewidth=2, label=f'$f(x) = {a_eine} · (x-({x0_eine})) · (x-({x0_eine})) = {a_eine} · (x-({x0_eine}))^2$')
        ax_eine.plot(x0_eine, 0, 'ro', markersize=10, label=f'Nullstelle: x₀={x0_eine}')
        
        ax_eine.axhline(y=0, color='k', linewidth=0.5)
        ax_eine.axvline(x=0, color='k', linewidth=0.5)
        ax_eine.grid(True, alpha=0.3)
        ax_eine.set_xlim(-10, 10)
        ax_eine.set_ylim(-2, 10)
        ax_eine.set_xticks(range(-10, 11, 1))
        ax_eine.set_yticks(range(-2, 11, 1))
        ax_eine.set_xlabel('x', fontsize=12)
        ax_eine.set_ylabel('f(x)', fontsize=12)
        ax_eine.legend(fontsize=10)
        ax_eine.set_title('Faktorisierte Form - Nullstellenform', fontsize=14, fontweight='bold')
        
        st.pyplot(fig_eine)
        plt.close()
    
    st.markdown("---")
    st.markdown(r"""
**Lösung:**

Wenn es nur eine Nullstelle $x_{0}$ gibt, dann liegt der Scheitelpunkt auf der x-Achse.
Aus diesem Grund sind in diesem Fall die Scheitelpunktform und die faktorisierte Form (Nullstellenform) identisch:

$$f(x)=a\cdot (x - x_{0})^2$$
    """)

with st.expander("💡 Frage: Wie sieht die faktorisierte Form aus, wenn es **keine Nullstellen** gibt?"):
    st.markdown("""
**Lösung:**

Wenn es keine Nullstellen gibt, dann gibt es auch keine Funktionsgleichung in faktorisierter Form.
    """)

st.divider()

# Zusammenfassung Nullstellenform
st.markdown("""
#### Zusammenfassung: Eigenschaften der Parabel ausgehend von der Nullstellenform

An einer Funktionsgleichung, die in Nullstellenform gegeben ist,
""")
st.latex(r"f(x) = a \cdot (x - x_{1}) \cdot (x - x_{2})")
st.markdown("""
können wir folgendes direkt ablesen:

- **Nullstellen**: $x_1$ und $x_2$ (*oder evtl. nur eine Nullstelle*)
- **Öffnung**:
    - $a>0$ → nach oben
    - $a<0$ → nach unten
- **Streckung**: 
    - $|a|>1$ → gestreckt
    - $|a|<1$ → gestaucht
""")

st.divider()

# 2.3 Bestimmung des Scheitelpunkts
st.subheader("2.3 Bestimmung des Scheitelpunkts ausgehend von der Nullstellenform")

with st.expander("💡 Frage: Wo liegt die **x-Koordinate des Scheitelpunkts** in Bezug auf die Nullstellen?"):
    st.markdown("""
**Hilfestellung**

Bewege die Slider. Achte auf die Lage der Nullstellen und die Lage des Scheitelpunkts.
""")
    
    col_sp1, col_sp2 = st.columns([1, 2])
    
    with col_sp1:
        a_sp_null = st.slider("Parameter a:", -3.0, 3.0, 1.0, 0.1, key="a_sp_null")
        x1_sp_null = st.slider("Nullstelle x₁:", -8.0, 8.0, -2.0, 0.5, key="x1_sp_null")
        x2_sp_null = st.slider("Nullstelle x₂:", -8.0, 8.0, 2.0, 0.5, key="x2_sp_null")
    
    with col_sp2:
        x = np.linspace(-10, 10, 400)
        y = a_sp_null * (x - x1_sp_null) * (x - x2_sp_null)
        
        # Scheitelpunkt berechnen
        d_sp_null = (x1_sp_null + x2_sp_null) / 2
        e_sp_null = a_sp_null * (d_sp_null - x1_sp_null) * (d_sp_null - x2_sp_null)
        
        fig_sp_null, ax_sp_null = plt.subplots(figsize=(10, 6))
        ax_sp_null.plot(x, y, 'g-', linewidth=2, label=f'$f(x) = {a_sp_null}(x-({x1_sp_null}))(x-({x2_sp_null}))$')
        ax_sp_null.plot([x1_sp_null, x2_sp_null], [0, 0], 'ro', markersize=10, label=f'Nullstellen: $x_1={x1_sp_null}$, $x_2={x2_sp_null}$')
        ax_sp_null.plot(d_sp_null, e_sp_null, 'mo', markersize=10, label=f'Scheitelpunkt S({d_sp_null:.1f}|{e_sp_null:.1f})')
        
        ax_sp_null.axhline(y=0, color='k', linewidth=0.5)
        ax_sp_null.axvline(x=0, color='k', linewidth=0.5)
        ax_sp_null.grid(True, alpha=0.3)
        ax_sp_null.set_xlim(-10, 10)
        ax_sp_null.set_ylim(-10, 10)
        ax_sp_null.set_xticks(range(-10, 11, 1))
        ax_sp_null.set_yticks(range(-10, 11, 1))
        ax_sp_null.set_xlabel('x', fontsize=12)
        ax_sp_null.set_ylabel('f(x)', fontsize=12)
        ax_sp_null.legend(fontsize=10)
        ax_sp_null.set_title('Faktorisierte Form (Nullstellenform)', fontsize=14, fontweight='bold')
        
        st.pyplot(fig_sp_null)
        plt.close()
    
    st.markdown("---")
    st.markdown("""
**Lösung:**

Die x-Koordinate des Scheitelpunkts $d$ liegt immer **in der Mitte der beiden Nullstellen**.
    """)

with st.expander("💡 Frage: Wie bestimmen wir die **y-Koordinate e des Scheitelpunkts**?"):
    st.markdown(r"""
**Lösung:**

Immer wenn wir zu einem gegebenen x-Wert den dazugehörigen y-Wert bestimmen möchten, gehen wir wie folgt vor:

1. Wir setzen den x-Wert (in diesem Fall wäre das $d$) in die Funktionsgleichung ein.
2. Wir rechnen alles aus. Das Ergebnis ist der dazugehörige y-Wert (in diesem Fall wäre das $e$).
    """)

st.markdown("""
#### Zusammenfassung: Bestimmung des Scheitelpunkts ausgehend von der Nullstellenform

Um den Scheitelpunkt $S(d|e)$ ausgehend von einer Funktionsgleichung in Nullstellenform zu bestimmen, gehen wir wie folgt vor:

**1. Wir bestimmen die x-Koordinate $d$ des Scheitelpunkts**

Da der Scheitelpunkt immer in der Mitte zwischen den beiden Nullstellen liegt, können wir seine x-Koordinate folgendermaßen berechnen:
""")
st.latex(r"d = \frac{x_{1} + x_{2}}{2}")

st.markdown("""
**2. Wir bestimmen die y-Koordinate $e$ des Scheitelpunkts**

Wir setzen $d$ in die Funktionsgleichung ein und berechnen dadurch $e$:
""")
st.latex(r"e = f(d)")

st.divider()

# 2.4 Übungen
st.subheader("2.4 Übungen")

# Übung 1
with st.expander("📝 Übung 1: $f(x) = 2 \\cdot (x - 1) \\cdot (x + 3)$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $f(x) = 2 \cdot (x - 1) \cdot (x + 3)$

Bestimme:

1. Die **Nullstellen** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung1"):
        st.markdown(r"""
**Lösung:**

1. **Nullstellen**: $x_1 = 1$ und $x_2 = -3$
2. **Öffnungsrichtung**: Nach oben (da $a = 2 > 0$)
3. **Streckung**: Gestreckt (da $|a| = 2 > 1$)
4. **Scheitelpunkt**: 
   - $d = \frac{1 + (-3)}{2} = \frac{-2}{2} = -1$
   - $e = f(-1) = 2 \cdot (-1-1) \cdot (-1+3) = 2 \cdot (-2) \cdot 2 = -8$
   - Also: $S(-1|-8)$
        """)

# Übung 2
with st.expander("📝 Übung 2: $g(x) = -3(x+2)(x-4)$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $g(x) = -3(x+2)(x-4)$

Bestimme:

1. Die **Nullstellen** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung2"):
        st.markdown(r"""
**Lösung:**

1. **Nullstellen**: $x_1 = -2$ und $x_2 = 4$
2. **Öffnungsrichtung**: Nach unten (da $a = -3 < 0$)
3. **Streckung**: Gestreckt (da $|a| = 3 > 1$)
4. **Scheitelpunkt**: 
   - $d = \frac{-2 + 4}{2} = \frac{2}{2} = 1$
   - $e = f(1) = -3 \cdot (1+2) \cdot (1-4) = -3 \cdot 3 \cdot (-3) = 27$
   - Also: $S(1|27)$
        """)

# Übung 3
with st.expander("📝 Übung 3: $h(x)=\\frac{1}{2}(x-5)(x+1)$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $h(x)=\frac{1}{2}(x-5)(x+1)$

Bestimme:

1. Die **Nullstellen** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung3"):
        st.markdown(r"""
**Lösung:**

1. **Nullstellen**: $x_1 = 5$ und $x_2 = -1$
2. **Öffnungsrichtung**: Nach oben (da $a = \frac{1}{2} > 0$)
3. **Streckung**: Gestaucht (da $|a| = \frac{1}{2} < 1$)
4. **Scheitelpunkt**: 
   - $d = \frac{5 + (-1)}{2} = \frac{4}{2} = 2$
   - $e = f(2) = \frac{1}{2} \cdot (2-5) \cdot (2+1) = \frac{1}{2} \cdot (-3) \cdot 3 = -\frac{9}{2} = -4.5$
   - Also: $S(2|-4.5)$
        """)

# Übung 4
with st.expander("📝 Übung 4: $k(x)=-2(x-3)^2$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $k(x)=-2(x-3)^2$

Bestimme:

1. Die **Nullstellen** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung4"):
        st.markdown(r"""
**Lösung:**

1. **Nullstellen**: Nur eine Nullstelle: $x_0 = 3$
2. **Öffnungsrichtung**: Nach unten (da $a = -2 < 0$)
3. **Streckung**: Gestreckt (da $|a| = 2 > 1$)
4. **Scheitelpunkt**: Da dies die Scheitelpunktform ist mit nur einer Nullstelle, liegt der Scheitelpunkt auf der x-Achse: $S(3|0)$
        """)

st.divider()

# ==================================================
# 3. POLYNOMFORM
# ==================================================

st.header("3. Die Polynomform (allgemeine Form)")
st.latex(r"f(x) = ax^2 + bx + c")

# 3.1 Wiederholung: y-Achsenabschnitt
st.subheader("3.1 Wiederholung des Begriffs **y-Achsenabschnitt**")

fig4, ax4 = plt.subplots(figsize=(12, 8))
x = np.linspace(-6, 6, 400)

y1 = (x - 3)**2 - 2
y2 = -(x + 2)**2 + 5
y3 = -0.5 * x**2 + 4

c1 = 7
c2 = 1
c3 = 4

ax4.plot(x, y1, 'b-', linewidth=2.5, label=f'Linker Ast: $f(x) = (x-3)^2 - 2$ (c = {c1})')
ax4.plot(x, y2, 'g-', linewidth=2.5, label=f'Rechter Ast: $f(x) = -(x+2)^2 + 5$ (c = {c2})')
ax4.plot(x, y3, 'r-', linewidth=2.5, label=f'Scheitelpunkt: $f(x) = -0.5x^2 + 4$ (c = {c3})')

ax4.plot(0, c1, 'bo', markersize=12, zorder=5)
ax4.plot(0, c2, 'go', markersize=12, zorder=5)
ax4.plot(0, c3, 'ro', markersize=12, zorder=5)

ax4.axhline(y=0, color='k', linewidth=0.8)
ax4.axvline(x=0, color='k', linewidth=1.2)
ax4.grid(True, alpha=0.3)
ax4.set_xlim(-6, 6)
ax4.set_ylim(-4, 8)
ax4.set_xticks(range(-6, 7, 1))
ax4.set_yticks(range(-4, 9, 1))
ax4.set_xlabel('x', fontsize=12)
ax4.set_ylabel('f(x)', fontsize=12)
ax4.legend(fontsize=11, loc='upper right')
ax4.set_title('y-Achsenabschnitt bei quadratischen Funktionen', fontsize=14, fontweight='bold')

st.pyplot(fig4)
plt.close()

with st.expander("💡 Aufgabe: Was versteht man unter dem y-Achsenabschnitt einer Parabel?"):
    st.markdown(r"""
**Lösung:**

Der *y-Achsenabschnitt* einer Parabel ist der $f(x)$-Wert (bzw. $y$-Wert), an dem die Parabel die **y-Achse schneidet**.
    """)

with st.expander("💡 Aufgabe: Wie berechnet man den y-Achsenabschnitt einer Parabel?"):
    st.markdown(r"""
**Lösung:**

Man berechnet den Wert für $f(0)$.

D.h. man setzt für jedes $x$ in der Funktionsgleichung den Wert $0$ ein.
    """)

st.divider()

st.markdown("### 3.2 Ablesbare Eigenschaften der Parabel")
st.markdown("**Aufgabe:** Verändere die Parameter und beobachte die Veränderungen. Finde das Muster in der Funktionsgleichung.")

col5, col6 = st.columns([1, 2])

with col5:
    a_poly = st.slider("Parameter a:", -3.0, 3.0, 1.0, 0.1, key="a_poly")
    b_poly = st.slider("Parameter b:", -10.0, 10.0, 0.0, 0.5, key="b_poly")
    c_poly = st.slider("Parameter c:", -10.0, 10.0, 0.0, 0.5, key="c_poly")

with col6:
    x = np.linspace(-10, 10, 400)
    y = a_poly * x**2 + b_poly * x + c_poly
    
    # Scheitelpunkt berechnen
    if a_poly != 0:
        d_poly = -b_poly / (2 * a_poly)
        e_poly = a_poly * d_poly**2 + b_poly * d_poly + c_poly
    else:
        d_poly = 0
        e_poly = c_poly
    
    # Diskriminante für Nullstellen
    discriminant = b_poly**2 - 4 * a_poly * c_poly
    
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    ax5.plot(x, y, 'r-', linewidth=2, label=f'$f(x) = {a_poly}x^2 + {b_poly}x + {c_poly}$')
    ax5.plot(0, c_poly, 'bo', markersize=10, label=f'y-Achsenabschnitt: c={c_poly}')
    
    
    
    ax5.axhline(y=0, color='k', linewidth=0.5)
    ax5.axvline(x=0, color='k', linewidth=0.5)
    ax5.grid(True, alpha=0.3)
    ax5.set_xlim(-10, 10)
    ax5.set_ylim(-10, 10)
    ax5.set_xticks(range(-10, 11, 1))
    ax5.set_yticks(range(-10, 11, 1))
    ax5.set_xlabel('x', fontsize=12)
    ax5.set_ylabel('f(x)', fontsize=12)
    ax5.legend(fontsize=10)
    ax5.set_title('Polynomform (Normalform)', fontsize=14, fontweight='bold')
    
    # Eigenschaften
    oeffnung = "nach oben" if a_poly > 0 else "nach unten"
    if abs(a_poly) > 1:
        streckung = "gestreckt"
    elif abs(a_poly) < 1:
        streckung = "gestaucht"
    else:
        streckung = "keine Streckung"
    
    ax5.text(0.02, 0.98, f'Öffnung: {oeffnung}\nStreckung: {streckung}', 
            transform=ax5.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5), fontsize=10)

    st.pyplot(fig5)
    plt.close()
    
with st.expander("✅ Lösung anzeigen: Was kann man aus der Polynomform direkt ablesen?"):
    st.markdown(r"""
**Lösung:**

- **y-Achsenabschnitt**: $c$
- **Öffnung**:
    - $a>0$ → nach oben
    - $a<0$ → nach unten
- **Streckung**: 
    - $|a|>1$ → gestreckt
    - $|a|<1$ → gestaucht
    """)


st.divider()


# 2.3 Bestimmung des Scheitelpunkts ausgehend von der Polynomform
st.subheader("2.3 Bestimmung des Scheitelpunkts ausgehend von der Polynomform")

st.markdown("""
Die Bestimmung des Scheitelpunkts ausgehend von der Polynomform ist nicht unbedingt trivial. 
Um uns das Leben in Zukunft zu vereinfachen, werden wir die **allgemeine Polynomform schrittweise 
in die Scheitelpunktform umformen**. Aus dieser Umformung können wir dann eine **Formel für die 
x-Koordinate des Scheitelpunkts** direkt ablesen. Die **y-Koordinate** bestimmen wir anschließend 
wie gewohnt durch Einsetzen in die Funktionsgleichung.

Los geht's! 🚀
""")

st.markdown("---")

st.markdown("#### Schritt-für-Schritt Umformung")

st.markdown("""
**Gegeben:** Die allgemeine Polynomform
""")
st.latex(r"f(x) = ax^2 + bx + c")

st.markdown("""
**Ziel:** Umformung in die Scheitelpunktform
""")
st.latex(r"f(x) = a(x-d)^2 + e")

st.markdown("---")

# Umformungsschritte
st.markdown("##### 📐 Umformung durch quadratische Ergänzung")

st.markdown("**Schritt 1:** Faktor $a$ ausklammern")
st.latex(r"f(x) = a\left(x^2 + \frac{b}{a}x\right) + c")

st.markdown("**Schritt 2:** Quadratische Ergänzung vorbereiten")
st.markdown(r"""
Wir ergänzen den Term in der Klammer so, dass eine binomische Formel entsteht.
Dafür addieren und subtrahieren wir $\left(\frac{b}{2a}\right)^2$:
""")
st.latex(r"f(x) = a\left(x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 - \left(\frac{b}{2a}\right)^2\right) + c")

st.markdown("**Schritt 3:** Binomische Formel anwenden")
st.markdown(r"Die ersten drei Terme ergeben ein Binom:")
st.latex(r"f(x) = a\left[\left(x + \frac{b}{2a}\right)^2 - \left(\frac{b}{2a}\right)^2\right] + c")

st.markdown("**Schritt 4:** Ausmultiplizieren und zusammenfassen")
st.latex(r"f(x) = a\left(x + \frac{b}{2a}\right)^2 - a\left(\frac{b}{2a}\right)^2 + c")

st.latex(r"f(x) = a\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a} + c")

st.markdown("**Schritt 5:** In Scheitelpunktform schreiben")
st.markdown(r"Vergleichen wir mit $f(x) = a(x-d)^2 + e$, erkennen wir:")
st.latex(r"f(x) = a\left(x - \left(-\frac{b}{2a}\right)\right)^2 + \left(c - \frac{b^2}{4a}\right)")

st.markdown("---")

# Formeln hervorheben
st.markdown("#### 🎯 Abgelesene Formeln für den Scheitelpunkt")

col_form1, col_form2 = st.columns(2)

with col_form1:
    st.markdown("**x-Koordinate des Scheitelpunkts:**")
    st.latex(r"d = -\frac{b}{2a}")

with col_form2:
    st.markdown("**y-Koordinate des Scheitelpunkts:**")
    st.latex(r"e = f(d) = ad^2 + bd + c")

st.info("""
💡 **Merke:** 
- Die **x-Koordinate** $d$ des Scheitelpunkts können wir direkt mit der Formel $d = -\\frac{b}{2a}$ berechnen.
- Die **y-Koordinate** $e$ erhalten wir durch Einsetzen von $d$ in die ursprüngliche Funktionsgleichung.
""")

st.markdown("---")

# Beispielrechnung
st.markdown("#### 📝 Beispiel zur Anwendung")

with st.expander("🔍 Beispiel: Scheitelpunkt von $f(x) = 2x^2 - 8x + 5$ bestimmen"):
    st.markdown(r"""
**Gegeben:** $f(x) = 2x^2 - 8x + 5$

Das bedeutet: $a = 2$, $b = -8$, $c = 5$

**Schritt 1: x-Koordinate berechnen**
""")
    st.latex(r"d = -\frac{b}{2a} = -\frac{-8}{2 \cdot 2} = -\frac{-8}{4} = 2")
    
    st.markdown(r"""
**Schritt 2: y-Koordinate berechnen**

Wir setzen $d = 2$ in die Funktionsgleichung ein:
""")
    st.latex(r"e = f(2) = 2 \cdot 2^2 - 8 \cdot 2 + 5 = 2 \cdot 4 - 16 + 5 = 8 - 16 + 5 = -3")
    
    st.markdown(r"""
**Ergebnis:** Der Scheitelpunkt liegt bei $S(2|-3)$

**Probe:** Die Scheitelpunktform lautet also:
""")
    st.latex(r"f(x) = 2(x-2)^2 - 3")
    
    st.success("✅ Wenn wir diese Form ausmultiplizieren, erhalten wir wieder die ursprüngliche Polynomform!")

st.markdown("---")

# Zusammenfassung
st.markdown("""
#### 📋 Zusammenfassung: Scheitelpunkt aus Polynomform bestimmen

Um den Scheitelpunkt $S(d|e)$ einer quadratischen Funktion in Polynomform $f(x) = ax^2 + bx + c$ zu bestimmen:

**1. Berechne die x-Koordinate mit der Formel:**
""")
st.latex(r"d = -\frac{b}{2a}")

st.markdown("""
**2. Berechne die y-Koordinate durch Einsetzen:**
""")
st.latex(r"e = f(d)")

st.markdown("""
**Fertig!** Der Scheitelpunkt ist $S(d|e)$.
""")


st.divider()



# 3.3 Übungen
st.subheader("3.3 Übungen")

st.markdown("""
Übe nun das Ablesen und Berechnen von Eigenschaften quadratischer Funktionen in Polynomform!
""")

# Übung 1
with st.expander("📝 Übung 1: $f(x) = x^2 + 4x + 3$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $f(x) = x^2 + 4x + 3$

Bestimme:

1. Den **y-Achsenabschnitt** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung_poly1"):
        st.markdown(r"""
**Lösung:**

Zunächst identifizieren wir die Parameter: $a = 1$, $b = 4$, $c = 3$

1. **y-Achsenabschnitt**: $c = 3$
   
2. **Öffnungsrichtung**: Nach oben (da $a = 1 > 0$)
   
3. **Streckung**: Keine Streckung (da $|a| = 1$)
   
4. **Scheitelpunkt**: 
   - $d = -\frac{b}{2a} = -\frac{4}{2 \cdot 1} = -\frac{4}{2} = -2$
   - $e = f(-2) = (-2)^2 + 4 \cdot (-2) + 3 = 4 - 8 + 3 = -1$
   - Also: $S(-2|-1)$
        """)

# Übung 2
with st.expander("📝 Übung 2: $g(x) = -2x^2 + 8x - 5$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $g(x) = -2x^2 + 8x - 5$

Bestimme:

1. Den **y-Achsenabschnitt** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung_poly2"):
        st.markdown(r"""
**Lösung:**

Zunächst identifizieren wir die Parameter: $a = -2$, $b = 8$, $c = -5$

1. **y-Achsenabschnitt**: $c = -5$
   
2. **Öffnungsrichtung**: Nach unten (da $a = -2 < 0$)
   
3. **Streckung**: Gestreckt (da $|a| = 2 > 1$)
   
4. **Scheitelpunkt**: 
   - $d = -\frac{b}{2a} = -\frac{8}{2 \cdot (-2)} = -\frac{8}{-4} = 2$
   - $e = f(2) = -2 \cdot 2^2 + 8 \cdot 2 - 5 = -2 \cdot 4 + 16 - 5 = -8 + 16 - 5 = 3$
   - Also: $S(2|3)$
        """)

# Übung 3
with st.expander("📝 Übung 3: $h(x) = 0.5x^2 - 3x + 2$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $h(x) = 0.5x^2 - 3x + 2$

Bestimme:

1. Den **y-Achsenabschnitt** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung_poly3"):
        st.markdown(r"""
**Lösung:**

Zunächst identifizieren wir die Parameter: $a = 0.5$, $b = -3$, $c = 2$

1. **y-Achsenabschnitt**: $c = 2$
   
2. **Öffnungsrichtung**: Nach oben (da $a = 0.5 > 0$)
   
3. **Streckung**: Gestaucht (da $|a| = 0.5 < 1$)
   
4. **Scheitelpunkt**: 
   - $d = -\frac{b}{2a} = -\frac{-3}{2 \cdot 0.5} = -\frac{-3}{1} = 3$
   - $e = f(3) = 0.5 \cdot 3^2 - 3 \cdot 3 + 2 = 0.5 \cdot 9 - 9 + 2 = 4.5 - 9 + 2 = -2.5$
   - Also: $S(3|-2.5)$
        """)

# Übung 4
with st.expander("📝 Übung 4: $k(x) = 3x^2 + 12x + 7$"):
    st.markdown(r"""
**Aufgabe:**

Gegeben ist $k(x) = 3x^2 + 12x + 7$

Bestimme:

1. Den **y-Achsenabschnitt** der Parabel
2. Die **Öffnungsrichtung** der Parabel
3. Die **Streckung** der Parabel
4. Den **Scheitelpunkt** der Parabel
    """)
    
    if st.button("✅ Lösung anzeigen", key="loesung_poly4"):
        st.markdown(r"""
**Lösung:**

Zunächst identifizieren wir die Parameter: $a = 3$, $b = 12$, $c = 7$

1. **y-Achsenabschnitt**: $c = 7$
   
2. **Öffnungsrichtung**: Nach oben (da $a = 3 > 0$)
   
3. **Streckung**: Gestreckt (da $|a| = 3 > 1$)
   
4. **Scheitelpunkt**: 
   - $d = -\frac{b}{2a} = -\frac{12}{2 \cdot 3} = -\frac{12}{6} = -2$
   - $e = f(-2) = 3 \cdot (-2)^2 + 12 \cdot (-2) + 7 = 3 \cdot 4 - 24 + 7 = 12 - 24 + 7 = -5$
   - Also: $S(-2|-5)$
        """)

st.divider()




# ==================================================
# 4. VERGLEICH
# ==================================================

st.header("4. Vergleich: Welche Form für welchen Zweck?")

# Tabelle als Markdown
st.markdown("""
| Darstellungsform | Direkt ablesbar | Beste Anwendung |
|------------------|-----------------|-----------------|
| **Scheitelpunktform** $a(x-d)^2 + e$ | Scheitelpunkt $S(d\|e)$ | Graph zeichnen, Verschiebungen verstehen |
| **Faktorisierte Form** $a(x-x_1)(x-x_2)$ | Nullstellen $x_1, x_2$ | Schnittpunkte mit x-Achse finden |
| **Polynomform** $ax^2 + bx + c$ | y-Achsenabschnitt $c$ | Funktionswerte berechnen, Ableitungen, ... |
""")

st.success("🎉 Herzlichen Glückwunsch! Du hast alle drei Darstellungsformen kennengelernt und geübt!")

# Footer
st.divider()
st.markdown("""
---
*Interaktives Lerntool für Quadratische Funktionen*  
Erstellt mit Streamlit 🎈
""")