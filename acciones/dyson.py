from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from math import sin, cos, radians  # Importar funciones trigonométricas 
import time
import math

def draw_rectangle(width, height, depth, position):
    x, y, z = position
    half_w, half_h, half_d = width / 2, height / 2, depth / 2
    
    glBegin(GL_QUADS)
    
    # Front Face
    glNormal3f(0, 0, 1)
    glVertex3f(x - half_w, y - half_h, z + half_d)
    glVertex3f(x + half_w, y - half_h, z + half_d)
    glVertex3f(x + half_w, y + half_h, z + half_d)
    glVertex3f(x - half_w, y + half_h, z + half_d)
    
    # Back Face
    glNormal3f(0, 0, -1)
    glVertex3f(x - half_w, y - half_h, z - half_d)
    glVertex3f(x - half_w, y + half_h, z - half_d)
    glVertex3f(x + half_w, y + half_h, z - half_d)
    glVertex3f(x + half_w, y - half_h, z - half_d)
    
    # Top Face
    glNormal3f(0, 1, 0)
    glVertex3f(x - half_w, y + half_h, z - half_d)
    glVertex3f(x - half_w, y + half_h, z + half_d)
    glVertex3f(x + half_w, y + half_h, z + half_d)
    glVertex3f(x + half_w, y + half_h, z - half_d)
    
    # Bottom Face
    glNormal3f(0, -1, 0)
    glVertex3f(x - half_w, y - half_h, z - half_d)
    glVertex3f(x + half_w, y - half_h, z - half_d)
    glVertex3f(x + half_w, y - half_h, z + half_d)
    glVertex3f(x - half_w, y - half_h, z + half_d)
    
    # Right Face
    glNormal3f(1, 0, 0)
    glVertex3f(x + half_w, y - half_h, z - half_d)
    glVertex3f(x + half_w, y + half_h, z - half_d)
    glVertex3f(x + half_w, y + half_h, z + half_d)
    glVertex3f(x + half_w, y - half_h, z + half_d)
    
    # Left Face
    glNormal3f(-1, 0, 0)
    glVertex3f(x - half_w, y - half_h, z - half_d)
    glVertex3f(x - half_w, y - half_h, z + half_d)
    glVertex3f(x - half_w, y + half_h, z + half_d)
    glVertex3f(x - half_w, y + half_h, z - half_d)
    
    glEnd()

def draw_cube(size, position):
    x, y, z = position
    half = size / 2
    glBegin(GL_QUADS)
    
    # Front Face
    glVertex3f(x - half, y - half, z + half)
    glVertex3f(x + half, y - half, z + half)
    glVertex3f(x + half, y + half, z + half)
    glVertex3f(x - half, y + half, z + half)
    
    # Back Face
    glVertex3f(x - half, y - half, z - half)
    glVertex3f(x - half, y + half, z - half)
    glVertex3f(x + half, y + half, z - half)
    glVertex3f(x + half, y - half, z - half)
    
    # Top Face
    glVertex3f(x - half, y + half, z - half)
    glVertex3f(x - half, y + half, z + half)
    glVertex3f(x + half, y + half, z + half)
    glVertex3f(x + half, y + half, z - half)
    
    # Bottom Face
    glVertex3f(x - half, y - half, z - half)
    glVertex3f(x + half, y - half, z - half)
    glVertex3f(x + half, y - half, z + half)
    glVertex3f(x - half, y - half, z + half)
    
    # Right face
    glVertex3f(x + half, y - half, z - half)
    glVertex3f(x + half, y + half, z - half)
    glVertex3f(x + half, y + half, z + half)
    glVertex3f(x + half, y - half, z + half)
    
    # Left Face
    glVertex3f(x - half, y - half, z - half)
    glVertex3f(x - half, y - half, z + half)
    glVertex3f(x - half, y + half, z + half)
    glVertex3f(x - half, y + half, z - half)
    
    glEnd()

