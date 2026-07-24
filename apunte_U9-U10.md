# Mecánica del Continuo — Apunte integrado de estudio
## Unidades 9 y 10: Ecuaciones de Campo y Principios Variacionales

*(Continuación directa de [`apunte_U5-U8.md`](apunte_U5-U8.md) — mismo curso, mismo examen. U5-6 dieron el lenguaje cinemático, U7-8 el material; acá se cierran las leyes universales de balance y se recorre el camino inverso con los principios variacionales.)*

Teoría + demostraciones + banco de preguntas sintéticas + recetario de parciales reales (2023–2026)

---

# PARTE 0 — El mapa mental (leer primero, releer último)

Todo el bloque se sostiene sobre **una sola receta** aplicada cuatro veces:

> **Ley física global (integral) → Gauss + derivada material + volumen arbitrario → ecuación local**

| Ley global | Resultado local |
|---|---|
| Conservación de masa | Ecuación de continuidad (1 PDE) |
| Momento lineal (Newton) | Ecuación de Cauchy (3 PDEs) |
| Momento angular | **Ninguna PDE nueva**: σ = σᵀ (3 ecs. algebraicas) |
| Primera ley (energía) | Balance térmico (1 PDE) |

**Cerrar el sistema** = enchufar constitutiva: Cauchy + Newtoniano → **Navier-Stokes**; Cauchy + Hooke → **Navier**; balance térmico + Fourier + ε=cT → **ecuación del calor**.

El capítulo variacional recorre el camino **al revés**: forma fuerte (PDE + bordes) → forma débil (δW_ext = δW_int ∀ variación admisible), equivalencia demostrable en ambos sentidos → discretización → **Kα = f**.

**La cuenta de cierre:** 15 incógnitas = 3 de movimiento + 6 cinemáticas + 6 constitutivas. El momento angular no suma ecuaciones: ya está gastado en reducir σ de 9 a 6.

---

# TABLA MAESTRA DE FÓRMULAS (forma abreviada · forma completa · significado)

> Referencia rápida. La "forma abreviada" es la que conviene memorizar; la "completa" es en índices/coordenadas para las cuentas; el "significado" es la frase para el examen.

## Herramientas matemáticas

| Abreviada | Completa (índices) | Significado |
|---|---|---|
| $\displaystyle\int_V \text{div}\,\mathbf w\,dV=\int_S\mathbf w\cdot\boldsymbol\nu\,dS$ | $\displaystyle\int_V A_{jkl\ldots,i}\,dV=\int_S\nu_i A_{jkl\ldots}\,dS$ | **Gauss.** La integral de volumen de una derivada = integral de superficie del campo por la normal. Convierte superficie ↔ volumen. La $\nu_i$ de afuera ↔ $\partial_i$ adentro. |
| $\dfrac{DF}{Dt}=\dfrac{\partial F}{\partial t}+\mathbf v\cdot\nabla F$ | $\dfrac{DF}{Dt}=\dfrac{\partial F}{\partial t}+v_j\dfrac{\partial F}{\partial x_j}$ | **Derivada material.** Tasa de cambio de la propiedad *de la partícula*. Término 1 = el campo cambia (sensor fijo); término 2 = la partícula se muda (convectivo). |
| $\dfrac{D}{Dt}\!\displaystyle\int_V A\,dV=\int_V\!\left[\dot A+A\,\text{div}\,\mathbf v\right]dV$ | $\dfrac{D}{Dt}\!\displaystyle\int_V A\,dV=\int_V\!\left[\dfrac{\partial A}{\partial t}+\dfrac{\partial(Av_i)}{\partial x_i}\right]dV$ | **Reynolds.** Derivar una integral sobre volumen material. El término extra $A\,\text{div}\,\mathbf v$ = dilatación del volumen (por eso D/Dt no conmuta con ∫). |
| $\dfrac{D}{Dt}\!\displaystyle\int_V\rho A\,dV=\int_V\rho\dot A\,dV$ | $\dfrac{D}{Dt}\!\displaystyle\int_V\rho A\,dV=\int_V\rho\dfrac{DA}{Dt}\,dV$ | **Lema oro.** Con ρ adelante, la D/Dt entra "limpia" (el término de continuidad se anula). Base de las demos de momento y energía. |
| $\displaystyle\int_V f\,dV=0\ \forall V\Rightarrow f=0$ | — | **Volumen arbitrario.** Si una integral se anula para todo volumen, el integrando es nulo punto a punto. Cierra toda derivación local. |

## Cinemática (repaso, unidades 5-6)

| Abreviada | Completa | Significado |
|---|---|---|
| $\boldsymbol\varepsilon=\tfrac12(\nabla\mathbf u+\nabla\mathbf u^T)$ | $\varepsilon_{ij}=\tfrac12(u_{i,j}+u_{j,i})$ | **Deformación** (pequeña): parte simétrica del gradiente de desplazamientos. Mide estiramiento/corte. |
| $\mathbf V=\tfrac12(\nabla\mathbf v+\nabla\mathbf v^T)$ | $V_{ij}=\tfrac12(v_{i,j}+v_{j,i})$ | **Tasa de deformación:** versión con velocidades. Propia de fluidos. |
| $\text{tr}\,\boldsymbol\varepsilon=e$ | $\varepsilon_{kk}=u_{k,k}=\nabla\cdot\mathbf u$ | **Dilatación volumétrica:** cambio relativo de volumen ΔV/V₀. La traza = parte "de tamaño". |
| $\boldsymbol\Omega=\text{rot}\,\mathbf v$ | $(\text{rot}\,\mathbf v)_i=e_{ijk}v_{k,j}$ | **Vorticidad.** ½ rot v = velocidad angular local (¡factor 2!). rot v = 0 ⟺ irrotacional. |
| $\varepsilon_n=\mathbf n^T\boldsymbol\varepsilon\,\mathbf n$ | $\varepsilon_n=n_i\varepsilon_{ij}n_j$ | **Deformación de una fibra** en dirección unitaria n. Cambio de longitud: $\Delta l=\varepsilon_n\,l$. |

## Leyes de balance (el corazón de la unidad 10)

| Abreviada | Completa | Significado |
|---|---|---|
| $\dot\rho+\rho\,\text{div}\,\mathbf v=0$ | $\dfrac{\partial\rho}{\partial t}+\dfrac{\partial(\rho v_j)}{\partial x_j}=0$ | **Continuidad** (conservación de masa). La densidad cae a la tasa a la que el elemento se expande. |
| $\text{div}\,\mathbf v=0$ | $\dfrac{\partial v_k}{\partial x_k}=0$ | **Incompresibilidad.** Caso de continuidad con Dρ/Dt=0. No cambia volumen (sí forma). |
| $\rho\dfrac{D\mathbf v}{Dt}=\text{div}\,\boldsymbol\sigma+\mathbf X$ | $\rho\dfrac{Dv_i}{Dt}=\sigma_{ji,j}+X_i$ | **Cauchy** (momento lineal = Newton local). Masa×aceleración material = divergencia de σ + fuerza de cuerpo. La fuerza interna neta es la *divergencia* de σ. |
| $\boldsymbol\sigma=\boldsymbol\sigma^T$ | $\sigma_{ij}=\sigma_{ji}$ | **Simetría de σ** (momento angular). No es una PDE: es la condición algebraica que baja σ de 9 a 6 incógnitas. |
| $\boldsymbol\sigma\,\mathbf n=\mathbf T^{(n)}$ | $\overset{n}{T}_i=\sigma_{ji}n_j$ | **Fórmula de Cauchy.** La tracción sobre una cara = σ actuando sobre su normal. Eslabón que permite volumetrizar fuerzas de superficie. |
| $\rho\dfrac{\partial\varepsilon}{\partial t}=q-\text{div}\,\mathbf h$ | $\rho\dfrac{\partial\varepsilon}{\partial t}=q-\dfrac{\partial h_i}{\partial x_i}$ | **Balance de energía** (1ª ley, cuerpo en reposo). Cambio de energía interna = calor generado − calor que sale. |

