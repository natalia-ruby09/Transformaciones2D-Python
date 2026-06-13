import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# ==========================
# CUADRADO ORIGINAL
# ==========================

cuadrado_original = np.array([
    [0, 0],
    [4, 0],
    [4, 4],
    [0, 4]
])

# ==========================
# FUNCION ESCALADO
# ==========================

def escalar(figura, factor):
    return figura * factor

# ==========================
# DIBUJAR
# ==========================

def dibujar(figura, titulo, formula):

    ax.clear()

    cuadrado = Polygon(
        figura,
        closed=True,
        color="limegreen"
    )

    ax.add_patch(cuadrado)

    ax.set_title(titulo, fontsize=14)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    ax.set_aspect('equal')

    ax.grid(True)

    ax.text(
        -9,
        8,
        formula,
        fontsize=12,
        bbox=dict(facecolor="lightyellow")
    )

    ax.text(
        -9,
        5,
        "1 = Original\n2 = Ampliación\n3 = Reducción",
        fontsize=11,
        bbox=dict(facecolor="lightblue")
    )

    fig.canvas.draw_idle()

# ==========================
# EVENTOS
# ==========================

def tecla(event):

    if event.key == "1":

        dibujar(
            cuadrado_original,
            "Figura Original",
            "Sin transformación"
        )

    elif event.key == "2":

        figura = escalar(
            cuadrado_original,
            2
        )

        dibujar(
            figura,
            "Ampliación (Factor = 2)",
            "X' = X × 2\nY' = Y × 2"
        )

    elif event.key == "3":

        figura = escalar(
            cuadrado_original,
            0.5
        )

        dibujar(
            figura,
            "Reducción (Factor = 0.5)",
            "X' = X × 0.5\nY' = Y × 0.5"
        )

# ==========================
# VENTANA
# ==========================

fig, ax = plt.subplots(figsize=(7,7))

fig.canvas.mpl_connect(
    'key_press_event',
    tecla
)

dibujar(
    cuadrado_original,
    "Figura Original",
    "Sin transformación"
)

plt.show()