def draw_triangular_prism(base, height, depth, position):
    x, y, z = position
    glBegin(GL_TRIANGLES)
    glVertex3f(x, y, z)
    glVertex3f(x + base, y, z)
    glVertex3f(x + base / 2, y + height, z)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x + base, y, z)
    glVertex3f(x + base, y, z + depth)
    glVertex3f(x, y, z + depth)
    glEnd()

def draw_rotated_rectangle(width, height, depth, position, angle):
    x, y, z = position
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(angle, 0, 0, 1)  # Rotar alrededor del eje Z
    draw_rectangle(width, height, depth, (0, 0, 0))  # Dibujar en el origen
    glPopMatrix()


def draw_cone(base_radius, height, slices, position):
    x, y, z = position
    glPushMatrix()
    glTranslatef(x, y, z)
    quadric = gluNewQuadric()
    gluCylinder(quadric, base_radius, 0, height, slices, 1)  # Radio superior 0 para hacer un cono
    gluDeleteQuadric(quadric)
    glPopMatrix()

def set_amarillo():
    # Amarillo 
    glColor3f(255/255.0, 255/255.0, 143/255.0)  # amarillo claro


def set_verde():
    # Verde 
    glColor3f( 99/255.0, 148/255.0, 53/255.0)  # verde azulado oscuro

def set_robot_purple():
    # Púrpura
    glColor3f(148/255.0, 0.0, 211/255.0)

def set_naranja():
    # Naranja
    glColor3f(1.0, 0.5, 0.0)  # Naranja

def set_blanco_sucio():
    # Blanco Sucio (ligeramente amarillento)
    glColor3f(0.9, 0.9, 0.8)

def set_color_rgb(r, g, b):
    glColor3f(r / 255.0, g / 255.0, b / 255.0)


def set_azul():
    # Azul
    glColor3f(0.0, 0.0, 1.0)  # Azul

# Variables globales (configuración)
ILUMINACION_HABILITADA = True

SCALE_FACTOR = 0.3

# Dimensiones del cuerpo (calculadas una vez)
CUERPO_ANCHO = 6 * SCALE_FACTOR
CUERPO_ALTO = 9 * SCALE_FACTOR
CUERPO_PROFUNDIDAD = 4.5 * SCALE_FACTOR
BRAZOS_ANCHO = 1.5 * SCALE_FACTOR
BRAZOS_ALTO = 6 * SCALE_FACTOR
PIERNAS_ANCHO = 2.1 * SCALE_FACTOR
PIERNAS_ALTO = 12 * SCALE_FACTOR
PIERNAS_BASE_ANCHO = 1.8 * SCALE_FACTOR
SEPARACION_X = 0.5 * SCALE_FACTOR
COLOR_CUERPO = None
COLOR_BRAZOS = None
COLOR_PIERNAS = None
COLOR_CABEZA = None
COLOR_CASCO = None
COLOR_OJOS = None
COLOR_PICO = None

def dibujar_brazo_izquierdo(position, color_func):
    x, y, z = position
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2
    glPushMatrix()
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_left, y_arm, z - 5))
    glPopMatrix()

def dibujar_brazo_derecho(position, color_func):
    x, y, z = position
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2
    glPushMatrix()
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_right, y_arm, z - 5))
    glPopMatrix()

def dibujar_pierna_izquierda(position, color_func):
    x, y, z = position
    y_leg = y - 4
    x_left_leg = x - PIERNAS_BASE_ANCHO / 2 - SEPARACION_X
    glPushMatrix()
    color_func()
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_left_leg, y_leg, z - 5))
    glPopMatrix()

def dibujar_pierna_derecha(position, color_func):
    x, y, z = position
    y_leg = y - 4
    x_right_leg = x + PIERNAS_BASE_ANCHO / 2 + SEPARACION_X
    glPushMatrix()
    color_func()
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_right_leg, y_leg, z - 5))
    glPopMatrix()


def dibujar_cuerpo(position, color_func):
    x, y, z = position
    glPushMatrix()
    color_func()
    y_body = y + CUERPO_ALTO / 2 - 4
    draw_rectangle(CUERPO_ANCHO, CUERPO_ALTO, CUERPO_PROFUNDIDAD, (x, y_body, z - 5))
    glPopMatrix()

