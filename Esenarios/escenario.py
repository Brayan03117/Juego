from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

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
    glTexCoord2f(0, 0); glVertex3f(-15, -15, 15)
    glTexCoord2f(1, 0); glVertex3f(15, -15, 15)
    glTexCoord2f(1, 1); glVertex3f(15, 15, 15)
    glTexCoord2f(0, 1); glVertex3f(-15, 15, 15)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar pared izquierda
def dibujar_pared_izq(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-15, -15, 15)
    glTexCoord2f(1, 0); glVertex3f(-15, -15, -15)
    glTexCoord2f(1, 1); glVertex3f(-15, 15, -15)
    glTexCoord2f(0, 1); glVertex3f(-15, 15, 15)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar pared derecha
def dibujar_pared_der(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(15, -15, -15)
    glTexCoord2f(1, 0); glVertex3f(15, -15, 15)
    glTexCoord2f(1, 1); glVertex3f(15, 15, 15)
    glTexCoord2f(0, 1); glVertex3f(15, 15, -15)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar pared delantera
def dibujar_pared_frontal(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-15, -15, -15)
    glTexCoord2f(1, 0); glVertex3f(15, -15, -15)
    glTexCoord2f(1, 1); glVertex3f(15, 15, -15)
    glTexCoord2f(0, 1); glVertex3f(-15, 15, -15)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Dibujar suelo usando la última textura cargada
def dibujar_suelo(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-15, -15, -15)
    glTexCoord2f(1, 0); glVertex3f(15, -15, -15)
    glTexCoord2f(1, 1); glVertex3f(15, -15, 15)
    glTexCoord2f(0, 1); glVertex3f(-15, -15, 15)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Cargar texturas de las paredes y suelo
fondos_rutas = [
    "imagenes/paisaje.jpg",
    "imagenes/paisaje2.jpg",
    "imagenes/paisaje3.jpg",
    "imagenes/paisaje4.jpeg",
    "imagenes/paisaje5.jpeg",
    "imagenes/paisaje6.jpg",
    "imagenes/paisaje7.jpg",
    "imagenes/suelo.jpg"
]

fondos_texturas = []

# Inicializar texturas
def inicializar_fondos():
    global fondos_texturas,piedra_textura_id, cilindro_textura_id
    fondos_texturas = [cargar_textura(ruta) for ruta in fondos_rutas]
    piedra_textura_id = cargar_textura("Imagenes/piedra.jpg")      # Textura para piedra
    cilindro_textura_id = cargar_textura("Imagenes/madera.jpg")  # Textura para cilindro

# Dibujar escenario completo con fondo y paredes laterales y suelo
def mostrar_escenario(num):
    if 0 <= num < len(fondos_texturas) - 1:
        textura_paredes = fondos_texturas[num]
        textura_suelo = fondos_texturas[-1]  # Ultima textura es suelo
        dibujar_fondo(textura_paredes)
        dibujar_pared_izq(textura_paredes)
        dibujar_pared_der(textura_paredes)
        dibujar_pared_frontal(textura_paredes)
        dibujar_suelo(textura_suelo)
