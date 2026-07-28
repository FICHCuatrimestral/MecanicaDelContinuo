"""
Parcial 26/06/2025, ejercicio 2 (archivo Parciales2/parcial2026.jpg)
=====================================================================
Placa con una fibra quebrada l1-l2-l3 (l1=1 horizontal, l2=sqrt(2) a 45,
l3=sqrt(3) a 30), sometida a deformacion homogenea. Dos incisos, dos
tensores distintos:

  (a) termico:  eps = alpha*dT*delta_ij = 1e-4 * I        (ESFERICO/ISOTROPO)
  (b) generico: eps = 1e-4 * [[1, 0.5],[0.5, 1]]           (NO isotropo)

La pregunta del inciso (c) -"que caracteristica presenta el tensor de (a)
frente al de (b)"- es EXACTAMENTE el criterio de tensor isotropo de rango 2
de la Unidad 8: A_ij isotropo <=> A_ij = alpha*delta_ij (diagonal igual Y
fuera de diagonal CERO). El tensor (b) tiene la diagonal igual (1,1) pero
el fuera-de-diagonal NO es cero -> por eso NO es isotropo, aunque a primera
vista "se parezca". Esa es la trampa que este script hace visible.

Genera:
  fig_geometria_fibra.png      -> la figura del parcial, a escala
  fig_isotropia_comparacion.png -> polar de estiramiento + circulo deformado,
                                   (a) vs (b), lado a lado

Corre con: python visualizacion_fibra_isotropia.py
"""

import numpy as np
import matplotlib.pyplot as plt

L1, L2, L3 = 1.0, np.sqrt(2), np.sqrt(3)
ANG2, ANG3 = 45, 30  # grados, respecto de la horizontal


def figura_geometria():
    P0 = np.array([0.0, 0.0])
    P1 = P0 + L1 * np.array([1, 0])
    P2 = P1 + L2 * np.array([np.cos(np.radians(ANG2)), np.sin(np.radians(ANG2))])
    P3 = P2 + L3 * np.array([np.cos(np.radians(ANG3)), np.sin(np.radians(ANG3))])

    fig, ax = plt.subplots(figsize=(9, 6))

    # marco/placa (rectangulo contenedor, como en el enunciado)
    margin_x, margin_y = 0.6, 0.9
    xmin, xmax = P0[0]-margin_x, P3[0]+margin_x
    ymin, ymax = P0[1]-margin_y*0.3, P3[1]+margin_y
    ax.plot([xmin,xmax,xmax,xmin,xmin],[ymin,ymin,ymax,ymax,ymin], color='0.55', lw=1.4)

    # apoyos (triangulos con rayado) en las dos esquinas inferiores
    def apoyo(xc, y0, w=0.22, h=0.22):
        tri = plt.Polygon([[xc,y0],[xc-w/2,y0-h],[xc+w/2,y0-h]], closed=True,
                           facecolor='0.8', edgecolor='0.3', lw=1.2)
        ax.add_patch(tri)
        for i in range(5):
            xh = xc-w/2 + i*w/4
            ax.plot([xh,xh-0.06],[y0-h,y0-h-0.1], color='0.3', lw=0.8)
    apoyo(P0[0], ymin)
    apoyo(xmax-margin_x*0.4, ymin)

    # la fibra quebrada
    pts = np.array([P0,P1,P2,P3])
    ax.plot(pts[:,0], pts[:,1], color='crimson', lw=3, solid_capstyle='round', zorder=5)
    for P,lbl in zip(pts, ['P0','P1','P2','P3']):
        ax.plot(*P, 'o', color='crimson', markersize=6, zorder=6)

    # etiquetas de tramos
    mid1, mid2, mid3 = (P0+P1)/2, (P1+P2)/2, (P2+P3)/2
    ax.annotate(r'$l_1=1$', mid1+[0,-0.18], ha='center', fontsize=13, color='crimson')
    ax.annotate(r'$l_2=\sqrt{2}$', mid2+[-0.22,0.05], ha='center', fontsize=13, color='crimson')
    ax.annotate(r'$l_3=\sqrt{3}$', mid3+[0.05,0.22], ha='center', fontsize=13, color='crimson')

    # angulos
    arc2 = np.linspace(0, np.radians(ANG2), 30)
    ax.plot(P1[0]+0.3*np.cos(arc2), P1[1]+0.3*np.sin(arc2), color='steelblue', lw=1.3)
    ax.annotate('45°', P1+[0.42,0.14], color='steelblue', fontsize=11)
    arc3 = np.linspace(0, np.radians(ANG3), 30)
    ax.plot(P2[0]+0.3*np.cos(arc3), P2[1]+0.3*np.sin(arc3), color='steelblue', lw=1.3)
    ax.annotate('30°', P2+[0.42,0.06], color='steelblue', fontsize=11)
    ax.plot([P1[0],P1[0]+0.5],[P1[1],P1[1]], '--', color='0.6', lw=1)
    ax.plot([P2[0],P2[0]+0.5],[P2[1],P2[1]], '--', color='0.6', lw=1)

    ax.set_xlim(xmin-0.3, xmax+0.3); ax.set_ylim(ymin-0.5, ymax+0.3)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title("Parcial 26/06/2025, ej.2 — fibra quebrada $l_1$-$l_2$-$l_3$ en la placa\n"
                 r"($l_1{=}1$, $l_2{=}\sqrt{2}$ a $45°$, $l_3{=}\sqrt{3}$ a $30°$, respecto de la horizontal)",
                 fontsize=12.5)
    fig.tight_layout()
    fig.savefig("fig_geometria_fibra.png", dpi=130, bbox_inches="tight")
    print("  -> fig_geometria_fibra.png")


