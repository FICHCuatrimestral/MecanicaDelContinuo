"""
Visualizacion Unidad 9/10 — Observador fijo vs. observador que viaja
con la particula (parcial 2023-1, tipo T2 de la guia)
=======================================================================
El campo de velocidad euleriano v=(0,z,y) (estacionario: no depende de
t) sale de derivar el mapeo
    y(Y,Z,t) = 0.5[(Y+Z)e^t + (Y-Z)e^-t]
    z(Y,Z,t) = 0.5[(Y+Z)e^t - (Y-Z)e^-t]
Es un flujo tipo "silla": las particulas con Y=Z se quedan para siempre
sobre la diagonal y=z y se alejan del origen exponencialmente.

La trampa conceptual del ejercicio: la aceleracion "vista por un
observador fijo en (1,1,1)" (Dv/Dt = v.grad(v) evaluado en ese punto,
constante en el tiempo porque el campo es estacionario) NO es la misma
cantidad que "la aceleracion de la particula que en t=0 estaba en
(1,1,1)" (que crece sin limite, e^t). Coinciden solo en t=0 -- el
instante en que ambas nociones describen literalmente a la misma
particula en el mismo lugar.

Corre con: python visualizacion_derivada_material_2023_1.py
"""

import numpy as np
import matplotlib.pyplot as plt


def figura_observador_fijo_vs_viajero():
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 6))

    # ------------------------------------------------------------
    # PANEL A: campo de velocidad v=(z,y) en el plano (y,z) + trayectoria
    # ------------------------------------------------------------
    yy, zz = np.meshgrid(np.linspace(-2.5, 2.5, 22), np.linspace(-2.5, 2.5, 22))
    Vy, Vz = zz, yy  # v_y = z, v_z = y
    speed = np.hypot(Vy, Vz)
    ax0.streamplot(yy, zz, Vy, Vz, color="0.75", density=1.1, linewidth=0.8, arrowsize=0.9)

    # trayectoria de la particula Y=Z=1: y(t)=z(t)=e^t (sobre la diagonal)
    t_path = np.linspace(-0.7, 0.9, 100)
    diag = np.exp(t_path)
    ax0.plot(diag, diag, color="firebrick", lw=2.6,
             label=r"trayectoria de la partícula $Y{=}Z{=}1$: $y(t)=z(t)=e^t$")
    ax0.plot(-diag, -diag, color="firebrick", lw=1.3, ls=":", alpha=0.6)

    ax0.scatter([1], [1], color="black", zorder=5, s=70, marker="*",
                label=r"punto fijo de observación $(y,z)=(1,1)$")
    ax0.set_xlim(-2.5, 2.5)
    ax0.set_ylim(-2.5, 2.5)
    ax0.set_aspect("equal")
    ax0.set_xlabel("$y$")
    ax0.set_ylabel("$z$")
    ax0.set_title(r"Campo estacionario $\mathbf{v}=(0,z,y)$: flujo tipo silla"
                 "\ntoda partícula que pasa por $(1,1)$ viene y va por la diagonal", fontsize=10.5)
    ax0.legend(fontsize=8, loc="upper left")
    ax0.grid(alpha=0.2)

    # ------------------------------------------------------------
    # PANEL B: aceleracion en el tiempo, fijo vs viajero
    # ------------------------------------------------------------
    t = np.linspace(-0.8, 1.2, 300)
    acel_fijo = np.ones_like(t)          # Dv/Dt en (1,1) = (y,z) = (1,1) SIEMPRE (campo estacionario)
    acel_viajero = np.exp(t)             # d^2y/dt^2 de la particula que en t=0 esta en (1,1)

    ax1.plot(t, acel_fijo, color="steelblue", lw=2.4,
             label=r"observador FIJO en $(1,1,1)$: $D\mathbf{v}/Dt|_{(1,1)}=(1,1)$ — constante")
    ax1.plot(t, acel_viajero, color="firebrick", lw=2.4,
             label=r"observador VIAJERO (nace en $(1,1,1)$ en $t{=}0$): $\ddot y=\ddot z=e^t$ — crece")
    ax1.scatter([0], [1], color="black", zorder=5, s=60)
    ax1.annotate("coinciden en t=0\n(es la MISMA partícula\nen ESE instante)", xy=(0, 1),
                xytext=(0.15, 1.9), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color="0.3"))
    ax1.set_xlabel("tiempo $t$")
    ax1.set_ylabel(r"componente $y$ (=componente $z$) de la aceleración")
    ax1.set_title("La trampa del ejercicio 2023-1: dos nociones de\n"
                 "\"aceleración en ese punto\" que NO son lo mismo", fontsize=10.5)
    ax1.legend(fontsize=8.3, loc="upper left")
    ax1.grid(alpha=0.25)

    fig.suptitle(r"Observador fijo vs. observador que viaja con la partícula ($D/Dt$ vs. $\partial/\partial t$ en acción)",
                 fontsize=12.5)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig("fig_observador_fijo_vs_viajero.png", dpi=130, bbox_inches="tight")
    print("  -> fig_observador_fijo_vs_viajero.png")


if __name__ == "__main__":
    print("Generando figura de derivada material (parcial 2023-1)...")
    figura_observador_fijo_vs_viajero()
    print("Listo.")
