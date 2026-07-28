# Mecánica del Continuo

Apuntes, guías y material de la cursada.

## Material de estudio

| Archivo | Qué es |
|---|---|
| [`apunte_U3-U10.md`](apunte_U3-U10.md) | **La referencia completa.** El curso entero en un solo documento: Tensiones y direcciones principales (U3-U4), Deformaciones, Velocidades, Ecuaciones Constitutivas e Isotropía (U5-U8), y Ecuaciones de Campo y Principios Variacionales (U9-U10). Con visualizaciones. |
| [`guion_balances.md`](guion_balances.md) | **El guion de las demostraciones.** Los tres balances (masa, cantidad de movimiento, energía) paso a paso, para recitar de memoria. Incluye la lista negra de errores típicos. |
| [`repaso_furioso.html`](repaso_furioso.html) | **El día previo al parcial.** Página autocontenida para abrir en el navegador: patrones de los parciales año por año, plan del día por bloques, formulario con **modo tapado** para memorizar, las cinco demostraciones a reproducir de memoria, y el banco de preguntas sintéticas. Se imprime bien (Ctrl+P revela todas las fórmulas). |

Cada unidad tiene su carpeta (`U1`...`U8`, `U9-U10`) con el capítulo en PDF, la guía de ejercicios, y — de la U5 en adelante — un script `visualizacion_*.py` que genera las figuras (`fig_*.png`) embebidas en los apuntes. Para regenerarlas: `python visualizacion_*.py` desde la carpeta de la unidad (requiere `numpy` y `matplotlib`).

## Estructura

- `U1`–`U8`, `U9-U10`: material por unidad (teoría, guía, figuras).
- `Parciales1`, `Parciales2`: parciales viejos, organizados por parte del examen.
- `TrabajoPractico`: TP de la cursada (notebooks, informe, simulaciones).
- `Simulaciones`: fluido (SPH) vs. sólido (masa-resorte) — la distinción de la U7 hecha animación. Ver [`Simulaciones/README.md`](Simulaciones/README.md).
- `Material_General`: bibliografía y planificación de la materia, no atadas a una unidad puntual.

## Convención de nombres

Sin espacios, sin acentos y sin caracteres especiales, para que los enlaces funcionen y los archivos ordenen alfabéticamente.

**Parciales** — `P{1,2}_<año>[_recu][_resuelto].{pdf,jpg}`

```
P1_2016_resuelto.pdf        Parcial 1 de 2016, con solución
P2_2024_recu.pdf            Recuperatorio del Parcial 2 de 2024, sin solución
P1_2019_recu_resuelto.pdf   Recuperatorio del Parcial 1 de 2019, con solución
P2_2025_24jun.jpg           Parcial 2 de 2025 — hubo dos fechas, se desambigua con el día
```

**Capítulos de teoría** — `Cap<NN>_<Titulo>.pdf`, numeración arábiga con cero a la izquierda (`Cap03_Tensiones.pdf`), para que ordenen bien.

**Guías** — `Guia<N>.pdf`, y las notas de clase asociadas `Guia<N>_Ej<n>_notas.pdf`.

**Figuras y scripts** — `fig_<tema>.png` generada por `visualizacion_<tema>.py`, en la carpeta de la unidad.
