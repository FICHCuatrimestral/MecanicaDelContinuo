# Los tres balances — guion de derivación

> **Cómo usar esto:** es el guion para *recitar* las tres demostraciones en el parcial, no un resumen de fórmulas. Los bloques 💡 son la lectura física, los ⚠️ son las trampas donde se cae siempre. Si podés decir el guion en voz alta sin mirar, no hace falta memorizar las ecuaciones: salen solas.

---

## 📑 Índice

- [La receta común](#la-receta-común)
- [1. Conservación de masa (continuidad)](#1-conservación-de-masa-continuidad)
- [2. Balance de cantidad de movimiento lineal](#2-balance-de-cantidad-de-movimiento-lineal)
- [3. Balance de energía (primer principio)](#3-balance-de-energía-primer-principio)
- [Caso particular: conducción en un sólido rígido](#caso-particular-conducción-en-un-sólido-rígido)
- [Resumen](#resumen)
- [⚠️ Lista negra de errores](#️-lista-negra-de-errores)

---

## La receta común

$$\text{Axioma sobre }V(t)\ \longrightarrow\ \text{Reynolds}\ \longrightarrow\ \text{Cauchy}\ \longrightarrow\ \text{Gauss}\ \longrightarrow\ V\text{ arbitrario}\Rightarrow\text{localizar}$$

Los tres balances son **el mismo procedimiento** cambiando qué magnitud se balancea:

| Balance | Se balancea | Flujo por $S$ | Fuente en $V$ |
|---|---|---|---|
| Masa | $\rho$ | — | — |
| Momento lineal | $\rho v_i$ | $t_i$ (tracción) | $b_i$ |
| Energía | $\rho(\varepsilon+\tfrac12 v^2)$ | $t_iv_i - h_in_i$ | $b_iv_i + q$ |

💡 El **lema que sirve para los tres** (y que conviene memorizar en lugar de los desarrollos):

$$\boxed{\ \frac{D}{Dt}\int_{V(t)}\rho\,\psi\,dV=\int_{V(t)}\rho\,\frac{D\psi}{Dt}\,dV\ }$$

*La masa de la partícula ($\rho\,dV$) no cambia, así que $\rho$ sale afuera de la derivada.* Vale con $\psi=1$ (masa), $\psi=v_i$ (momento), $\psi=\varepsilon+\tfrac12v^2$ (energía). **Un solo lema, tres balances.**

---

## 1. Conservación de masa (continuidad)

### El guion

Postulo que la masa de un volumen material no cambia:

$$\frac{D}{Dt}\int_{V(t)}\rho\,dV=0$$

donde $\rho$ es la **densidad** (masa por unidad de volumen), no la masa. La masa es $m=\int_V\rho\,dV$.

⚠️ **Esto no se demuestra: es un axioma.** Lo que derivás es su **forma local**, la ecuación de continuidad.

Aplico el **teorema del transporte de Reynolds** y me quedan dos efectos:

$$\int_V\left[\underbrace{\frac{D\rho}{Dt}}_{\substack{\text{cuánto cambia la densidad}\\\text{siguiendo a la partícula}}}+\underbrace{\rho\frac{\partial v_k}{\partial x_k}}_{\substack{\text{cuánto cambia}\\\text{su volumen}}}\right]dV=0$$

Como el volumen $V$ es **arbitrario**, el integrando debe anularse (**localización**):

$$\boxed{\ \frac{D\rho}{Dt}+\rho\frac{\partial v_k}{\partial x_k}=0\ }$$

### Lectura

$$\frac{D\rho}{Dt}=-\rho\frac{\partial v_k}{\partial x_k}$$

💡 Densidad y volumen cambian en **sentidos opuestos**, de forma que la masa quede igual. Si la partícula se hincha, su densidad baja exactamente en la misma proporción. **Eso *es* la conservación de masa, expresada punto a punto.**

💡 El término $\partial v_k/\partial x_k$ es la **tasa de expansión volumétrica relativa**:

$$\frac{\partial v_k}{\partial x_k}=\nabla\cdot\boldsymbol v=\frac{1}{dV}\frac{D(dV)}{Dt}$$

Es el análogo en velocidades de la dilatación cúbica $\varepsilon_{kk}=\nabla\cdot\boldsymbol u$: $\varepsilon_{kk}$ es *cuánto se hinchó*, $\nabla\cdot\boldsymbol v$ es *a qué velocidad se está hinchando*.

### Incompresibilidad

Si **además** impongo $D\rho/Dt=0$ (hipótesis adicional):

$$\boxed{\ \nabla\cdot\boldsymbol v=\frac{\partial v_k}{\partial x_k}=0\ }$$

⚠️ **La trampa clásica:**

| Hipótesis | Qué dice | Nombre |
|---|---|---|
| $\partial\rho/\partial t=0$ | En un **punto fijo del espacio**, $\rho$ no cambia | **Estacionario** |
| $D\rho/Dt=0$ | Siguiendo a **una partícula**, su $\rho$ no cambia | **Incompresible** |

Son **independientes**. Ejemplo: gas en una tobera convergente en régimen permanente — $\partial\rho/\partial t=0$ pero cada partícula se comprime al avanzar, $D\rho/Dt\neq0$.

⚠️ Incompresibilidad **no significa que no se mueva**. El agua en un caño se mueve rapidísimo, se deforma, se estira — pero no cambia de volumen. Si $v=0$ el resultado es trivial (cuerpo en reposo), no es incompresibilidad.

---

## 2. Balance de cantidad de movimiento lineal

### El guion

Postulo la **segunda ley de Newton**: la tasa de cambio de la cantidad de movimiento de un volumen material iguala a las fuerzas de superficie más las de volumen.

$$\frac{D}{Dt}\int_{V(t)}\rho v_i\,dV=\int_{S(t)}t_i\,dS+\int_{V(t)}b_i\,dV$$

⚠️ Es un **balance**, no una conservación. El momento lineal **cambia** cuando hay fuerzas; solo se conserva si la resultante es nula. La masa sí se conserva siempre. Por eso se llama *balance de cantidad de movimiento*.

**Lado izquierdo.** Aplico Reynolds. Los términos que tienen $v_i$ como **factor común** forman la ecuación de continuidad y se anulan — acá uso conservación de masa:

$$\frac{D}{Dt}\int_V\rho v_i\,dV=\int_V\left[\rho\frac{Dv_i}{Dt}+v_i\underbrace{\left(\frac{D\rho}{Dt}+\rho\frac{\partial v_k}{\partial x_k}\right)}_{=\,0}\right]dV=\int_V\rho\frac{Dv_i}{Dt}\,dV$$

💡 **Truco para no perderse:** no abras los 5 términos. Los que se anulan son **los que tienen $v_i$ de factor común** — sacás $v_i$ afuera y adentro te queda continuidad.

**Lado derecho.** La tracción **depende de la orientación del plano**, $t_i=t_i(\boldsymbol x,\boldsymbol n)$, así que no podés aplicar Gauss directamente. Primero uso el **teorema de Cauchy**, que prueba que esa dependencia es lineal:

$$t_i=\sigma_{ij}n_j$$

y **recién entonces** aplico **Gauss**:

$$\int_S t_i\,dS=\int_S\sigma_{ij}n_j\,dS=\int_V\frac{\partial\sigma_{ij}}{\partial x_j}\,dV$$

⚠️ **Cauchy va antes que Gauss.** Gauss no se puede aplicar hasta que el integrando de superficie tenga la forma $(\text{algo})\cdot n_j$.

**Localización.** Como $V$ es arbitrario:

$$\boxed{\ \rho\frac{Dv_i}{Dt}=\frac{\partial\sigma_{ij}}{\partial x_j}+b_i\ }\qquad\Longleftrightarrow\qquad\rho\,\dot{\boldsymbol v}=\nabla\cdot\boldsymbol\sigma+\boldsymbol b$$

### Lectura

$$\rho\underbrace{\left(\frac{\partial v_i}{\partial t}+v_j\frac{\partial v_i}{\partial x_j}\right)}_{\text{aceleración}}=\underbrace{\frac{\partial\sigma_{ij}}{\partial x_j}}_{\text{desbalance de tensiones}}+\underbrace{b_i}_{\text{peso}}$$

💡 La derivada material:

$$\frac{Dv_i}{Dt}=\underbrace{\frac{\partial v_i}{\partial t}}_{\substack{\text{el campo cambia}\\\text{bajo mis pies}}}+\underbrace{v_j\frac{\partial v_i}{\partial x_j}}_{\substack{\text{yo me muevo hacia}\\\text{otro lugar del campo}}}$$

El término convectivo es **no lineal**: de ahí viene toda la dificultad de Navier–Stokes y la turbulencia.

💡 **Lo que empuja es el desbalance, no la tensión.** Si $\sigma_{ij}$ es uniforme su divergencia es cero y no hay fuerza neta — igual que una presión uniforme no acelera nada, lo que acelera es $-\nabla p$.

### El complemento: momento angular

El mismo procedimiento con $\rho\,\epsilon_{ijk}x_jv_k$ **no da una ecuación nueva**: da una **restricción**.

$$\boxed{\ \sigma_{ij}=\sigma_{ji}\ }$$

💡 Por eso el tensor tiene 6 componentes independientes y no 9, y por eso existen direcciones principales, autovalores reales y círculo de Mohr.

---

## 3. Balance de energía (primer principio)

### El guion

Postulo el **primer principio de la termodinámica**: la tasa de cambio de la energía **total** (interna + cinética) de un volumen material es igual a la potencia de las fuerzas de superficie y de volumen, más el calor generado internamente, menos el calor que se escapa por el contorno.

$$\frac{D}{Dt}\int_{V(t)}\rho\left(\varepsilon+\tfrac12v_kv_k\right)dV=\underbrace{\int_S t_iv_i\,dS+\int_V b_iv_i\,dV}_{\text{potencia mecánica}}+\underbrace{\int_V q\,dV-\int_S h_in_i\,dS}_{\text{potencia calórica}}$$

⚠️ **$q$ no es la energía interna.** Es la **fuente o sumidero volumétrico de calor**: calor generado por unidad de volumen y tiempo (radiación, reacción química, efecto Joule, decaimiento nuclear). La energía interna es $\varepsilon$, y está **del otro lado** de la ecuación.

⚠️ **El signo menos de $-\int_S h_in_i\,dS$** viene de que $\boldsymbol n$ es la normal **saliente**: $h_in_i$ es el calor que *se va*, lo que entra es su negativo. Va $h_i n_i$ (mismo índice repetido, es $\boldsymbol h\cdot\boldsymbol n$, un escalar), no $h_in_j$.

💡 El flujo $h_i$ nace del **mismo argumento del tetraedro** que $\sigma_{ij}$: a priori el calor que cruza una superficie depende de su orientación, $h=h(\boldsymbol x,\boldsymbol n)$, y el balance en el tetraedro prueba que la dependencia es lineal, $h=h_in_i$. Por eso el flujo de calor es un **vector**.

**Lado izquierdo.** Por el lema de conservación de masa, $\rho$ sale afuera de la derivada:

$$\frac{D}{Dt}\int_V\rho\left(\varepsilon+\tfrac12v_kv_k\right)dV=\int_V\rho\left(\frac{D\varepsilon}{Dt}+v_k\frac{Dv_k}{Dt}\right)dV$$

⚠️ El término que se anula acá es **el mismo de siempre**: $\left(\varepsilon+\tfrac12v^2\right)\left(\frac{D\rho}{Dt}+\rho\partial_kv_k\right)=0$. **No es "porque la velocidad es cero"** — es conservación de masa.

**Lado derecho.** Uso Cauchy ($t_i=\sigma_{ij}n_j$) y Gauss. Como $V$ es arbitrario, **localizo**:

$$\rho\frac{D\varepsilon}{Dt}+\rho v_i\frac{Dv_i}{Dt}=v_i\frac{\partial\sigma_{ij}}{\partial x_j}+\sigma_{ij}\frac{\partial v_i}{\partial x_j}+b_iv_i+q-\frac{\partial h_i}{\partial x_i}$$

⚠️ $\operatorname{div}\boldsymbol h=\partial h_i/\partial x_i$ es una divergencia **espacial**, no una tasa temporal: significa *cuánto flujo neto sale del punto por unidad de volumen*.

### El paso que solo tiene este balance: restar la energía mecánica

Multiplico la **ecuación de Cauchy** por $v_i$ — eso es el **teorema de la energía mecánica**:

$$\rho v_i\frac{Dv_i}{Dt}=v_i\frac{\partial\sigma_{ij}}{\partial x_j}+b_iv_i$$

y se la **resto** a la anterior. Se cancelan de un saque la energía cinética, $v_i\partial_j\sigma_{ij}$ y $b_iv_i$:

$$\rho\frac{D\varepsilon}{Dt}=\sigma_{ij}\frac{\partial v_i}{\partial x_j}+q-\frac{\partial h_i}{\partial x_i}$$

Descomponiendo $\partial v_i/\partial x_j=V_{ij}+W_{ij}$ y usando que $\sigma_{ij}$ es **simétrico** y $W_{ij}$ **antisimétrico**:

$$\sigma_{ij}W_{ij}=0\qquad\text{(la rotación rígida no hace trabajo)}$$

$$\boxed{\ \rho\frac{D\varepsilon}{Dt}=\sigma_{ij}V_{ij}+q-\frac{\partial h_i}{\partial x_i}\ }$$

💡 **Por qué este cuesta más:** los otros dos son una sola línea de razonamiento; este tiene **dos ecuaciones que se restan**.

$$\underbrace{\text{Energía TOTAL}}_{\text{1er principio}}-\underbrace{\text{Energía MECÁNICA}}_{\text{Cauchy}\cdot v_i}=\underbrace{\text{Energía INTERNA}}_{\text{lo que buscás}}$$

La parte mecánica **ya la sabías** (sale de Cauchy). Se la restás y lo que sobra es lo puramente térmico. **$\sigma_{ij}V_{ij}$ es el residuo que no se cancela: el puente entre lo mecánico y lo térmico.**

### El término $\sigma_{ij}V_{ij}$ cambia de personalidad según el material

| Material | $\sigma_{ij}V_{ij}$ vale | Significado |
|---|---|---|
| **Rígido** | $V_{ij}=0\Rightarrow 0$ | Nada. Problema térmico **desacoplado** |
| **Elástico** | $\sigma_{ij}\dot\varepsilon_{ij}=\dfrac{d}{dt}\left(\tfrac12\sigma_{ij}\varepsilon_{ij}\right)$ | Energía de deformación, **recuperable** |
| **Viscoso Newtoniano** | $-p\,V_{kk}+2\mu V_{ij}V_{ij}=\Phi\ge0$ | **Disipación** irreversible en calor |

💡 Por eso **revolver un fluido lo calienta y estirar un resorte no**: en el fluido $\Phi=2\mu V_{ij}V_{ij}$ es suma de cuadrados, siempre $\ge0$, energía perdida para siempre. En el elástico es un diferencial exacto: la devolvés toda.

---

## Caso particular: conducción en un sólido rígido

$$\rho\frac{D\varepsilon}{Dt}=\underbrace{\sigma_{ij}V_{ij}}_{\substack{=\,0\\ \text{rígido}}}+q-\frac{\partial h_i}{\partial x_i}$$

| Hipótesis | Qué anula |
|---|---|
| **Sólido rígido** | $V_{ij}=0\Rightarrow\sigma_{ij}V_{ij}=0$. Desacopla lo mecánico de lo térmico |
| **En reposo** ($v_i=0$) | Muere el convectivo: $D/Dt\to\partial/\partial t$ |
| **Estacionario** | $\partial/\partial t=0$ |
| **$k$ uniforme** | Sale afuera de la derivada |

$$0=q-\frac{\partial h_i}{\partial x_i}$$

Con la **ley de Fourier** $h_i=-k\,\partial T/\partial x_i$:

$$-\frac{\partial h_i}{\partial x_i}=-\frac{\partial}{\partial x_i}\left(-k\frac{\partial T}{\partial x_i}\right)=+k\frac{\partial^2T}{\partial x_i\partial x_i}$$

$$\boxed{\ k\,\nabla^2T+q=0\ }$$

Es la **ecuación de Poisson**. Si $q=0$, es **Laplace** ($\nabla^2T=0$, campo armónico).

⚠️ **Los dos signos menos son independientes** — confundirlos es error de parcial:

| Signo | De dónde viene |
|---|---|
| $-\dfrac{\partial h_i}{\partial x_i}$ | **Geométrico**: $\boldsymbol n$ es la normal saliente, lo que se va se resta |
| $h_i=-k\,\partial_iT$ | **Físico**: el calor va de caliente a frío (2da ley) |

💡 **Chequeo:** los dos menos se multiplican y dan **más**. Si la ecuación final te da $k\nabla^2T-q=0$ o con el laplaciano negativo, te comiste uno.

💡 **Interpretación de $q$:** despejando, $q=-k\nabla^2T$ es *el calor que hay que inyectar (o extraer) en cada punto para que ese campo $T$ pueda sostenerse en régimen estacionario*. Si $T$ es armónico, $q=0$: la conducción sola lo mantiene.

---

## Resumen

| | Se balancea | Axioma | Resultado local |
|---|---|---|---|
| **Masa** | $\rho$ | $\dfrac{D}{Dt}\displaystyle\int\rho\,dV=0$ | $\dfrac{D\rho}{Dt}+\rho\dfrac{\partial v_k}{\partial x_k}=0$ |
| **Mom. lineal** | $\rho v_i$ | Newton | $\rho\dfrac{Dv_i}{Dt}=\dfrac{\partial\sigma_{ij}}{\partial x_j}+b_i$ |
| **Mom. angular** | $\rho\,\epsilon_{ijk}x_jv_k$ | Newton (momentos) | $\sigma_{ij}=\sigma_{ji}$ *(restricción)* |
| **Energía** | $\rho(\varepsilon+\tfrac12v^2)$ | 1er principio | $\rho\dfrac{D\varepsilon}{Dt}=\sigma_{ij}V_{ij}+q-\dfrac{\partial h_i}{\partial x_i}$ |
| **Entropía** | $\rho\eta$ | 2do principio | $\ge$ *(restringe constitutivas: $\mu\ge0$, $k\ge0$)* |

Y después:

$$\textbf{Balance (universal)}\ +\ \textbf{Ley constitutiva (del material)}\ +\ \textbf{Cinemática}\ =\ \textbf{Ecuación de campo}$$

| | Balance | Constitutiva | Resultado |
|---|---|---|---|
| Sólido elástico | $\rho\ddot u_i=\partial_j\sigma_{ij}+b_i$ | $\sigma_{ij}=\lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}$ | **Navier** |
| Fluido viscoso | $\rho\dot v_i=\partial_j\sigma_{ij}+b_i$ | $\sigma_{ij}=-p\delta_{ij}+2\mu V_{ij}$ | **Navier–Stokes** |
| Conducción | $\rho\dot\varepsilon=\sigma_{ij}V_{ij}+q-\partial_ih_i$ | $h_i=-k\,\partial_iT$ | **Calor / Poisson** |

---

## ⚠️ Lista negra de errores

1. **"Demuestro que la masa se conserva."** No: es un **axioma**. Demostrás su **forma local**.
2. **"Conservación de momento lineal."** Es un **balance** — el momento cambia si hay fuerzas.
3. **Olvidarse de localizar.** Después de Reynolds tenés una *integral*. Falta: *"como $V$ es arbitrario, el integrando se anula"*.
4. **Aplicar Gauss antes que Cauchy.** No se puede: primero hay que escribir $t_i=\sigma_{ij}n_j$.
5. **Confundir $\rho$ con la masa.** $\rho$ es densidad; $m=\int\rho\,dV$.
6. **Confundir $\partial\rho/\partial t=0$ (estacionario) con $D\rho/Dt=0$ (incompresible).**
7. **Creer que $\partial v_k/\partial x_k$ mide el cambio de densidad.** Mide el cambio de **volumen**.
8. **Creer que incompresible = no se mueve.**
9. **Decir que $q$ es la energía interna.** Es la **fuente volumétrica de calor**.
10. **Confundir los dos signos menos** del balance de energía (geométrico vs. Fourier).
11. **Escribir Fourier sin el menos.** El menos *es* la ley (2da ley de la termodinámica).
12. **Equilibrio $\neq$ reposo.** Equilibrio es aceleración nula: podés moverte a velocidad constante.

---

🔗 Ver también: [apunte_U3-U10.md](apunte_U3-U10.md) — U9-U10 (balances) y U7 (constitutivas).
