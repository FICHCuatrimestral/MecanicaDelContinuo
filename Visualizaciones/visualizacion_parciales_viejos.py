"""
Visualizacion de ejercicios de Unidad 6 encontrados en parciales viejos (2014-2023)
====================================================================================
Complementa visualizacion_cinematica.py: en vez de los 6 flujos "de manual",
estos son ejercicios REALES de parciales anteriores que todavia no estaban en el
apunte (fuente: carpeta Parciales2/).

fig4: RECP2_2016 ej.1 -- v = (x/r^2, y/r^2, 0), incompresible E irrotacional
      (resulta ser un flujo potencial: v = grad(ln r))
fig5: [2023] recuperatorio ej.2 -- dos perfiles de corte en z, uno incompresible
      (tipo Poiseuille) y otro NO incompresible
fig6: RECP2_2014 ej.2 -- v = (-3x2+x3, 3x1-5x3, -x1+5x2), rotacion rigida
      alrededor de un eje oblicuo (no coincide con ningun eje coordenado)

Corre con:  python visualizacion_parciales_viejos.py
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (necesario para proyeccion 3d)


# ----------------------------------------------------------------------
# FIGURA 4 -- RECP2_2016 ej.1: fuente puntual 2D = flujo potencial
# ----------------------------------------------------------------------
def figura_fuente_potencial():
    def v(x, y):
        r2 = x**2 + y**2 + 1e-9
        return x / r2, y / r2

    xs = np.linspace(-2, 2, 25)
    ys = np.linspace(-2, 2, 25)
    X, Y = np.meshgrid(xs, ys)
    U, W = v(X, Y)
    speed = np.sqrt(U**2 + W**2)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2))

    ax = axes[0]
    strm = ax.streamplot(X, Y, U, W, color=speed, cmap="viridis", density=1.3,
                          linewidth=1.2)
    ax.plot(0, 0, "r*", markersize=14, label="origen (singularidad)")
    ax.set_title("$v = (x/r^2,\\; y/r^2)$\nlíneas de corriente radiales,"
                  " color = rapidez", fontsize=11)
    ax.set_aspect("equal")
    ax.legend(loc="upper right", fontsize=8)
    fig.colorbar(strm.lines, ax=ax, shrink=0.75, label="|v|")

    r = np.linspace(0.15, 2.5, 100)
    vr_teorico = 1.0 / r
    ax2 = axes[1]
    ax2.plot(r, vr_teorico, color="crimson", lw=2.5, label=r"$v_r(r) = 1/r$ (teórico)")
    ax2.set_xlabel("r (distancia al origen)")
    ax2.set_ylabel(r"$v_r$")
    ax2.set_title("Perfil radial: decae como $1/r$\n"
                   "(idéntico al de una fuente puntual 2D en flujo potencial)",
                   fontsize=11)
    ax2.grid(alpha=0.3)
    ax2.legend()

    div0 = 0.0  # analitico: (y^2-x^2)/r^4 + (x^2-y^2)/r^4 = 0 en todo punto != origen
    rot0 = 0.0
    fig.suptitle(f"RECP2_2016 ej.1 — div v = {div0:.0f} (incompresible)   "
                 f"rot v = {rot0:.0f} (irrotacional)   ⟹   v = ∇φ,  φ = ln(r)",
                 fontsize=12.5)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("fig4_fuente_potencial.png", dpi=130, bbox_inches="tight")
    print("  -> fig4_fuente_potencial.png")


# ----------------------------------------------------------------------
# FIGURA 5 -- [2023] recuperatorio ej.2: dos perfiles de corte en z
# ----------------------------------------------------------------------
def figura_perfiles_corte():
    H = 1.0
    lam = 1.0
    U0 = 1.0
    alpha = 0.6

    z = np.linspace(0, H, 200)

    # (a) v = lam * (H^4 - (H-z)^4, 0, 0)  -- tipo Poiseuille, INCOMPRESIBLE
    vx_a = lam * (H**4 - (H - z) ** 4)
    V13_a = 2 * lam * (H - z) ** 3  # = 1/2 * dvx/dz = 1/2 * 4*lam*(H-z)^3

    # (b) v = (U + alpha*z, 0, -alpha*z)  -- NO incompresible (div = -alpha)
    z2 = np.linspace(0, H, 200)
    vx_b = U0 + alpha * z2
    vz_b = -alpha * z2

    fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))

    ax = axes[0, 0]
    ax.plot(vx_a, z, color="teal", lw=2.5)
    ax.fill_betweenx(z, 0, vx_a, color="teal", alpha=0.12)
    ax.set_xlabel("$v_x(z) = \\lambda[H^4-(H-z)^4]$")
    ax.set_ylabel("z")
    ax.set_title("(a) Perfil de velocidad — incompresible", fontsize=11)
    ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(V13_a, z, color="darkorange", lw=2.5)
    ax.set_xlabel(r"$V_{13}(z) = \lambda(H-z)^3 \cdot 2$")
    ax.set_ylabel("z")
    ax.set_title("(a) Tasa de corte: máxima en la pared (z=0),\nnula en z=H", fontsize=11)
    ax.grid(alpha=0.3)
    ax.axhline(H, color="0.6", ls="--", lw=1)
    ax.text(V13_a[0] * 0.5, H - 0.05, "$V_{13}=0$ acá", fontsize=9, color="0.4")

    ax = axes[1, 0]
    ax.plot(vx_b, z2, color="firebrick", lw=2.5, label="$v_x = U+\\alpha z$")
    ax.plot(vz_b, z2, color="navy", lw=2.5, label="$v_z = -\\alpha z$")
    ax.set_xlabel("componente de velocidad")
    ax.set_ylabel("z")
    ax.set_title("(b) Perfil de velocidad — NO incompresible", fontsize=11)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    ax = axes[1, 1]
    ax.axis("off")
    texto = (
        "(a) $\\mathbf{v}=\\lambda\\{H^4-(H-z)^4,\\,0,\\,0\\}$\n"
        "     $V_{13}=V_{31}=\\lambda(H-z)^3$, resto nulo\n"
        "     $\\mathrm{div}\\,v = \\partial_1 v_1+\\partial_2v_2+\\partial_3v_3=0$\n"
        "     $\\Rightarrow$ INCOMPRESIBLE (perfil tipo Poiseuille)\n\n"
        "(b) $\\mathbf{v}=\\{U+\\alpha z,\\,0,\\,-\\alpha z\\}$\n"
        "     $V_{13}=V_{31}=\\alpha/2,\\quad V_{33}=-\\alpha$\n"
        f"     $\\mathrm{{div}}\\,v = -\\alpha = {-alpha:.1f} \\neq 0$\n"
        "     $\\Rightarrow$ NO incompresible (salvo $\\alpha=0$)"
    )
    ax.text(0.02, 0.95, texto, fontsize=11.5, va="top", family="monospace",
            transform=ax.transAxes,
            bbox=dict(boxstyle="round", facecolor="0.95", edgecolor="0.7"))

    fig.suptitle("Recuperatorio 2023, ej.2 — mismo tipo de perfil (corte en z),"
                 " un caso incompresible y otro no", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig("fig5_perfiles_corte_z.png", dpi=130, bbox_inches="tight")
    print("  -> fig5_perfiles_corte_z.png")


# ----------------------------------------------------------------------
# FIGURA 6 -- RECP2_2014 ej.2: rotacion rigida alrededor de un eje oblicuo
# ----------------------------------------------------------------------
def figura_rotacion_eje_oblicuo():
    # v = (-3x2+x3, 3x1-5x3, -x1+5x2)  -->  L = grad(v) es ANTISIMETRICA pura
    L = np.array([
        [0.0, -3.0, 1.0],
        [3.0, 0.0, -5.0],
        [-1.0, 5.0, 0.0],
    ])
    V = 0.5 * (L + L.T)
    assert np.allclose(V, 0), "V deberia ser exactamente 0 (movimiento rigido)"

    def v(p):
        x1, x2, x3 = p
        return np.array([-3 * x2 + x3, 3 * x1 - 5 * x3, -x1 + 5 * x2])

    # vector vorticidad = rot(v):  omega_i = eps_ijk dv_k/dx_j
    omega_vort = np.array([
        L[2, 1] - L[1, 2],  # dv3/dx2 - dv2/dx3
        L[0, 2] - L[2, 0],  # dv1/dx3 - dv3/dx1
        L[1, 0] - L[0, 1],  # dv2/dx1 - dv1/dx2
    ])
    omega_local = omega_vort / 2.0  # velocidad angular local (eje de rotacion)
    n = omega_vort / np.linalg.norm(omega_vort)

    # verificacion numerica de la identidad de Lamb: a = domega/dt + omega x v + 1/2 grad(v.v)
    # (aca "omega" de la identidad es el vector rot v; el flujo es estacionario => dv/dt=0)
    p_test = np.array([0.7, -0.4, 0.3])
    a_directo = L @ v(p_test)  # a_i = v_j dv_i/dx_j (estacionario, = (v.grad)v)
    a_lamb = np.cross(omega_vort, v(p_test))  # + (1/2) grad(v.v), calculado abajo
    h = 1e-6
    grad_v2 = np.zeros(3)
    for k in range(3):
        pp = p_test.copy(); pp[k] += h
        pm = p_test.copy(); pm[k] -= h
        grad_v2[k] = (v(pp) @ v(pp) - v(pm) @ v(pm)) / (2 * h)
    a_lamb_completo = a_lamb + 0.5 * grad_v2
    print("  Verificación identidad de Lamb (P2_2015 ej.1) en el campo de RECP2_2014 ej.2:")
    print(f"    a = (v.grad)v          = {np.round(a_directo, 4)}")
    print(f"    omega x v + 1/2 grad(v^2) = {np.round(a_lamb_completo, 4)}")
    print(f"    coinciden: {np.allclose(a_directo, a_lamb_completo, atol=1e-3)}")

    # base ortonormal perpendicular a n (Gram-Schmidt)
    tmp = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(tmp, n)) > 0.9:
        tmp = np.array([0.0, 1.0, 0.0])
    e1 = tmp - np.dot(tmp, n) * n
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)

    fig = plt.figure(figsize=(8.5, 8))
    ax = fig.add_subplot(111, projection="3d")

    for radio in (0.4, 0.8, 1.2):
        thetas = np.linspace(0, 2 * np.pi, 16, endpoint=False)
        for th in thetas:
            p = radio * (np.cos(th) * e1 + np.sin(th) * e2)
            vp = v(p)
            ax.quiver(*p, *vp, length=0.09, normalize=False, color="teal", linewidth=1.3,
                      arrow_length_ratio=0.3)

    axis_pts = np.array([-1.6 * n, 1.6 * n])
    ax.plot(axis_pts[:, 0], axis_pts[:, 1], axis_pts[:, 2], color="crimson", lw=2.5,
            label=f"eje de rotación  ω = {np.round(omega_local,2)}")

    ax.set_xlabel("x1"); ax.set_ylabel("x2"); ax.set_zlabel("x3")
    ax.set_title("RECP2_2014 ej.2 — rotación rígida alrededor de un eje OBLICUO\n"
                 "$v=(-3x_2{+}x_3,\\;3x_1{-}5x_3,\\;{-}x_1{+}5x_2)$   —   $V\\equiv 0$ en todo punto",
                 fontsize=12)
    ax.legend(loc="upper left", fontsize=9)
    fig.tight_layout()
    fig.savefig("fig6_rotacion_eje_oblicuo.png", dpi=130, bbox_inches="tight")
    print("  -> fig6_rotacion_eje_oblicuo.png")


if __name__ == "__main__":
    print("Generando figuras de ejercicios de parciales viejos (Unidad 6)...")
    figura_fuente_potencial()
    figura_perfiles_corte()
    figura_rotacion_eje_oblicuo()
    print("Listo. Abrí los PNG generados.")