## Constitutivas (el "material", unidades 7-8)

| Abreviada | Completa | Significado |
|---|---|---|
| $\boldsymbol\sigma=\lambda\,\text{tr}(\boldsymbol\varepsilon)\,\mathbf I+2\mu\boldsymbol\varepsilon$ | $\sigma_{ij}=\lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}$ | **Hooke isótropo** (sólido). σ acoplado a la deformación ε. λ, μ (=G) = constantes de Lamé. |
| $\boldsymbol\sigma=-p\mathbf I+\lambda\,\text{tr}(\mathbf V)\mathbf I+2\mu\mathbf V$ | $\sigma_{ij}=-p\delta_{ij}+\lambda V_{kk}\delta_{ij}+2\mu V_{ij}$ | **Newtoniano isótropo** (fluido). σ acoplado a la *tasa* V. Misma estructura que Hooke + presión. |
| $\mathbb C_{ijkl}=\lambda\delta_{ij}\delta_{kl}+\mu(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})$ | $\sigma_{ij}=\mathbb C_{ijkl}A_{kl}=\lambda A_{kk}\delta_{ij}+2\mu A_{ij}$ | **Tensor isótropo de 4º orden.** Al contraerlo con las deltas recuperás Hooke/Newton. Exactamente 2 constantes (teorema de isotropía). |
| $\boldsymbol\varepsilon=\tfrac{1}{2\mu}\boldsymbol\sigma-\tfrac{\lambda}{2\mu(3\lambda+2\mu)}\text{tr}(\boldsymbol\sigma)\mathbf I$ | $\varepsilon_{ij}=\tfrac{\sigma_{ij}}{2\mu}-\tfrac{\lambda\,\sigma_{kk}}{2\mu(3\lambda+2\mu)}\delta_{ij}$ | **Hooke invertido** (ε desde σ). Para verificar placas. ⚠ En tensión plana ε_zz≠0 (Poisson). |
| $\mathbf h=-\kappa\nabla T$ | $h_i=-\kappa\,T_{,i}$ | **Fourier.** Flujo de calor contra el gradiente de temperatura. κ escalar por isotropía. |
| $\lambda=\dfrac{2\mu\nu}{1-2\nu}$, $\ E=2\mu(1+\nu)$ | — | **Relaciones entre constantes elásticas.** Si un hookeano "no da cero", suele faltar usar una de estas. |

## Grandes PDEs (balance + constitutiva)

| Abreviada | Completa | Significado |
|---|---|---|
| $\rho\dfrac{D\mathbf v}{Dt}=\rho\mathbf b-\nabla p+\mu\nabla^2\mathbf v$ | $\rho\dfrac{Dv_i}{Dt}=\rho b_i-\dfrac{\partial p}{\partial x_i}+\mu\dfrac{\partial^2v_i}{\partial x_j\partial x_j}$ | **Navier-Stokes incompr.** Cauchy + Newtoniano con ∇·v=0. p = incógnita/multiplicador. Con ν=μ/ρ. |
| $\rho\ddot{\mathbf u}=\mu\nabla^2\mathbf u+(\lambda+\mu)\nabla e+\mathbf b$ | $\rho\dfrac{D^2u_i}{Dt^2}=\mu\dfrac{\partial^2u_i}{\partial x_j\partial x_j}+(\lambda+\mu)\dfrac{\partial\varepsilon_{jj}}{\partial x_i}+b_i$ | **Navier elasticidad.** Cauchy + Hooke + pequeñas def. El término cruzado *sobrevive* (a diferencia del fluido). |
| $\rho c\,\dot T=q+\nabla\cdot(\kappa\nabla T)$ | $\rho c\dfrac{\partial T}{\partial t}=q+\dfrac{\partial}{\partial x_i}\!\left(\kappa\dfrac{\partial T}{\partial x_i}\right)$ | **Ecuación del calor.** Balance de energía + Fourier + ε=cT. |

## Principios variacionales

| Abreviada | Completa | Significado |
|---|---|---|
| $\delta W_{ext}=\delta W_{int}$ | (ver filas siguientes) | **Trabajos virtuales.** Equilibrio ⟺ para toda perturbación admisible δ, el trabajo externo iguala al interno. Equivale a la forma fuerte. |
| **(calor)** $\displaystyle\int_{\Gamma_\phi}\!\bar\phi\,\delta T+\int_V q\,\delta T=\int_V\kappa\nabla T\!\cdot\!\nabla\delta T$ | mismo, con $dS$ y $dV$ | Forma débil del calor. Izq = datos (fuente + flujo); der = "rigidez" (gradiente contra gradiente). |
| **(elast.)** $\displaystyle\int_V X_i\delta u_i+\int_{\Gamma_\sigma}\!\overset{n}{T}_i\delta u_i=\int_V\sigma_{ij}\delta e_{ij}$ | mismo, con $dV$ y $d\Gamma$ | Forma débil de elasticidad. Izq = fuerzas externas·desplaz. virtual; der = tensión·deform. virtual. |
| $\sigma_{ij}\delta u_{i,j}=\sigma_{ij}\delta e_{ij}$ | $\delta u_{i,j}=\delta e_{ij}+\delta\omega_{ij}$, y $\sigma_{ij}\delta\omega_{ij}=0$ | **Paso estrella.** σ (simétrico) solo trabaja contra la parte simétrica del gradiente virtual (deformación), no contra la rotación. |
| $\delta=0$ en (Γ_T, Γ_u); libre en (Γ_φ, Γ_σ) | — | **Admisibilidad.** La perturbación se anula donde el *valor* está impuesto (esencial); es libre donde se impone la *fuerza* (natural). |
| $\mathbf K\boldsymbol\alpha=\mathbf f$ | $\mathbf K=\int\mathbf B^T\kappa\,\mathbf B\,dV$, $\ \mathbf f=\int\mathbf N^T q\,dV$ | **Sistema discreto.** Campo admisible finito + arbitrariedad de δα. K simétrica (hereda la simetría de κ/C). Antesala de elementos finitos. |

## Los "operadores mecánicos" que se repiten en las cuentas

| Truco | Qué hace | Dónde aparece |
|---|---|---|
| $\partial_j(f\,\delta_{ij})=\partial_i f$ | La delta convierte el índice de derivación | Divergencia de σ en Navier-Stokes/Navier |
| $\partial_j\partial_i=\partial_i\partial_j$ | Conmutar derivadas parciales | Matar el término cruzado en NS |
| (simétrico):(antisimétrico) $=0$ | Anula la contracción | $e_{ijk}v_jv_k=0$; $\sigma\delta\omega=0$; rot(∇φ)=0 |
| $a_{ip}a_{kp}=\delta_{ik}$ | Ortogonalidad de la rotación | Verificar isotropía de un tensor |

---

# PARTE 1 — Las tres herramientas (con demostración)

## 1.1 Teorema de Gauss

$$\int_V A_{jkl\ldots,i}\, dV = \int_S \nu_i\, A_{jkl\ldots}\, dS$$

**Mnemónica:** al cruzar la frontera, la normal $\nu_i$ de afuera ↔ $\partial/\partial x_i$ adentro.

**Demostración (dirección x₁):** (1) rebanar V en tubos paralelos a x₁; teorema fundamental del cálculo a lo largo del tubo → diferencia de valores en las caras de entrada/salida sobre proyecciones $dx_2dx_3$. (2) Geometría: $dx_2dx_3 = \nu_1^*dS^*$ (coseno director = componente de la normal) y $-dx_2dx_3 = \nu_1^{**}dS^{**}$. (3) El signo lo absorbe la normal de entrada; las dos integrales se unifican sobre S. ∎

