"""
Simulacion de particulas: FLUIDO NEWTONIANO via SPH (Smoothed Particle
Hydrodynamics), escenario "dam break" (colapso de una columna de agua).
==========================================================================
Esto es la Unidad 7 (constitutiva newtoniana) hecha animacion: en vez de
resolver Navier-Stokes con derivadas continuas, se discretiza el fluido
en particulas que cargan masa, y se aproxima cada derivada espacial como
una suma pesada sobre los vecinos (el "kernel" W). El resultado es el
mismo tipo de ecuacion que dedujimos a mano:

    rho * Dv/Dt = -grad(p) + mu * laplaciano(v) + rho*g

pero en vez de resolverla con condiciones de borde analiticas (como el
tubo de Poiseuille), se le da vida punto a punto: cada particula "siente"
presion (que empuja para igualar densidades) y viscosidad (que resiste
el corte, exactamente como el sigma_ij = -p*delta + 2*mu*V_ij de U7).

Ecuacion de estado (Tait, weakly-compressible): la presion es una
funcion empinada de la densidad, para que el fluido se comporte casi
incompresible sin resolver una restriccion dura.

Corre con: python sph_fluido_dambreak.py
Genera: sph_dambreak.gif
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(0)

# ---------------------- parametros fisicos ----------------------
RHO0 = 1000.0        # densidad de referencia (agua, kg/m^3 "conceptual")
MU = 3.0             # viscosidad dinamica (mas alta que el agua real, para que
                      # el video se vea suave con pocas particulas)
GRAVITY = -9.8
GAMMA = 7.0          # exponente de Tait
C0 = 12.0            # "velocidad del sonido" artificial (controla rigidez/dt)
B_TAIT = C0**2 * RHO0 / GAMMA

# ---------------------- dominio y particulas ----------------------
SPACING = 0.20
H = 1.3 * SPACING          # longitud de suavizado (smoothing length)
DOMAIN_X = (0.0, 8.0)
DOMAIN_Y = (0.0, 5.0)

# bloque inicial de agua: columna a la izquierda
xs = np.arange(0.15, 2.6, SPACING)
ys = np.arange(0.15, 3.6, SPACING)
X, Y = np.meshgrid(xs, ys)
pos = np.stack([X.ravel(), Y.ravel()], axis=1)
N = pos.shape[0]
mass = np.full(N, RHO0 * SPACING**2)
vel = np.zeros((N, 2))

print(f"N particulas = {N}")

# ---------------------- kernel cubico (M4), 2D ----------------------
SIGMA = 10.0 / (7.0 * np.pi * H**2)


def kernel_and_grad(r, rij):
    """r: (N,N) distancias; rij: (N,N,2) vectores. Devuelve W y grad_W (N,N,2)."""
    q = r / H
    W = np.zeros_like(r)
    dWdq = np.zeros_like(r)

    m1 = (q >= 0) & (q < 1)
    m2 = (q >= 1) & (q < 2)

    W[m1] = SIGMA * (1 - 1.5 * q[m1]**2 + 0.75 * q[m1]**3)
    W[m2] = SIGMA * 0.25 * (2 - q[m2])**3

    dWdq[m1] = SIGMA * (-3 * q[m1] + 2.25 * q[m1]**2)
    dWdq[m2] = -SIGMA * 0.75 * (2 - q[m2])**2

    dWdr = dWdq / H
    with np.errstate(divide="ignore", invalid="ignore"):
        factor = np.where(r > 1e-9, dWdr / r, 0.0)
    gradW = rij * factor[:, :, None]
    return W, gradW


def step(pos, vel, dt):
    diff = pos[:, None, :] - pos[None, :, :]        # rij = ri - rj  (N,N,2)
    r = np.linalg.norm(diff, axis=-1)                # (N,N)
    within = r < 2 * H
    np.fill_diagonal(within, False)

    W, gradW = kernel_and_grad(np.where(within, r, 0.0), diff)
    W = W * within
    gradW = gradW * within[:, :, None]

    # densidad por particula (suma incluye self-contribution vía W(0))
    q0 = np.zeros(1)
    W0 = SIGMA  # W(0)
    rho = mass @ W.T + mass * W0  # (N,)  (aprox: self kernel contribution)
    rho = np.maximum(rho, 0.35 * RHO0)  # piso de seguridad numerica

    # presion (Tait)
    press = B_TAIT * ((rho / RHO0) ** GAMMA - 1.0)
    press = np.maximum(press, 0.0)  # solo empuja, no succiona (mas estable)

    # ---- fuerza de presion (forma simetrica estandar de SPH) ----
    Pi_over_rho2 = press / rho**2
    coef_p = Pi_over_rho2[:, None] + Pi_over_rho2[None, :]  # (N,N)
    acc_press = -np.einsum("ij,ijk,j->ik", coef_p, gradW, mass)

    # ---- viscosidad laminar aproximada (Morris et al.) ----
    vdiff = vel[:, None, :] - vel[None, :, :]        # (N,N,2)
    r2 = r**2 + 0.01 * H**2
    dot_rv = np.einsum("ijk,ijk->ij", diff, gradW)
    visc_coef = (mass[None, :] * (MU + MU) / (rho[:, None] * rho[None, :])) * (dot_rv / r2)
    visc_coef = visc_coef * within
    acc_visc = np.einsum("ij,ijk->ik", visc_coef, vdiff)

    acc = acc_press + acc_visc
    acc[:, 1] += GRAVITY

    # ---- integracion (Euler simplectico) ----
    vel_new = vel + acc * dt
    pos_new = pos + vel_new * dt

    # ---- paredes: reflejar con restitucion ----
    REST = 0.35
    for dim, (lo, hi) in enumerate([DOMAIN_X, DOMAIN_Y]):
        below = pos_new[:, dim] < lo
        above = pos_new[:, dim] > hi
        pos_new[below, dim] = lo
        pos_new[above, dim] = hi
        vel_new[below, dim] *= -REST
        vel_new[above, dim] *= -REST

    return pos_new, vel_new, rho


DT = 0.00035
STEPS_PER_FRAME = 12
N_FRAMES = 160

fig, ax = plt.subplots(figsize=(8, 5.2))
scat = ax.scatter(pos[:, 0], pos[:, 1], s=14, c=np.zeros(N), cmap="viridis", vmin=800, vmax=1250)
ax.set_xlim(*DOMAIN_X)
ax.set_ylim(*DOMAIN_Y)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
title = ax.set_title("SPH dam-break — fluido newtoniano (t=0.00 s)")
cbar = fig.colorbar(scat, ax=ax, label="densidad local (kg/m³)")
fig.tight_layout()

state = {"pos": pos, "vel": vel, "t": 0.0}


def update(frame):
    p, v = state["pos"], state["vel"]
    for _ in range(STEPS_PER_FRAME):
        p, v, rho = step(p, v, DT)
        state["t"] += DT
    state["pos"], state["vel"] = p, v
    scat.set_offsets(p)
    scat.set_array(rho)
    title.set_text(f"SPH dam-break — fluido newtoniano (t={state['t']:.2f} s)")
    return scat, title


if __name__ == "__main__":
    print("Simulando y animando (puede tardar un minuto)...")
    anim = animation.FuncAnimation(fig, update, frames=N_FRAMES, blit=False)
    writer = animation.PillowWriter(fps=24)
    anim.save("sph_dambreak.gif", writer=writer, dpi=110)
    print("-> sph_dambreak.gif")
