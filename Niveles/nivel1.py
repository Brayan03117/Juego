import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import sys

# Importar módulos segmentados del nivel 1
from Niveles.nivel1_config import inicializar_nivel
from Niveles.nivel1_sudoku import crear_tablero_sudoku, verificar_solucion, dibujar_tablero_sudoku
from Niveles.nivel1_render import renderizar_escena, actualizar_personaje
from Niveles.nivel1_eventos import manejar_eventos, manejar_movimiento

def iniciar_nivel1(personaje_id):
    """
    Inicia el Nivel 1 con el personaje seleccionado.
    
    Args:
        personaje_id: ID del personaje seleccionado (0=JesusL, 1=Torchic, 2=Dyson)
    """
    # Inicializar configuraciones del nivel
    config = inicializar_nivel(personaje_id)
    
    # Crear tablero de Sudoku
    tablero, solucion = crear_tablero_sudoku()
    
    # Variables de estado del juego
    estado_juego = {
        'selected_cell': None,
        'input_value': 0,
        'error_count': 0,
        'showing_options': False,
        'cell_options': [],
        'options_cell_coords': None,
        'last_insertion': None,
        'correct_answers': 0
    }
    
    # Bucle principal del juego
    while True:
        # Manejar eventos (teclado, ratón, etc.)
        accion = manejar_eventos(config, estado_juego, tablero, solucion)
        if accion == "salir":
            return
            
        # Manejar movimiento del personaje
        manejar_movimiento(config)
        
        # Renderizar la escena
        renderizar_escena(config, estado_juego, tablero)
        
        # Actualizar el personaje según el estado del juego
        actualizar_personaje(config, estado_juego)
        
        # Actualizar la pantalla
        pygame.display.flip()
        config['clock'].tick(60)