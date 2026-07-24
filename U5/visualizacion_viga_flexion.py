"""
Visualizacion 3D: flexion pura de una viga rectangular (Unidad 5 + Poisson de U7)
==================================================================================
Por que un ejemplo 3D aca (y no solo 2D): la teoria de vigas de 2do anio
("secciones planas permanecen planas") es un resultado 2D (plano x-y). Pero
el efecto Poisson (seccion 7.3) actua en TODAS las direcciones transversales
a la vez, y eso genera un efecto que NO EXISTE en una teoria estrictamente 2D:
la curvatura anticlastica (la seccion transversal se alabea en silla de montar).
Verlo en 3D es la unica manera de que el efecto Poisson dentro de una viga se
haga visible como geometria y no solo como formula.

Campo de desplazamientos de flexion pura (solucion de Saint-Venant, con Poisson):
    u_x = -kappa * x * y
    u_y =  (kappa/2) * ( x^2 + nu*y^2 - nu*z^2 )
    u_z = -kappa * nu * y * z
con kappa = 1/R (curvatura impuesta) y nu = coeficiente de Poisson.

Deformaciones resultantes (chequealo derivando):
    eps_xx = -kappa*y      (fibra longitudinal: tension si y<0, compresion si y>0)
    eps_yy =  kappa*nu*y
    eps_zz = -kappa*nu*y
    resto = 0

Corre con: python visualizacion_viga_flexion.py
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

KAPPA = 0.12   # curvatura impuesta (1/R), exagerada para que se vea
NU = 0.3       # coeficiente de Poisson (tipico de un metal)
L, H, D = 4.0, 1.0, 0.8  # largo, alto, profundidad de la viga


def u_field(x, y, z):
    ux = -KAPPA * x * y
    uy = 0.5 * KAPPA * (x**2 + NU * y**2 - NU * z**2)
    uz = -KAPPA * NU * y * z
    return ux, uy, uz


def figura_viga_flexion():
    fig = plt.figure(figsize=(14, 6.2))

    # ------------------------------------------------------------------
    # PANEL IZQUIERDO: cara superior (y = +H/2) antes y despues -> silla
    # ------------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    xs = np.linspace(-L / 2, L / 2, 40)
    zs = np.linspace(-D / 2, D / 2, 20)
    X, Z = np.meshgrid(xs, zs)
    Y0 = np.full_like(X, H / 2)
    _, uy, _ = u_field(X, Y0, Z)
    Ydef = Y0 + uy

    # La flexion principal (~kappa*x^2/2) es ~100x mas grande que el alabeo
    # transversal (~kappa*nu*z^2/2): si se grafica Ydef tal cual, el alabeo
    # queda invisible. Por eso restamos la tendencia en x (perfil a z=0) y
    # mostramos la ALTURA RELATIVA AL CENTRO: lo que queda es puramente el
    # efecto Poisson transversal, aislado.
    baseline_x = 0.5 * KAPPA * X**2
    Yrel = Ydef - Y0 - baseline_x  # = -0.5*kappa*nu*(z^2 - (D/2)^2), func. solo de z

    surf = ax1.plot_surface(X, Z, Yrel * 1000, cmap="coolwarm", linewidth=0,
                             antialiased=True, alpha=0.95)
    ax1.set_xlabel("x (a lo largo)")
    ax1.set_ylabel("z (ancho)")
    ax1.set_zlabel("altura rel. al centro\n(× $10^{-3}$)")
    ax1.set_title("Cara superior, altura relativa al eje central de la viga\n"
                   "(se restó la flexión principal en x para AISLAR el alabeo)\n"
                   "→ hundimiento parabólico en z puro: la firma del efecto Poisson",
                   fontsize=10.5)
    ax1.view_init(elev=24, azim=-50)
    ax1.set_yticks(np.linspace(-D / 2, D / 2, 5))
    ax1.tick_params(labelsize=8)

    # ------------------------------------------------------------------
    # PANEL DERECHO: corte longitudinal z=0, fibras a distintas alturas y
    # ------------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2)
    x_line = np.linspace(-L / 2, L / 2, 200)
    y_levels = np.linspace(-H / 2, H / 2, 5)
    cmap = plt.get_cmap("RdBu_r")

    R = 1.0 / KAPPA  # centro de curvatura queda MUY lejos (R=8.3 vs viga de alto 1):
    # no lo ploteamos (aplastaría el resto contra el eje), solo lo citamos en el título.

    for y0 in y_levels:
        ux, uy, _ = u_field(x_line, y0, 0.0)
        xdef = x_line + ux
        ydef = y0 + uy
        eps_xx = -KAPPA * y0
        color = cmap(0.5 - eps_xx / (2 * KAPPA * H / 2) * 0.5)
        lbl = None
        if abs(y0) < 1e-9:
            lbl = "y=0: fibra neutra (no cambia de longitud)"
            ax2.plot(xdef, ydef, color="0.15", lw=2.2, ls="--", label=lbl)
        else:
            tag = "compresión" if eps_xx < 0 else "tensión"
            ax2.plot(xdef, ydef, color=color, lw=2.2,
                     label=f"y={y0:+.2f}  ($\\varepsilon_{{xx}}$={eps_xx:+.3f}, {tag})")
        ax2.plot(x_line, np.full_like(x_line, y0), color="0.8", lw=1, ls=":")

    # un par de secciones transversales (antes/despues) para mostrar que
    # "planas y perpendiculares a la fibra neutra" se mantiene
    for x0 in (-1.4, 0.0, 1.4):
        y_sec = np.linspace(-H / 2, H / 2, 15)
        ux, uy, _ = u_field(np.full_like(y_sec, x0), y_sec, 0.0)
        ax2.plot(x0 + ux, y_sec + uy, color="seagreen", lw=1.6, alpha=0.8)

    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_xlim(-L / 2 - 0.15, L / 2 + 0.15)
    ax2.set_ylim(-0.85, 1.0)
    ax2.set_title(f"Corte longitudinal (z=0): fibras curvándose alrededor de un\n"
                 f"centro común a distancia R=1/κ={R:.1f} — secciones (verde) siguen planas",
                 fontsize=11)
    ax2.set_aspect("equal")
    ax2.legend(fontsize=7.5, loc="upper center", ncol=1)
    ax2.grid(alpha=0.25)

    fig.suptitle(r"Flexión pura de una viga — $\kappa=$" + f"{KAPPA}"
                 r",  $\nu=$" + f"{NU}"
                 r"   ($\varepsilon_{xx}=-\kappa y,\ \varepsilon_{yy}=\varepsilon_{zz}=-\nu\,\varepsilon_{xx}$)",
                 fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("fig_viga_flexion.png", dpi=130, bbox_inches="tight")
    print("  -> fig_viga_flexion.png")


if __name__ == "__main__":
    print("Generando figura de flexión de viga (curvatura anticlástica)...")
    figura_viga_flexion()
    print("Listo.")
