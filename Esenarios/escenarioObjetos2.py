from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from src import objetos as obj

piedra_textura_id = None
cilindro_textura_id = None

pista_activa=False

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
    "imagenes/paisaje.jpg",
    "imagenes/paisaje2.jpg",
    "imagenes/paisaje3.jpg",
    "imagenes/paisaje4.jpeg",
    "imagenes/paisaje5.jpeg",
    "imagenes/paisaje6.jpg",
    "imagenes/paisaje7.jpg",
    "imagenes/paisaje8.png",
    "imagenes/paisaje9.png",
    "imagenes/paisaje10.png",
    "imagenes/paisaje11.png",
    "imagenes/paisaje12.png",
    "imagenes/paisaje13.png",
    "imagenes/paisaje14.png",
    "imagenes/paisaje15.png",
    "imagenes/suelo.jpg"
]

fondos_texturas = ["imagenes/madera.jpg"]

# Inicializar texturas
def inicializar_fondos():
    global fondos_texturas,piedra_textura_id, cilindro_textura_id
    fondos_texturas = [cargar_textura(ruta) for ruta in fondos_rutas]
    piedra_textura_id = cargar_textura("Imagenes/piedra.jpg")      # Textura para piedra
    cilindro_textura_id = cargar_textura("Imagenes/madera.jpg")  # Textura para cilindro
    inicializar_laberinto()  # Inicializar laberinto al cargar texturas

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
        #dibujar_laberinto_con_textura(0)
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













laberinto_cubos = []  # Para almacenar posiciones y registrar colisiones

def inicializar_laberinto():
    global laberinto_cubos, obstaculos
    laberinto_cubos = []  # Limpiar por si se reinicia
    obstaculos_extra = []

    # Construcción cuadrada: 5x5 con entrada arriba
    base_x = -20
    base_z = 0
    for i in range(5):  # filas (y)
        for j in range(5):  # columnas (x)
            x = base_x + j  # x de -20 a -16
            y = -5 + i      # y de -5 a -1
            is_borde = i in [0, 4] or j in [0, 4]
            if is_borde and not (i == 4 and j == 2):  # dejar entrada arriba en (4,2)
                laberinto_cubos.append((x, y, base_z))
                obstaculos_extra.append({
                    "tipo": "pared",
                    "pos": (x, y, base_z),
                    "radio": 1.0
                })

    obstaculos += obstaculos_extra  # Agregar a lista global

def dibujar_laberinto_con_textura(textura_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)
    for (x, y, z) in laberinto_cubos:
        glPushMatrix()
        glTranslatef(x, y, z)
        glColor3f(1, 1, 1)
        obj.draw_textured_cube((0, 0, 0))  # Asegúrate que `draw_textured_cube` usa `GL_QUADS` y coords
        glPopMatrix()
    glDisable(GL_TEXTURE_2D)