def dibujar_brazos(position, color_func):
    x, y, z = position
    glPushMatrix()
    color_func()
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_left, y_arm, z - 5))
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_right, y_arm, z - 5))
    glPopMatrix()

def dibujar_piernas(position, color_func):
    x, y, z = position
    glPushMatrix()
    color_func()
    y_legs = y - 4
    x_left = x - PIERNAS_BASE_ANCHO / 2 - SEPARACION_X
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_left, y_legs, z - 5))
    x_right = x + PIERNAS_BASE_ANCHO / 2 + SEPARACION_X
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_right, y_legs, z - 5))
    glPopMatrix()

def dibujar_cabeza(position, color_cabeza, color_ojos, color_casco, color_pico):
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor_head = cabeza_lado / (6 * SCALE_FACTOR)
    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    pos_cabeza = (x, y_head, z - 5)

    glPushMatrix()
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, pos_cabeza)
    glPopMatrix()

    dibujar_casco(pos_cabeza, cabeza_lado, scale_factor_head, color_casco)
    dibujar_ojos(pos_cabeza, cabeza_lado, scale_factor_head, color_ojos)
    dibujar_pico(pos_cabeza, scale_factor_head, color_pico)

def dibujar_casco(position, cabeza_lado, scale_factor, color_func):
    x, y, z = position
    glPushMatrix()
    color_func()
    y_helmet = y + cabeza_lado / 2 - 0.2 * scale_factor
    z_helmet = z + cabeza_lado / 2 + 0.1 * scale_factor
    draw_rectangle(2 * scale_factor, 0.3 * scale_factor, 0.2 * scale_factor,
                   (x, y_helmet, z_helmet))
    glPopMatrix()

def dibujar_ojos(position, cabeza_lado, scale_factor, color_func):
    x, y, z = position
    glPushMatrix()
    color_func()
    y_eye = y + 0.1 * scale_factor
    z_eye = z + cabeza_lado / 2 - 0.1
    draw_cube(0.3 * scale_factor, (x - 0.6 * scale_factor, y_eye, z_eye))
    draw_cube(0.3 * scale_factor, (x + 0.6 * scale_factor, y_eye, z_eye))
    glPopMatrix()

def dibujar_pico(position, scale_factor, color_func):
    x, y, z = position
    glPushMatrix()
    color_func()
    draw_triangular_prism(0.6 * scale_factor, 0.3 * scale_factor, 0.3 * scale_factor,
                          (x - 0.2 * scale_factor, y - 0.2 * scale_factor, z + (6 * SCALE_FACTOR) / 2 + 0.1))
    glPopMatrix()



def original5(position):
   # configurar_iluminacion()

        dibujar_cuerpo(position, set_naranja)
        dibujar_brazos(position, set_verde)
        dibujar_piernas(position, set_azul)
        dibujar_cabeza(position, set_amarillo)
    #deshabilitar_iluminacion()

