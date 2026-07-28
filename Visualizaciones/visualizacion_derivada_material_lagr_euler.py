"""
Visualizacion Unidad 9/10 — Derivada material: Lagrangiano vs Euleriano
=========================================================================
Ejemplo minimo pero completo (seccion 1.2 de la guia): un campo escalar
NO estacionario T(x,t) = sin(x - t) (una onda viajando a velocidad de
fase 1) observado por dos "sensores" distintos:

  - Sensor FIJO en x0 (euleriano): mide dT/dt = derivada PARCIAL.
  - Particula que viaja con velocidad v=2 (lagrangiano): mide DT/Dt =
    derivada MATERIAL. La particula es mas rapida que la onda, asi que
    la "atraviesa" -- eso es justamente lo que hace que DT/Dt != dT/dt.

Con v=2 constante:
    dT/dt   = -cos(x-t)
    v dT/dx =  2cos(x-t)     (termino convectivo)
    DT/Dt   =  dT/dt + v dT/dx = cos(x-t)     (verificable a mano)

Tres paneles:
  A) diagrama espacio-tiempo de T(x,t): la linea vertical es el sensor
     fijo, la diagonal es la trayectoria de la particula.
  B) lo que "siente" cada observador en el tiempo: T en el punto fijo
     vs T sobre la particula -- señales DISTINTAS pese a ser el MISMO
     campo T.
  C) la descomposicion local + convectivo = material, evaluada a lo
     largo de la trayectoria de la particula.

Corre con: python visualizacion_derivada_material_lagr_euler.py
"""

import numpy as np
import matplotlib.pyplot as plt

V = 2.0       # velocidad de la particula (mayor que la velocidad de fase = 1)
X0 = 0.0      # posicion del sensor fijo / posicion inicial de la particula


def T_field(x, t):
    return np.sin(x - t)


def figura_derivada_material():
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(16.5, 5.6))

    # ------------------------------------------------------------
    # PANEL A: diagrama espacio-tiempo
    # ------------------------------------------------------------
    x = np.linspace(-6, 10, 400)
    t = np.linspace(0, 6, 400)
    X, Tg = np.meshgrid(x, t)
    field = T_field(X, Tg)

    im = axA.pcolormesh(x, t, field, cmap="RdBu_r", shading="auto")
    axA.axvline(X0, color="black", lw=2.2, ls="--", label="sensor fijo (euleriano), $x=x_0$")
    t_line = np.linspace(0, 6, 100)
    axA.plot(X0 + V * t_line, t_line, color="gold", lw=2.6,
             label="partícula (lagrangiano), $x=x_0+Vt$")
    axA.set_xlim(-6, 10)
    axA.set_ylim(0, 6)
    axA.set_xlabel("$x$")
    axA.set_ylabel("$t$")
    axA.set_title(r"Campo NO estacionario $T(x,t)=\sin(x-t)$" + "\n(la onda se mueve sola, a velocidad 1)",
                   fontsize=11)
    axA.legend(fontsize=8.5, loc="upper left")
    fig.colorbar(im, ax=axA, shrink=0.75, label="T")

    # ------------------------------------------------------------
    # PANEL B: lo que percibe cada observador
    # ------------------------------------------------------------
    t_series = np.linspace(0, 6, 400)
    T_fijo = T_field(X0, t_series)
    T_particula = T_field(X0 + V * t_series, t_series)

    axB.plot(t_series, T_fijo, color="0.15", lw=2.4, ls="--",
             label=r"sensor fijo: $T(x_0,t)$")
    axB.plot(t_series, T_particula, color="darkorange", lw=2.4,
             label=r"partícula: $T(x_0+Vt,\,t)$")
    axB.set_xlabel("$t$")
    axB.set_ylabel("$T$")
    axB.set_title("Mismo campo, dos señales distintas\n(el sensor fijo y la partícula NO ven lo mismo)",
                   fontsize=11)
    axB.legend(fontsize=9, loc="upper right")
    axB.grid(alpha=0.25)
    axB.axhline(0, color="0.7", lw=0.6)

    # ------------------------------------------------------------
    # PANEL C: descomposicion local + convectivo = material
    # ------------------------------------------------------------
    x_p = X0 + V * t_series
    dTdt_local = -np.cos(x_p - t_series)          # dT/dt evaluado sobre la particula
    conv = V * np.cos(x_p - t_series)              # V * dT/dx
    DTDt_material = dTdt_local + conv

    axC.plot(t_series, dTdt_local, color="steelblue", lw=2.2,
             label=r"local: $\partial T/\partial t$")
    axC.plot(t_series, conv, color="seagreen", lw=2.2,
             label=r"convectivo: $V\,\partial T/\partial x$")
    axC.plot(t_series, DTDt_material, color="firebrick", lw=2.8,
             label=r"material: $DT/Dt=$ suma")
    axC.set_xlabel("$t$")
    axC.set_ylabel("tasa de cambio")
    axC.set_title(r"Lo que siente la partícula, descompuesto"
                 "\n" + r"$DT/Dt=\partial T/\partial t + V\,\partial T/\partial x$", fontsize=11)
    axC.legend(fontsize=9, loc="upper right")
    axC.grid(alpha=0.25)
    axC.axhline(0, color="0.7", lw=0.6)

    fig.suptitle(r"Derivada material: euleriano ($\partial/\partial t$, sensor fijo) vs. lagrangiano ($D/Dt$, partícula)",
                 fontsize=13.5)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig("fig_derivada_material_lagr_euler.png", dpi=130, bbox_inches="tight")
    print("  -> fig_derivada_material_lagr_euler.png")


if __name__ == "__main__":
    print("Generando figura de derivada material (lagrangiano vs euleriano)...")
    figura_derivada_material()
    print("Listo.")
