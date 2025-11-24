import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Seitenkonfiguration
st.set_page_config(
    page_title="Grafisches Lösungsverfahren",
    page_icon="⚖️",
    layout="wide"
)

st.title("Grafisches Lösungsverfahren")
st.markdown("---")

# Einführungsbeispiel
st.header("Einführungsbeispiel: Kraftstoffverbrauch eines PKW")

st.write("""
Der Kraftstoffverbrauch eines PKW hängt bekanntlich von der Geschwindigkeit ab. 
Durch Messungen wurde der funktionale Zusammenhang ermittelt. Es gilt:
""")

st.latex(r"K(v) = 0{,}002v^2 - 0{,}18v + 8{,}55")

st.markdown(f"""
für **v > 40**.

Dabei bedeutet:
- **$K(v)$**: Kraftstoffverbrauch in *Liter/100 km*
- **$v$**: Geschwindigkeit in *km/h*
""")

# Frage
st.markdown("#### Frage")
st.write("Bei welcher Geschwindigkeit beträgt der Verbrauch genau 7 Liter/100km?")

# Aufgabe
st.markdown("#### Aufgabe")
st.write("Übersetze diese Frage in eine Gleichung.")

# Eingabefeld
antwort = st.text_input(
    "Deine Gleichung:",
    placeholder="z.B. 4*v^2+4*v+2=1"
)

if st.button("Überprüfen"):
    # Bereinige die Eingabe (Leerzeichen entfernen, klein schreiben)
    antwort_clean = antwort.replace(" ", "").replace(",", ".").lower()
    
    # Mögliche richtige Antworten
    richtige_antworten = [
        "0.002v²-0.18v+8.55=7",
        "0.002v^2-0.18v+8.55=7",
        "0.002*v^2-0.18*v+8.55=7",
        "7=0.002v²-0.18v+8.55"  # Auch umgekehrt akzeptieren
        "7=0.002v^2-0.18v+8.55",
        "7=0.002*v^2-0.18*v+8.55",
    ]
    
    if any(antwort_clean == richtig for richtig in richtige_antworten):
        st.success("✅ Richtig! Die Gleichung lautet $0,002v^2+0,18v+8,55=7$")
    else:
        st.error("❌ Nicht ganz. Tipp: $K(v) = 7$ einsetzen")

# Zusatzerklärung
with st.expander("💡 Erklärung der Gleichung"):
    st.markdown("""
    1. Die Funktionsgleichung lautet: <span style='color: green;'>$K(v)$</span> $= 0,002v² - 0,18v + 8,55$
    2. Wir suchen die Geschwindigkeit für <span style='color: green;'>$K(v)=7$</span>
    3. Setze ein: $0,002v² - 0,18v + 8,55 =$ <span style='color: green;'>$7$</span>
    """, unsafe_allow_html=True)


# Interaktive Visualisierung
st.subheader("Interaktive Visualisierung")

st.write("""
Bewege den **Schieberegler**, um verschiedene Verbrauchswerte einzustellen. 
Die **rote horizontale Linie** zeigt den gewählten Verbrauch. 
Die **grünen Punkte** zeigen die Lösungen (Geschwindigkeiten) an.
""")

# Slider für den Kraftstoffverbrauch
ziel_verbrauch = st.slider(
    "Kraftstoffverbrauch K (Liter/100km)", 
    min_value=4.0, 
    max_value=9.0, 
    value=4.0, 
    step=0.1,
    help="Verschiebe den Regler, um verschiedene Verbrauchswerte zu testen"
)

# Funktion definieren
def kraftstoff(v):
    return 0.002 * v**2 - 0.18 * v + 8.55

# Geschwindigkeitsbereich (v > 40)
v = np.linspace(40, 120, 400)
K = kraftstoff(v)

# Plot erstellen
fig, ax = plt.subplots(figsize=(8, 5))

# Parabel zeichnen
ax.plot(v, K, 'b-', linewidth=2.5, label='K(v) = 0,002v² - 0,18v + 8,55')

# Horizontale Linie für Zielverbrauch
ax.axhline(y=ziel_verbrauch, color='red', linestyle='--', linewidth=2, 
           label=f'Zielverbrauch: {ziel_verbrauch} L/100km')