def pAsco(position):
    import time
    x, y, z = position

    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor_head = cabeza_lado / (6 * SCALE_FACTOR)

    current_time = time.time()
    
    # Movimiento de cabeza lateral (como decir "no")
    head_rotation_z = 25 * math.sin(current_time * 3)
    
    # Movimiento amplio del brazo derecho (0 a 150 grados)
    arm_angle_front = 75 + 75 * math.sin(current_time * 2)

    glPushMatrix()

    # Cuerpo (misma posición que en original5)
    set_verde()
    y_body = y + CUERPO_ALTO / 2 - 4
    draw_rectangle(CUERPO_ANCHO, CUERPO_ALTO, CUERPO_PROFUNDIDAD, (x, y_body, z - 5))

    # Brazos - ajustados para misma altura visual
    set_amarillo()
    y_arm = y_body  # Misma altura para ambos brazos
    
    # Brazo izquierdo (estático)
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_left, y_arm, z - 5))

    # Brazo derecho (con movimiento pero misma altura base)
    glPushMatrix()
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2
    glTranslatef(x_right, y_arm + BRAZOS_ALTO/2, z - 5)  # Pivote en el hombro
    glRotatef(-arm_angle_front, 1, 0, 0)
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (0, -BRAZOS_ALTO/2, 0))
    glPopMatrix()

    # Piernas
    set_naranja()
    y_legs = y - 4
    x_left_leg = x - PIERNAS_BASE_ANCHO / 2 - SEPARACION_X
    x_right_leg = x + PIERNAS_BASE_ANCHO / 2 + SEPARACION_X
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_left_leg, y_legs, z - 5))
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_right_leg, y_legs, z - 5))

    # Cabeza con movimiento
    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    head_z = z - 5
    
    glPushMatrix()
    glTranslatef(x, y_head, head_z)  # Movemos al centro de la cabeza
    glRotatef(head_rotation_z, 0, 1, 0)  # Rotación lateral
    glTranslatef(-x, -y_head, -head_z)  # Volvemos al sistema original

    # Cabeza
    set_verde()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, head_z))

    # Casco
    set_naranja()
    draw_rectangle(
        2 * scale_factor_head,
        0.3 * scale_factor_head,
        0.2 * scale_factor_head,
        (x, y_head + cabeza_lado / 2 - 0.2 * SCALE_FACTOR, head_z + cabeza_lado / 2 + 0.1 * SCALE_FACTOR)
    )

    # Ojos cuadrados como en el método original (visibles con rotación de cabeza)
    set_color_rgb(10, 10, 10)  # Negro mate como en dibujar_ojos()
    
    # Ojo izquierdo
    glPushMatrix()
    glTranslatef(x - 0.6 * scale_factor_head, y_head + 0.1 * scale_factor_head, head_z + cabeza_lado / 2 - 0.1)
    # Dibujamos cubo en lugar de rectángulo para que sea visible desde cualquier ángulo
    draw_cube(0.3 * scale_factor_head, position)
    glPopMatrix()
    
    # Ojo derecho
    glPushMatrix()
    glTranslatef(x + 0.6 * scale_factor_head, y_head + 0.1 * scale_factor_head, head_z + cabeza_lado / 2 - 0.1)
    draw_cube(0.3 * scale_factor_head, position)
    glPopMatrix()

    # Pico
    set_amarillo()
    draw_triangular_prism(
        0.6 * scale_factor_head,
        0.3 * scale_factor_head,
        0.3 * scale_factor_head,
        (x - 1.0 * SCALE_FACTOR, y_head - 0.2 * scale_factor_head, head_z + cabeza_lado / 2 + 0.1 * SCALE_FACTOR)
    )

    glPopMatrix()  # Fin de transformaciones de cabeza

    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

#========================================================== == ANIMACIONES========================================================== ===

#================================ ASCO ================================
def animar_brazo_asco(position, color_func):
    x, y, z = position
    current_time = time.time()
    angle = 75 + 75 * math.sin(current_time * 2)

    y_arm = y + CUERPO_ALTO / 2 - 4
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2

    glPushMatrix()
    glTranslatef(x_right, y_arm + BRAZOS_ALTO / 2, z - 5)
    glRotatef(-angle, 1, 0, 0)
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (0, -BRAZOS_ALTO / 2, 0))
    glPopMatrix()

def animar_cabeza_asco(position, color_cabeza, color_ojos, color_casco, color_pico):
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor = cabeza_lado / (6 * SCALE_FACTOR)
    current_time = time.time()
    angle = 25 * math.sin(current_time * 3)

    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    head_z = z - 5

    glPushMatrix()
    glTranslatef(x, y_head, head_z)
    glRotatef(angle, 0, 1, 0)
    glTranslatef(-x, -y_head, -head_z)

    # Cabeza
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, head_z))

    # Casco
    dibujar_casco((x, y_head, head_z), cabeza_lado, scale_factor, color_casco)

    # Ojos
    dibujar_ojos((x, y_head, head_z), cabeza_lado, scale_factor, color_ojos)

    # Pico
    dibujar_pico((x, y_head, head_z), scale_factor, color_pico)

    glPopMatrix()

