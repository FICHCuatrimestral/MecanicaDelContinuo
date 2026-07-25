# Simulaciones de partículas

Dos simulaciones chicas que ponen en movimiento la distinción central de la Unidad 7 (constitutivas): un fluido newtoniano (σ acoplado a la *tasa* de deformación) vs. un sólido Hookeano (σ acoplado a la deformación misma — "memoria de forma").

## `sph_fluido_dambreak.py` → `sph_dambreak.gif`

Fluido newtoniano discretizado en partículas (**SPH — Smoothed Particle Hydrodynamics**): una columna de agua colapsa y se desparrama por el piso. Cada partícula calcula presión (ecuación de estado de Tait) y viscosidad (término laminar, la contraparte discreta de $\mu\nabla^2\mathbf v$) a partir de sus vecinas, vía un kernel suavizador. Una vez que se desparrama, **se queda desparramado** — el fluido no tiene forma de referencia a la cual volver.

## `masa_resorte_solido.py` → `solido_rebote.gif`

Sólido elástico discretizado como una grilla masa-resorte (resortes estructurales + diagonales, estos últimos dan rigidez de corte — el análogo discreto de $\mu$ en $\sigma_{ij}=\lambda\,\text{tr}(\varepsilon)\delta_{ij}+2\mu\varepsilon_{ij}$). Cae, se aplasta contra el piso, y **recupera su forma** — la memoria de forma de Hooke, visible.

## Correrlas

```bash
python sph_fluido_dambreak.py       # ~1-2 min, genera sph_dambreak.gif
python masa_resorte_solido.py       # ~1-2 min, genera solido_rebote.gif
```

Requieren `numpy`, `matplotlib` y `pillow` (para exportar el `.gif`).

Son deliberadamente simples (SPH sin partículas de borde reales, masa-resorte sin isotropía estricta) — el objetivo es *ver* la distinción de U7, no un solver de producción.