def stretch(eps, theta):
    n1, n2 = np.cos(theta), np.sin(theta)
    return eps[0,0]*n1*n1 + eps[1,1]*n2*n2 + 2*eps[0,1]*n1*n2


def figura_isotropia():
    eps_a = 1e-4 * np.eye(2)                      # (a) termico: esferico
    eps_b = 1e-4 * np.array([[1, 0.5],[0.5, 1]])  # (b) generico: NO esferico

    theta = np.linspace(0, 2*np.pi, 400)
    r_a = stretch(eps_a, theta) * 1e4   # reescalado x1e4 para que el numero sea legible
    r_b = stretch(eps_b, theta) * 1e4

    w_a, v_a = np.linalg.eigh(eps_a)
    w_b, v_b = np.linalg.eigh(eps_b)

    fig = plt.figure(figsize=(11, 10.5))

    # --- fila 1: diagrama polar de estiramiento eps(n) vs theta ---
    ax1 = fig.add_subplot(2,2,1, projection='polar')
    ax1.plot(theta, r_a, color='teal', lw=2.5)
    ax1.fill(theta, r_a, color='teal', alpha=0.15)
    ax1.set_title("(a) Térmico — $\\varepsilon(\\mathbf{n})\\times10^4$\n"
                  "CÍRCULO PERFECTO: estira igual en toda dirección", fontsize=11, pad=18)
    ax1.set_ylim(0, 2)

    ax2 = fig.add_subplot(2,2,2, projection='polar')
    ax2.plot(theta, r_b, color='darkorange', lw=2.5)
    ax2.fill(theta, r_b, color='darkorange', alpha=0.15)
    for wi, vi, c in zip(w_b, v_b.T, ['purple','purple']):
        ang = np.arctan2(vi[1], vi[0])
        ax2.plot([ang, ang], [0, wi*1e4], color=c, lw=1.6, ls='--')
        ax2.plot([ang+np.pi, ang+np.pi], [0, wi*1e4], color=c, lw=1.6, ls='--')
    ax2.set_title("(b) Genérico — $\\varepsilon(\\mathbf{n})\\times10^4$\n"
                  "óvalo: MÁXIMO a 45° (=1.5), MÍNIMO a 135° (=0.5)", fontsize=11, pad=18)
    ax2.set_ylim(0, 2)

    # --- fila 2: circulo unitario deformado (I + eps), muy exagerado para que se vea ---
    EXAG = 3000  # factor de exageracion visual (eps es ~1e-4, invisible sin esto)
    circ = np.array([np.cos(theta), np.sin(theta)])
    def_a = (np.eye(2) + EXAG*eps_a) @ circ
    def_b = (np.eye(2) + EXAG*eps_b) @ circ

    ax3 = fig.add_subplot(2,2,3)
    ax3.plot(*circ, '--', color='0.7', lw=1.3, label='círculo original')
    ax3.plot(*def_a, color='teal', lw=2.5, label='deformado (× exagerado)')
    ax3.set_aspect('equal'); ax3.set_title("(a) círculo → CÍRCULO más grande\n(solo cambia tamaño, cero distorsión)", fontsize=11)
    ax3.legend(fontsize=8, loc='upper right'); ax3.set_xlim(-1.8,1.8); ax3.set_ylim(-1.8,1.8)

    ax4 = fig.add_subplot(2,2,4)
    ax4.plot(*circ, '--', color='0.7', lw=1.3, label='círculo original')
    ax4.plot(*def_b, color='darkorange', lw=2.5, label='deformado (× exagerado)')
    for wi, vi in zip(w_b, v_b.T):
        ax4.plot([-1.5*vi[0],1.5*vi[0]], [-1.5*vi[1],1.5*vi[1]], color='purple', lw=1, ls=':')
    ax4.set_aspect('equal'); ax4.set_title("(b) círculo → ELIPSE\n(direcciones principales a ±45°, líneas punteadas)", fontsize=11)
    ax4.legend(fontsize=8, loc='upper right'); ax4.set_xlim(-1.8,1.8); ax4.set_ylim(-1.8,1.8)

    fig.suptitle("¿Cómo me doy cuenta si un tensor es isótropo? — comparación directa\n"
                 r"(a) $\varepsilon=10^{-4}\delta_{ij}$ (diag. igual, fuera-diag.=0)"
                 r"   vs   (b) diag.=(1,1) PERO fuera-diag.=0.5 $\neq 0$",
                 fontsize=13)
    fig.tight_layout(rect=[0,0,1,0.93])
    fig.savefig("fig_isotropia_comparacion.png", dpi=130, bbox_inches="tight")
    print("  -> fig_isotropia_comparacion.png")
    print(f"\nValores principales (b): {w_b*1e4} (x1e-4)  -- max=1.5 a 45°, min=0.5 a 135°")


if __name__ == "__main__":
    print("Generando figuras del ejercicio de la fibra quebrada...")
    figura_geometria()
    figura_isotropia()
    print("Listo.")
