import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Agregar el directorio padre al sys.path

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from time import time

from acciones.renderizarTexto import cargar_textura_desde_texto, renderizar_texto_textura

def mostrar_felicitacion(display):
    glutInit()
    if not pygame.mixer.get_init(): # Inicializar pygame.mixer si no lo está
        pygame.mixer.init()
    
    try:
        # Cambiamos la música a una canción más festiva
        pygame.mixer.music.load("Sonidos/Electroman.mp3") # Asegúrate de tener este archivo
        pygame.mixer.music.play(-1)  # Reproducir en bucle (-1)
    except pygame.error as e:
        try:
            # Intentar con la canción original como respaldo
            pygame.mixer.music.load("Sonidos/victory.mp3")
            pygame.mixer.music.play(-1)
        except pygame.error as e2:
            print(f"No se pudo cargar o reproducir ninguna música de victoria: {e2}")

    parpadeo_activo = True
    tiempo_ultimo_parpadeo = time()
    intervalo_parpadeo = 0.5  # Segundos

    fuente_grande = pygame.font.Font("Fuentes/PressStart2P-Regular.ttf", 50) # Tamaño para el título
    fuente_pequena = pygame.font.Font("Fuentes/PressStart2P-Regular.ttf", 18)

    # Título "¡FELICIDADES!"
    titulo_felicitacion = "¡FELICIDADES!"
    tex_felicitacion, w_felicitacion, h_felicitacion = cargar_textura_desde_texto(titulo_felicitacion, fuente_grande, (0, 255, 0))  # Verde brillante

    # Subtítulo "NIVEL SUPERADO"
    subtitulo_texto = "NIVEL SUPERADO"
    tex_subtitulo, w_subtitulo, h_subtitulo = cargar_textura_desde_texto(subtitulo_texto, fuente_grande, (255, 215, 0))  # Dorado

    # Opciones
    opcion_menu_texto = "Presiona ENTER para ir al Menú Principal"
    tex_op_menu, w_op_menu, h_op_menu = cargar_textura_desde_texto(opcion_menu_texto, fuente_pequena, (255, 255, 255))
    
    opcion_salir_texto = "Presiona ESC para Salir del Juego"
    tex_op_salir, w_op_salir, h_op_salir = cargar_textura_desde_texto(opcion_salir_texto, fuente_pequena, (255, 255, 255))

    # Configuración de OpenGL para renderizado 2D con texturas
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, display[0], display[1], 0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    clock = pygame.time.Clock()
    corriendo = True
    decision = None # Para almacenar la decisión del usuario ('menu', 'salir')

    # Colores para efectos de fondo
    colores = [
        (0.0, 0.5, 0.0),  # Verde oscuro
        (0.0, 0.7, 0.0),  # Verde medio
        (0.0, 1.0, 0.0),  # Verde brillante
        (0.5, 1.0, 0.0),  # Verde-amarillo
        (1.0, 1.0, 0.0),  # Amarillo
    ]
    indice_color = 0
    tiempo_cambio_color = time()
    intervalo_cambio_color = 0.2  # Cambiar color cada 0.2 segundos

    # Posición de los triángulos (movidos hacia abajo)
    posicion_triangulos = display[1] - 100  # Ajusta este valor para mover los triángulos más arriba o abajo

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_RETURN:
                    decision = 'menu'
                    corriendo = False
                if evento.key == K_ESCAPE:
                    decision = 'salir'
                    corriendo = False

        # Cambiar color de fondo
        if time() - tiempo_cambio_color > intervalo_cambio_color:
            indice_color = (indice_color + 1) % len(colores)
            tiempo_cambio_color = time()

        # Fondo con degradado
        glClearColor(0.0, 0.2, 0.0, 1)  # Verde muy oscuro
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Efectos decorativos (estrellas o destellos)
        glColor3f(*colores[indice_color])
        glBegin(GL_TRIANGLES)
        margen = 40
        
        # Triángulos en la parte inferior (movidos hacia abajo)
        for i in range(10):
            x = (i * display[0] // 10) + (display[0] // 20)
            y = posicion_triangulos
            tam = 15
            glVertex2f(x, y + tam); glVertex2f(x - tam, y - tam); glVertex2f(x + tam, y - tam)
        
        # Mantenemos las esquinas
        glVertex2f(0, 0); glVertex2f(margen, 0); glVertex2f(0, margen)
        glVertex2f(display[0], 0); glVertex2f(display[0] - margen, 0); glVertex2f(display[0], margen)
        glVertex2f(0, display[1]); glVertex2f(margen, display[1]); glVertex2f(0, display[1] - margen)
        glVertex2f(display[0], display[1]); glVertex2f(display[0] - margen, display[1]); glVertex2f(display[0], display[1] - margen)
        
        glEnd()

        # Parpadeo del título
        if time() - tiempo_ultimo_parpadeo > intervalo_parpadeo:
            parpadeo_activo = not parpadeo_activo
            tiempo_ultimo_parpadeo = time()

        # Renderizar título y subtítulo
        centro_x = display[0] // 2
        y_felicitacion = display[1] // 3 - h_felicitacion // 2
        
        # El título siempre visible
        renderizar_texto_textura(tex_felicitacion, centro_x - w_felicitacion // 2, y_felicitacion, w_felicitacion, h_felicitacion)
        
        # El subtítulo parpadea
        if parpadeo_activo:
            y_subtitulo = y_felicitacion + h_felicitacion + 20
            renderizar_texto_textura(tex_subtitulo, centro_x - w_subtitulo // 2, y_subtitulo, w_subtitulo, h_subtitulo)

        # Renderizar opciones
        centro_x_opciones = display[0] // 2
        y_opciones_base = display[1] * 2 // 3

        renderizar_texto_textura(tex_op_menu, centro_x_opciones - w_op_menu // 2, y_opciones_base, w_op_menu, h_op_menu)
        renderizar_texto_textura(tex_op_salir, centro_x_opciones - w_op_salir // 2, y_opciones_base + h_op_menu + 20, w_op_salir, h_op_salir)
        
        pygame.display.flip()
        clock.tick(30) # Controlar FPS

    # Limpiar matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glDisable(GL_TEXTURE_2D)
    
    if pygame.mixer.get_init():
        pygame.mixer.music.stop() # Detener la música al salir de la pantalla
        
    return decision

def main_test_felicitacion(): # Función de prueba para esta pantalla
    pygame.init()
    display = (800, 550)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    decision_usuario = mostrar_felicitacion(display)
    print(f"El usuario decidió: {decision_usuario}")

    if decision_usuario == 'menu':
        print("Yendo al Menú Principal...")
        # Aquí llamarías a la función que muestra el menú principal
        pass
    elif decision_usuario == 'salir':
        print("Saliendo del juego...")
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_test_felicitacion()