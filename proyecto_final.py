import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import numpy as np

# ==========================================
# FIGURAS ORIGINALES
# ==========================================

cohete_original = np.array([
    [0, 8],
    [2, 5],
    [2, -5],
    [4, -7],
    [2, -7],
    [2, -10],
    [-2, -10],
    [-2, -7],
    [-4, -7],
    [-2, -5],
    [-2, 5]
])

cabina_original = np.array([0, 1])

fuego_original = np.array([
    [-1, -10],
    [0, -14],
    [1, -10]
])

titulo_actual = "Nave Espacial Original"
formula_actual = "Figura Original"

# ==========================================
# TRANSFORMACIONES
# ==========================================

def trasladar(figura, dx, dy):
    return figura + np.array([dx, dy])

def escalar(figura, factor):
    return figura * factor

def rotar(figura, angulo):

    rad = np.radians(angulo)

    matriz = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad),  np.cos(rad)]
    ])

    return figura @ matriz.T

# ==========================================
# DIBUJAR ESCENA
# ==========================================

def dibujar(cohete, cabina, fuego, titulo, formula):

    ax.clear()

    ax.set_facecolor("black")

    # ==================================
    # ESTRELLAS
    # ==================================

    np.random.seed(1)

    estrellas_x = np.random.uniform(-20, 20, 50)
    estrellas_y = np.random.uniform(-20, 20, 50)

    ax.scatter(
        estrellas_x,
        estrellas_y,
        s=20,
        color="yellow"
    )

    # ==================================
    # PLANETA
    # ==================================

    planeta = Circle(
        (14, -14),
        3,
        color="deepskyblue"
    )

    continente1 = Circle(
        (13, -13),
        0.8,
        color="green"
    )

    continente2 = Circle(
        (15, -15),
        0.7,
        color="green"
    )

    ax.add_patch(planeta)
    ax.add_patch(continente1)
    ax.add_patch(continente2)

    # ==================================
    # FUEGO
    # ==================================

    fuego_patch = Polygon(
        fuego,
        closed=True,
        color="orange"
    )

    ax.add_patch(fuego_patch)

    # ==================================
    # COHETE
    # ==================================

    cuerpo = Polygon(
        cohete,
        closed=True,
        color="silver"
    )

    ax.add_patch(cuerpo)

    # ==================================
    # CABINA
    # ==================================

    cabina_patch = Circle(
        (cabina[0], cabina[1]),
        1,
        color="deepskyblue"
    )

    ax.add_patch(cabina_patch)

    # ==================================
    # TITULO
    # ==================================

    ax.set_title(
        titulo,
        fontsize=16,
        color="white"
    )

    # ==================================
    # FORMULA
    # ==================================

    ax.text(
        -19,
        -18,
        formula,
        color="cyan",
        fontsize=11,
        bbox=dict(facecolor="black")
    )

    # ==================================
    # PANEL DE AYUDA
    # ==================================

    texto = (
        "CONTROLES\n\n"
        "1 = Original\n"
        "2 = Traslacion\n"
        "3 = Ampliacion\n"
        "4 = Reduccion\n"
        "5 = Rotacion 90°\n"
        "6 = Rotacion 180°\n"
        "7 = Rotacion 270°\n"
        "ESC = Salir"
    )

    ax.text(
        11,
        11,
        texto,
        color="white",
        fontsize=10,
        bbox=dict(facecolor="black")
    )

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    ax.set_aspect('equal')

    ax.grid(color="gray")

    fig.canvas.draw_idle()

# ==========================================
# TECLAS
# ==========================================

def tecla(event):

    if event.key == "1":

        dibujar(
            cohete_original,
            cabina_original,
            fuego_original,
            "Nave Espacial Original",
            "Figura Original"
        )

    elif event.key == "2":

        dibujar(
            trasladar(cohete_original, 6, 4),
            trasladar(cabina_original, 6, 4),
            trasladar(fuego_original, 6, 4),
            "Traslacion",
            "X' = X + dx    Y' = Y + dy"
        )

    elif event.key == "3":

        dibujar(
            escalar(cohete_original, 1.8),
            escalar(cabina_original, 1.8),
            escalar(fuego_original, 1.8),
            "Ampliacion",
            "X' = X * s    Y' = Y * s"
        )

    elif event.key == "4":

        dibujar(
            escalar(cohete_original, 0.5),
            escalar(cabina_original, 0.5),
            escalar(fuego_original, 0.5),
            "Reduccion",
            "X' = X * 0.5    Y' = Y * 0.5"
        )

    elif event.key == "5":

        dibujar(
            rotar(cohete_original, 90),
            rotar(cabina_original, 90),
            rotar(fuego_original, 90),
            "Rotacion 90°",
            "θ = 90°"
        )

    elif event.key == "6":

        dibujar(
            rotar(cohete_original, 180),
            rotar(cabina_original, 180),
            rotar(fuego_original, 180),
            "Rotacion 180°",
            "θ = 180°"
        )

    elif event.key == "7":

        dibujar(
            rotar(cohete_original, 270),
            rotar(cabina_original, 270),
            rotar(fuego_original, 270),
            "Rotacion 270°",
            "θ = 270°"
        )

    elif event.key == "escape":

        plt.close()

# ==========================================
# VENTANA
# ==========================================

fig, ax = plt.subplots(figsize=(10, 8))

fig.canvas.mpl_connect(
    'key_press_event',
    tecla
)

dibujar(
    cohete_original,
    cabina_original,
    fuego_original,
    "Nave Espacial Original",
    "Figura Original"
)

plt.show()
