"""
Vortice girando: AGUA vs MIEL, lado a lado, mismo motor SPH que
sph_fluido_dambreak.py -- misma ecuacion, solo cambia mu.
=============================================================================
Se arma un disco de fluido con un campo de velocidad inicial en remolino
(rotacion diferencial: las capas internas giran mas rapido que las
externas -- por eso hay corte, y por eso la viscosidad tiene algo para
suavizar). Sin gravedad, para aislar el efecto puramente viscoso.

Lo que deberia verse: el nucleo del vortice se difunde/ensancha con el
tiempo -- exactamente el problema de Lamb-Oseen (solucion exacta de
Navier-Stokes viscoso), donde el radio del nucleo crece como sqrt(4*nu*t).
Con nu = mu/rho mucho mas grande en la miel, su vortice se "emborrona"
mucho mas rapido que el del agua, con la MISMA ecuacion.

Corre con: python vortice_agua_miel.py
Genera: vortice_agua_miel.gif
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

RHO0 = 1000.0
GAMMA = 7.0
C0 = 10.0
B_TAIT = C0**2 * RHO0 / GAMMA

SPACING = 0.22
H = 1.3 * SPACING
DOMAIN = (-3.2, 3.2)   # mismo dominio en x e y (cuadrado)

R_DISK = 2.3
R_CORE = 0.75
OMEGA0 = 6.0

# ---------------------- particulas: disco lleno ----------------------
xs = np.arange(-R_DISK, R_DISK + 1e-9, SPACING)
Xg, Yg = np.meshgrid(xs, xs)
mask = Xg**2 + Yg**2 <= R_DISK**2
pos0 = np.stack([Xg[mask], Yg[mask]], axis=1)
N = pos0.shape[0]
mass = np.full(N, RHO0 * SPACING**2)
print(f"N particulas (por simulacion) = {N}")

r0 = np.linalg.norm(pos0, axis=1)
vtheta0 = OMEGA0 * r0 * np.exp(-(r0 / R_CORE) ** 2)
with np.errstate(divide="ignore", invalid="ignore"):
    vel0 = np.stack([
        np.where(r0 > 1e-9, -vtheta0 * pos0[:, 1] / np.maximum(r0, 1e-9), 0.0),
        np.where(r0 > 1e-9, vtheta0 * pos0[:, 0] / np.maximum(r0, 1e-9), 0.0),
    ], axis=1)

SIGMA = 10.0 / (7.0 * np.pi * H**2)


def kernel_and_grad(r, rij):
    q = r / H
    W = np.zeros_like(r)
    dWdq = np.zeros_like(r)
    m1 = (q >= 0) & (q < 1)
    m2 = (q >= 1) & (q < 2)
    W[m1] = SIGMA * (1 - 1.5 * q[m1] ** 2 + 0.75 * q[m1] ** 3)
    W[m2] = SIGMA * 0.25 * (2 - q[m2]) ** 3
    dWdq[m1] = SIGMA * (-3 * q[m1] + 2.25 * q[m1] ** 2)
    dWdq[m2] = -SIGMA * 0.75 * (2 - q[m2]) ** 2
    dWdr = dWdq / H
    with np.errstate(divide="ignore", invalid="ignore"):
        factor = np.where(r > 1e-9, dWdr / r, 0.0)
    gradW = rij * factor[:, :, None]
    return W, gradW


def step(pos, vel, mu, dt):
    diff = pos[:, None, :] - pos[None, :, :]
    r = np.linalg.norm(diff, axis=-1)
    within = r < 2 * H
    np.fill_diagonal(within, False)

    W, gradW = kernel_and_grad(np.where(within, r, 0.0), diff)
    W = W * within
    gradW = gradW * within[:, :, None]

    rho = mass @ W.T + mass * SIGMA
    rho = np.maximum(rho, 0.35 * RHO0)

    press = B_TAIT * ((rho / RHO0) ** GAMMA - 1.0)
    press = np.maximum(press, 0.0)

    Pi_over_rho2 = press / rho**2
    coef_p = Pi_over_rho2[:, None] + Pi_over_rho2[None, :]
    acc_press = -np.einsum("ij,ijk,j->ik", coef_p, gradW, mass)

    vdiff = vel[:, None, :] - vel[None, :, :]
    r2 = r**2 + 0.01 * H**2
    dot_rv = np.einsum("ijk,ijk->ij", diff, gradW)
    visc_coef = (mass[None, :] * (2 * mu) / (rho[:, None] * rho[None, :])) * (dot_rv / r2)
    visc_coef = visc_coef * within
    acc_visc = np.einsum("ij,ijk->ik", visc_coef, vdiff)

    acc = acc_press + acc_visc

    vel_new = vel + acc * dt
    pos_new = pos + vel_new * dt

    # dominio grande, solo un tope de seguridad blando (no deberia activarse)
    for dim in range(2):
        lo, hi = DOMAIN
        below = pos_new[:, dim] < lo
        above = pos_new[:, dim] > hi
        pos_new[below, dim] = lo
        pos_new[above, dim] = hi
        vel_new[below, dim] *= -0.3
        vel_new[above, dim] *= -0.3

    return pos_new, vel_new, rho


MU_AGUA = 0.25
MU_MIEL = 25.0
DT = 0.0004
STEPS_PER_FRAME = 8
N_FRAMES = 220
VMAX_COLOR = 2.0

if __name__ == "__main__":
    import sys
    n_test = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    if n_test:
        for nombre, mu in [("AGUA", MU_AGUA), ("MIEL", MU_MIEL)]:
            p, v = pos0.copy(), vel0.copy()
            for i in range(n_test):
                p, v, rho = step(p, v, mu, DT)
                if not np.isfinite(p).all() or not np.isfinite(v).all():
                    print(f"{nombre}: BLOWUP en paso {i}")
                    break
            else:
                print(f"{nombre}: OK {n_test} pasos, |v|max={np.linalg.norm(v,axis=1).max():.3f}, "
                      f"rho=[{rho.min():.0f},{rho.max():.0f}]")
        sys.exit()

    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, (axA, axM) = plt.subplots(1, 2, figsize=(12, 6))
    state = {
        "AGUA": {"pos": pos0.copy(), "vel": vel0.copy(), "mu": MU_AGUA, "ax": axA, "t": 0.0},
        "MIEL": {"pos": pos0.copy(), "vel": vel0.copy(), "mu": MU_MIEL, "ax": axM, "t": 0.0},
    }
    scats = {}
    for nombre, s in state.items():
        speed0 = np.linalg.norm(s["vel"], axis=1)
        sc = s["ax"].scatter(s["pos"][:, 0], s["pos"][:, 1], c=speed0, cmap="inferno",
                              vmin=0, vmax=VMAX_COLOR, s=20)
        s["ax"].set_xlim(-R_DISK - 0.3, R_DISK + 0.3)
        s["ax"].set_ylim(-R_DISK - 0.3, R_DISK + 0.3)
        s["ax"].set_aspect("equal")
        mu_lbl = f"$\\mu$={s['mu']}"
        s["ax"].set_title(f"{nombre} ({mu_lbl})")
        scats[nombre] = sc
    fig.colorbar(scats["AGUA"], ax=[axA, axM], shrink=0.75, label="rapidez |v|")
    suptitle = fig.suptitle("Vórtice difundiéndose — misma ecuación (Navier-Stokes), solo cambia μ (t=0.00 s)",
                             fontsize=13)

    def update(frame):
        for nombre, s in state.items():
            p, v = s["pos"], s["vel"]
            for _ in range(STEPS_PER_FRAME):
                p, v, rho = step(p, v, s["mu"], DT)
                s["t"] += DT
            s["pos"], s["vel"] = p, v
            speed = np.linalg.norm(v, axis=1)
            scats[nombre].set_offsets(p)
            scats[nombre].set_array(speed)
        suptitle.set_text(
            f"Vórtice difundiéndose — misma ecuación (Navier-Stokes), solo cambia μ (t={state['AGUA']['t']:.2f} s)"
        )
        return (*scats.values(), suptitle)

    print("Simulando y animando ambos fluidos (puede tardar varios minutos)...")
    anim = animation.FuncAnimation(fig, update, frames=N_FRAMES, blit=False)
    writer = animation.PillowWriter(fps=20)
    anim.save("vortice_agua_miel.gif", writer=writer, dpi=105)
    print("-> vortice_agua_miel.gif")
