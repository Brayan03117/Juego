import math
from OpenGL.GL import *
from src.objetos import draw_sphere, draw_cylinder, draw_param_surface

# ========================
# Ajustes para centrado y escala
# ========================
ESCALA = 0.5
OFFSET_X = 0
OFFSET_Y = 0.6 * ESCALA
OFFSET_Z = -5.5 * ESCALA
# ========================
# Cuerpo del Personaje CENTRADO Y ESCALADO
# ========================
def draw_cuerpo():
    glColor3f(1.0, 0.5, 0.0)  # Naranja
    draw_sphere((0, (0.3 * ESCALA) - OFFSET_Y, (9.2 * ESCALA) + OFFSET_Z), 3 * ESCALA)   # Cabeza
    draw_sphere((0, (-0.6 * ESCALA) - OFFSET_Y, (5.5 * ESCALA) + OFFSET_Z), 2.5 * ESCALA)  # Cuerpo

    glColor3f(1.0, 0.95, 0.6)
    draw_cylinder((-1 * ESCALA, -1 * ESCALA - OFFSET_Y, (1.2 * ESCALA) + OFFSET_Z),
                  (-1 * ESCALA, -1 * ESCALA - OFFSET_Y, (3.7 * ESCALA) + OFFSET_Z), 0.5 * ESCALA)
    draw_cylinder((1 * ESCALA, -1 * ESCALA - OFFSET_Y, (1.2 * ESCALA) + OFFSET_Z),
                  (1 * ESCALA, -1 * ESCALA - OFFSET_Y, (3.7 * ESCALA) + OFFSET_Z), 0.5 * ESCALA)

    glColor3f(1.0, 0.95, 0.6)
    def fx_j(u, t): return ESCALA * (1 - t) * math.cos(u)
    def fy_j(u, t): return ESCALA * ((1 - t) * math.sin(u) + 2.8) - OFFSET_Y
    def fz_j(u, t): return ESCALA * (1.5 * t + 7) + OFFSET_Z
    draw_param_surface(fx_j, fy_j, fz_j, (0, 2*math.pi), (0, 1))

    glColor3f(1.0, 0.85, 0.1)
    def fx_l(u, t): return 1.6 * ESCALA * (1 - t) * math.cos(u)
    def fy_l(u, t): return ESCALA * (-2 - 2.5 * t) - OFFSET_Y
    def fz_l(u, t): return 1.6 * ESCALA * (1 - t) * math.sin(u) + OFFSET_Z + (5.5 * ESCALA)
    draw_param_surface(fx_l, fy_l, fz_l, (0, 2*math.pi), (0.3, 1))

# ========================
# Detalles (Zigzag y Ojos) CENTRADOS Y ESCALADOS
# ========================
def draw_detalles():
    angle = math.radians(-13)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    glColor3f(1.0, 0.85, 0.1)
    def fx_zz(u, t): return ESCALA * ((3.2 - t) * math.cos(u) + 0.35 * math.sin(10 * u))
    def fy_zz(u, t): return ESCALA * (((3.2 - t) * math.sin(u) + 0.35 * math.cos(10 * u)) * cos_a - (0.4 * t + 6.3) * sin_a) - OFFSET_Y-.8
    def fz_zz(u, t): return ESCALA * (((3.2 - t) * math.sin(u) + 0.35 * math.cos(10 * u)) * sin_a + (0.4 * t + 6.3) * cos_a) + OFFSET_Z+.3
    draw_param_surface(fx_zz, fy_zz, fz_zz, (0, 2*math.pi), (0, 1))

    def fx_zz2(u, t): return ESCALA * ((3.5 - t) * math.cos(u) + 0.35 * math.sin(14 * u))
    def fy_zz2(u, t): return ESCALA * (((3.5 - t) * math.sin(u) + 0.35 * math.cos(14 * u)) * cos_a - (0.4 * t + 6.3) * sin_a) - OFFSET_Y-.8
    def fz_zz2(u, t): return ESCALA * (((3.5 - t) * math.sin(u) + 0.35 * math.cos(14 * u)) * sin_a + (0.4 * t + 6.3) * cos_a) + OFFSET_Z
    draw_param_surface(fx_zz2, fy_zz2, fz_zz2, (0, 2*math.pi), (0, 1))

    glColor3f(0.0, 0.0, 0.0)
    draw_sphere((-1.5 * ESCALA, 2.5 * ESCALA - OFFSET_Y, 9.2 * ESCALA + OFFSET_Z), 0.7 * ESCALA)
    draw_sphere((1.5 * ESCALA, 2.5 * ESCALA - OFFSET_Y, 9.2 * ESCALA + OFFSET_Z), 0.7 * ESCALA)

    glColor3f(1.0, 1.0, 1.0)
    draw_sphere((-1.7 * ESCALA, 2.99 * ESCALA - OFFSET_Y, 9.3 * ESCALA + OFFSET_Z), 0.3 * ESCALA)
    draw_sphere((1.7 * ESCALA, 2.99 * ESCALA - OFFSET_Y, 9.3 * ESCALA + OFFSET_Z), 0.3 * ESCALA)

