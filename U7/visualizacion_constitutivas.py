"""
Visualizaciones Unidad 7 — Ecuaciones constitutivas
=====================================================
Tres figuras, cada una ataca una idea central del capitulo:

1. fig_vol_desviador.png
   La "clave del capitulo" (seccion 7.2): la ley de Hooke isotropa son DOS leyes
   escalares desacopladas. Se toma un tensor de deformacion 2D generico, se separa
   en parte volumetrica (esferica) + parte desviadora, y se muestra que:
     - la parte volumetrica cambia el AREA pero no la FORMA (sigue siendo cuadrado)
     - la parte desviadora cambia la FORMA pero preserva el AREA (a primer orden)
   Exactamente el "tamano/forma" de la U5 acoplado por separado por el material.

2. fig_tres_modelos_tiempo.png
   La observacion central de 7.1: inviscido / Newtoniano / Hookeano difieren en
   A QUE variable cinematica se acopla la tension. Se impone la MISMA historia de
   deformacion de corte (rampa-meseta-rampa-cero) a los tres modelos y se grafica
   la tension resultante: el fluido responde a la TASA (pulso rectangular, "solo le
   importa la velocidad ahora"), el solido responde a la deformacion misma (repite
   la forma de la entrada, "memoria de forma"), el inviscido no responde nunca.

3. fig_incompresibilidad_limite.png
   La advertencia de 7.3: nu -> 1/2 hace explotar lambda y K (denominador 1-2nu).
   Se grafica K(nu) y lambda(nu) a E fijo y se marca la goma (nu~0.499).

Corre con: python visualizacion_constitutivas.py
"""

import numpy as np
import matplotlib.pyplot as plt


# =====================================================================
# FIGURA 1: descomposicion volumetrico / desviador
# =====================================================================

