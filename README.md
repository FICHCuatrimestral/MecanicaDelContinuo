# Mecánica del Continuo

Apuntes, guías y material de la cursada. Tres carpetas: lo que se lee, lo que se resuelve, y lo que se mira.

```
Teoria/           capítulos de la cátedra + apuntes propios
Practica/         guías, parciales viejos, trabajo práctico
Visualizaciones/  figuras del apunte, scripts que las generan, simulaciones
```

## Temario

Ingeniería en Informática, 4to año, 1er cuatrimestre. 90 hs. Un repaso rápido de qué se ve en cada unidad (la versión completa está en el apunte de abajo):

1. **Introducción.** La idea de "continuo": tratar la materia como si fuera infinitamente divisible (como los números reales), para poder describir fenómenos físicos — una ala deformándose por el peso del avión, un puente colgante, el flujo de calor en una central — con ecuaciones diferenciales sujetas a condiciones de borde, en vez de rastrear partícula por partícula.
2. **Vectores y tensores.** El álgebra que se usa en todo el curso: operaciones con vectores, notación indicial, cambio de base y transformación de coordenadas — la caja de herramientas matemática antes de entrar en la física.
3. **Tensiones.** Cómo un cuerpo transmite fuerza internamente. Se distingue entre fuerzas de cuerpo (a distancia, como la gravedad) y fuerzas de superficie (de contacto). El postulado de Cauchy dice que la tracción en un punto depende solo de la normal de la superficie, no de su forma — eso es lo que permite definir el tensor de tensiones y la fórmula de Cauchy, además de las condiciones de borde en tensiones (qué pasa en la interfaz entre dos medios).
4. **Tensiones y direcciones principales.** Dado el tensor de tensiones de la U3 (6 componentes independientes), ¿existe una orientación de ejes donde se simplifique al máximo? Es un problema de autovalores — la misma estructura que va a reaparecer para las deformaciones (U5) y las velocidades (U6) —, y en 2D es exactamente el Círculo de Mohr.
5. **Deformaciones.** Un cuerpo puede moverse (trasladarse, rotar) sin deformarse; la deformación tiene que medir el cambio de forma y tamaño, no el movimiento. Se construye comparando distancias entre puntos vecinos antes y después (tensores de Green-Lagrange y de Almansi), y se linealiza para el caso infinitesimal (chico), descomponiendo el gradiente de desplazamiento en una parte simétrica (deformación) y una antisimétrica (rotación rígida).
6. **Velocidad y relaciones de compatibilidad.** Si la U5 compara dos "fotos" (antes/después), la U6 mira la "película": la tasa a la que cambia la forma de un fluido. El gradiente de velocidad se descompone en tasa de deformación y vorticidad (spin), con los mismos casos canónicos (corte simple, Poiseuille, flujos rígidos) resueltos explícitamente. La compatibilidad es la pregunta inversa: dado un campo de deformaciones, ¿existe un campo de desplazamientos que lo genere?
7. **Ecuaciones constitutivas.** El equilibrio y la cinemática valen para cualquier material — y por eso solos no alcanzan para resolver nada (acero y miel responden distinto a la misma carga). La constitutiva es lo que distingue un material de otro: fluido invíscido, fluido Newtoniano, sólido Hookeano — modelos, no leyes exactas, cada uno con su rango de validez.
8. **Isotropía.** Demuestra por qué la forma que usa Hooke para un material isótropo (sin direcciones privilegiadas) es la única posible, reduciendo 81 coeficientes elásticos a solo 2 (los parámetros de Lamé, o equivalentemente el módulo de Young y el de Poisson).
9-10. **Ecuaciones de campo y principios variacionales.** Los balances universales — masa (continuidad), cantidad de movimiento (lineal y angular) y energía — combinados con la constitutiva de la U7 dan las ecuaciones diferenciales que gobiernan el movimiento de un continuo: Navier-Stokes para fluidos, la ecuación de Navier para sólidos elásticos. Es el cierre de todo el curso: cinemática + equilibrio + constitutiva en una sola ecuación.

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

## Proyectos relacionados

Dos proyectos personales que nacieron de la simulación de fluidos de `Visualizaciones/` y se independizaron:

- **[FluidSim](https://github.com/FICHCuatrimestral/FluidSim)** — simulación de fluidos SPH en Unity (C#).
- **[FluidWeb](https://github.com/FICHCuatrimestral/FluidWeb)** — la misma idea, corriendo en el navegador (TypeScript + WebGL).

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
