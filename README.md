# Mecánica del Continuo

Apuntes, guías y material de la cursada. Tres carpetas: lo que se lee, lo que se resuelve, y lo que se mira.

```
Teoria/           capítulos de la cátedra + apuntes propios
Practica/         guías, parciales viejos, trabajo práctico
Visualizaciones/  figuras del apunte, scripts que las generan, simulaciones
```

## Material de estudio

| Archivo | Qué es |
|---|---|
| [`Teoria/apunte_U3-U10.md`](Teoria/apunte_U3-U10.md) | **La referencia completa.** El curso entero en un solo documento: Tensiones y direcciones principales (U3-U4), Deformaciones, Velocidades, Ecuaciones Constitutivas e Isotropía (U5-U8), y Ecuaciones de Campo y Principios Variacionales (U9-U10). Con visualizaciones. |
| [`Teoria/guion_balances.md`](Teoria/guion_balances.md) | **El guion de las demostraciones.** Los tres balances (masa, cantidad de movimiento, energía) paso a paso, para recitar de memoria. Incluye la lista negra de errores típicos. |
| [`Teoria/repaso_furioso.html`](Teoria/repaso_furioso.html) | **El día previo al parcial.** Página autocontenida para abrir en el navegador: patrones de los parciales año por año, plan del día por bloques, formulario con **modo tapado** para memorizar, las cinco demostraciones a reproducir de memoria, y el banco de preguntas sintéticas. Se imprime bien (Ctrl+P revela todas las fórmulas). |

## Estructura

### `Teoria/`

Los capítulos de la cátedra (`Cap01`...`Cap10`), la bibliografía (`Fung1994.pdf`), la planificación de la materia, y los tres documentos de estudio de la tabla de arriba.

### `Practica/`

- `Guias/` — las guías de ejercicios de todas las unidades, más las notas de clase asociadas.
- `Parciales/` — parciales viejos de ambas partes, varios con solución.
- `TrabajoPractico/` — el TP de la cursada: consigna, notebooks, informe LaTeX y sus salidas. Es autocontenido, con sus propias carpetas `Imagenes/` y `outputs/`.

### `Visualizaciones/`

Todas las figuras del apunte (`fig_*.png`), los scripts que las generan (`visualizacion_*.py`) y las simulaciones de partículas (fluido SPH vs. sólido masa-resorte). Cada script guarda su salida en esa misma carpeta, así que se corre desde ahí sin argumentos. Ver [`Visualizaciones/README.md`](Visualizaciones/README.md) para el mapa de qué script genera qué figura.

## Convención de nombres

Sin espacios, sin acentos y sin caracteres especiales, para que los enlaces funcionen y los archivos ordenen alfabéticamente.

**Parciales** — `P{1,2}_<año>[_recu][_resuelto].{pdf,jpg}`

```
P1_2016_resuelto.pdf          Parcial 1 de 2016, con solución
P2_2024_recu.pdf              Recuperatorio del Parcial 2 de 2024, sin solución
P1_2019_recu_resuelto.pdf     Recuperatorio del Parcial 1 de 2019, con solución
P2_2025_24jun.jpg             Parcial 2 de 2025 — hubo dos fechas, se desambigua con el día
```

**Capítulos de teoría** — `Cap<NN>_<Titulo>.pdf`, numeración arábiga con cero a la izquierda (`Cap03_Tensiones.pdf`), para que ordenen bien.

**Guías** — `Guia<N>.pdf`, y las notas de clase asociadas `Guia<N>_Ej<n>_notas.pdf`.

**Figuras y scripts** — `fig_<tema>.png` generada por `visualizacion_<tema>.py`, ambos en `Visualizaciones/`.