**Tres formas útiles:**
$$\int_V \text{div}\,\mathbf{w}\,dV = \int_S \mathbf{w}\cdot\boldsymbol\nu\,dS \qquad \int_V\nabla\phi\,dV=\int_S\phi\boldsymbol\nu\,dS \qquad \int_V\text{rot}\,\mathbf{u}\,dV=\int_S\boldsymbol\nu\times\mathbf{u}\,dS$$

## 1.2 Derivada material

**Concepto:** tasa de cambio de la propiedad **de la partícula** que pasa por x en t. NO es ∂/∂t (esa es la del sensor fijo; la material es la de la hoja que flota).

**Derivación:** la partícula en x pasa a x+vΔt; Taylor a primer orden en ambas dependencias; cancelar y tomar límite:

$$\boxed{\frac{DF}{Dt}=\underbrace{\frac{\partial F}{\partial t}}_{\text{el campo cambia}}+\underbrace{v_j\frac{\partial F}{\partial x_j}}_{\text{la partícula se muda (convectivo)}}}$$

Vale para CUALQUIER propiedad transportada (velocidad, temperatura, cada componente de un vector). Con F = vᵢ: el convectivo es **cuadrático en v** → no-linealidad de Navier-Stokes.

**Los dos caminos:**

| Euleriano | Lagrangiano |
|---|---|
| Datos: F(x,t) y v(x,t) | Datos: F y el mapeo xᵢ = xᵢ(a,t) |
| $DF/Dt = \partial_tF + v_j\partial_jF$ | Sustituir el mapeo en F, luego $\partial/\partial t\big|_{\mathbf a}$ (SIN convectivo) |
| Pagás el convectivo | Pagás la sustitución |

**Deben dar lo mismo** (convertir con el mapeo para chequear). Verificación extra: $v_i=\partial x_i/\partial t|_\mathbf{a}$ debe reproducir el campo dado.

### 🖼️ Visualización: observador fijo vs. observador que viaja con la partícula (parcial 2023-1, tipo T2)

La trampa conceptual de este tramo se vuelve intuitiva con un ejemplo concreto. El campo $\mathbf{v}=(0,z,y)$ es **estacionario** (no depende de $t$) y sale de derivar el mapeo del ejercicio 2023-1 (resuelto completo en la Parte 6, tipo T2):

![Observador fijo vs observador viajero](U9-U10/fig_observador_fijo_vs_viajero.png)

**Panel izquierdo:** es un flujo tipo *silla*: las líneas de corriente se alejan del origen a lo largo de la diagonal $y=z$ y se acercan por la otra. La partícula que en $t=0$ está en $(1,1)$ se queda **para siempre** sobre esa diagonal, alejándose como $e^t$.

**Panel derecho** es el núcleo de la trampa: un observador **fijo** en $(1,1,1)$ mide $D\mathbf{v}/Dt$ evaluado en ese punto espacial — como el campo es estacionario, ese valor es **siempre el mismo**, $(1,1)$, aunque a cada instante sea una partícula distinta la que está pasando por ahí. Un observador que **viaja** con la partícula que nació en $(1,1,1)$ mide la aceleración de esa partícula específica, que crece como $e^t$. Coinciden solo en $t=0$, porque ahí —y solo ahí— ambas descripciones señalan a la misma partícula en el mismo lugar. Es exactamente la diferencia $\partial/\partial t$ (sensor fijo) vs. $D/Dt$ (la hoja que flota) de la sección 1.2, hecha número.

*(Generado con `U9-U10/visualizacion_derivada_material_2023_1.py`.)*

## 1.3 Transporte de Reynolds

$$\boxed{\frac{D}{Dt}\int_VA\,dV=\int_V\left[\frac{\partial A}{\partial t}+\frac{\partial(Av_i)}{\partial x_i}\right]dV=\int_V\left[\frac{DA}{Dt}+A\frac{\partial v_i}{\partial x_i}\right]dV}$$

**Derivación:** separar (cambio del integrando a dominio quieto) + (aporte de la cáscara ΔV barrida por S: cada dS barre $(\mathbf v\cdot\mathbf n)\Delta t\,dS$) → integral de superficie → Gauss.

**⚠ D/Dt NO conmuta con ∫**: el término $A\,\partial_iv_i$ es la dilatación del volumen material.

**LEMA ORO** (aparece en TODAS las demos; acá entra la conservación de masa):

$$\boxed{\frac{D}{Dt}\int_V\rho A\,dV=\int_V\rho\frac{DA}{Dt}\,dV}$$

*Demo:* Reynolds con integrando ρA + regla del producto; el paréntesis $(D\rho/Dt+\rho\,\partial_iv_i)$ muere **por continuidad**. ∎

### 🖼️ Visualización: las dos geometrías detrás de todo el bloque

Gauss (1.1) y Reynolds (esta sección) son ambas, en el fondo, el mismo tipo de argumento: relacionar lo que pasa **en el borde** con lo que pasa **adentro**. Verlas una al lado de la otra deja clara la familia:

![Gauss y Reynolds, lado a lado](U9-U10/fig_gauss_reynolds.png)

**Izquierda (Gauss):** la demostración de 1.1 rebana el volumen en tubos paralelos a $x_1$; cada tubo entra con normal $\nu_1<0$ (flecha roja) y sale con $\nu_1>0$ (flecha verde), y el teorema fundamental del cálculo a lo largo de cada tubo, sumado sobre todos, ES la demostración.

**Derecha (Reynolds):** el mismo volumen material en $t$ y $t+dt$, bajo un campo que lo expande. La cáscara sombreada entre ambos contornos es exactamente $(\mathbf{v}\cdot\mathbf{n})\,dt\,dS$ integrada sobre el borde — el término extra que hace que $D/Dt$ no conmute con $\int_V$. 🔗 Es la misma "geometría de superficie" de Gauss, ahora con el borde moviéndose en vez de quieto.

*(Generado con `U9-U10/visualizacion_gauss_reynolds.py`.)*

## 1.4 Volumen arbitrario / lema fundamental

$\int_Vf\,dV=0$ ∀ V ⇒ f=0 punto a punto. Parientes: lema fundamental ($\int f\,\delta u\,dV=0$ ∀ δu ⇒ f=0) y su versión discreta ($\delta\boldsymbol\alpha^T(\mathbf K\boldsymbol\alpha-\mathbf f)=0$ ∀ δα ⇒ Kα=f).

---

# PARTE 2 — Las cuatro leyes de balance

## 2.1 Conservación de masa

**Lagrangiana:** cambio de variables con $J=|\partial x_i/\partial a_j|$ + volumen arbitrario:
$$\boxed{\rho_0(\mathbf a)=\rho(\mathbf x)\,J}$$
J = factor local de cambio de volumen; J≠0 obligatorio (J=0 ⇒ densidad infinita; J<0 ⇒ material invertido).

**Euleriana (continuidad):** Dm/Dt=0 + Reynolds + volumen arbitrario:
$$\boxed{\frac{\partial\rho}{\partial t}+\frac{\partial(\rho v_j)}{\partial x_j}=0}\iff\boxed{\frac{D\rho}{Dt}+\rho\frac{\partial v_j}{\partial x_j}=0}\iff\int_V\partial_t\rho\,dV+\int_S\rho v_jn_j\,dS=0$$
La integral es la más general (vale con choques). Conexión: $\partial_jv_j=\text{tr}\,\mathbf V$. Incompresible ⇒ Dρ/Dt=0 ⇒ ∇·v=0.

## 2.2 Momento lineal → Cauchy

$$\frac{D}{Dt}\int_V\rho v_i\,dV=\int_S\overset{n}{T}_i\,dS+\int_VX_i\,dV$$

1. Izquierda: Reynolds → $\int[\partial_t(\rho v_i)+\partial_j(\rho v_iv_j)]dV$.
2. Derecha: **fórmula de Cauchy** $\overset{n}{T}_i=\sigma_{ji}n_j$ + Gauss → $\int(\sigma_{ji,j}+X_i)dV$.
3. Volumen arbitrario; reagrupar la izquierda:
$$v_i\underbrace{[\partial_t\rho+\partial_j(\rho v_j)]}_{=0\text{ continuidad}}+\rho\underbrace{[\partial_tv_i+v_j\partial_jv_i]}_{Dv_i/Dt}$$