#================================ ADMIRAR ================================
def animar_brazo_izquierdo_admirar(position, color_func):
    import math, time
    x, y, z = position
    current_time = time.time()
    angle = 60 * math.sin(current_time * 2)

    y_arm = y + CUERPO_ALTO / 2 - 4
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2

    glPushMatrix()
    glTranslatef(x_left, y_arm + BRAZOS_ALTO / 2, z - 5)
    glRotatef(-angle, 0, 0, 1)
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (0, -BRAZOS_ALTO / 2, 0))
    glPopMatrix()

def animar_cabeza_admirar(position, color_cabeza, color_ojos, color_casco, color_pico):
    import math, time
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor = cabeza_lado / (6 * SCALE_FACTOR)
    current_time = time.time()
    angle = 10 * math.sin(current_time * 1.5)

    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    z_head = z - 5

    glPushMatrix()
    glTranslatef(x, y_head, z_head)
    glRotatef(angle, 0, 1, 0)
    glTranslatef(-x, -y_head, -z_head)

    # Cabeza
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, z_head))

    # Casco
    dibujar_casco((x, y_head, z_head), cabeza_lado, scale_factor, color_casco)

    # Cejas (negras)
    set_negro()  # o usa color_por_parte("cejas", paleta) si prefieres
    ceja_z = z_head + cabeza_lado / 2 - 0.05
    draw_rotated_rectangle(
        0.6 * scale_factor, 0.15 * scale_factor, 0.15 * scale_factor,
        (x - 0.6 * scale_factor, y_head + 0.35 * scale_factor, ceja_z),
        60
    )
    draw_rotated_rectangle(
        0.6 * scale_factor, 0.15 * scale_factor, 0.15 * scale_factor,
        (x + 0.6 * scale_factor, y_head + 0.35 * scale_factor, ceja_z),
        -60
    )

    # Ojos
    dibujar_ojos((x, y_head, z_head), cabeza_lado, scale_factor, color_ojos)

    # Pico (tipo cono)
    glPushMatrix()
    glTranslatef(x - 0.2 * scale_factor, y_head - 0.2 * scale_factor, z_head + cabeza_lado / 2 + 0.1 * scale_factor)
    color_pico()
    draw_cone(0.2, 0.3, 32, (0, 0, 0))
    glPopMatrix()

    glPopMatrix()

#================================ SAD ================================
def animar_brazo_izquierdo_sad(position, color_func):
    x, y, z = position
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2

    glPushMatrix()
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_left, y_arm, z - 5))
    glPopMatrix()

def animar_brazo_derecho_sad(position, color_func):
    x, y, z = position
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2

    glPushMatrix()
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_right, y_arm, z - 5))
    glPopMatrix()

def animar_cabeza_sad(position, color_cabeza, color_ojos, color_casco, color_pico):
    import time
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor = cabeza_lado / (6 * SCALE_FACTOR)

    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    z_head = z - 5
    t = time.time()

    glPushMatrix()

    # Cabeza
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, z_head))

    # Casco
    dibujar_casco((x, y_head, z_head), cabeza_lado, scale_factor, color_casco)

    # Ojos
    dibujar_ojos((x, y_head, z_head), cabeza_lado, scale_factor, color_ojos)

    # Pico
    dibujar_pico((x, y_head, z_head), scale_factor, color_pico)

    # Lágrimas animadas
    glColor3f(0.0, 0.0, 1.0)  # Azul fuerte
    glBegin(GL_LINES)
    for i in range(2):  # Ojo izq y der
        offset_x = (-0.6 if i == 0 else 0.6) * scale_factor
        for j in range(5):  # 5 líneas por ojo
            base_x = x + offset_x + 0.1 * j * scale_factor
            base_y = (y_head+0.5) - 0.1 * scale_factor - 0.15 * j * scale_factor
            lagrima_length = 0.8 + 0.2 * math.sin(t * 2 + j)  # animar longitud
            glVertex3f(base_x, base_y, z_head + cabeza_lado / 2 - 0.1)
            glVertex3f(base_x, base_y - lagrima_length, z_head + cabeza_lado / 2 - 0.1)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glPopMatrix()

#================================ Happy ================================

