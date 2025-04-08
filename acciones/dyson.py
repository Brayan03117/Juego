from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame


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

# Variables globales (configuración)
SCALE_FACTOR = 0.3
ILUMINACION_HABILITADA = True

# Dimensiones del cuerpo (calculadas una vez)
CUERPO_ANCHO = 6 * SCALE_FACTOR
CUERPO_ALTO = 9 * SCALE_FACTOR
CUERPO_PROFUNDIDAD = 4.5 * SCALE_FACTOR
BRAZOS_ANCHO = 1.5 * SCALE_FACTOR
BRAZOS_ALTO = 6 * SCALE_FACTOR
PIERNAS_ANCHO = 2.1 * SCALE_FACTOR
PIERNAS_ALTO = 12 * SCALE_FACTOR
PIERNAS_BASE_ANCHO = 1.8 * SCALE_FACTOR
SEPARACION_X = 0.2 * SCALE_FACTOR

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

def set_color_rgb(r, g, b):
    glColor3f(r / 255.0, g / 255.0, b / 255.0)

def dibujar_cuerpo(position):
    x, y, z = position
    glPushMatrix()
    set_naranja()
    y_body = y + CUERPO_ALTO / 2 - 4
    draw_rectangle(CUERPO_ANCHO, CUERPO_ALTO, CUERPO_PROFUNDIDAD, (x, y_body, z - 5))
    glPopMatrix()

def dibujar_brazos(position):
    x, y, z = position
    glPushMatrix()
    set_verde() 
    y_arm = y + CUERPO_ALTO / 2 - 4
    x_left = x - CUERPO_ANCHO / 2 - BRAZOS_ANCHO / 2
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_left, y_arm, z - 5))
    x_right = x + CUERPO_ANCHO / 2 + BRAZOS_ANCHO / 2
    draw_rectangle(BRAZOS_ANCHO, BRAZOS_ALTO, BRAZOS_ANCHO, (x_right, y_arm, z - 5))
    glPopMatrix()

def dibujar_piernas(position):
    x, y, z = position
    glPushMatrix()
    set_verde()  
    y_legs = y - 4
    x_left = x - PIERNAS_BASE_ANCHO / 2 - SEPARACION_X
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_left, y_legs, z - 5))
    x_right = x + PIERNAS_BASE_ANCHO / 2 + SEPARACION_X
    draw_rectangle(PIERNAS_BASE_ANCHO, PIERNAS_ALTO, PIERNAS_BASE_ANCHO, (x_right, y_legs, z - 5))
    glPopMatrix()

def dibujar_cabeza(position):
    x, y, z = position
    cabeza_lado = 6 * SCALE_FACTOR
    scale_factor_head = cabeza_lado / (6 * SCALE_FACTOR)

    glPushMatrix()
    set_amarillo()
    y_head = y + CUERPO_ALTO + cabeza_lado / 2 - 4
    draw_rectangle(cabeza_lado, cabeza_lado, cabeza_lado, (x, y_head, z - 5))
    glPopMatrix()

    dibujar_casco((x, y_head, z - 5), cabeza_lado, scale_factor_head)
    dibujar_ojos((x, y_head, z - 5), cabeza_lado, scale_factor_head)
    dibujar_pico((x, y_head, z - 5), scale_factor_head)

def dibujar_casco(position, cabeza_lado, scale_factor):
    x, y, z = position
    glPushMatrix()
    set_robot_purple()
    y_helmet = y + cabeza_lado / 2 - 0.2 * scale_factor
    z_helmet = z + cabeza_lado / 2 + 0.1 * scale_factor
    draw_rectangle(2 * scale_factor, 0.3 * scale_factor, 0.2 * scale_factor, 
                  (x, y_helmet, z_helmet))
    glPopMatrix()

def dibujar_ojos(position, cabeza_lado, scale_factor):
    x, y, z = position
    glPushMatrix()
    set_color_rgb(10, 10, 10)  # negro mate
    x_left = x - 0.6 * scale_factor
    y_eye = y + 0.1 * scale_factor
    z_eye = z + cabeza_lado / 2 - 0.1
    draw_cube(0.3 * scale_factor, (x_left, y_eye, z_eye))
    x_right = x + 0.6 * scale_factor
    draw_cube(0.3 * scale_factor, (x_right, y_eye, z_eye))
    glPopMatrix()

def dibujar_pico(position, scale_factor):
    x, y, z = position
    glPushMatrix()
    set_verde()
    x_pico = x - 0.2 * scale_factor
    y_pico = y - 0.2 * scale_factor
    z_pico = z + (6 * SCALE_FACTOR) / 2 + 0.1
    draw_triangular_prism(0.6 * scale_factor, 0.3 * scale_factor, 0.3 * scale_factor,
                         (x_pico, y_pico, z_pico))
    glPopMatrix()

def original5(position):
   # configurar_iluminacion()

    dibujar_cuerpo(position)
    dibujar_brazos(position)
    dibujar_piernas(position)
    dibujar_cabeza(position)

    #deshabilitar_iluminacion()
