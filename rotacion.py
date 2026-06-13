import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# ==========================================
# FLECHA ORIGINAL
# ==========================================

flecha_original = np.array([
    [0, 4],    # punta
    [2, 1],
    [1, 1],
    [1, -4],
    [-1, -4],
    [-1, 1],
    [-2, 1]
])

# ==========================================
# FUNCION ROTACION
# ==========================================

def rotar(figura, angulo):

    rad = np.radians(angulo)

    matriz = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad),  np.cos(rad)]
    ])

    return figura @ matriz.T

# ==========================================
# DIBUJAR
# ==========================================

def dibujar(figura, titulo, formula):

    ax.clear()

    flecha = Polygon(
        figura,
        closed=True,
        color="orange"
    )

    ax.add_patch(flecha)

    ax.set_title(titulo, fontsize=14)

    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)

    ax.set_aspect('equal')

    ax.grid(True)

    # Fórmula
    ax.text(
        -7,
        6,
        formula,
        fontsize=10,
        bbox=dict(facecolor="lightyellow")
    )

    # Ayuda
    ax.text(
        -7,
        -7,
        "1 = Original\n2 = Rotar 90°\n3 = Rotar 180°\n4 = Rotar 270°",
        fontsize=10,
        bbox=dict(facecolor="lightblue")
    )

    fig.canvas.draw_idle()

# ==========================================
# TECLAS
# ==========================================

def tecla(event):

    if event.key == "1":

        dibujar(
            flecha_original,
            "Figura Original",
            "Sin transformación"
        )

    elif event.key == "2":

        dibujar(
            rotar(flecha_original, 90),
            "Rotación 90°",
            "θ = 90°"
        )

    elif event.key == "3":

        dibujar(
            rotar(flecha_original, 180),
            "Rotación 180°",
            "θ = 180°"
        )

    elif event.key == "4":

        dibujar(
            rotar(flecha_original, 270),
            "Rotación 270°",
            "θ = 270°"
        )

# ==========================================
# VENTANA
# ==========================================

fig, ax = plt.subplots(figsize=(7,7))

fig.canvas.mpl_connect(
    'key_press_event',
    tecla
)

dibujar(
    flecha_original,
    "Figura Original",
    "Sin transformación"
)

plt.show()