def animar_brazo_izquierdo_happy(position, color_func):
    import time, math
    x, y, z = position
    angle = 25 * math.sin(time.time() * 2)

    y_arm = y + CUERPO_ALTO / 2 - 4
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2

    glPushMatrix()
    glTranslatef(x_left, y_arm + BRAZOS_ALTO / 2, z - 5)
    glRotatef(-angle, 0, 1, 0)
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (0, -BRAZOS_ALTO / 2, 0))
    glPopMatrix()

def animar_brazo_derecho_happy(position, color_func):
    import time, math
    x, y, z = position
    angle = 25 * math.sin(time.time() * 2)

    y_arm = y + CUERPO_ALTO / 2 - 4
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2

    glPushMatrix()
    glTranslatef(x_right, y_arm + BRAZOS_ALTO / 2, z - 5)
    glRotatef(-angle, 0, 1, 0)
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (0, -BRAZOS_ALTO / 2, 0))
    glPopMatrix()

def dibujar_cabeza_happy(position, color_cabeza, color_ojos, color_casco, color_pico):
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor = cabeza_lado / (6 * SCALE_FACTOR)

    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    z_head = z - 5

    glPushMatrix()

    # Cabeza
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, z_head))

    # Casco
    dibujar_casco((x, y_head, z_head), cabeza_lado, scale_factor, color_casco)

    # Ojos
    dibujar_ojos((x, y_head, z_head), cabeza_lado, scale_factor, color_ojos)

    # Pico
    glPushMatrix()
    glTranslatef(x - 0.2 * scale_factor, y_head - 0.2 * scale_factor, z_head + cabeza_lado / 2 + 0.1 * scale_factor)
    color_pico()
    draw_cone(0.2, 0.3, 32, (0, 0, 0))
    glPopMatrix()

    # Pestañas negras
    set_negro()
    draw_rotated_rectangle(
        0.5 * scale_factor, 0.08 * scale_factor, 0.1 * scale_factor,
        (x - 0.6 * scale_factor, y_head + 0.25 * scale_factor, z_head + cabeza_lado / 2 - 0.05),
        15
    )
    draw_rotated_rectangle(
        0.5 * scale_factor, 0.08 * scale_factor, 0.1 * scale_factor,
        (x + 0.6 * scale_factor, y_head + 0.25 * scale_factor, z_head + cabeza_lado / 2 - 0.05),
        -15
    )

    glPopMatrix()

#================================ Enojo ================================

def animar_cabeza_enojar(position, color_cabeza, color_ojos, color_casco, color_pico):
    import time, math
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor = cabeza_lado / (6 * SCALE_FACTOR)
    current_time = time.time()
    shake_angle = 10 * math.sin(current_time * 8)

    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    z_head = z - 5

    glPushMatrix()
    glTranslatef(x, y_head, z_head)
    glRotatef(shake_angle, 0, 0, 0)
    glTranslatef(-x, -y_head, -z_head)

    # Cabeza
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, z_head))

    # Casco
    dibujar_casco((x, y_head, z_head), cabeza_lado, scale_factor, color_casco)

    # Ojos
    dibujar_ojos((x, y_head, z_head), cabeza_lado, scale_factor, color_ojos)

    # Pico
    dibujar_pico((x, y_head, z_head), scale_factor, color_pico)

    # Cejas rectas negras
    set_negro()
    ceja_ancho = 0.4 * scale_factor
    ceja_alto = 0.1 * scale_factor
    ceja_z = z_head + cabeza_lado / 2 - 0.1
    y_ceja = y_head + 0.3 * scale_factor

    draw_rectangle(ceja_ancho, ceja_alto, 0.1 * scale_factor, (x - 0.6 * scale_factor, y_ceja, ceja_z))
    draw_rectangle(ceja_ancho, ceja_alto, 0.1 * scale_factor, (x + 0.6 * scale_factor, y_ceja, ceja_z))

    glPopMatrix()

def animar_brazo_izquierdo_enojar(position, color_func):
    x, y, z = position
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2

    glPushMatrix()
    glTranslatef(x_left, y_arm, z - 5)
    glRotatef(-15, 1, 0, 0)  # Ligeramente hacia el frente
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (0, 0, 0))
    glPopMatrix()

