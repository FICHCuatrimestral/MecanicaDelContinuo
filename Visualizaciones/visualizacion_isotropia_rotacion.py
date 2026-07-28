"""
Visualizacion Unidad 8 — Isotropia: el test de rotacion en accion
=====================================================================
La seccion 8.1 prueba que "vector isotropo -> v=0" y "tensor rango 2
isotropo -> alpha*delta_ij" usando solo un PUÑADO de rotaciones astutas
(180 y 90 grados). Esta figura hace el argumento completo y continuo:
en vez de 2 o 3 angulos, se aplican TODOS los angulos theta en [0,2pi)
y se grafica como responde cada objeto. Si es realmente isotropo, la
curva tiene que ser PLANA (invariante); si no, oscila.

Panel A (rango 1, vectores): se toma un vector generico v y se grafica
su punta rotada R(theta)v para todo theta -> barre un circulo completo
(cambia). Solo v=0 queda quieto en el origen para todo theta: coincide
con el "unico vector isotropo es el nulo" de 8.1.

Panel B (rango 2, tensores): se toma un tensor A generico (con parte
simetrica y antisimetrica) y se calcula la transformacion completa
A'(theta) = R(theta) A R(theta)^T, graficando sus 4 componentes contra
theta. Se comparan con un tensor isotropo alpha*delta: sus componentes
son CONSTANTES (linea plana) para cualquier theta -- la firma exacta
de "A_ij isotropo <=> alpha*delta_ij" (boxed en 8.1).

Corre con: python visualizacion_isotropia_rotacion.py
"""

import numpy as np
import matplotlib.pyplot as plt


def rot(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def figura_test_isotropia():
    thetas = np.linspace(0, 2 * np.pi, 400)

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13.5, 6))

    # ------------------------------------------------------------
    # PANEL A: vectores. v generico vs v=0
    # ------------------------------------------------------------
    v = np.array([1.3, 0.6])
    puntos = np.array([rot(th) @ v for th in thetas])
    ax0.plot(puntos[:, 0], puntos[:, 1], color="firebrick", lw=2.2,
             label=r"$v\neq 0$: la punta de $R(\theta)v$ barre un círculo completo")
    ax0.scatter([v[0]], [v[1]], color="firebrick", zorder=5, s=40)
    ax0.annotate(r"$v$ original", v, textcoords="offset points", xytext=(8, 6), fontsize=9)
    ax0.scatter([0], [0], color="seagreen", zorder=5, s=90, marker="*",
                label=r"$v=0$: único punto fijo para *todo* $\theta$ (único vector isótropo)")
    ax0.set_aspect("equal")
    ax0.set_xlim(-1.8, 1.8)
    ax0.set_ylim(-1.8, 1.8)
    ax0.grid(alpha=0.25)
    ax0.legend(fontsize=8.3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax0.set_title("Rango 1 — un vector genérico CAMBIA al rotar\n"
                   r"$\Rightarrow$ ninguna dirección puede ser 'la misma en todas direcciones'",
                   fontsize=10.5)

    # ------------------------------------------------------------
    # PANEL B: tensores rango 2. A generico vs alpha*delta
    # ------------------------------------------------------------
    A = np.array([[3.0, 1.0],
                  [-0.5, 1.0]])          # generico: ni simetrico puro ni isotropo
    alpha = 2.0
    A_iso = alpha * np.eye(2)

    comp_labels = [("A11", 0, 0, "steelblue"), ("A22", 1, 1, "darkorange"),
                   ("A12", 0, 1, "seagreen"), ("A21", 1, 0, "purple")]

    for nombre, i, j, color in comp_labels:
        serie = np.array([(rot(th) @ A @ rot(th).T)[i, j] for th in thetas])
        ax1.plot(thetas, serie, color=color, lw=1.8, label=f"${nombre}$ genérico (oscila)")

    for nombre, i, j, color in comp_labels:
        serie_iso = np.array([(rot(th) @ A_iso @ rot(th).T)[i, j] for th in thetas])
        ls = "--" if nombre in ("A12", "A21") else ":"
        ax1.plot(thetas, serie_iso, color=color, lw=2.6, ls=ls, alpha=0.9)

    ax1.axhline(alpha, color="0.15", lw=1.2, ls="--",
                label=r"$\alpha\delta_{ij}$: TODAS las componentes constantes (plano)")
    ax1.set_xlabel(r"$\theta$ (ángulo de rotación del marco)")
    ax1.set_ylabel("componente transformada")
    ax1.set_xticks(np.arange(0, 2 * np.pi + 0.01, np.pi / 2))
    ax1.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
    ax1.grid(alpha=0.25)
    ax1.legend(fontsize=7.6, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)
    ax1.set_title("Rango 2 — componentes de $A'(\\theta)=R(\\theta)AR(\\theta)^T$\n"
                   r"genérico oscila; $\alpha\delta_{ij}$ es invariante $\Leftrightarrow$ único isótropo",
                   fontsize=10.5)

    fig.suptitle("El test de rotación de la sección 8.1, para TODO ángulo (no solo 180°/90°)",
                 fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("fig_test_isotropia_rotacion.png", dpi=130, bbox_inches="tight")
    print("  -> fig_test_isotropia_rotacion.png")


if __name__ == "__main__":
    print("Generando figura de Unidad 8 (isotropía)...")
    figura_test_isotropia()
    print("Listo.")