# Schnittpunkte berechnen
# 0.002v² - 0.18v + 8.55 = ziel_verbrauch
# 0.002v² - 0.18v + (8.55 - ziel_verbrauch) = 0
a = 0.002
b = -0.18
c = 8.55 - ziel_verbrauch

diskriminante = b**2 - 4*a*c

if diskriminante >= 0:
    v1 = (-b + np.sqrt(diskriminante)) / (2*a)
    v2 = (-b - np.sqrt(diskriminante)) / (2*a)
    
    # Nur Lösungen für v > 40 anzeigen
    loesungen = []
    if v1 > 40:
        loesungen.append(v1)
        ax.plot(v1, ziel_verbrauch, 'go', markersize=12, 
                markeredgewidth=2, markeredgecolor='darkgreen',
                label=f'Lösung: v = {v1:.1f} km/h')
        # Vertikale Hilfslinie
        ax.plot([v1, v1], [0, ziel_verbrauch], 'g--', alpha=0.5, linewidth=1)
    
    if v2 > 40 and abs(v1 - v2) > 0.1:  # Zweite Lösung nur wenn verschieden
        loesungen.append(v2)
        ax.plot(v2, ziel_verbrauch, 'go', markersize=12, 
                markeredgewidth=2, markeredgecolor='darkgreen',
                label=f'Lösung 2: v = {v2:.1f} km/h')
        # Vertikale Hilfslinie
        ax.plot([v2, v2], [0, ziel_verbrauch], 'g--', alpha=0.5, linewidth=1)

# Achsenbeschriftung
ax.set_xlabel('Geschwindigkeit v (km/h)', fontsize=13, fontweight='bold')
ax.set_ylabel('Kraftstoffverbrauch K (Liter/100 km)', fontsize=13, fontweight='bold')
ax.set_title('Kraftstoffverbrauch in Abhängigkeit von der Geschwindigkeit', 
             fontsize=15, fontweight='bold', pad=20)

# Gitter
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.set_xlim(40, 120)
ax.set_ylim(3, 9)

# Legende
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# Plot anzeigen
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# Übungen
st.header("Mögliche Anzahl von Lösungen quadratischer Gleichungen")

st.markdown("""
    #### Aufgabe
    
    1. Nutze die Schieberegler, um die Lösungen der Gleichungen graphisch zu bestimmen.
    2. Trage deine Lösung(en) in das Antwortfeld ein.
            """)

st.write("")

col4, col5, col6 = st.columns([1,1,1])