def area_shoelace(corners):
    x = corners[:, 0]
    y = corners[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def figura_vol_desviador():
    # Tensor de deformacion 2D generico (combina cambio de tamano + de forma)
    eps = np.array([[0.15, 0.10],
                     [0.10, -0.05]])
    eps_vol_escalar = np.trace(eps) / 2.0          # promedio normal (analogo 2D de eps_kk/3)
    eps_vol = eps_vol_escalar * np.eye(2)
    eps_dev = eps - eps_vol                          # traza nula por construccion

    cuadrado = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]], dtype=float)

    def deformar(e):
        return cuadrado @ (np.eye(2) + e).T

    casos = [
        ("Deformación total  " + r"$\varepsilon$", eps, "steelblue"),
        ("Parte volumétrica  " + r"$\varepsilon_{vol}=\frac{\varepsilon_{kk}}{2}\delta_{ij}$", eps_vol, "seagreen"),
        ("Parte desviadora  " + r"$\varepsilon'=\varepsilon-\varepsilon_{vol}$", eps_dev, "firebrick"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    area0 = area_shoelace(cuadrado)

    for ax, (titulo, e, color) in zip(axes, casos):
        deformado = deformar(e)
        area1 = area_shoelace(deformado)
        ax.plot(cuadrado[:, 0], cuadrado[:, 1], "--", color="0.6", lw=1.3, label="original")
        ax.fill(deformado[:, 0], deformado[:, 1], color=color, alpha=0.25)
        ax.plot(deformado[:, 0], deformado[:, 1], color=color, lw=2.2, label="deformado")
        ax.set_aspect("equal")
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.6, 1.6)
        ax.grid(alpha=0.25)
        cambio_area = 100 * (area1 - area0) / area0
        cambio_forma = "sí" if not np.allclose(e, eps_vol_escalar * np.eye(2)) else "no (sigue cuadrado)"
        ax.set_title(f"{titulo}\nΔárea = {cambio_area:+.1f}%   ¿cambia forma? {cambio_forma}",
                     fontsize=10.5)
        ax.legend(fontsize=8, loc="lower right")

    fig.suptitle("Hooke isótropo = dos leyes desacopladas (sección 7.2): "
                  "volumen ↔ K,  forma ↔ 2μ", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig("fig_vol_desviador.png", dpi=130, bbox_inches="tight")
    print("  -> fig_vol_desviador.png")


# =====================================================================
# FIGURA 2: historia temporal, los tres modelos ante la misma deformacion
# =====================================================================

def perfil_trapezoidal(t, e0=1.0):
    """ rampa 0->1, meseta 1->2, rampa 2->3, cero 3->4 (periodo repetido) """
    tt = np.mod(t, 4.0)
    e = np.zeros_like(tt)
    m1 = tt < 1
    m2 = (tt >= 1) & (tt < 2)
    m3 = (tt >= 2) & (tt < 3)
    e[m1] = e0 * tt[m1]
    e[m2] = e0
    e[m3] = e0 * (3 - tt[m3])
    return e


def figura_tres_modelos_tiempo():
    mu_solido = 1.0
    mu_fluido = 1.0

    t = np.linspace(0, 4, 2000)
    dt = t[1] - t[0]
    e = perfil_trapezoidal(t)
    rate = np.gradient(e, dt)

    sigma_invisc = np.zeros_like(t)
    sigma_newton = 2 * mu_fluido * rate
    sigma_hooke = 2 * mu_solido * e

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(11, 7), sharex=True,
                                    gridspec_kw={"height_ratios": [1, 1.6]})

    ax0.plot(t, e, color="0.2", lw=2.2)
    ax0.set_ylabel(r"deformación impuesta $\varepsilon_{xy}(t)$" + "\n(misma para los 3 modelos)")
    ax0.grid(alpha=0.25)
    ax0.set_title("Misma historia cinemática, tres respuestas distintas (sección 7.1)", fontsize=12)

    ax1.plot(t, sigma_invisc, color="gray", lw=2.2, label=r"Invíscido: $\sigma_{xy}=0$ (nunca resiste corte)")
    ax1.plot(t, sigma_newton, color="steelblue", lw=2.2,
             label=r"Newtoniano: $\sigma_{xy}=2\mu V_{xy}$ (responde a la $\it{tasa}$ — pulso)")
    ax1.plot(t, sigma_hooke, color="firebrick", lw=2.2,
             label=r"Hookeano: $\sigma_{xy}=2\mu\varepsilon_{xy}$ (repite la forma — memoria)")
    ax1.set_xlabel("tiempo")
    ax1.set_ylabel(r"tensión de corte $\sigma_{xy}(t)$")
    ax1.grid(alpha=0.25)
    ax1.legend(fontsize=9.5, loc="upper right")
    ax1.axhline(0, color="k", lw=0.6)

    fig.tight_layout()
    fig.savefig("fig_tres_modelos_tiempo.png", dpi=130, bbox_inches="tight")
    print("  -> fig_tres_modelos_tiempo.png")


# =====================================================================
# FIGURA 3: limite de incompresibilidad nu -> 1/2
# =====================================================================

def figura_incompresibilidad_limite():
    E = 1.0
    nu = np.linspace(0.0, 0.499, 800)
    K = E / (3 * (1 - 2 * nu))
    lam = E * nu / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))

    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.plot(nu, K, color="seagreen", lw=2.2, label=r"$K=\dfrac{E}{3(1-2\nu)}$  (módulo volumétrico)")
    ax.plot(nu, lam, color="firebrick", lw=2.2, label=r"$\lambda=\dfrac{E\nu}{(1+\nu)(1-2\nu)}$")
    ax.plot(nu, mu, color="steelblue", lw=2.2, label=r"$\mu=\dfrac{E}{2(1+\nu)}$  (no diverge)")
    ax.set_ylim(0, 20)
    ax.axvline(0.499, color="0.3", ls=":", lw=1.5)
    ax.text(0.499, 12, "  goma\n  ν≈0.499", fontsize=9)
    ax.set_xlabel(r"$\nu$")
    ax.set_ylabel("módulo (con E=1)")
    ax.set_title(r"$\nu\to\frac{1}{2}$: incompresibilidad — $K,\lambda\to\infty$, $\mu$ se queda quieto"
                 "\n(sección 7.3 — el origen del *locking* volumétrico en FEM)", fontsize=11.5)
    ax.legend(fontsize=9.5)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig("fig_incompresibilidad_limite.png", dpi=130, bbox_inches="tight")
    print("  -> fig_incompresibilidad_limite.png")


if __name__ == "__main__":
    print("Generando figuras de Unidad 7 (constitutivas)...")
    figura_vol_desviador()
    figura_tres_modelos_tiempo()
    figura_incompresibilidad_limite()
    print("Listo.")
