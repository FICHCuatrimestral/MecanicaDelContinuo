# Visualizaciones

Todo lo que se ve: las figuras del apunte, los scripts que las generan, y las simulaciones de partículas.

Cada script guarda sus salidas **en esta misma carpeta**, así que se corren desde acá sin argumentos:

```bash
python visualizacion_cinematica.py
```

Requieren `numpy` y `matplotlib`; las simulaciones además `pillow` (para exportar el `.gif`).

## Figuras del apunte

Las embebe [`../Teoria/apunte_U3-U10.md`](../Teoria/apunte_U3-U10.md). Cada `fig_*.png` sale del script indicado:

| Script | Figuras que genera | Tema |
|---|---|---|
| `visualizacion_fibra_isotropia.py` | `fig_geometria_fibra.png`, `fig_isotropia_comparacion.png` | U5 — deformación de una fibra, isotropía |
| `visualizacion_viga_flexion.py` | `fig_viga_flexion.png` | U5 — campo de desplazamientos en flexión |
| `visualizacion_cinematica.py` | `fig1_zoologico_divergencia.png`, `fig2_deformacion_vs_rotacion.png`, `fig3_shear_descompuesto.png` | U6 — gradiente de velocidad y su descomposición |
| `visualizacion_parciales_viejos.py` | `fig4_fuente_potencial.png`, `fig5_perfiles_corte_z.png`, `fig6_rotacion_eje_oblicuo.png` | U6 — casos tomados en parciales |
| `visualizacion_poiseuille_3d.py` | `fig7_poiseuille_3d.png` | U6 — flujo de Poiseuille |
| `visualizacion_constitutivas.py` | `fig_vol_desviador.png`, `fig_tres_modelos_tiempo.png`, `fig_incompresibilidad_limite.png` | U7 — volumétrico/desviador, los tres modelos |
| `visualizacion_isotropia_rotacion.py` | `fig_test_isotropia_rotacion.png` | U8 — test de isotropía por rotación |
| `visualizacion_derivada_material_lagr_euler.py` | `fig_derivada_material_lagr_euler.png` | U9-U10 — lagrangiano vs. euleriano |
| `visualizacion_derivada_material_2023_1.py` | `fig_observador_fijo_vs_viajero.png` | U9-U10 — observador fijo vs. viajero |
| `visualizacion_gauss_reynolds.py` | `fig_gauss_reynolds.png` | U9-U10 — Gauss y Reynolds |

## Simulaciones de partículas

Simulaciones chicas que ponen en movimiento la distinción central de la Unidad 7 (constitutivas): un fluido newtoniano (σ acoplado a la *tasa* de deformación) vs. un sólido Hookeano (σ acoplado a la deformación misma — "memoria de forma"), y el rol físico de μ dentro del propio fluido.

### `sph_fluido_dambreak.py` → `sph_dambreak.gif`

Fluido newtoniano discretizado en partículas (**SPH — Smoothed Particle Hydrodynamics**): una columna de agua colapsa y se desparrama por el piso. Cada partícula calcula presión (ecuación de estado de Tait) y viscosidad (término laminar, la contraparte discreta de $\mu\nabla^2\mathbf v$) a partir de sus vecinas, vía un kernel suavizador. Una vez que se desparrama, **se queda desparramado** — el fluido no tiene forma de referencia a la cual volver.

### `masa_resorte_solido.py` → `solido_rebote.gif`

Sólido elástico discretizado como una grilla masa-resorte (resortes estructurales + diagonales, estos últimos dan rigidez de corte — el análogo discreto de $\mu$ en $\sigma_{ij}=\lambda\,\text{tr}(\varepsilon)\delta_{ij}+2\mu\varepsilon_{ij}$). Cae, se aplasta contra el piso, y **recupera su forma** — la memoria de forma de Hooke, visible.

### `vortice_agua_miel.py` → `vortice_agua_miel.gif`

Mismo motor SPH que el dam-break, pero ahora **agua y miel lado a lado**, mismo disco de fluido con rotación diferencial inicial (sin gravedad, para aislar el efecto viscoso puro). Con μ mucho más alto, la miel disipa más energía cinética y su velocidad pico decae más rápido — la ecuación es literalmente la misma, solo cambia μ. La diferencia acá es más sutil a simple vista que en un flujo forzado (ver `fig_incompresibilidad_limite.png` o el ejemplo de Poiseuille del apunte): en un decaimiento libre el efecto de μ se nota en la *tasa*, no en un multiplicador inmediato como en un tubo en régimen estacionario.

### Correrlas

```bash
python sph_fluido_dambreak.py       # ~1-2 min, genera sph_dambreak.gif
python masa_resorte_solido.py       # ~1-2 min, genera solido_rebote.gif
python vortice_agua_miel.py         # ~5-8 min (corre agua Y miel), genera vortice_agua_miel.gif
```

Son deliberadamente simples (SPH sin partículas de borde reales, masa-resorte sin isotropía estricta) — el objetivo es *ver* la distinción de U7, no un solver de producción.
