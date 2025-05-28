from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from src import objetos as obj

piedra_textura_id = None
cilindro_textura_id = None
import os
import sys

def ruta_absoluta(relativa):
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.abspath(".")  # usa raíz del proyecto
    return os.path.join(base, relativa)


def dibujar_objetos_del_escenario(X,Y):
    # ----- Cubo -----
    glColor3f(0.0, 1.0, 0.0)  # Verde
    obj.draw_cube((X, 0, Y))


# Cargar imagen como textura
def cargar_textura(ruta):
    textura_surface = pygame.image.load(ruta)
    textura_datos = pygame.image.tostring(textura_surface, "RGB", 1)
    ancho, alto = textura_surface.get_size()

    textura_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ancho, alto, 0, GL_RGB, GL_UNSIGNED_BYTE, textura_datos)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return textura_id

# Dibujar fondo (pared trasera)
def dibujar_fondo(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, -20, 20)
    glTexCoord2f(1, 0); glVertex3f(20, -20, 20)
    glTexCoord2f(1, 1); glVertex3f(20, 20, 20)
    glTexCoord2f(0, 1); glVertex3f(-20, 20, 20)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar pared izquierda
def dibujar_pared_izq(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, -20, 20)
    glTexCoord2f(1, 0); glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 1); glVertex3f(-20, 20, -20)
    glTexCoord2f(0, 1); glVertex3f(-20, 20, 20)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar pared derecha
def dibujar_pared_der(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(20, -20, -20)
    glTexCoord2f(1, 0); glVertex3f(20, -20, 20)
    glTexCoord2f(1, 1); glVertex3f(20, 20, 20)
    glTexCoord2f(0, 1); glVertex3f(20, 20, -20)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar pared delantera
def dibujar_pared_frontal(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0); glVertex3f(20, -20, -20)
    glTexCoord2f(1, 1); glVertex3f(20, 20, -20)
    glTexCoord2f(0, 1); glVertex3f(-20, 20, -20)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar suelo usando la última textura cargada
def dibujar_suelo(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0); glVertex3f(20, -20, -20)
    glTexCoord2f(1, 1); glVertex3f(20, -20, 20)
    glTexCoord2f(0, 1); glVertex3f(-20, -20, 20)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Cargar texturas de las paredes y suelo
fondos_rutas = [
    ruta_absoluta(r"imagenes\paisaje.jpg"),
    ruta_absoluta(r"imagenes\paisaje2.jpg"),
    ruta_absoluta(r"imagenes\paisaje3.jpg"),
    ruta_absoluta(r"imagenes\paisaje4.jpeg"),
    ruta_absoluta(r"imagenes\paisaje5.jpeg"),
    ruta_absoluta(r"imagenes\paisaje6.jpg"),
    ruta_absoluta(r"imagenes\paisaje7.jpg"),
    ruta_absoluta(r"imagenes\paisaje8.png"),
    ruta_absoluta(r"imagenes\paisaje9.png"),
    ruta_absoluta(r"imagenes\paisaje10.png"),
    ruta_absoluta(r"imagenes\paisaje11.png"),
    ruta_absoluta(r"imagenes\paisaje12.png"),
    ruta_absoluta(r"imagenes\paisaje13.png"),
    ruta_absoluta(r"imagenes\paisaje14.png"),
    ruta_absoluta(r"imagenes\paisaje15.png"),
    ruta_absoluta(r"imagenes\suelo.jpg")
]

fondos_texturas = []

# Inicializar texturas
def inicializar_fondos():
    global fondos_texturas,piedra_textura_id, cilindro_textura_id
    fondos_texturas = [cargar_textura(ruta) for ruta in fondos_rutas]

# Dibujar escenario completo con fondo y paredes laterales y suelo
def mostrar_escenario(num, X=0, Y=0, pista_activa=False):
    if 0 <= num < len(fondos_texturas) - 1:
        textura_paredes = fondos_texturas[num]
        textura_suelo = fondos_texturas[-1]  # Ultima textura es suelo
        dibujar_fondo(textura_paredes)
        dibujar_pared_izq(textura_paredes)
        dibujar_pared_der(textura_paredes)
        dibujar_pared_frontal(textura_paredes)
        dibujar_suelo(textura_suelo)
        if pista_activa==False:
            dibujar_objetos_del_escenario(X, Y)
            


obstaculos = [
    {"tipo": "invisible", "pos": (-30.0, 0.0, 0.0), "radio": 12.0},
    {"tipo": "invisible", "pos": (30.0, 0.0, 0.0), "radio": 12.0},
    {"tipo": "invisible", "pos": (0.0, 30.0, 0.0), "radio": 20.0},
    {"tipo": "invisible", "pos": (0.0, -30.0, 0.0), "radio": 20.0},
]


def obtener_obstaculos():
    return obstaculos