def animar_brazo_derecho_enojar(position, color_func):
    x, y, z = position
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2

    glPushMatrix()
    glTranslatef(x_right, y_arm, z - 5)
    glRotatef(15, 1, 0, 0)
    color_func()
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (0, 0, 0))
    glPopMatrix()

#================================ Gesto ================================

def animar_cabeza_gesto(position, color_cabeza, color_ojos, color_casco, color_pico):
    import time
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor = cabeza_lado / (6 * SCALE_FACTOR)

    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    z_head = z - 5

    glPushMatrix()

    # Cabeza
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, z_head))

    # Casco
    dibujar_casco((x, y_head, z_head), cabeza_lado, scale_factor, color_casco)

    # OJOS: Ojo izquierdo animado (guiño), derecho normal
    current_time = time.time()
    wink_duration = 0.5
    cycle_time = 3.0
    elapsed = current_time % cycle_time
    if elapsed < wink_duration:
        t = elapsed / wink_duration
        wink_scale = 1.0 - abs(t * 2 - 1)
    else:
        wink_scale = 1.0

    # Ojo izquierdo (animado)
    glPushMatrix()
    color_ojos()
    draw_cube(0.3 * scale_factor * wink_scale, (x - 0.6 * scale_factor, y_head + 0.1 * scale_factor, z_head + cabeza_lado / 2 - 0.1))
    glPopMatrix()

    # Ojo derecho
    glPushMatrix()
    color_ojos()
    draw_cube(0.3 * scale_factor, (x + 0.6 * scale_factor, y_head + 0.1 * scale_factor, z_head + cabeza_lado / 2 - 0.1))
    glPopMatrix()

    # Pico
    dibujar_pico((x, y_head, z_head), scale_factor, color_pico)

    # Cejas confiadas (inclinadas levemente hacia abajo en centro)
    set_negro()
    draw_rotated_rectangle(
        0.6 * scale_factor, 0.08 * scale_factor, 0.1 * scale_factor,
        (x - 0.6 * scale_factor, y_head + 0.3 * scale_factor, z_head + cabeza_lado / 2 - 0.05),
        25
    )
    draw_rotated_rectangle(
        0.6 * scale_factor, 0.08 * scale_factor, 0.1 * scale_factor,
        (x + 0.6 * scale_factor, y_head + 0.3 * scale_factor, z_head + cabeza_lado / 2 - 0.05),
        -25
    )

    glPopMatrix()

#================================ Dormir ================================

def animar_cabeza_dormir(position, color_cabeza, color_ojos, color_casco, color_pico):
    import time, math
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor = cabeza_lado / (6 * SCALE_FACTOR)

    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    z_head = z - 5

    current_time = time.time()
    tilt_angle = 15 + 5 * math.sin(current_time * 2)  # cabeza inclinada suavemente (cabeceo)

    glPushMatrix()
    glTranslatef(x, y_head, z_head)
    glRotatef(tilt_angle, 1, 0, 0)
    glTranslatef(-x, -y_head, -z_head)

    # Cabeza
    color_cabeza()
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, z_head))

    # Casco
    dibujar_casco((x, y_head, z_head), cabeza_lado, scale_factor, color_casco)

    # Ojos entrecerrados como rectángulos planos
    color_ojos()

    # Ojo izquierdo (ligeramente caído)
    draw_rotated_rectangle(
        0.35 * scale_factor, 0.08 * scale_factor, 0.1 * scale_factor,
        (x - 0.6 * scale_factor, y_head + 0.1 * scale_factor, z_head + cabeza_lado / 2 - 0.05),
        10  # leve caída diagonal
    )

    # Ojo derecho (igual, pero en sentido contrario)
    draw_rotated_rectangle(
        0.35 * scale_factor, 0.08 * scale_factor, 0.1 * scale_factor,
        (x + 0.6 * scale_factor, y_head + 0.1 * scale_factor, z_head + cabeza_lado / 2 - 0.05),
        -10
    )

    # Pico (tipo cono)
    glPushMatrix()
    glTranslatef(x - 0.2 * scale_factor, y_head - 0.2 * scale_factor, z_head + cabeza_lado / 2 + 0.1)
    color_pico()
    draw_cone(0.2, 0.3, 32, (0, 0, 0))
    glPopMatrix()

    glPopMatrix()


