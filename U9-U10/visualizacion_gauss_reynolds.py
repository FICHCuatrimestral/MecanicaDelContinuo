"""
Visualizacion Unidad 9/10 — Teorema de Gauss y transporte de Reynolds
=======================================================================
Dos ideas puramente geometricas que sostienen TODAS las demostraciones
del bloque de ecuaciones de campo (seccion 1.1 y 1.3 de la guia):

Panel A — la demostracion de Gauss "rebanada en tubos" (1.1): un volumen
2D generico (una mancha) se corta en tiras verticales paralelas a x1.
Cada tira entra por la izquierda (normal con componente x1<0) y sale por
la derecha (normal con componente x1>0). El teorema fundamental del
calculo a lo largo de cada tira, sumado sobre todas las tiras, es
exactamente la demostracion. Se dibujan unas pocas tiras con sus
normales de entrada/salida para que la mecanica quede a la vista.

Panel B — el transporte de Reynolds (1.3): el MISMO volumen material en
dos instantes, t y t+dt, bajo un campo de velocidad que lo expande y
distorsiona. La cascara barrida (sombreada) es exactamente el termino
extra que hace que D/Dt no conmute con la integral: en cada punto del
borde, el volumen barrido es (v·n) dt dS -- por eso aparece la normal
multiplicada por la velocidad, no la velocidad sola.

Corre con: python visualizacion_gauss_reynolds.py
"""

import numpy as np
import matplotlib.pyplot as plt


def blob(theta, coefs, r0=1.0):
    """Curva cerrada 'organica' via suma de armonicos, para no usar un circulo perfecto."""
    r = r0 * np.ones_like(theta)
    for k, (a, b, n) in enumerate(coefs):
        r = r + a * np.cos(n * theta) + b * np.sin(n * theta)
    return r


COEFS = [(0.18, 0.05, 2), (0.08, -0.10, 3), (-0.05, 0.06, 5)]


def figura_gauss_reynolds():
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(14, 6.4))

    # ------------------------------------------------------------
    # PANEL A: Gauss, rebanado en tubos paralelos a x1
    # ------------------------------------------------------------
    theta = np.linspace(0, 2 * np.pi, 600)
    r = blob(theta, COEFS)
    X = r * np.cos(theta)
    Y = r * np.sin(theta)

    axA.plot(X, Y, color="steelblue", lw=2.2)
    axA.fill(X, Y, color="steelblue", alpha=0.08)

    x_tubos = np.linspace(-0.85, 0.85, 7)
    for xt in x_tubos:
        # intersecciones tira vertical x=xt con el contorno (dos cruces: entrada/salida)
        cruces_y = []
        for i in range(len(X) - 1):
            x0, x1_ = X[i], X[i + 1]
            if (x0 - xt) * (x1_ - xt) < 0:
                f = (xt - x0) / (x1_ - x0)
                y_int = Y[i] + f * (Y[i + 1] - Y[i])
                cruces_y.append(y_int)
        if len(cruces_y) >= 2:
            y_lo, y_hi = min(cruces_y), max(cruces_y)
            axA.plot([xt, xt], [y_lo, y_hi], color="0.55", lw=1.0, ls=":")
            axA.annotate("", xy=(xt - 0.13, y_lo), xytext=(xt, y_lo),
                         arrowprops=dict(arrowstyle="-|>", color="firebrick", lw=1.6))
            axA.annotate("", xy=(xt + 0.13, y_hi), xytext=(xt, y_hi),
                         arrowprops=dict(arrowstyle="-|>", color="seagreen", lw=1.6))

    axA.plot([], [], color="firebrick", lw=1.6, marker=">", label=r"entrada: $\nu_1<0$")
    axA.plot([], [], color="seagreen", lw=1.6, marker=">", label=r"salida: $\nu_1>0$")
    axA.set_aspect("equal")
    axA.set_title("Gauss: rebanar en tubos paralelos a $x_1$ (sección 1.1)\n"
                   r"cada tira: teor. fundamental del cálculo en $x_1$ $\Rightarrow$ $\int_V\partial_1 A\,dV=\int_S A\nu_1\,dS$",
                   fontsize=10.5)
    axA.legend(fontsize=9, loc="lower center")
    axA.set_xlabel("$x_1$")
    axA.set_ylabel("$x_2$")
    axA.grid(alpha=0.2)

    # ------------------------------------------------------------
    # PANEL B: Reynolds, cascara barrida entre t y t+dt
    # ------------------------------------------------------------
    def campo_v(x, y):
        # expansion (divergencia>0) + un poco de corte, para que la cascara no sea uniforme
        vx = 0.35 * x + 0.10 * y
        vy = 0.25 * y
        return vx, vy

    theta2 = np.linspace(0, 2 * np.pi, 300)
    r2 = blob(theta2, COEFS, r0=0.8)
    X0 = r2 * np.cos(theta2)
    Y0 = r2 * np.sin(theta2)
    VX, VY = campo_v(X0, Y0)
    dt = 0.55
    X1 = X0 + VX * dt
    Y1 = Y0 + VY * dt

    axB.fill(np.r_[X1, X0[::-1]], np.r_[Y1, Y0[::-1]], color="darkorange", alpha=0.30,
              label=r"cáscara barrida $\approx (\mathbf{v}\cdot\mathbf{n})\,dt\,dS$")
    axB.plot(X0, Y0, color="steelblue", lw=2.2, label="$V(t)$")
    axB.plot(X1, Y1, color="firebrick", lw=2.0, ls="--", label="$V(t+dt)$")

    idx = np.arange(0, len(theta2), 24)
    for i in idx:
        axB.annotate("", xy=(X1[i], Y1[i]), xytext=(X0[i], Y0[i]),
                     arrowprops=dict(arrowstyle="-|>", color="0.25", lw=1.1))

    axB.set_aspect("equal")
    axB.set_title(r"Reynolds: cada $dS$ barre $(\mathbf{v}\cdot\mathbf{n})\,dt$ (sección 1.3)"
                 "\nla cáscara sombreada, integrada, es el término extra que $D/Dt$ agrega a $\\int_V$",
                 fontsize=10.5)
    axB.legend(fontsize=8.5, loc="lower center")
    axB.set_xlabel("$x_1$")
    axB.set_ylabel("$x_2$")
    axB.grid(alpha=0.2)

    fig.suptitle("Las dos herramientas geométricas detrás de TODAS las demostraciones del bloque", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("fig_gauss_reynolds.png", dpi=130, bbox_inches="tight")
    print("  -> fig_gauss_reynolds.png")


if __name__ == "__main__":
    print("Generando figura de Gauss / Reynolds (Unidad 9-10)...")
    figura_gauss_reynolds()
    print("Listo.")
