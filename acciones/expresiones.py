from OpenGL.GL import *
from src import objetos as obj
import math
from OpenGL.GLU import *


ESCALA = 0.5
OFFSET_X = 0
OFFSET_Y = 0.6 * ESCALA
OFFSET_Z = -5.5 * ESCALA

# ========================
# personaje  levantando ceja
# ========================

def draw_cejas_chad():
    obj.draw_cuerpo()
    obj.draw_detalles()
    obj.draw_plumas()
    glColor3f(0.0, 0.0, 0.0)  # Negro
    # Ceja Izquierda (acercada en Z)
    glBegin(GL_LINES)
    glVertex3f((-2.0) * ESCALA, (10.7 * ESCALA) + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.8)
    glVertex3f((-1.4) * ESCALA, (10.7 * ESCALA) + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.8)
    glEnd()

    # Ceja Derecha (curva acercada)
    glBegin(GL_LINE_STRIP)
    for i in range(20):
        t = math.pi * i / 19
        x = (1.7 + 0.3 * math.cos(t)) * ESCALA
        y = 3.0 * ESCALA-.8
        z = (11 + 0.6 * math.sin(t)) * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y)
    glEnd()

# ========================
# personaje  feliz
# ========================

def draw_feliz():
    glColor3f(0.0, 0.0, 0.0)  # Negro

    # Cejas felices (curvas)
    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (1.5 + 0.35 * math.cos(t)) * ESCALA
        y = (2.5 + 0.1 * math.cos(2 * t)) * ESCALA-.6
        z = (11.0 - 0.2 * math.cos(2 * t)) * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y)
    glEnd()

    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (-1.5 + 0.35 * math.cos(t)) * ESCALA
        y = (2.5 + 0.1 * math.cos(2 * t)) * ESCALA-.6
        z = (11.0 - 0.2 * math.cos(2 * t)) * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y)
    glEnd()

    # Ojo Izquierdo (dos segmentos en V)
    glBegin(GL_LINES)
    glVertex3f(-2.0 * ESCALA, 9.2 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glVertex3f(-1.5 * ESCALA, 9.7 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)

    glVertex3f(-1.5 * ESCALA, 9.7 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glVertex3f(-1.0 * ESCALA, 9.2 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glEnd()

    # Ojo Derecho (dos segmentos en V)
    glBegin(GL_LINES)
    glVertex3f(1.0 * ESCALA, 9.2 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glVertex3f(1.5 * ESCALA, 9.7 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)

    glVertex3f(1.5 * ESCALA, 9.7 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glVertex3f(2.0 * ESCALA, 9.2 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glEnd()
    #Las plumas del cuello
    angle = math.radians(-13)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    glColor3f(1.0, 0.85, 0.1)
    def fx_zz(u, t): return ESCALA * ((3.2 - t) * math.cos(u) + 0.35 * math.sin(10 * u))
    def fy_zz(u, t): return ESCALA * (((3.2 - t) * math.sin(u) + 0.35 * math.cos(10 * u)) * cos_a - (0.4 * t + 6.3) * sin_a) - OFFSET_Y-.8
    def fz_zz(u, t): return ESCALA * (((3.2 - t) * math.sin(u) + 0.35 * math.cos(10 * u)) * sin_a + (0.4 * t + 6.3) * cos_a) + OFFSET_Z+.3
    obj.draw_param_surface(fx_zz, fy_zz, fz_zz, (0, 2*math.pi), (0, 1))

    def fx_zz2(u, t): return ESCALA * ((3.5 - t) * math.cos(u) + 0.35 * math.sin(14 * u))
    def fy_zz2(u, t): return ESCALA * (((3.5 - t) * math.sin(u) + 0.35 * math.cos(14 * u)) * cos_a - (0.4 * t + 6.3) * sin_a) - OFFSET_Y-.8
    def fz_zz2(u, t): return ESCALA * (((3.5 - t) * math.sin(u) + 0.35 * math.cos(14 * u)) * sin_a + (0.4 * t + 6.3) * cos_a) + OFFSET_Z
    obj.draw_param_surface(fx_zz2, fy_zz2, fz_zz2, (0, 2*math.pi), (0, 1))
    obj.draw_cuerpo()
    obj.draw_plumas()

# ========================
# personaje  indiferente
# ========================

def draw_indiferente():
    glColor3f(0.0, 0.0, 0.0)  # Negro
    # Cejas felices (curvas)
    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (1.5 + 0.35 * math.cos(t)) * ESCALA
        y = (2.5 + 0.1 * math.cos(2 * t)) * ESCALA-.6
        z = (11.0 - 0.2 * math.cos(2 * t)) * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y)
    glEnd()

    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (-1.5 + 0.35 * math.cos(t)) * ESCALA
        y = (2.5 + 0.1 * math.cos(2 * t)) * ESCALA-.6
        z = (11.0 - 0.2 * math.cos(2 * t)) * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y)
    glEnd()

    glBegin(GL_LINES)
    # Ojo izquierdo (línea recta)
    glVertex3f(-1.7 * ESCALA, 9.5 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glVertex3f(-1.3 * ESCALA, 9.5 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)

    # Ojo derecho (línea recta)
    glVertex3f(1.3 * ESCALA, 9.5 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glVertex3f(1.7 * ESCALA, 9.5 * ESCALA + OFFSET_Z, -3.0 * ESCALA - OFFSET_Y+.6)
    glEnd()

    angle = math.radians(-13)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    glColor3f(1.0, 0.85, 0.1)
    def fx_zz(u, t): return ESCALA * ((3.2 - t) * math.cos(u) + 0.35 * math.sin(10 * u))
    def fy_zz(u, t): return ESCALA * (((3.2 - t) * math.sin(u) + 0.35 * math.cos(10 * u)) * cos_a - (0.4 * t + 6.3) * sin_a) - OFFSET_Y-.8
    def fz_zz(u, t): return ESCALA * (((3.2 - t) * math.sin(u) + 0.35 * math.cos(10 * u)) * sin_a + (0.4 * t + 6.3) * cos_a) + OFFSET_Z+.3
    obj.draw_param_surface(fx_zz, fy_zz, fz_zz, (0, 2*math.pi), (0, 1))

    def fx_zz2(u, t): return ESCALA * ((3.5 - t) * math.cos(u) + 0.35 * math.sin(14 * u))
    def fy_zz2(u, t): return ESCALA * (((3.5 - t) * math.sin(u) + 0.35 * math.cos(14 * u)) * cos_a - (0.4 * t + 6.3) * sin_a) - OFFSET_Y-.8
    def fz_zz2(u, t): return ESCALA * (((3.5 - t) * math.sin(u) + 0.35 * math.cos(14 * u)) * sin_a + (0.4 * t + 6.3) * cos_a) + OFFSET_Z
    obj.draw_param_surface(fx_zz2, fy_zz2, fz_zz2, (0, 2*math.pi), (0, 1))
    obj.draw_cuerpo()
    obj.draw_plumas()

# ========================
# personaje  sorprendido
# ========================

def draw_sorprendido():
    obj.draw_cuerpo()
    obj.draw_detalles()
    obj.draw_plumas()

    glColor3f(0.0, 0.0, 0.0)  # Negro

    # Ceja Izquierda (curva)
    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (1.2 + 0.25 * math.cos(t)) * ESCALA
        y = (0.65 + 0.05 * math.sin(t)) * ESCALA-.6  # ya ajustado
        z = 12.3 * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y - .6)  # Bajamos ceja con -0.6
    glEnd()

    # Ceja Derecha (curva)
    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (-1.2 + 0.25 * math.cos(t)) * ESCALA
        y = (0.65 + 0.05 * math.sin(t)) * ESCALA-.6
        z = 12.3 * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y - .6)
    glEnd()

# ========================
# personaje  triste
# ========================

def draw_triste():
    obj.draw_cuerpo()
    obj.draw_detalles()
    obj.draw_plumas()

    glColor3f(0.0, 0.0, 0.0)  # Negro (cejas)

    # Cejas (curvas hacia abajo)
    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (1.5 + 0.35 * math.cos(t)) * ESCALA
        y = (2.5 + 0.1 * math.cos(2 * t)) * ESCALA - 0.6
        z = (11.0 - 0.2 * math.cos(2 * t)) * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y)
    glEnd()

    glBegin(GL_LINE_STRIP)
    for i in range(30):
        t = (2 * math.pi) * i / 29
        x = (-1.5 + 0.35 * math.cos(t)) * ESCALA
        y = (2.5 + 0.1 * math.cos(2 * t)) * ESCALA - 0.6
        z = (11.0 - 0.2 * math.cos(2 * t)) * ESCALA
        glVertex3f(x, z + OFFSET_Z, -y - OFFSET_Y)
    glEnd()

    # LÁGRIMA (esfera clásica)
    glColor3f(0.0, 0.4, 1.0)  # Azul
    quad = gluNewQuadric()
    glPushMatrix()
    glTranslatef(-1.5 * ESCALA, 8.5 * ESCALA + OFFSET_Z, -2.5 * ESCALA - OFFSET_Y+.6)
    gluSphere(quad, 0.5 * ESCALA, 16, 16)
    glPopMatrix()

# ========================
# personaje  enojado
# ========================

def draw_enojado():

    obj.draw_cuerpo()
    obj.draw_detalles()
    obj.draw_plumas()

    glColor3f(0, 0, 0)  # Azul oscuro, para distinguir

    # Segmento m
    start_m = (-2.8 * ESCALA, 3.6 * ESCALA - OFFSET_Y, 10.6 * ESCALA + OFFSET_Z)
    end_m = (-0.7 * ESCALA, 3.2 * ESCALA - OFFSET_Y, 9.8 * ESCALA + OFFSET_Z)
    obj.draw_cylinder(start_m, end_m, 0.2 * ESCALA)

    # Segmento n
    start_n = (2.8 * ESCALA, 3.6 * ESCALA - OFFSET_Y, 10.6 * ESCALA + OFFSET_Z)
    end_n = (0.7 * ESCALA, 3.2 * ESCALA - OFFSET_Y, 9.8 * ESCALA + OFFSET_Z)
    obj.draw_cylinder(start_n, end_n, 0.2 * ESCALA)

# ========================
# personaje  nervisos
# ========================

def draw_nervioso():
    obj.draw_plumas()
    obj.draw_detalles()
    glColor3f(1.0, 0.5, 0.0)  # Naranja
    obj.draw_sphere((0, (-0.6 * ESCALA) - OFFSET_Y, (5.5 * ESCALA) + OFFSET_Z), 2.5 * ESCALA)  # Cuerpo
    glColor3f(1.0, 0.95, 0.6)
    obj.draw_cylinder((-1 * ESCALA, -1 * ESCALA - OFFSET_Y, (1.2 * ESCALA) + OFFSET_Z),
                  (-1 * ESCALA, -1 * ESCALA - OFFSET_Y, (3.7 * ESCALA) + OFFSET_Z), 0.5 * ESCALA)
    obj.draw_cylinder((1 * ESCALA, -1 * ESCALA - OFFSET_Y, (1.2 * ESCALA) + OFFSET_Z),
                  (1 * ESCALA, -1 * ESCALA - OFFSET_Y, (3.7 * ESCALA) + OFFSET_Z), 0.5 * ESCALA)
    glColor3f(1.0, 0.95, 0.6)
    def fx_j(u, t): return ESCALA * (1 - t) * math.cos(u)
    def fy_j(u, t): return ESCALA * ((1 - t) * math.sin(u) + 2.8) - OFFSET_Y
    def fz_j(u, t): return ESCALA * (1.5 * t + 7) + OFFSET_Z
    obj.draw_param_surface(fx_j, fy_j, fz_j, (0, 2*math.pi), (0, 1))

    glColor3f(1.0, 0.85, 0.1)
    def fx_l(u, t): return 1.6 * ESCALA * (1 - t) * math.cos(u)
    def fy_l(u, t): return ESCALA * (-2 - 2.5 * t) - OFFSET_Y
    def fz_l(u, t): return 1.6 * ESCALA * (1 - t) * math.sin(u) + OFFSET_Z + (5.5 * ESCALA)
    obj.draw_param_surface(fx_l, fy_l, fz_l, (0, 2*math.pi), (0.3, 1))  
    glColor3f(1.0, 0.0, 0.0)
    obj.draw_sphere((0, (0.3 * ESCALA) - OFFSET_Y, (9.2 * ESCALA) + OFFSET_Z), 3 * ESCALA)   # Cabeza
    from math import sqrt
    glColor3f(1, 192/255,203/255)
    # Esfera n: Centro C, punto D
    C = (1.78, 2.1, 7.59)
    D = (2.03, 2.03, 7.82)
    radio_CD = sqrt((D[0]-C[0])**2 + (D[1]-C[1])**2 + (D[2]-C[2])**2)

    pos_C = (C[0] * ESCALA, C[1] * ESCALA - OFFSET_Y, C[2] * ESCALA + OFFSET_Z)
    obj.draw_sphere(pos_C, radio_CD * ESCALA)

    # Esfera n: Centro A, punto B
    A = (-1.78, 2.1, 7.59)
    B = (-2.03, 2.03, 7.82)
    radio_AB = sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2 + (B[2]-A[2])**2)

    pos_A = (A[0] * ESCALA, A[1] * ESCALA - OFFSET_Y, A[2] * ESCALA + OFFSET_Z)
    obj.draw_sphere(pos_A, radio_AB * ESCALA)
    
# ========================
# personaje  agachado
# ========================
def draw_agachado():
    glColor3f(1.0, 0.5, 0.0)  # Naranja
    obj.draw_sphere((0, (0.3 * ESCALA) - OFFSET_Y, (9.2 * ESCALA) + OFFSET_Z), 3 * ESCALA)   # Cabeza
    obj.draw_sphere((0, (-0.6 * ESCALA) - OFFSET_Y, (5.5 * ESCALA) + OFFSET_Z), 2.5 * ESCALA)  # Cuerpo
    glColor3f(1.0, 0.95, 0.6)
    def fx_j(u, t): return ESCALA * (1 - t) * math.cos(u)
    def fy_j(u, t): return ESCALA * ((1 - t) * math.sin(u) + 2.8) - OFFSET_Y
    def fz_j(u, t): return ESCALA * (1.5 * t + 7) + OFFSET_Z
    obj.draw_param_surface(fx_j, fy_j, fz_j, (0, 2*math.pi), (0, 1))

    glColor3f(1.0, 0.85, 0.1)
    def fx_l(u, t): return 1.6 * ESCALA * (1 - t) * math.cos(u)
    def fy_l(u, t): return ESCALA * (-2 - 2.5 * t) - OFFSET_Y
    def fz_l(u, t): return 1.6 * ESCALA * (1 - t) * math.sin(u) + OFFSET_Z + (5.5 * ESCALA)
    obj.draw_param_surface(fx_l, fy_l, fz_l, (0, 2*math.pi), (0.3, 1))
    glColor3f(1.0, 0.95, 0.7)  # Color crema para las piernas
   # ============ Pierna Izquierda Superior ============
    glPushMatrix()
    glTranslatef(-1.0 * ESCALA, 1.2 * ESCALA + OFFSET_Z + 0.7, -1.0 * ESCALA - OFFSET_Y + 0.9)
    glRotatef(30, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.5 * ESCALA, 0.5 * ESCALA, 2.0 * ESCALA, 20, 20)  # Alargado
    glPopMatrix()
# ============ Pierna Izquierda Inferior ============
    glPushMatrix()
    glTranslatef(-1.2 * ESCALA, 2.45 * ESCALA + OFFSET_Z + 0.2, -0.5 * ESCALA - OFFSET_Y + 0.8)
    glRotatef(-30, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.5 * ESCALA, 0.5 * ESCALA, 2.0 * ESCALA, 20, 20)  # Alargado
    glPopMatrix()
# ============ Pierna Derecha Superior ============
    glPushMatrix()
    glTranslatef(1.0 * ESCALA, 1.2 * ESCALA + OFFSET_Z + 0.7, -1.0 * ESCALA - OFFSET_Y + 0.9)
    glRotatef(30, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.5 * ESCALA, 0.5 * ESCALA, 2.0 * ESCALA, 20, 20)  # Alargado
    glPopMatrix()
# ============ Pierna Derecha Inferior ============
    glPushMatrix()
    glTranslatef(1.2 * ESCALA, 2.45 * ESCALA + OFFSET_Z + 0.2, -0.5 * ESCALA - OFFSET_Y + 0.8)
    glRotatef(-30, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.5 * ESCALA, 0.5 * ESCALA, 2.0 * ESCALA, 20, 20)  # Alargado
    glPopMatrix()
    # Dibuja cuerpo y plumas
    obj.draw_detalles()
    obj.draw_plumas()

# ========================
# personaje  sentado
# ========================
def dibujar_personaje_sentado():
    obj.draw_detalles()
    obj.draw_plumas()
    glColor3f(1.0, 0.5, 0.0)  # Naranja
    obj.draw_sphere((0, (0.3 * ESCALA) - OFFSET_Y, (9.2 * ESCALA) + OFFSET_Z), 3 * ESCALA)   # Cabeza
    obj.draw_sphere((0, (-0.6 * ESCALA) - OFFSET_Y, (5.5 * ESCALA) + OFFSET_Z), 2.5 * ESCALA)  # Cuerpo
    glColor3f(1.0, 0.95, 0.6)
    # Pierna Izquierda acostada e inclinada hacia abajo
    glPushMatrix()
    glTranslatef(-1.0 * ESCALA, -1.0 * ESCALA - OFFSET_Y, (3.2 * ESCALA) + OFFSET_Z)
    glRotatef(-60, 1, 0, 0)  # Inclinación más suave
    gluCylinder(gluNewQuadric(), 0.5 * ESCALA, 0.5 * ESCALA, 2.0 * ESCALA, 20, 20)
    glPopMatrix()

    # Pierna Derecha acostada e inclinada hacia abajo
    glPushMatrix()
    glTranslatef(1.0 * ESCALA, -1.0 * ESCALA - OFFSET_Y, (3.2 * ESCALA) + OFFSET_Z)
    glRotatef(-60, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.5 * ESCALA, 0.5 * ESCALA, 2.0 * ESCALA, 20, 20)
    glPopMatrix()
    glColor3f(1.0, 0.95, 0.6)
    def fx_j(u, t): return ESCALA * (1 - t) * math.cos(u)
    def fy_j(u, t): return ESCALA * ((1 - t) * math.sin(u) + 2.8) - OFFSET_Y
    def fz_j(u, t): return ESCALA * (1.5 * t + 7) + OFFSET_Z
    obj.draw_param_surface(fx_j, fy_j, fz_j, (0, 2*math.pi), (0, 1))
    glColor3f(1.0, 0.85, 0.1)
    def fx_l(u, t): return 1.6 * ESCALA * (1 - t) * math.cos(u)
    def fy_l(u, t): return ESCALA * (-2 - 2.5 * t) - OFFSET_Y
    def fz_l(u, t): return 1.6 * ESCALA * (1 - t) * math.sin(u) + OFFSET_Z + (5.5 * ESCALA)
    obj.draw_param_surface(fx_l, fy_l, fz_l, (0, 2*math.pi), (0.3, 1))

def dibujar_personaje_acostado():
    glPushMatrix()
    # Rotar todo el personaje sobre el eje X para acostarlo
    glTranslatef(0, 0, 0)  # punto de pivote
    glRotatef(90, 1, 0, 0)  # rotación hacia atrás (mirando hacia arriba)
    
    # Dibujo normal, pero rotado
    obj.draw_cuerpo()
    obj.draw_detalles()
    obj.draw_plumas()
    
    glPopMatrix()