"""
Simulacion de particulas: SOLIDO HOOKEANO via masa-resorte, cayendo y
rebotando contra el piso.
=============================================================================
El contraste directo con el fluido SPH del otro script (misma carpeta):
ahi el fluido, una vez que se desparrama, se queda desparramado para
siempre (no tiene "forma de referencia" a la cual volver -- U7, sigma
acoplado a la TASA V). Aca, un solido elastico cae, se aplasta contra el
piso, y VUELVE a su forma original -- porque sigma esta acoplado a la
DEFORMACION epsilon (memoria de forma), no a la velocidad.

Discretizacion: una grilla de particulas conectadas por resortes.
  - resortes estructurales (horizontales/verticales): resisten cambio de
    longitud en x e y por separado.
  - resortes diagonales (de corte): sin ellos, la grilla se corta como un
    rombo sin resistencia -- son los que le dan rigidez de CORTE a la
    malla, el analogo discreto de mu en sigma_ij = lambda*tr(eps)*delta +
    2*mu*eps_ij.

Ley de cada resorte: F = -k*(longitud_actual - longitud_de_reposo), la
version mas simple posible de "memoria de forma" -- exactamente Hooke,
particula a particula.

Corre con: python masa_resorte_solido.py
Genera: solido_rebote.gif
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---------------------- grilla del solido ----------------------
NX, NY = 9, 9
SPACING = 0.30
K_STRUCT = 900.0
K_SHEAR = 500.0
MASS = 0.06
DAMPING = 0.03         # amortiguamiento global (viscoelastico leve)
GRAVITY = -9.8
FLOOR_Y = 0.0
FLOOR_K = 4000.0        # rigidez de penalizacion del piso
FLOOR_DAMP = 8.0

X0, Y0 = 1.0, 2.6       # posicion inicial (cae desde altura Y0)

xs = np.arange(NX) * SPACING
ys = np.arange(NY) * SPACING
Xg, Yg = np.meshgrid(xs, ys)
pos0 = np.stack([Xg.ravel() + X0, Yg.ravel() + Y0], axis=1)
N = pos0.shape[0]


def idx(i, j):
    return j * NX + i


springs_a, springs_b, rest, kk = [], [], [], []


def add_spring(a, b, k):
    springs_a.append(a)
    springs_b.append(b)
    rest.append(np.linalg.norm(pos0[a] - pos0[b]))
    kk.append(k)


for j in range(NY):
    for i in range(NX):
        if i < NX - 1:
            add_spring(idx(i, j), idx(i + 1, j), K_STRUCT)
        if j < NY - 1:
            add_spring(idx(i, j), idx(i, j + 1), K_STRUCT)
        if i < NX - 1 and j < NY - 1:
            add_spring(idx(i, j), idx(i + 1, j + 1), K_SHEAR)
            add_spring(idx(i + 1, j), idx(i, j + 1), K_SHEAR)

springs_a = np.array(springs_a)
springs_b = np.array(springs_b)
rest = np.array(rest)
kk = np.array(kk)

print(f"N particulas = {N}, N resortes = {len(springs_a)}")


def compute_forces(pos, vel):
    d = pos[springs_a] - pos[springs_b]              # (Ns,2)
    length = np.linalg.norm(d, axis=1)                # (Ns,)
    length_safe = np.where(length > 1e-9, length, 1e-9)
    dirn = d / length_safe[:, None]
    fmag = -kk * (length - rest)                       # negativo si estirado -> atrae
    fvec = fmag[:, None] * dirn                          # fuerza sobre 'a'

    force = np.zeros_like(pos)
    np.add.at(force, springs_a, fvec)
    np.add.at(force, springs_b, -fvec)

    # gravedad
    force[:, 1] += MASS * GRAVITY

    # amortiguamiento viscoso interno (proporcional a velocidad)
    force -= DAMPING * vel

    # piso: penalizacion tipo resorte + amortiguador, solo si penetra
    penetr = FLOOR_Y - pos[:, 1]
    hit = penetr > 0
    force[hit, 1] += FLOOR_K * penetr[hit] - FLOOR_DAMP * vel[hit, 1]
    # friccion simple con el piso (frena la velocidad horizontal si esta apoyado)
    force[hit, 0] -= 3.0 * vel[hit, 0]

    return force


def step(pos, vel, dt):
    force = compute_forces(pos, vel)
    acc = force / MASS
    vel_new = vel + acc * dt
    pos_new = pos + vel_new * dt
    return pos_new, vel_new


DT = 0.0006
STEPS_PER_FRAME = 10
N_FRAMES = 260

# ------------------- indices del contorno, para dibujar la malla -------------------
edges = []
for j in range(NY):
    for i in range(NX - 1):
        edges.append((idx(i, j), idx(i + 1, j)))
for i in range(NX):
    for j in range(NY - 1):
        edges.append((idx(i, j), idx(i, j + 1)))
edges = np.array(edges)

fig, ax = plt.subplots(figsize=(7, 6))
ax.axhline(FLOOR_Y, color="0.3", lw=3)
lines = ax.plot(
    np.zeros((2, len(edges))), np.zeros((2, len(edges))),
    color="steelblue", lw=1.0, alpha=0.7,
)
scat = ax.scatter(pos0[:, 0], pos0[:, 1], s=18, color="firebrick", zorder=5)
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.3, 4.0)
ax.set_aspect("equal")
title = ax.set_title("Sólido Hookeano (masa-resorte) — cae, rebota, recupera forma (t=0.00 s)")
fig.tight_layout()

state = {"pos": pos0.copy(), "vel": np.zeros_like(pos0), "t": 0.0}


def update(frame):
    p, v = state["pos"], state["vel"]
    for _ in range(STEPS_PER_FRAME):
        p, v = step(p, v, DT)
        state["t"] += DT
    state["pos"], state["vel"] = p, v

    for k, (a, b) in enumerate(edges):
        lines[k].set_data([p[a, 0], p[b, 0]], [p[a, 1], p[b, 1]])
    scat.set_offsets(p)
    title.set_text(f"Sólido Hookeano (masa-resorte) — cae, rebota, recupera forma (t={state['t']:.2f} s)")
    return (*lines, scat, title)


if __name__ == "__main__":
    print("Simulando y animando (puede tardar un minuto)...")
    anim = animation.FuncAnimation(fig, update, frames=N_FRAMES, blit=False)
    writer = animation.PillowWriter(fps=24)
    anim.save("solido_rebote.gif", writer=writer, dpi=110)
    print("-> solido_rebote.gif")