with col4:
# Aufgabe 1
    st.markdown(f"$x² - 4x + 5 = 1$")

    ziel_1 = st.slider(
        "Rechte Seite der Gleichung (y-Wert):",
        min_value=-2.0,
        max_value=8.0,
        value=0.0,
        step=0.1,
        key="slider_1"
    )
    
    # Plot für Aufgabe 1
    x = np.linspace(-2, 6, 400)
    y1 = x**2 - 4*x + 5
    
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(x, y1, 'b-', linewidth=2.5, label='f(x) = x² - 4x + 5')
    ax1.axhline(y=ziel_1, color='red', linestyle='--', linewidth=2, 
                label=f'y = {ziel_1}')
    
    # Schnittpunkte berechnen: x² - 4x + 5 = ziel_1
    # x² - 4x + (5 - ziel_1) = 0
    a, b, c = 1, -4, (5 - ziel_1)
    disk = b**2 - 4*a*c
    
    if disk >= 0:
        x1 = (-b + np.sqrt(disk)) / (2*a)
        x2 = (-b - np.sqrt(disk)) / (2*a)
        
        if abs(x1 - x2) > 0.01:
            ax1.plot([x1, x2], [ziel_1, ziel_1], 'go', markersize=10,
                    markeredgewidth=2, markeredgecolor='darkgreen')
            ax1.plot([x1, x1], [0, ziel_1], 'g--', alpha=0.5, linewidth=1)
            ax1.plot([x2, x2], [0, ziel_1], 'g--', alpha=0.5, linewidth=1)
        else:
            ax1.plot(x1, ziel_1, 'go', markersize=10,
                    markeredgewidth=2, markeredgecolor='darkgreen')
            ax1.plot([x1, x1], [0, ziel_1], 'g--', alpha=0.5, linewidth=1)
    
    ax1.set_xlabel('x', fontsize=12, fontweight='bold')
    ax1.set_ylabel('y', fontsize=12, fontweight='bold')
    ax1.set_title('Aufgabe 1: x² - 4x + 5 = 1', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.spines['left'].set_position('zero')     # y-Achse durch x=0
    ax1.spines['bottom'].set_position('zero')   # x-Achse durch y=0
    ax1.spines['right'].set_color('none')       # Rechten Rand ausblenden
    ax1.spines['top'].set_color('none')         # Oberen Rand ausblenden
    
    if disk >= 0:
        ax1.plot([x1, x2], [ziel_1, ziel_1], 'go', markersize=10,
                markeredgewidth=2, markeredgecolor='darkgreen')
        # Legende nur für Info
        if abs(x1 - x2) > 0.01:
            ax1.plot([], [], ' ', label=f'x₁≈{x2:.2f}, x₂≈{x1:.2f}')
        else:
            ax1.plot([], [], ' ', label=f'x≈{x1:.2f}')
    else:
        ax1.plot([], [], ' ', label='Keine Lösungen')

    ax1.legend(loc='upper right', fontsize=10)
    ax1.set_xlim(-2, 6)
    ax1.set_ylim(-2, 10)
    ax1.set_xticks(np.arange(-2, 7, 1))   # x-Achse: von -2 bis 6 in 1er-Schritten
    ax1.set_yticks(np.arange(-2, 11, 1))  # y-Achse: von -2 bis 10 in 1er-Schritten
    
    st.pyplot(fig1)
    plt.close()

    
    # Eingabefeld
    lösung1 = st.text_input(
        "Deine Lösung:",
        placeholder="z.B. x=3 oder x=5 oder 'nicht lösbar'", key="input2"
    )

    if st.button("Überprüfen", key="button2"):        
        # Mögliche richtige Antworten
        richtige_antworten = [
            "x=2",
            "2=x",
            "x = 2",
            "2 = x"
        ]
        
        if any(lösung1 == richtig for richtig in richtige_antworten):
            st.success("✅ Richtig! $x=2$ ist die Lösung der Gleichung")
        else:
            st.error("❌ Nicht ganz. Tipp: Es gibt nur eine Lösung")

with col5:
    # Aufgabe 2
    st.markdown(f"$x² - 4x + 3 = 2$")

    ziel_2 = st.slider(
        "Rechte Seite der Gleichung (y-Wert):",
        min_value=-2.0,
        max_value=8.0,
        value=0.0,
        step=0.1,
        key="slider_2"
    )
    
    # Plot für Aufgabe 2
    y2 = x**2 - 4*x + 3
    
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(x, y2, 'b-', linewidth=2.5, label='f(x) = x² - 4x + 3')
    ax2.axhline(y=ziel_2, color='red', linestyle='--', linewidth=2, 
                label=f'y = {ziel_2}')
    
    # Schnittpunkte berechnen: x² - 4x + 3 = ziel_2
    # x² - 4x + (3 - ziel_2) = 0
    a, b, c = 1, -4, (3 - ziel_2)
    disk = b**2 - 4*a*c
    
    if disk >= 0:
        x1 = (-b + np.sqrt(disk)) / (2*a)
        x2 = (-b - np.sqrt(disk)) / (2*a)
        
        if abs(x1 - x2) > 0.01:
            ax2.plot([x1, x2], [ziel_2, ziel_2], 'go', markersize=10,
                    markeredgewidth=2, markeredgecolor='darkgreen')
            ax2.plot([x1, x1], [0, ziel_2], 'g--', alpha=0.5, linewidth=1)
            ax2.plot([x2, x2], [0, ziel_2], 'g--', alpha=0.5, linewidth=1)
        else:
            ax2.plot(x1, ziel_2, 'go', markersize=10,
                    markeredgewidth=2, markeredgecolor='darkgreen')
            ax2.plot([x1, x1], [0, ziel_2], 'g--', alpha=0.5, linewidth=1)
    
    ax2.set_xlabel('x', fontsize=12, fontweight='bold')
    ax2.set_ylabel('y', fontsize=12, fontweight='bold')
    ax2.set_title('Aufgabe 2: x² - 4x + 3 = 2', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.spines['left'].set_position('zero')     # y-Achse durch x=0
    ax2.spines['bottom'].set_position('zero')   # x-Achse durch y=0
    ax2.spines['right'].set_color('none')       # Rechten Rand ausblenden
    ax2.spines['top'].set_color('none')         # Oberen Rand ausblenden
    
    if disk >= 0:
        ax2.plot([x1, x2], [ziel_2, ziel_2], 'go', markersize=10,
                markeredgewidth=2, markeredgecolor='darkgreen')
        # Legende nur für Info
        if abs(x1 - x2) > 0.01:
            ax2.plot([], [], ' ', label=f'x₁≈{x2:.2f}, x₂≈{x1:.2f}')
        else:
            ax2.plot([], [], ' ', label=f'x≈{x1:.2f}')
    else:
        ax2.plot([], [], ' ', label='Keine Lösungen')

    ax2.legend(loc='upper right', fontsize=10)
    ax2.set_xlim(-2, 6)
    ax2.set_ylim(-2, 10)
    ax2.set_xticks(np.arange(-2, 7, 1))   # x-Achse: von -2 bis 6 in 1er-Schritten
    ax2.set_yticks(np.arange(-2, 11, 1))  # y-Achse: von -2 bis 10 in 1er-Schritten
    
    st.pyplot(fig2)
    plt.close()

   # Eingabefeld
    lösung2 = st.text_input(
        "Deine Lösung:",
        placeholder="z.B. x=3 oder x=5 oder 'nicht lösbar'", key="input3"
    )

    if st.button("Überprüfen", key="button3"):        
        # Mögliche richtige Antworten
        richtige_antworten = [
            "x=0,27 oder x=3,73",
            "x=0.27 oder x=3.73",
            "x = 0,27 oder x = 3,73",
            "x = 0.27 oder x = 3.73",
        ]
        
        if any(lösung2 == richtig for richtig in richtige_antworten):
            st.success("✅ Richtig! $x=0$,$27$ oder $x=3$,$73$ sind die Lösungen der Gleichung")
        else:
            st.error("❌ Nicht ganz. Tipp: Es gibt zwei Lösungen")

with col6:
    # Aufgabe 3
    st.markdown(f"$x² + 4x + 7 = 2$")

    ziel_3 = st.slider(
        "Rechte Seite der Gleichung (y-Wert):",
        min_value=-2.0,
        max_value=8.0,
        value=0.0,
        step=0.1,
        key="slider_3"
    )
    
    # Plot für Aufgabe 3
    x3 = np.linspace(-8, 4, 400)
    y3 = x3**2 + 4*x3 + 7
    
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.plot(x3, y3, 'b-', linewidth=2.5, label='f(x) = x² + 4x + 7')
    ax3.axhline(y=ziel_3, color='red', linestyle='--', linewidth=2, 
                label=f'y = {ziel_3}')
    
    # Schnittpunkte berechnen: x² + 4x + 7 = ziel_3
    # x² + 4x + (7 - ziel_3) = 0
    a, b, c = 1, 4, (7 - ziel_3)
    disk = b**2 - 4*a*c
    
    if disk >= 0:
        x1 = (-b + np.sqrt(disk)) / (2*a)
        x2 = (-b - np.sqrt(disk)) / (2*a)
        
        if abs(x1 - x2) > 0.01:
            ax3.plot([x1, x2], [ziel_3, ziel_3], 'go', markersize=10,
                    markeredgewidth=2, markeredgecolor='darkgreen')
            ax3.plot([x1, x1], [0, ziel_3], 'g--', alpha=0.5, linewidth=1)
            ax3.plot([x2, x2], [0, ziel_3], 'g--', alpha=0.5, linewidth=1)
        else:
            ax3.plot(x1, ziel_3, 'go', markersize=10,
                    markeredgewidth=2, markeredgecolor='darkgreen')
            ax3.plot([x1, x1], [0, ziel_3], 'g--', alpha=0.5, linewidth=1)
    
    ax3.set_xlabel('x', fontsize=12, fontweight='bold')
    ax3.set_ylabel('y', fontsize=12, fontweight='bold')
    ax3.set_title('Aufgabe 3: x² + 4x + 7 = 2', fontsize=13, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.spines['left'].set_position('zero')     # y-Achse durch x=0
    ax3.spines['bottom'].set_position('zero')   # x-Achse durch y=0
    ax3.spines['right'].set_color('none')       # Rechten Rand ausblenden
    ax3.spines['top'].set_color('none')         # Oberen Rand ausblenden
    
    if disk >= 0:
        ax3.plot([x1, x2], [ziel_3, ziel_3], 'go', markersize=10,
                markeredgewidth=2, markeredgecolor='darkgreen')
        # Legende nur für Info
        if abs(x1 - x2) > 0.01:
            ax3.plot([], [], ' ', label=f'x₁≈{x2:.2f}, x₂≈{x1:.2f}')
        else:
            ax3.plot([], [], ' ', label=f'x≈{x1:.2f}')
    else:
        ax3.plot([], [], ' ', label='Keine Lösungen')
    
    ax3.legend(loc='upper right', fontsize=10)
    ax3.set_xlim(-8, 4)
    ax3.set_ylim(-2, 8)
    ax3.set_xticks(np.arange(-6, 2, 1))   # x-Achse: von -2 bis 6 in 1er-Schritten
    ax3.set_yticks(np.arange(-2, 10, 1))  # y-Achse: von -2 bis 10 in 1er-Schritten
    
    st.pyplot(fig3)
    plt.close()

    # Eingabefeld
    lösung3 = st.text_input(
        "Deine Lösung:",
        placeholder="z.B. x=3 oder x=5 oder 'nicht lösbar'", key="input4"
    )

    if st.button("Überprüfen", key="button4"):        
        # Mögliche richtige Antworten
        richtige_antworten = [
            "nicht lösbar",
            "'nicht lösbar'"
        ]
        
        if any(lösung3 == richtig for richtig in richtige_antworten):
            st.success("✅ Richtig! Diese Gleichung ist nicht lösbar.")
        else:
            st.error("❌ Nicht ganz. Tipp: Wie viele Lösungen gibt es?")

st.markdown("""
#### Schlussfolgerung: 
            
Schauen wir uns unsere drei Beispiele an: Dort siehst du, dass eine quadratische Gleichung unterschiedlich viele Lösungen haben kann.
            
Es gibt genau drei Möglichkeiten:
            
**1. Keine Lösung**
            
Die Parabel liegt komplett über oder komplett unter der gesuchten Höhe (dem Funktionswert).
→ Sie schneidet die waagerechte Linie nirgendwo.
            
**2. Genau eine Lösung**
            
Der Scheitelpunkt der Parabel liegt genau auf der Höhe des Funktionswerts
→ Parabel und Linie berühren sich in einem Punkt.
            
**3. Zwei Lösungen**
            
Die Parabel schneidet die Linie auf Höhe des Funktionswertes in zwei Punkten.
→ Es gibt zwei x-Werte, die den selbeb Funktionswert haben.

Merke:
Eine quadratische Gleichung kann also 0, 1 oder 2 Lösungen haben.
""")

st.markdown("---")

st.header("Übungen: Graphisches Lösen quadratischer Gleichungen")

st.markdown(r"""
            Gib die quadratischen Gleichungen ein und löse sie graphisch.

            a) $x^2-5x+6=0$

            b) $x^2-3x=4$

            c) $x^2-4x+7=3$

            d) $x^2+4x+4=-1$

            e) $x^2-x-2=0$
            """)


col1, col2, col3= st.columns([1,2,1])

with col2: 
    # Eingabefelder für die Koeffizienten
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        a_user = st.number_input("Koeffizient a:", value=1, step=1, key="a_user")
    with col2:
        b_user = st.number_input("Koeffizient b:", value=1, step=1, key="b_user")
    with col3:
        c_user = st.number_input("Koeffizient c:", value=1, step=1, key="c_user")
    with col4:
        ziel_user_init = st.number_input("Rechte Seite:", value=1, step=1, key="ziel_init")

    # Zeige die eingegebene Gleichung an
    st.markdown(f"**Deine Gleichung:** ${a_user}x² {b_user:+}x {c_user:+} = {ziel_user_init}$")

    st.markdown("<br>", unsafe_allow_html=True)

    # Slider für grafisches Lösen
    ziel_user = st.slider(
        "Rechte Seite der Gleichung (y-Wert):",
        min_value=-10,
        max_value=10,
        value=ziel_user_init,
        step=1,
        key="slider_user"
    )

    # Bestimme x-Bereich automatisch (Scheitelpunkt ± Bereich)
    x_scheitel = -b_user / (2 * a_user)
    x_min = x_scheitel - 3
    x_max = x_scheitel + 3

    # Plot
    x = np.linspace(x_min, x_max, 400)
    y_user = a_user * x**2 + b_user * x + c_user

    fig_user, ax_user = plt.subplots(figsize=(8, 5))
    ax_user.plot(x, y_user, 'b-', linewidth=2.5, 
                label=f'f(x) = {a_user}x² {b_user:+}x {c_user:+}')
    ax_user.axhline(y=ziel_user, color='red', linestyle='--', linewidth=2, 
                    label=f'y = {ziel_user}')

    # Schnittpunkte berechnen
    c_neu = c_user - ziel_user
    disk = b_user**2 - 4*a_user*c_neu

    if disk >= 0:
        x1 = (-b_user + np.sqrt(disk)) / (2*a_user)
        x2 = (-b_user - np.sqrt(disk)) / (2*a_user)
        
        if abs(x1 - x2) > 0.01:
            ax_user.plot([x1, x2], [ziel_user, ziel_user], 'go', markersize=10,
                        markeredgewidth=2, markeredgecolor='darkgreen')
            ax_user.plot([x1, x1], [0, ziel_user], 'g--', alpha=0.5, linewidth=1)
            ax_user.plot([x2, x2], [0, ziel_user], 'g--', alpha=0.5, linewidth=1)
            ax_user.plot([], [], ' ', label=f'x₁≈{x2:.2f}, x₂≈{x1:.2f}')
        else:
            ax_user.plot(x1, ziel_user, 'go', markersize=10,
                        markeredgewidth=2, markeredgecolor='darkgreen')
            ax_user.plot([x1, x1], [0, ziel_user], 'g--', alpha=0.5, linewidth=1)
            ax_user.plot([], [], ' ', label=f'x≈{x1:.2f}')
    else:
        ax_user.plot([], [], ' ', label='Keine Lösungen')

    ax_user.set_xlabel('x', fontsize=12, fontweight='bold')
    ax_user.set_ylabel('y', fontsize=12, fontweight='bold')
    ax_user.set_title('Grafische Lösung deiner Gleichung', fontsize=13, fontweight='bold')
    ax_user.grid(True, alpha=0.3)

    # Koordinatensystem durch Ursprung
    ax_user.spines['left'].set_position('zero')
    ax_user.spines['bottom'].set_position('zero')
    ax_user.spines['right'].set_color('none')
    ax_user.spines['top'].set_color('none')

    ax_user.legend(loc='upper right', fontsize=10)

    # Berechne Scheitelwert
    y_scheitel = a_user * x_scheitel**2 + b_user * x_scheitel + c_user

    # Setze Grenzen relativ zum Scheitel
    y_min = min(y_scheitel - 5, ziel_user - 2)
    y_max = max(y_scheitel + 5, ziel_user + 2)

    # Automatische Achsenbereiche
    #y_min = min(y_user.min(), ziel_user) - 1
    #y_max = max(y_user.max(), ziel_user) + 1
    ax_user.set_xlim(x_min, x_max)
    ax_user.set_ylim(y_min, y_max)

    st.pyplot(fig_user)
    plt.close()
    