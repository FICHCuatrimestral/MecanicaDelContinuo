# Mecánica del Continuo

Apuntes, guías y material de la cursada.

## Apunte de estudio (con visualizaciones)

[`apunte_U5-U10.md`](apunte_U5-U10.md) — el curso completo en un solo documento: Tensiones y direcciones principales (U3-U4), Deformaciones, Velocidades, Ecuaciones Constitutivas e Isotropía (U5-U8), y Ecuaciones de Campo y Principios Variacionales (U9-U10).

## Repaso de un día (antes del parcial)

[`repaso-furioso.html`](repaso-furioso.html) — página autocontenida para abrir en el navegador: patrones de los parciales año por año, plan del día por bloques, formulario completo con **modo tapado** para memorizar, las cinco demostraciones a reproducir de memoria, y el banco de preguntas sintéticas. Se imprime bien (Ctrl+P revela todas las fórmulas).

Cada unidad tiene su carpeta (`U1`...`U8`, `U9-U10`) con el capítulo en PDF, la guía de ejercicios, y — de la U5 en adelante — un script `visualizacion_*.py` que genera las figuras (`fig_*.png`) embebidas en los apuntes. Para regenerarlas: `python visualizacion_*.py` desde la carpeta de la unidad (requiere `numpy` y `matplotlib`).

## Estructura

- `U1`–`U8`, `U9-U10`: material por unidad (teoría, guía, figuras).
- `Parciales1`, `Parciales2`: parciales viejos resueltos, organizados por parte del examen.
- `TrabajoPractico`: TP de la cursada (notebooks, informe, simulaciones).
- `Simulaciones`: fluido (SPH) vs. sólido (masa-resorte) — la distinción de la U7 hecha animación. Ver [`Simulaciones/README.md`](Simulaciones/README.md).
- `Material_General`: bibliografía y planificación de la materia, no atadas a una unidad puntual.