#####-------------------------------------------COLORES----------------------------------------#############

def set_azul_grisaceo():
    # Azul Grisáceo
    glColor3f(0.4, 0.5, 0.6) # RGB: 102, 128, 153

def set_gris_oscuro():
    # Gris Oscuro
    glColor3f(0.2, 0.2, 0.2) # RGB: 51, 51, 51

def set_purpura():
    # Púrpura (basado en ambiente)
    glColor3f(0.5, 0.0, 0.5) # RGB: 128, 0, 128

def set_marron_opaco():
    # Marrón Opaco
    glColor3f(0.3, 0.2, 0.1) # RGB: 77, 51, 26

def set_blanco_sucio():
    # Blanco Sucio (basado en ambiente)
    glColor3f(0.9, 0.9, 0.8) # RGB: 230, 230, 204

def set_negro():
    # Negro
    glColor3f(0.0, 0.0, 0.0) # RGB: 0, 0, 0

def set_black():
    # Negro
    glColor3f(10, 10, 10) # RGB: 0, 0, 0

def set_robot_dark():
    # Robot Oscuro (Gris Oscuro)
    glColor3f(0.2, 0.2, 0.2) # RGB: 51, 51, 51

def set_robot_purple():
    # Robot Púrpura (basado en ambiente)
    glColor3f(0.4, 0.0, 0.8) # RGB: 102, 0, 204

def set_blue():
    # Azul (basado en ambiente)
    glColor3f(0.0, 0.0, 1.0) # RGB: 0, 0, 255

def set_dark_blue():
    # Azul Oscuro
    glColor3f(0.0, 0.0, 0.5) # RGB: 0, 0, 128

def set_grey():
    # Gris
    glColor3f(0.5, 0.5, 0.5) # RGB: 128, 128, 128

def set_purple():
    # Púrpura (basado en ambiente)
    glColor3f(0.5, 0.0, 0.5) # RGB: 128, 0, 128

def set_morado():
    # Morado (aproximado)
    glColor3f(0.4039, 0.2275, 0.7176) # RGB: 103, 58, 183


def set_gray2():
    # Gris Claro
    glColor3f(176/255.0, 190/255.0, 197/255.0) # RGB: 176, 190, 197

def set_rojo():
    # Rojo (basado en ambiente)
    glColor3f(198/255.0, 40/255.0, 40/255.0) # RGB: 198, 40, 40

def set_gray():
    # Gris
    glColor3f(0.5, 0.5, 0.5) # RGB: 128, 128, 128

def set_blue_light():
    # Azul Claro
    glColor3f(0.2, 0.5, 1.0) # RGB: 51, 128, 255

def set_naranja_claro_transparente():
    # Naranja Claro Transparente (ignorando transparencia)
    glColor3f(1.0, 0.7, 0.3) # RGB: 255, 179, 77

def set_verde_claro_transparente():
    # Verde Claro Transparente (ignorando transparencia)
    glColor3f(0.5, 1.0, 0.5) # RGB: 128, 255, 128

def set_blue_light_claro_transparente():
    # Azul Claro Transparente (ignorando transparencia)
    glColor3f(0.6, 0.8, 1.0) # RGB: 153, 204, 255

def set_rojo_claro_transparente():
    # Rojo Claro Transparente (ignorando transparencia)
    glColor3f(1.0, 0.5, 0.5) # RGB: 255, 128, 128

def set_robot_dark_claro_transparente():
    # Robot Oscuro Claro Transparente (ignorando transparencia)
    glColor3f(0.4, 0.4, 0.4) # RGB: 102, 102, 102

def set_amarillo_claro_transparente():
    # Amarillo Claro Transparente (ignorando transparencia)
    glColor3f(1.0, 1.0, 0.6) # RGB: 255, 255, 153