$$\boxed{\rho\frac{Dv_i}{Dt}=\sigma_{ji,j}+X_i}$$

Lecturas: la fuerza interna neta es la **divergencia** de σ (tensión uniforme no acelera); con v=0 recuperás la estática; las leyes colaboran (masa simplifica a momento).

## 2.3 Momento angular → simetría de σ (DEMO DE EXAMEN — cayó en 2024R)

**Ley:** $\dfrac{D}{Dt}\int_Ve_{ijk}x_j\rho v_k\,dV=\int_Ve_{ijk}x_jX_k\,dV+\int_Se_{ijk}x_j\overset{n}{T}_k\,dS$

1. **Lema oro** (masa): LHS $=\int\rho\,e_{ijk}\left(v_jv_k+x_j\frac{Dv_k}{Dt}\right)dV$, usando $Dx_j/Dt=v_j$.
2. $e_{ijk}v_jv_k=0$ (antisimétrico : simétrico; es v×v).
3. **Cauchy + Gauss** en el torque, derivando el producto (¡x_j también se deriva, $\partial x_j/\partial x_l=\delta_{jl}$!):
$$\int_Se_{ijk}x_j\sigma_{lk}n_l\,dS=\int_Ve_{ijk}(\sigma_{jk}+x_j\sigma_{lk,l})\,dV$$
El término huérfano $e_{ijk}\sigma_{jk}$ nace de derivar el brazo de palanca — es el protagonista.
4. Agrupar lo que lleva x_j:
$$\int_Ve_{ijk}x_j\underbrace{\left[\rho\frac{Dv_k}{Dt}-\sigma_{lk,l}-X_k\right]}_{=0\text{ ec. de movimiento}}dV=\int_Ve_{ijk}\sigma_{jk}\,dV\ \Rightarrow\ \int_Ve_{ijk}\sigma_{jk}\,dV=0$$
5. Volumen arbitrario: $e_{ijk}\sigma_{jk}=0$ para i=1,2,3 ⇒ σ₂₃=σ₃₂, σ₃₁=σ₁₃, σ₁₂=σ₂₁:

$$\boxed{\sigma_{jk}=\sigma_{kj}}\ \blacksquare$$

**Checklist de ingredientes (declararlos en el examen):** masa→lema; Dx/Dt=v + antisimetría; Cauchy+Gauss con derivada del brazo; ec. de movimiento; volumen arbitrario. **Conclusión conceptual:** el momento angular no da PDE nueva, solo la condición algebraica.

## 2.4 Energía → ecuación del calor

Primera ley con cuerpo en reposo: $\int\rho\partial_t\varepsilon\,dV=\int q\,dV-\int\text{div}\,\mathbf h\,dV$ (Gauss en el flujo entrante $-\int h_in_i\,dS$; ∂ρ/∂t=0 por continuidad con v=0). Volumen arbitrario + DOS constitutivas (Fourier $\mathbf h=-\kappa\nabla T$, con κ escalar por isotropía; almacenamiento ε=cT):

$$\boxed{\rho c\frac{\partial T}{\partial t}=q+\frac{\partial}{\partial x_i}\left(\kappa\frac{\partial T}{\partial x_i}\right)}$$

+ inicial T=T₀ + bordes T=T̄ en Γ_T (esencial) y κ∇T·n=φ̄ en Γ_φ (natural).

---

# PARTE 3 — Cierre con constitutivas

## 3.0 Mecánica de índices que se repite siempre

- La delta convierte el índice de derivación: $\partial_j(f\delta_{ij})=\partial_if$.
- Contracción del isótropo de 4º orden (aparece en el parcial 2025/2026):
$$\mathbb{C}_{ijkl}A_{kl}=\lambda\delta_{ij}\delta_{kl}A_{kl}+\mu(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})A_{kl}=\lambda A_{kk}\delta_{ij}+2\mu A_{ij}\ (A\text{ sim.})$$
- Conmutar derivadas: $\partial_j\partial_i=\partial_i\partial_j$.
- **Simétrico : antisimétrico = 0**: mata $e_{ijk}v_jv_k$, mata $\sigma_{ij}\delta\omega_{ij}$, demuestra rot(∇φ)=0.

## 3.1 Navier-Stokes incompresible (con razones — cayó 2025 y 2026)

Datos: Cauchy + $\sigma_{ij}=-p\delta_{ij}+\lambda V_{kk}\delta_{ij}+2\mu V_{ij}$ (si viene con ℂ: contraer primero, §3.0); ρ, λ, μ ctes.

- **[R0]** Si pide "partir del balance": derivar Cauchy (§2.2). Si menciona momento angular: "⇒ σ simétrico, habilita $\sigma_{ji,j}=\sigma_{ij,j}$".
- **[R1]** Continuidad + ρ cte ⇒ $V_{kk}=\partial_kv_k=0$.
- **[R2]** Muere el término λ (la viscosidad volumétrica no tiene cambio de volumen contra qué trabajar).
- **[R3]** $\mu\,\partial_j(\partial_iv_j)=\mu\,\partial_i(\partial_jv_j)=0$: conmutar derivadas + **otra vez** incompresibilidad.
- **[R4]** μ cte sale de las derivadas.
- **[R5]** p queda sin constitutiva: incógnita/multiplicador de ∇·v=0. Sistema 4×4.

$$\boxed{\rho\frac{Dv_i}{Dt}=\rho b_i-\frac{\partial p}{\partial x_i}+\mu\nabla^2v_i\qquad\partial_kv_k=0}$$

**μ = viscosidad dinámica** (pregunta 2026-4b): constante de proporcionalidad tensión ↔ gradiente de velocidad (σ₁₂=μU/h en corte entre placas; eso DEFINE newtoniano). Fricción interna entre capas; término difusivo de momento. El sólido resiste *estar* deformado; el fluido solo resiste *estar deformándose*.

## 3.2 Navier elasticidad (cayó 2024-4)

Datos: Cauchy + Hooke $\sigma_{ij}=\lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}$; pequeñas deformaciones; ρ,λ,μ uniformes.

- **[R1]** Pequeñas def. ⇒ convectivo de 2º orden ⇒ $Dv_i/Dt\approx\partial_t^2u_i$.
- **[R2]** Masa + pequeñas def. ⇒ ρ ≈ cte.
- **[R3]** Divergencia de Hooke: término λ → $\lambda\,\partial_i\varepsilon_{jj}$; términos μ → $\mu\nabla^2u_i+\mu\,\partial_i(\partial_ju_j)$.
- **⚠ EL término cruzado acá SOBREVIVE** ($\varepsilon_{jj}=e\neq0$: el sólido cambia volumen) y se suma al de λ. En el fluido incompresible moría. Misma cuenta, destino opuesto.

$$\boxed{\rho\frac{D^2u_i}{Dt^2}=\mu\frac{\partial^2u_i}{\partial x_j\partial x_j}+(\mu+\lambda)\frac{\partial\varepsilon_{jj}}{\partial x_i}+b_i}$$

## 3.3 Tabla comparativa

| | Navier-Stokes incompr. | Navier elasticidad |
|---|---|---|
| Campo / constitutiva acopla a | v / **tasa** V | u / **deformación** ε |
| Inercia | Dv/Dt completo (no lineal) | ∂²u/∂t² (linealizada) |
| Término λ | muere (V_kk=0) | vive (ε_kk=e) |
| Término cruzado μ | muere | vive → (λ+μ)∂e |
| Presión | incógnita | no hay |

---

# PARTE 4 — Principios Variacionales

## 4.0 Conceptos

