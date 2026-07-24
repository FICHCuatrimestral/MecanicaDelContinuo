"""
Visualizacion de cinematica del continuo - Unidad 6 (FICH-UNL)
=============================================================

Objetivo: "ver" que significan geometricamente
    - gradiente de velocidad   grad v = nabla v      ([nabla v]_ij = dv_i/dx_j)
    - traza                     tr(nabla v) = div v
    - divergencia               div v                 (tasa de cambio de VOLUMEN)
    - tasa-de-deformacion       V = parte SIMETRICA de nabla v (estira/deforma)
    - vorticidad / spin         Omega = parte ANTISIMETRICA de nabla v (gira)
    - rotor / rotacional        rot v = curl v = vector vorticidad Omega_k

Notacion del curso (Cap. 6):
    dv_i/dx_j = V_ij  -  Omega_ij
    V_ij     =  1/2 ( dv_i/dx_j + dv_j/dx_i )     (simetrico)
    Omega_ij =  1/2 ( dv_j/dx_i - dv_i/dx_j )     (antisimetrico)  <-- ojo al signo del curso
    Omega_k  = eps_kij Omega_ij = [rot v]_k        (vector vorticidad = curl v)

Corre con:  python visualizacion_cinematica.py
Genera PNGs en la misma carpeta.
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1) EL ZOOLOGICO DE FLUJOS 2D
#    Cada flujo v(x,y) = (u, w). Elegimos casos "puros" para aislar
#    cada concepto.
# ----------------------------------------------------------------------
FLUJOS = {
    "Fuente (divergencia pura)": {
        "v": lambda x, y: (x, y),
        "info": "div>0 : el volumen se EXPANDE. rot=0 : no gira.",
    },
    "Sumidero": {
        "v": lambda x, y: (-x, -y),
        "info": "div<0 : el volumen se CONTRAE. rot=0.",
    },
    "Rotacion rigida": {
        "v": lambda x, y: (-y, x),
        "info": "div=0 : volumen constante. rot=2 : gira como solido.",
    },
    "Corte simple (shear)": {
        "v": lambda x, y: (y, 0.0 * x),
        "info": "div=0. rot!=0. = deformacion + rotacion (mitad y mitad).",
    },
    "Estiramiento puro (silla)": {
        "v": lambda x, y: (x, -y),
        "info": "div=0 (estira en x, comprime en y). rot=0 : NO gira.",
    },
    "Vortice irrotacional": {
        # v = (-y, x) / r^2  -> gira alrededor del centro pero rot=0 (salvo el origen)
        "v": lambda x, y: (-y / (x**2 + y**2 + 1e-9), x / (x**2 + y**2 + 1e-9)),
        "info": "Gira alrededor del centro PERO rot=0: la particulita NO rota.",
    },
}


def gradiente_velocidad(vfun, x0=0.6, y0=0.4, h=1e-4):
    """nabla v numerico en (x0,y0):  L[i,j] = dv_i/dx_j  (i,j en {x,y})."""
    ux1, wx1 = vfun(x0 + h, y0)
    ux0, wx0 = vfun(x0 - h, y0)
    uy1, wy1 = vfun(x0, y0 + h)
    uy0, wy0 = vfun(x0, y0 - h)
    du_dx = (ux1 - ux0) / (2 * h)
    du_dy = (uy1 - uy0) / (2 * h)
    dw_dx = (wx1 - wx0) / (2 * h)
    dw_dy = (wy1 - wy0) / (2 * h)
    return np.array([[du_dx, du_dy],
                     [dw_dx, dw_dy]])


def descomponer(L):
    """Devuelve V (simetrico), Omega (antisimetrico), div y curl_z."""
    V = 0.5 * (L + L.T)                 # tasa-de-deformacion
    W = 0.5 * (L.T - L)                 # tensor de vorticidad Omega_ij = 1/2(v_j,i - v_i,j)
    div = np.trace(L)                   # = dv_i/dx_i  (traza)
    curl_z = L[1, 0] - L[0, 1]          # (dw/dx - du/dy) = [rot v]_z = vector vorticidad
    return V, W, div, curl_z


# ----------------------------------------------------------------------
# 2) FIGURA 1: campo de velocidad + divergencia (color) + numeros
# ----------------------------------------------------------------------
def figura_zoologico():
    xs = np.linspace(-1.5, 1.5, 21)
    ys = np.linspace(-1.5, 1.5, 21)
    X, Y = np.meshgrid(xs, ys)

    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    for ax, (nombre, d) in zip(axes.flat, FLUJOS.items()):
        U, W = d["v"](X, Y)
        # divergencia numerica sobre la grilla (para el mapa de color)
        dudx = np.gradient(U, xs, axis=1)
        dwdy = np.gradient(W, ys, axis=0)
        div_grid = dudx + dwdy
        div_grid = np.clip(div_grid, -4, 4)

        speed = np.sqrt(U**2 + W**2)
        Un, Wn = U / (speed + 1e-9), W / (speed + 1e-9)  # flechas norm. para ver direccion

        pcm = ax.pcolormesh(X, Y, div_grid, cmap="RdBu_r", vmin=-4, vmax=4, shading="auto")
        ax.quiver(X, Y, Un, Wn, pivot="mid", scale=30, width=0.003, color="k", alpha=0.6)

        L = gradiente_velocidad(d["v"])
        _, _, div, curl = descomponer(L)
        ax.set_title(f"{nombre}\ndiv v = {div:+.2f}   |   rot v = {curl:+.2f}",
                     fontsize=11)
        ax.text(0.5, -1.98, d["info"], ha="center", fontsize=8.5, style="italic",
                transform=ax.transData)
        ax.set_aspect("equal")
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-2.1, 1.5)

    fig.suptitle("Zoologico de flujos:  color = divergencia (rojo se expande, azul se contrae)",
                 fontsize=14, y=0.98)
    fig.colorbar(pcm, ax=axes, shrink=0.6, label="div v")
    fig.savefig("fig1_zoologico_divergencia.png", dpi=130, bbox_inches="tight")
    print("  -> fig1_zoologico_divergencia.png")


# ----------------------------------------------------------------------
# 3) FIGURA 2: DEFORMACION vs ROTACION
#    Soltamos una "boyita" (circulo de trazadores + una cruz) y la dejamos
#    fluir un ratito. Asi se VE si el flujo estira (V) o gira (Omega).
# ----------------------------------------------------------------------
def advectar(vfun, pts, t_total=0.6, pasos=400):
    """Integra puntos por el campo de velocidad (Euler chico)."""
    dt = t_total / pasos
    p = pts.copy()
    for _ in range(pasos):
        u, w = vfun(p[:, 0], p[:, 1])
        p[:, 0] += u * dt
        p[:, 1] += w * dt
    return p


def figura_deformacion():
    # circulo de trazadores + dos diametros (cruz) centrados en (0.8, 0.6)
    cx, cy, r = 0.8, 0.6, 0.28
    th = np.linspace(0, 2 * np.pi, 80)
    circ = np.column_stack([cx + r * np.cos(th), cy + r * np.sin(th)])
    hor = np.column_stack([np.linspace(cx - r, cx + r, 30), np.full(30, cy)])
    ver = np.column_stack([np.full(30, cx), np.linspace(cy - r, cy + r, 30)])

    casos = ["Rotacion rigida", "Estiramiento puro (silla)",
             "Corte simple (shear)", "Fuente (divergencia pura)"]

    fig, axes = plt.subplots(1, 4, figsize=(19, 5))
    for ax, nombre in zip(axes, casos):
        vfun = FLUJOS[nombre]["v"]
        # estado inicial (gris) y final (color)
        for blob, col0 in [(circ, "0.6")]:
            ax.plot(blob[:, 0], blob[:, 1], color=col0, lw=1.5, ls="--")
        for blob in (hor, ver):
            ax.plot(blob[:, 0], blob[:, 1], color="0.6", lw=1.2, ls="--")

        c2 = advectar(vfun, circ)
        h2 = advectar(vfun, hor)
        v2 = advectar(vfun, ver)
        ax.plot(c2[:, 0], c2[:, 1], color="crimson", lw=2)
        ax.plot(h2[:, 0], h2[:, 1], color="navy", lw=2)
        ax.plot(v2[:, 0], v2[:, 1], color="navy", lw=2)

        L = gradiente_velocidad(vfun, cx, cy)
        V, W, div, curl = descomponer(L)
        ax.set_title(f"{nombre}\n"
                     f"tr(V)=div={div:+.2f}   rot={curl:+.2f}", fontsize=10)
        ax.set_aspect("equal")
        ax.grid(alpha=0.3)
    fig.suptitle("Boyita (--) que fluye un instante (linea llena).  "
                 "V la estira, Omega la gira.", fontsize=13)
    fig.savefig("fig2_deformacion_vs_rotacion.png", dpi=130, bbox_inches="tight")
    print("  -> fig2_deformacion_vs_rotacion.png")


# ----------------------------------------------------------------------
# 4) FIGURA 3: el corte = deformacion + rotacion  (nabla v = V - Omega)
# ----------------------------------------------------------------------
def figura_descomposicion_shear():
    xs = np.linspace(-1, 1, 15)
    X, Y = np.meshgrid(xs, xs)
    vfun = FLUJOS["Corte simple (shear)"]["v"]
    L = gradiente_velocidad(vfun)
    V, W, _, _ = descomponer(L)

    # campos lineales v = L x  para cada pieza
    def campo(M):
        U = M[0, 0] * X + M[0, 1] * Y
        Wv = M[1, 0] * X + M[1, 1] * Y
        return U, Wv

    piezas = [("nabla v (corte)", L),
              ("V  (deformacion)", V),
              ("-Omega  (rotacion)", -W)]
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax, (t, M) in zip(axes, piezas):
        U, Wv = campo(M)
        ax.quiver(X, Y, U, Wv, color="k", scale=12, width=0.004)
        ax.set_title(f"{t}\n{np.round(M,2).tolist()}", fontsize=10)
        ax.set_aspect("equal")
        ax.grid(alpha=0.3)
    fig.suptitle("Corte simple = deformacion pura  +  rotacion pura   "
                 "(nabla v = V - Omega)", fontsize=13)
    fig.savefig("fig3_shear_descompuesto.png", dpi=130, bbox_inches="tight")
    print("  -> fig3_shear_descompuesto.png")


# ----------------------------------------------------------------------
# 5) TABLA RESUMEN por consola
# ----------------------------------------------------------------------
def tabla_resumen():
    print("\n" + "=" * 78)
    print(f"{'FLUJO':<30}{'div v':>8}{'rot v':>8}{'tr(V)':>8}   interpretacion")
    print("-" * 78)
    for nombre, d in FLUJOS.items():
        L = gradiente_velocidad(d["v"])
        V, W, div, curl = descomponer(L)
        print(f"{nombre:<30}{div:>8.2f}{curl:>8.2f}{np.trace(V):>8.2f}   {d['info']}")
    print("=" * 78)
    print("Recordar:  div v = tr(nabla v) = tr(V)   (Omega no aporta a la traza)")
    print("           rot v = vector vorticidad = 2 x velocidad angular local\n")


if __name__ == "__main__":
    print("Generando figuras de cinematica (Unidad 6)...")
    tabla_resumen()
    figura_zoologico()
    figura_deformacion()
    figura_descomposicion_shear()
    print("Listo. Abri los PNG generados.")
