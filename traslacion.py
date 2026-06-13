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
# FUNCION DE TRASLACION
# ==========================

def trasladar(figura, dx, dy):
    return figura + np.array([dx, dy])

# ==========================
# DIBUJAR
# ==========================

def dibujar(figura, titulo):

    ax.clear()

    cuadrado = Polygon(
        figura,
        closed=True,
        color="deepskyblue"
    )

    ax.add_patch(cuadrado)

    ax.set_title(titulo)

    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)

    ax.set_aspect('equal')

    ax.grid(True)

    # Fórmula en pantalla
    ax.text(
        -1,
        10,
        "X' = X + dx\nY' = Y + dy",
        fontsize=12,
        bbox=dict(facecolor="lightyellow")
    )

    fig.canvas.draw_idle()

# ==========================
# TECLAS
# ==========================

def tecla(event):

    if event.key == "1":

        dibujar(
            cuadrado_original,
            "Cuadrado Original"
        )

    elif event.key == "2":

        cuadrado_trasladado = trasladar(
            cuadrado_original,
            5,   # dx
            3    # dy
        )

        dibujar(
            cuadrado_trasladado,
            "Traslacion (dx=5 , dy=3)"
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
    "Cuadrado Original"
)

plt.show()