**Fuerte:** PDE + bordes punto a punto. **Débil:** δW_ext = δW_int ∀ perturbación admisible (el "∀" es lo que la hace equivalente). **Para qué:** menos regularidad (integración por partes bajó un orden a la variación), absorbe gratis las naturales, se discretiza a Kα=f.

**Admisible:** perturbación hipotética (δ ≠ d: compara campos en el MISMO instante), diferenciable, **δ=0 donde el valor está impuesto** (Γ_T/Γ_u), libre donde no.

**Esencial** (T=T̄, u=ū): se construye a mano en el campo (factor: x·𝒫ₙ, (x−ℓₓ)·𝒫ₙ). **Natural** (flujo/tracción): NO se impone; queda absorbida en δW_ext y la vuelta la recupera sola.

## 4.1 DEMO — Ida, calor (5 movimientos)

Hipótesis: $\nabla\cdot(\kappa\nabla T)+q=0$; $T=\bar T$ en Γ_T; $\kappa\nabla T\cdot\mathbf n=\bar\phi$ en Γ_φ; $\mathbf h=-\kappa\nabla T$.

$$\delta W_{ext}=\int_Vq\,\delta T\,dV+\int_{\Gamma_\phi}\bar\phi\,\delta T\,dS$$

1. **Extender a Γ** (δT=0 en Γ_T; $\bar\phi=-\mathbf h\cdot\mathbf n$): $\int_{\Gamma_\phi}\bar\phi\delta T\,dS=\int_\Gamma(-\mathbf h\cdot\mathbf n)\delta T\,dS$.
2. **Gauss** del producto: $=-\int_V\text{div}(\mathbf h\,\delta T)dV$.
3. **Regla del producto** (= integración por partes): $=-\int\mathbf h\cdot\nabla(\delta T)dV-\int\delta T(\nabla\cdot\mathbf h)dV$.
4. **Balance:** $\nabla\cdot\mathbf h=q$.
5. **Constitutiva:** $\mathbf h=-\kappa\nabla T$.

$$\boxed{\int_{\Gamma_\phi}\delta T\,\bar\phi\,dS+\int_V\delta T\,q\,dV=\int_V\nabla(\delta T)\cdot(\kappa\nabla T)\,dV\quad\forall\,\delta T\text{ adm.}}\ \blacksquare$$

## 4.2 DEMO — Ida, elasticidad (con el paso estrella)

Igual con el diccionario, más un paso propio:

1-2. Extender a Γ (δu=0 en Γ_u) con Cauchy $\overset{n}{T}_i=\sigma_{ij}n_j$ + Gauss: $\int_{\Gamma_\sigma}\overset{n}{T}_i\delta u_i\,d\Gamma=\int_V\sigma_{ij,j}\delta u_i\,dV+\int_V\sigma_{ij}\delta u_{i,j}\,dV$.
3. Equilibrio: $\sigma_{ij,j}=-X_i$ (cancela con δW_ext volumétrico).
4. **PASO ESTRELLA** (simetrización por índices mudos, con σ simétrico):
$$\sigma_{ij}\delta u_{i,j}=\tfrac12(\sigma_{ij}\delta u_{i,j}+\sigma_{ji}\delta u_{i,j})\overset{i\leftrightarrow j}{=}\sigma_{ij}\underbrace{\tfrac12(\delta u_{i,j}+\delta u_{j,i})}_{\delta e_{ij}}$$
Lectura: $\sigma_{ij}\delta\omega_{ij}=0$ — **las tensiones no trabajan contra rotaciones virtuales**.

$$\boxed{\int_VX_i\delta u_i\,dV+\int_{\Gamma_\sigma}\overset{n}{T}_i\delta u_i\,d\Gamma=\int_V\sigma_{ij}\,\delta e_{ij}\,dV\quad\forall\,\delta u\text{ adm.}}\ \blacksquare$$

## 4.3 DEMO — Vuelta: débil ⇒ fuerte

Hipótesis: u=ū en Γ_u y δW_ext=δW_int ∀ δu admisible.

1. Desandar: $\sigma_{ij}\delta e_{ij}=\sigma_{ij}\delta u_{i,j}=(\sigma_{ij}\delta u_i)_{,j}-\sigma_{ij,j}\delta u_i$; Gauss: $\int\sigma\delta e\,dV=\int_\Gamma\sigma_{ij}n_j\delta u_i\,d\Gamma-\int\sigma_{ij,j}\delta u_i\,dV$.
2. Sustituir, usar δu=0 en Γ_u, agrupar:
$$\int_V(\sigma_{ij,j}+X_i)\delta u_i\,dV+\int_{\Gamma_\sigma}(\overset{n}{T}_i-\sigma_{ij}n_j)\delta u_i\,d\Gamma=0$$
3. **Lema fundamental en dos etapas:** primero δu nulas en frontera ⇒ paréntesis de volumen = 0; luego δu libres en Γ_σ ⇒ el otro también.

$$\boxed{\sigma_{ji,j}+X_i=0\ \text{en }V\qquad\sigma_{ij}n_j=\overset{n}{T}_i\ \text{en }\Gamma_\sigma}\ \blacksquare$$

**Remarcar:** la condición natural SALE SOLA — nunca fue impuesta.

## 4.4 Diccionario calor ↔ elasticidad

T↔u_i · ∇T↔e (con simetrización extra) · h=−κ∇T↔σ=Ce · q↔X · φ̄,Γ_φ↔T̄ⁿ,Γ_σ · T̄,Γ_T↔ū,Γ_u. Sabiendo una demo + diccionario + paso estrella, tenés las dos.

## 4.5 Discretización → Kα=f

Campo admisible finito T=**N**α (base × factor de la esencial); variación en la MISMA base δT=**N**δα (Galerkin); ∇T=**B**α; sustituir; constantes fuera de la integral; arbitrariedad de δα:

$$\mathbf K=\int\mathbf B^T\kappa\,\mathbf B\,dV\qquad\mathbf f=\int\mathbf N^Tq\,dV\qquad\boxed{\mathbf K\boldsymbol\alpha=\mathbf f}$$

K simétrica porque κ (o C) lo es — la simetría constitutiva baja al álgebra lineal. El método da la mejor aproximación dentro del espacio elegido.

---

# PARTE 5 — BANCO DE PREGUNTAS SINTÉTICAS (pregunta 1 de los parciales, con respuestas modelo)

> Todos los años la pregunta 1 es "responda en forma sintética". Estas son las que cayeron en 2025 y 2026, con la respuesta que hay que dar: 3-6 líneas, concepto + fórmula clave.

## P1. Interpretación física de la función potencial y la función de línea de corriente (2026-i)

**Potencial φ:** si $\mathbf v=\nabla\phi$, el flujo es automáticamente **irrotacional** (rot∇φ=0, ver P7). Recíproco: rot v=0 (dominio simplemente conexo) ⇒ existe φ. Interpretación: la velocidad "baja el gradiente" de φ; las superficies φ=cte son ortogonales al flujo.

**Función de corriente ψ (2D):** $v_x=\partial\psi/\partial y$, $v_y=-\partial\psi/\partial x$. Su existencia garantiza automáticamente la **incompresibilidad** ($\partial_xv_x+\partial_yv_y=\psi_{,yx}-\psi_{,xy}=0$). Interpretación: las curvas ψ=cte **son las líneas de corriente** (el flujo es tangente a ellas); la diferencia de ψ entre dos líneas es el caudal que pasa entre ellas.

**Síntesis:** potencial ↔ irrotacional; corriente ↔ incompresible. Un flujo potencial incompresible 2D tiene ambas y las dos son armónicas (∇²φ=∇²ψ=0). *(Conecta con el ejercicio 2024R-3, ver T4.)*

## P2. Homogéneo vs. isótropo; ¿puede un cuerpo presentar ambas? (2026-ii)