# ========================
# Plumas Cabeza CENTRADAS Y ESCALADAS
# ========================
def draw_plumas():
    glColor3f(1.0, 0.85, 0.1)
    def fx_p(u, t): return 0.7 * ESCALA * (1 - t) * math.cos(u)
    def fy_p(u, t): return 0.2 * ESCALA * (1 - t) * math.sin(u) - OFFSET_Y
    def fz_p(u, t): return ESCALA * (3 * t + 12) + OFFSET_Z
    draw_param_surface(fx_p, fy_p, fz_p, (0, 2*math.pi), (0, 1))

    def fx_p2(u, t): return 0.7 * ESCALA * (1 - t) * math.cos(u)
    def fy_p2(u, t): return 0.2 * ESCALA * (1 - t) * math.sin(u) + 0.2 * ESCALA - OFFSET_Y
    def fz_p2(u, t): return ESCALA * (1 * t + 12) + OFFSET_Z
    draw_param_surface(fx_p2, fy_p2, fz_p2, (0, 2*math.pi), (0, 1))

    angle25 = math.radians(25)
    cos25 = math.cos(angle25)
    sin25 = math.sin(angle25)

    glColor3f(1.0, 0.5, 0.0)
    def fx_pi(u, t): return ESCALA * (0.5 * (1 - t) * math.cos(u) * cos25 + 2 * t * sin25 + 1)
    def fy_pi(u, t): return 0.2 * ESCALA * (1 - t) * math.sin(u) - OFFSET_Y
    def fz_pi(u, t): return ESCALA * (-0.5 * (1 - t) * math.cos(u) * sin25 + 2 * t * cos25 + 11.8) + OFFSET_Z
    draw_param_surface(fx_pi, fy_pi, fz_pi, (0, 2*math.pi), (0, 1))

    glColor3f(1.0, 0.5, 0.0)
    def fx_pd(u, t): return ESCALA * (0.5 * (1 - t) * math.cos(u) * math.cos(-angle25) + 2 * t * math.sin(-angle25) - 1)
    def fy_pd(u, t): return 0.12 * ESCALA * (1 - t) * math.sin(u) - OFFSET_Y
    def fz_pd(u, t): return ESCALA * (-0.5 * (1 - t) * math.cos(u) * math.sin(-angle25) + 2 * t * math.cos(-angle25) + 11.8) + OFFSET_Z
    draw_param_surface(fx_pd, fy_pd, fz_pd, (0, 2*math.pi), (0, 1))

    glColor3f(1.0, 0.85, 0.1)
    def fx_p2i(u, t): return ESCALA * (0.7 * (1 - t) * math.cos(u) * cos25 + 2 * t * sin25 + 0.5)
    def fy_p2i(u, t): return 0.2 * ESCALA * (1 - t) * math.sin(u) + 0.2 * ESCALA - OFFSET_Y
    def fz_p2i(u, t): return ESCALA * (-0.5 * (1 - t) * math.cos(u) * sin25 + t * cos25 + 11.8) + OFFSET_Z
    draw_param_surface(fx_p2i, fy_p2i, fz_p2i, (0, 2*math.pi), (0, 1))

    def fx_p2d(u, t): return ESCALA * (0.7 * (1 - t) * math.cos(u) * math.cos(-angle25) + 2 * t * math.sin(-angle25) - 0.5)
    def fy_p2d(u, t): return 0.1 * ESCALA * (1 - t) * math.sin(u) + 0.2 * ESCALA - OFFSET_Y
    def fz_p2d(u, t): return ESCALA * (-0.5 * (1 - t) * math.cos(u) * math.sin(-angle25) + t * math.cos(-angle25) + 11.8) + OFFSET_Z
    draw_param_surface(fx_p2d, fy_p2d, fz_p2d, (0, 2*math.pi), (0, 1))


def personaje():
    draw_cuerpo()
    draw_plumas()
    draw_detalles()
