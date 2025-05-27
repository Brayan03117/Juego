import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from src.textos import dibujar_label_texto

opciones = ["Seleccionar Personaje", "Salir"]
coordenadas_opciones = [(150, 280), (150, 230)]
seleccion_actual = 0

def pantalla_inicial():
    global seleccion_actual
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonidos/Tetris.mp3")
    pygame.mixer.music.play(-1)  # -1 para que se repita en bucle
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)
    glClearColor(0, 0, 0, 1)

    # Para la animación del indicador
    tiempo_inicio = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return "salir"
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    seleccion_actual = (seleccion_actual - 1) % len(opciones)
                elif event.key == K_DOWN:
                    seleccion_actual = (seleccion_actual + 1) % len(opciones)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    return opciones[seleccion_actual].lower().replace(" ", "_")
                elif event.key == K_ESCAPE:
                    return "salir"

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Título del juego
        dibujar_label_texto("La Gran Aventura Numérica", pos_x=180, pos_y=500, tam=36)

        # Dibuja las opciones
        for i, texto in enumerate(opciones):
            x, y = coordenadas_opciones[i]
            
            # Resalta la opción seleccionada con un color diferente
            if i == seleccion_actual:
                dibujar_label_texto("> " + texto, pos_x=x - 30, pos_y=y, tam=28, color=(255, 0, 0))
            else:
                dibujar_label_texto(texto, pos_x=x, pos_y=y, tam=28)

        # Indicador de selección
        dibujar_label_texto("Usar las flechas para seleccionar opcion", pos_x=150, pos_y=190, tam=15)
        dibujar_label_texto("Presiona Enter para continuar", pos_x=150, pos_y=170, tam=15)

        # Créditos
        dibujar_label_texto("DESARROLLADO POR:", pos_x=280, pos_y=100, tam=20)
        dibujar_label_texto("Jesus Alberto Arroyo Lugo", pos_x=250, pos_y=80, tam=18)
        dibujar_label_texto("Milton Florencio Arzate", pos_x=260, pos_y=60, tam=18)
        dibujar_label_texto("Brayan Alberto Lara Garcia", pos_x=240, pos_y=40, tam=18)

        pygame.display.flip()
        pygame.time.wait(10)
