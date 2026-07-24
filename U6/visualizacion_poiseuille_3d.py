"""
Visualizacion 3D: flujo de Poiseuille en un tubo circular (Unidad 6, version fluida
de la viga de U5)
====================================================================================
Contraparte "fluido" del ejemplo de la viga (U5/visualizacion_viga_flexion.py):
mismo espiritu (una geometria 3D real, no un flujo de manual), pero del lado
de los fluidos.

Campo:  v = (vx(y,z), 0, 0),   vx = v_max * (1 - r^2/a^2),   r^2 = y^2+z^2

Punto central que justifica la figura (y que ya viene anunciado en 6.3(c)):
las trayectorias son RECTAS (todo el fluido va en linea recta en x) y sin
embargo el flujo NO es irrotacional: cada particula gira sobre si misma con
vorticidad proporcional a r. "Recta" y "sin rotacion" son cosas distintas,
y Poiseuille es el ejemplo real (no de juguete) mas importante de esa trampa.

Corre con: python visualizacion_poiseuille_3d.py
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

VMAX = 1.0
A = 1.0  # radio del tubo


def vx(y, z):
    r2 = y**2 + z**2
    return VMAX * (1 - r2 / A**2)


def figura_poiseuille():
    fig = plt.figure(figsize=(14, 6))

    # ------------------------------------------------------------------
    # PANEL IZQUIERDO: el "perfil bala" clasico en 3D
    # ------------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    theta = np.linspace(0, 2 * np.pi, 60)
    rr = np.linspace(0, A, 25)
    R, TH = np.meshgrid(rr, theta)
    Y, Z = R * np.cos(TH), R * np.sin(TH)
    Vx = vx(Y, Z)

    ax1.plot_surface(Y, Z, Vx, cmap="viridis", linewidth=0, antialiased=True, alpha=0.95)
    # tapa del tubo (pared, v=0) para dar contexto geometrico
    th_wall = np.linspace(0, 2 * np.pi, 100)
    ax1.plot(A * np.cos(th_wall), A * np.sin(th_wall), 0 * th_wall, color="0.3", lw=1.5)
    ax1.plot(A * np.cos(th_wall), A * np.sin(th_wall), 0 * th_wall + 0.001,
             color="0.3", lw=1.5, alpha=0.3)

    for r0 in (0, A / 2, A):
        ax1.plot([0, 0], [r0, r0], [0, vx(r0, 0)], color="0.4", lw=0.8, alpha=0.6)

    ax1.set_xlabel("y"); ax1.set_ylabel("z"); ax1.set_zlabel("$v_x$")
    ax1.set_title("Perfil de velocidad en el tubo — 'bala' parabólica\n"
                  r"$v_x = v_{max}(1-r^2/a^2)$: máxima en el eje, cero en la pared",
                  fontsize=11.5)
    ax1.view_init(elev=22, azim=-60)

    # ------------------------------------------------------------------
    # PANEL DERECHO: vorticidad en la seccion transversal + perfil radial
    # ------------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2)
    ys = np.linspace(-A * 1.15, A * 1.15, 46)
    zs = np.linspace(-A * 1.15, A * 1.15, 46)
    Yg, Zg = np.meshgrid(ys, zs)
    Rg = np.sqrt(Yg**2 + Zg**2)
    mask = Rg <= A

    # rot v = (0, dvx/dz, -dvx/dy) -> en el plano (y,z) es un campo AZIMUTAL
    # magnitud = 2*vmax*r/a^2 (crece linealmente con r, maxima en la pared)
    dvx_dy = -2 * VMAX * Yg / A**2
    dvx_dz = -2 * VMAX * Zg / A**2
    omega_y = dvx_dz          # (rot v)_y
    omega_z = -dvx_dy         # (rot v)_z
    omega_y_m = np.ma.array(omega_y, mask=~mask)
    omega_z_m = np.ma.array(omega_z, mask=~mask)
    omega_mag = np.sqrt(omega_y**2 + omega_z**2)

    pcm = ax2.pcolormesh(Yg, Zg, np.ma.array(omega_mag, mask=~mask),
                          cmap="magma", shading="auto")

    ysq = np.linspace(-A * 1.15, A * 1.15, 16)
    zsq = np.linspace(-A * 1.15, A * 1.15, 16)
    Yq, Zq = np.meshgrid(ysq, zsq)
    Rq = np.sqrt(Yq**2 + Zq**2)
    maskq = Rq <= A
    omega_yq = np.ma.array(-2 * VMAX * Zq / A**2, mask=~maskq)
    omega_zq = np.ma.array(2 * VMAX * Yq / A**2, mask=~maskq)
    ax2.quiver(Yq, Zq, omega_yq, omega_zq, color="white", scale=22, width=0.0055)
    th_wall2 = np.linspace(0, 2 * np.pi, 100)
    ax2.plot(A * np.cos(th_wall2), A * np.sin(th_wall2), color="cyan", lw=2)
    ax2.set_aspect("equal")
    ax2.set_xlabel("y"); ax2.set_ylabel("z")
    ax2.set_title("Vector vorticidad en la sección — azimutal, $\\propto r$\n"
                  "(¡el flujo NO es irrotacional aunque las trayectorias sean rectas!)",
                  fontsize=11.5)
    fig.colorbar(pcm, ax=ax2, shrink=0.75, label="|rot v|")

    fig.suptitle("Poiseuille en tubo circular — trayectorias rectas, "
                 "vorticidad NO nula (máx. en la pared, cero en el eje)", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("fig7_poiseuille_3d.png", dpi=130, bbox_inches="tight")
    print("  -> fig7_poiseuille_3d.png")


if __name__ == "__main__":
    print("Generando figura de Poiseuille 3D...")
    figura_poiseuille()
    print("Listo.")
