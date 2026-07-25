# Simulaciones de partículas

Simulaciones chicas que ponen en movimiento la distinción central de la Unidad 7 (constitutivas): un fluido newtoniano (σ acoplado a la *tasa* de deformación) vs. un sólido Hookeano (σ acoplado a la deformación misma — "memoria de forma"), y el rol físico de μ dentro del propio fluido.

## `sph_fluido_dambreak.py` → `sph_dambreak.gif`

Fluido newtoniano discretizado en partículas (**SPH — Smoothed Particle Hydrodynamics**): una columna de agua colapsa y se desparrama por el piso. Cada partícula calcula presión (ecuación de estado de Tait) y viscosidad (término laminar, la contraparte discreta de $\mu\nabla^2\mathbf v$) a partir de sus vecinas, vía un kernel suavizador. Una vez que se desparrama, **se queda desparramado** — el fluido no tiene forma de referencia a la cual volver.

## `masa_resorte_solido.py` → `solido_rebote.gif`

Sólido elástico discretizado como una grilla masa-resorte (resortes estructurales + diagonales, estos últimos dan rigidez de corte — el análogo discreto de $\mu$ en $\sigma_{ij}=\lambda\,\text{tr}(\varepsilon)\delta_{ij}+2\mu\varepsilon_{ij}$). Cae, se aplasta contra el piso, y **recupera su forma** — la memoria de forma de Hooke, visible.

## `vortice_agua_miel.py` → `vortice_agua_miel.gif`

Mismo motor SPH que el dam-break, pero ahora **agua y miel lado a lado**, mismo disco de fluido con rotación diferencial inicial (sin gravedad, para aislar el efecto viscoso puro). Con μ mucho más alto, la miel disipa más energía cinética y su velocidad pico decae más rápido — la ecuación es literalmente la misma, solo cambia μ. La diferencia acá es más sutil a simple vista que en un flujo forzado (ver `U7/fig_incompresibilidad_limite.png` o el ejemplo de Poiseuille del apunte): en un decaimiento libre el efecto de μ se nota en la *tasa*, no en un multiplicador inmediato como en un tubo en régimen estacionario.

## Correrlas

```bash
python sph_fluido_dambreak.py       # ~1-2 min, genera sph_dambreak.gif
python masa_resorte_solido.py       # ~1-2 min, genera solido_rebote.gif
python vortice_agua_miel.py          # ~5-8 min (corre agua Y miel), genera vortice_agua_miel.gif
```

Requieren `numpy`, `matplotlib` y `pillow` (para exportar el `.gif`).

Son deliberadamente simples (SPH sin partículas de borde reales, masa-resorte sin isotropía estricta) — el objetivo es *ver* la distinción de U7, no un solver de producción.