**Homogéneo:** las propiedades del material no dependen de la **posición** (invariancia ante traslación: todos los puntos son iguales). **Isótropo:** no dependen de la **dirección** (invariancia ante rotación: en un punto, todas las direcciones son iguales). Son propiedades **independientes**, y sí, un cuerpo puede tener ambas (acero estructural típico). Contraejemplos cruzados: madera = homogénea pero anisótropa (dirección de la fibra); material funcionalmente graduado = isótropo punto a punto pero no homogéneo.

## P3. ¿Qué conclusión se obtiene del balance de cantidad de movimiento angular? (2026-iii)

Que el tensor de tensiones es **simétrico**: $\sigma_{ij}=\sigma_{ji}$. No aporta ninguna PDE nueva (todo lo que lleva brazo de palanca ya lo garantiza el momento lineal): solo la condición algebraica que reduce σ de 9 a 6 componentes. (Demo completa: §2.3.)

## P4. ¿Qué se asume para reducir continuidad a la condición de incompresibilidad ∇·v=0 (descripción euleriana)? (2026-iv)

Se asume **incompresibilidad**: $D\rho/Dt=0$ — la densidad de cada partícula no cambia al moverse. Entonces la continuidad $D\rho/Dt+\rho\,\partial_jv_j=0$ deja $\rho\,\partial_jv_j=0\Rightarrow\partial_jv_j=0$. (Caso particular más fuerte: ρ = cte en todo el campo, que requiere además homogeneidad.)

## P5. Diferencia entre tensor de pequeñas deformaciones ε y tensor de tasa de deformación V (2025-i)

ε compara la configuración **actual contra una referencia** (se construye con desplazamientos; adimensional; propio de sólidos, que "recuerdan" su forma); vale solo si deformaciones Y rotaciones son pequeñas. V es la **tasa instantánea** (se construye con velocidades; unidades 1/s; propio de fluidos, sin configuración de referencia). El diccionario u→v, ε→V es **exacto** (no aproximado) porque una tasa es intrínsecamente infinitesimal.

## P6. ¿Qué garantiza la ecuación de compatibilidad? (2025-ii)

Que un campo de deformaciones dado **derive de un campo de desplazamientos continuo y univaluado**: 6 componentes de ε salen de solo 3 uᵢ (sistema sobredeterminado en el camino inverso ε→u), y compatibilidad es la condición para que "el rompecabezas deformado cierre" sin huecos ni solapamientos.

## P7. Rotor del campo de velocidad: qué indica, con qué tensores se relaciona; ¿qué pasa si v=∇φ? DEMOSTRAR (2025-iii)

Indica **rotación local** del fluido: $\boldsymbol\Omega=\text{rot}\,\mathbf v$ es la vorticidad, con $\frac12\text{rot}\,\mathbf v$ = velocidad angular local (¡factor 2!). Se relaciona con el **tensor de vorticidad/spin** $\Omega_{ij}$, la parte antisimétrica del gradiente de velocidades (la simétrica es V).

**Demostración de que v=∇φ ⇒ irrotacional:**
$$(\text{rot}\,\nabla\phi)_i=e_{ijk}\frac{\partial}{\partial x_j}\left(\frac{\partial\phi}{\partial x_k}\right)=e_{ijk}\,\phi_{,kj}=0$$
porque es la contracción del símbolo $e_{ijk}$, **antisimétrico** en (j,k), con $\phi_{,jk}$, **simétrico** en (j,k) (Schwarz). Contracción simétrico:antisimétrico = 0. ∎

## P8. ¿Qué relaciona el teorema de Gauss? (2025-iv)

La **integral de volumen de una derivada** (divergencia) con la **integral de superficie del campo por la normal externa**: $\int_VA_{,i}\,dV=\int_S\nu_iA\,dS$. Físicamente: lo que se "genera" dentro del volumen con lo que atraviesa su frontera. Es la herramienta que convierte términos de superficie (tracciones, flujos) en términos de volumen para derivar las ecuaciones locales.

## P9. Derivada material vs. derivada espacial de un campo f euleriano; ¿cómo se relacionan? (2025-v)

**Espacial** ∂f/∂t: tasa de cambio en un **punto fijo del espacio** (lo que mide un sensor anclado). **Material** Df/Dt: tasa de cambio de la propiedad **de la partícula** que pasa por ese punto (lo que siente una hoja que flota). Relación:
$$\frac{Df}{Dt}=\frac{\partial f}{\partial t}+\mathbf v\cdot\nabla f$$
El convectivo v·∇f existe porque la partícula se muda dentro de un campo no homogéneo. Pueden diferir incluso con campo estacionario (∂f/∂t=0 pero Df/Dt≠0 si la partícula viaja hacia zonas de otro valor) — ver T2.

---

# PARTE 6 — RECETARIO LIGADO A LOS PARCIALES REALES (2023–2026)

> Cada tipo con: dónde cayó, cómo leer el enunciado, receta y resolución/resultados clave.

## T1 — Derivada material de un campo dado (euleriana)
**Cayó:** 2026-3a, 2025-3a, 2024-5a, 2024R-5.

**Lectura del enunciado:** "xᵢ son las coordenadas actuales o espaciales" = descripción euleriana = usar la fórmula con convectivo. Escribir SIEMPRE la fórmula general primero.

**Receta:** ∂q/∂t (posición congelada) → matriz ∂qᵢ/∂xⱼ → producto con v → sumar.

**Resolución 2024-5a** — $\mathbf q=(x_1t^2,\ x_2\cos t,\ x_3e^t)$, $\mathbf v=(x_1/t,\ x_2\tan t,\ x_3)$:
$$\frac{\partial\mathbf q}{\partial t}=(2x_1t,\ -x_2\sin t,\ x_3e^t)\qquad v_j\partial_jq=(x_1t,\ x_2\tan t\cos t,\ x_3e^t)=(x_1t,\ x_2\sin t,\ x_3e^t)$$
$$\boxed{\frac{D\mathbf q}{Dt}=(3x_1t,\ 0,\ 2x_3e^t)}$$
La segunda componente se cancela exacta: la partícula "ve" constante lo que el sensor ve oscilar — interpretarlo suma puntos.

**Resolución 2026-3a** — $\mathbf q=(x_2t^2, x_1t, x_3e^t)$, $\mathbf v=(x_1t, x_1, -x_3)$: $D\mathbf q/Dt=(2x_2t+x_1t^2,\ x_1(1+t^2),\ 0)$ (la tercera se cancela).

**Variante mixta 2024R-5** (mapeo dado + campo euleriano, resultado pedido en euleriana): primero obtener v en euleriana desde el mapeo ($v_i=\partial x_i/\partial t|_\mathbf a$, luego invertir el mapeo para eliminar las a): con $x_1=a_1e^{-t}, x_2=a_2e^t, x_3=a_3+a_2(e^{-t}-1)$ sale $v=(-x_1,\ x_2,\ -x_2e^{-2t})$. Con $s=x_1-2x_2+3x_3$ y $A_i=e^{-it}s$:
$$\frac{DA_i}{Dt}=e^{-it}\left[-i\,s+(v_1-2v_2+3v_3)\right]=e^{-it}\left[-i(x_1-2x_2+3x_3)-x_1-2x_2-3x_2e^{-2t}\right]$$
(p.ej. i=1: $e^{-t}[-2x_1-3x_3-3x_2e^{-2t}]$). La estructura A_i = f_i(t)·s permite factorizar: $v\cdot\nabla A_i=f_i(t)\,(v\cdot\nabla s)$ — buscá siempre esa factorización.

## T2 — Observador fijo vs. observador que viaja con la partícula
**Cayó:** 2023-1 (con solución oficial).

**Lectura:** "cambio de velocidad por unidad de tiempo que observaría..." — (a) fijo en un punto vs. (b) viajando con la partícula. Es LA pregunta conceptual material/espacial hecha ejercicio.

**Resolución 2023-1** — $x=X$, $y=\frac12[(Y{+}Z)e^t+(Y{-}Z)e^{-t}]$, $z=\frac12[(Y{+}Z)e^t-(Y{-}Z)e^{-t}]$:
- Velocidades materiales: $\dot y=z$, $\dot z=y$ (¡el campo euleriano $\mathbf v=(0,z,y)$ es **estacionario**!).
- **(a) Observador fijo en (1,1,1):** registra la aceleración de la partícula que pasa en cada instante: $D\mathbf v/Dt=\mathbf v\cdot\nabla\mathbf v=(0,y,z)$ (equivalente: $\ddot y=y$, $\ddot z=z$ del mapeo, expresado espacialmente). En (1,1,1): $(0,1,1)$, **constante en el tiempo** (a cada rato pasa una partícula distinta con la misma aceleración).
- **(b) Observador viajero** (partícula que en t=0 estaba en (1,1,1), o sea Y=Z=1): su trayectoria es $y=z=e^t$, y su aceleración $\boldsymbol\alpha=(0,e^t,e^t)$, **creciente**.
- **(c)** La aceleración de LA partícula es **(b)**: la aceleración es una propiedad de la partícula seguida en el tiempo; (a) da en cada instante la de una partícula distinta. Consistencia: en t=0 ambas dan (0,1,1); y la fórmula de (a) evaluada en la posición actual de la partícula ($y=z=e^t$) reproduce (b). ✔

## T3 — Flujo sobre superficie de volumen arbitrario
**Cayó:** 2026-3b, 2024-5b; variante "verificar la divergencia por cálculo directo" en 2023R-1b.

**Lectura:** superficie NO especificada + "volumen fijo, arbitrario" = **Gauss inmediato** (nadie parametriza nada).

$$\iint_Sf_in_i\,dS=\int_V\text{div}\,\mathbf f\,dV$$

**2024-5b** con $\mathbf f=Dq/Dt=(3x_1t,0,2x_3e^t)$: div = $3t+2e^t$ (constante en el espacio) ⇒ flujo $=(3t+2e^t)\cdot A$ (A = volumen). **2026-3b**: div = t² ⇒ flujo = t²·V. Si la divergencia da constante, es señal de que vas bien.

**Variante 2023R-1b** (verificar Gauss por cálculo): calcular las 6 integrales de cara $\int\sigma n\,dS$ (con la normal de CADA cara, atentos a los signos de las caras "negativas") y la integral de volumen de $\sigma_{ij,j}$, y comprobar que coinciden. Trabajoso pero mecánico.

## T4 — ¿Irrotacional? ¿Incompresible? + función de corriente
**Cayó:** 2026-3c, 2024R-3, 2023R-2.

**Receta:** incompresible ⟺ $\partial_jv_j=\text{tr}\mathbf V=0$; irrotacional ⟺ rot v=0 componente a componente ($e_{ijk}\partial_jv_k$). Basta UNA componente ≠0 para responder que no. Son condiciones **independientes**. Evaluar sobre **v** (no sobre otros campos del enunciado).

**Resolución 2024R-3** — $v_x=k\,\partial\theta/\partial y$, $v_y=-k\,\partial\theta/\partial x$, $v_z=0$:
- **Incompresible SIEMPRE:** $\partial_xv_x+\partial_yv_y=k\theta_{,yx}-k\theta_{,xy}=0$ por Schwarz — por construcción, para cualquier θ.
- **Irrotacional solo si θ es armónica:** $(\text{rot}\,\mathbf v)_z=\partial_xv_y-\partial_yv_x=-k(\theta_{,xx}+\theta_{,yy})=-k\nabla^2\theta$ (las otras componentes son 0). ⇒ irrotacional ⟺ ∇²θ=0. En general NO.
- **Tasa de deformación:** $V_{11}=k\theta_{,xy}$, $V_{22}=-k\theta_{,xy}$, $V_{12}=\frac k2(\theta_{,yy}-\theta_{,xx})$, resto 0. (Chequeo: tr V=0 ✓, coherente con incompresible.)
- **kθ se llama función de corriente** — y esto conecta directo con la pregunta sintética P1 del parcial 2026: sus curvas de nivel son las líneas de corriente.

**2026-3c** — $\mathbf v=(x_1t, x_1, -x_3)$: $(\text{rot}\,\mathbf v)_3=\partial_1v_2-\partial_2v_1=1\neq0$ ⇒ NO irrotacional (corte simple en el plano 12, que siempre trae rotación).

## T5 — Demostración Navier-Stokes / Navier
**Cayó:** 2025-4, 2026-4a (con ℂ de 4º orden), 2024-4 (elasticidad).

Receta completa en §3.1 y §3.2 con las razones numeradas — el enunciado SIEMPRE pide "indicar la razón de las simplificaciones": cada tachado con su porqué al lado. Leer con lupa: ¿"partiendo del balance"? (derivar Cauchy primero); ¿menciona momento angular? (una línea de simetría); ¿constitutiva con ℂ? (contraer las deltas primero, §3.0); ¿b por masa o X por volumen? (define si aparece ρb o X solo).

## T6 — Demostración simetría de σ
**Cayó:** 2024R-4. Demo completa en §2.3 con checklist de ingredientes.

## T7 — Demostraciones variacionales / identidades tipo Green
**Cayó:** 2023-3 (con solución oficial); anunciadas para este año.

**Resolución 2023-3** — demostrar, con $\boldsymbol\phi=0$ en S:
$$\int_V\phi_i\,\Delta\psi_i\,dV=-\int_V\nabla\phi_i\cdot\nabla\psi_i\,dV$$

Es exactamente la jugada central de las demos variacionales (Gauss del producto + condición de borde que mata la superficie):

1. Considerar el producto $\phi_i\psi_{i,j}$ y su divergencia (regla del producto):
$$(\phi_i\psi_{i,j})_{,j}=\phi_{i,j}\psi_{i,j}+\phi_i\psi_{i,jj}$$
2. Integrar en V y aplicar **Gauss** al lado izquierdo:
$$\int_V(\phi_i\psi_{i,j})_{,j}\,dV=\int_S\phi_i\,\psi_{i,j}\,n_j\,dS=0$$
porque $\phi_i=0$ en S (este es el rol de "δT=0 en Γ_T" de las demos del apunte).
3. Entonces $\int_V(\phi_{i,j}\psi_{i,j}+\phi_i\psi_{i,jj})\,dV=0$, es decir:
$$\int_V\phi_i\Delta\psi_i\,dV=-\int_V\nabla\phi_i\cdot\nabla\psi_i\,dV\ \blacksquare$$

**Patrón general de estas demos** (si te dan otra identidad): (i) identificar el producto cuya divergencia genera los dos términos de la identidad; (ii) Gauss; (iii) usar la condición de borde dada para anular la superficie (o dejarla si la identidad la incluye); (iv) despejar. Las demos 4.1–4.3 del apunte son este patrón + usar balance y constitutiva en el camino.

## T8 — Verificar solución de tensiones propuesta (placa / Airy)
**Cayó:** 2024R-2 (placa, análoga a 2026-2 de práctica), 2024-2 (Airy).

**Receta placa (2024R-2):**
1. **Equilibrio:** $\sigma_{ji,j}+X_i=0$ (acá X=0): derivar polinomios; definir $k=\frac34\frac q{c^3}$ para el factor común; debe dar cancelación exacta (si no: error propio).
2. **Deformaciones en 3D:** Hooke invertido
$$\varepsilon_{ij}=\frac{\sigma_{ij}}{2\mu}-\frac{\lambda}{2\mu(3\lambda+2\mu)}\sigma_{kk}\delta_{ij}$$
(deducción exprés: traza de Hooke ⇒ $\sigma_{kk}=(3\lambda+2\mu)\varepsilon_{kk}$, despejar, sustituir). **⚠ Trampa "considerar en 3D":** en tensión plana $\sigma_{zz}=0$ pero $\varepsilon_{zz}=-\frac{\lambda}{2\mu(3\lambda+2\mu)}(\sigma_{xx}+\sigma_{yy})\neq0$ — efecto Poisson.
3. **Compatibilidad** (te dan la ecuación): segundas derivadas de cada ε, verificar la identidad; los términos de Poisson se cancelan entre sí.

**Receta Airy (2024-2)** — $\Phi=x^2y$: tensiones $\sigma_{xx}=\Phi_{,yy}=0$, $\sigma_{yy}=\Phi_{,xx}=2y$, $\sigma_{xy}=-\Phi_{,xy}=-2x$ (con b=0).
- **Equilibrio:** automático por construcción de Airy — pero verificarlo igual: $0+\partial_y(-2x)=0$ ✓; $\partial_x(-2x)+\partial_y(2y)=-2+2=0$ ✓.
- **Compatibilidad:** tensiones lineales ⇒ ε lineales (Hooke inverso) ⇒ todas las segundas derivadas son 0 ⇒ 0=0 ✓ (equivalente: Φ cúbica ⇒ ∇⁴Φ=0 trivial).
- **Bordes:** en cada lado, la tracción es $\mathbf T=\boldsymbol\sigma\,\mathbf n$ con la normal EXTERNA de ese lado; comparar con las cargas del dibujo. Para resultantes en el lado superior: $N=\int\sigma_{yy}\,dx\cdot e$, $Q=\int\sigma_{xy}\,dx\cdot e$, $M_z=\int\sigma_{yy}\,x\,dx\cdot e$ (e = espesor), integrando a lo ancho del lado.

## T9 — Hooke directo desde desplazamientos + verificar equilibrio (viga 2023-2)

**Receta:** ε desde u por derivación ($\varepsilon_{ij}=\frac12(u_{i,j}+u_{j,i})$) → Hooke directo $\sigma=2\mu\varepsilon+\lambda\,\text{tr}(\varepsilon)\delta$ → verificar $\text{div}\,\boldsymbol\sigma=0$.

**Resolución (viga en flexión):** $\varepsilon=\frac YR\,\text{diag}(-1,\nu,\nu)$, cortes todos nulos (se cancelan de a pares), $\text{tr}\,\varepsilon=\frac{(2\nu-1)Y}{R}$. Tensiones:
$$\sigma_{xx}=\frac YR[-2\mu+\lambda(2\nu-1)]=-\frac{EY}{R}\qquad\sigma_{yy}=\sigma_{zz}=\frac YR[2\mu\nu-\lambda(1-2\nu)]=0$$
**El punto clave:** para que $\sigma_{yy}=\sigma_{zz}=0$ y div σ=0 hay que usar la identidad $\lambda=\dfrac{2\mu\nu}{1-2\nu}$ (relación entre Lamé y Poisson; y $E=2\mu(1+\nu)$). **Moraleja de examen:** si "no da cero", antes de buscar el error revisá si falta una identidad entre constantes elásticas. Resultado físico limpio: flexión pura = tensión uniaxial $\sigma_{xx}=-EY/R$ (comprime arriba, tracciona abajo del eje neutro).

## T10 — Incisos de otras unidades que aparecen en los mismos parciales (referencia rápida)

- **Fibras con ε homogénea** (2024-1, 2026-2): deformación de una fibra recta en dirección unitaria n: $\varepsilon_n=\mathbf n^T\boldsymbol\varepsilon\,\mathbf n$; cambio de longitud $\Delta l=\varepsilon_n\,l$; fibra compuesta: sumar por segmento con el n de cada uno. **Térmica** $\varepsilon=\alpha\,\delta\,\Delta T$: puramente esférica ⇒ $\varepsilon_n=\alpha\Delta T$ para CUALQUIER dirección ⇒ $\Delta l_{tot}=\alpha\Delta T\sum l_i$. Característica (2026-2c): el tensor térmico es esférico/volumétrico puro (cambia tamaño, no forma, igual en toda dirección); uno con componentes de corte tiene parte desviadora (cambia forma).
- **Verificar isotropía de un tensor** (2024-3, $A_{ijkl}=\delta_{ik}\delta_{jl}$): transformar con la ley de rango 4 y usar ortogonalidad $a_{ip}a_{kp}=\delta_{ik}$: $A'_{ijkl}=a_{ip}a_{jq}a_{kr}a_{ls}\delta_{pr}\delta_{qs}=a_{ip}a_{kp}\,a_{jq}a_{lq}=\delta_{ik}\delta_{jl}=A_{ijkl}$ ✓.
- **Green-Lagrange desde figura** (2025-2, 2024R-1): armar el mapeo lineal $x_i=F_{ij}a_j$ desde los vértices, luego $E=\frac12(F^TF-I)$; Almansi con $F^{-1}$.

---

# PARTE 7 — Lista negra de errores

1. **∂/∂t donde va D/Dt** (o al revés); la lagrangiana NO lleva convectivo.
2. **Meter D/Dt en la integral sin el término de dilatación** (solo entra gratis con ρ adelante — lema §1.3).
3. **Cancelar $\mu\,\partial_i(\partial_ju_j)$ en elasticidad** por reflejo de fluidos: SOBREVIVE.
4. **Olvidar ε_zz≠0 en tensión plana** (Poisson).
5. **Confundir X por volumen vs. b por masa** (define si aparece ρb).
6. **Evaluar irrotacionalidad sobre el campo equivocado** (es sobre v).
7. **δ = d** (la variación compara campos en el MISMO instante).
8. **No declarar la admisibilidad** antes de una demo variacional.
9. **Cancelar sin razón escrita** (cada tachado con su porqué).
10. **Perder el término de derivar el brazo x_j** en la demo del momento angular — es el que da la simetría.
11. **No cerrar con "volumen arbitrario"** (o lema fundamental): sin eso no hay resultado local.
12. **Olvidar que la continuidad se usa DOS veces en Navier-Stokes** (bajar a Cauchy + matar términos de la constitutiva).
13. **"No me da cero" en un hookeano:** revisar primero si falta una identidad entre constantes (λ=2μν/(1−2ν), E=2μ(1+ν)) — caso viga 2023-2.
14. **Responder las sintéticas con desarrollo largo:** piden síntesis — concepto + fórmula clave + (si corresponde) demo de 2 líneas.
15. **Normales de las caras "negativas"** en cálculos directos de tracciones (2023R-1): la normal externa de la cara x₁=0 es (−1,0,0).

---

# PARTE 8 — El cierre conceptual (pregunta teórica abierta)

Las unidades 5-6 dieron el **lenguaje cinemático** (ε, V, ω, Ω, invariantes, compatibilidad). Las 7-8, el **material** (constitutivas; isotropía ⇒ exactamente dos constantes). Las ecuaciones de campo traducen las **leyes universales** (masa, Newton, termodinámica) a PDEs con tres herramientas (Gauss, derivada material, volumen arbitrario); balance + cinemática + constitutiva **cierran las 15 ecuaciones** y producen Navier-Stokes, Navier y la ecuación del calor como una única estructura con distintos materiales enchufados. Los principios variacionales reescriben ese problema de contorno como **una identidad de trabajos virtuales equivalente** (ida y vuelta demostrables), que pide menos regularidad, absorbe sola las condiciones naturales, y al discretizarse colapsa en **Kα=f simétrico**: la puerta de elementos finitos.

**Plan de repaso sugerido (orden de prioridad según los parciales):**
1. Reproducir a mano, sin mirar, las 5 demos: simetría de σ (§2.3), Navier-Stokes (§3.1), Navier (§3.2), ida variacional (§4.1-4.2), vuelta (§4.3) + la identidad tipo Green (T7).
2. Automatizar T1-T4 (derivada material en ambos caminos, Gauss para flujos, irrotacional/incompresible, función de corriente).
3. Memorizar el banco de sintéticas (Parte 5) — cae SIEMPRE como pregunta 1.
4. Una pasada por T8-T9 (hookeanos de verificación) con la lista negra al lado.
