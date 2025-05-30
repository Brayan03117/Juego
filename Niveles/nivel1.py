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

# Importar la función mostrar_felicitacion
from Transiciones.Felicitacion import mostrar_felicitacion

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
            return "salir"
        elif accion == "menu":
            return "menu"
        elif accion == "reiniciar":
            return "reiniciar"
        elif accion == "back":
            return "back"
            
        # Manejar movimiento del personaje
        manejar_movimiento(config)

        if config['pista_activa']== True and config['pistas_disponibles'] > 0:
            aplicar_pista(tablero, solucion, estado_juego)
            config['pistas_disponibles'] -= 1
        
        # Renderizar la escena
        renderizar_escena(config, estado_juego, tablero)
        
        # Actualizar el personaje según el estado del juego
        actualizar_personaje(config, estado_juego)
        
        # Verificar si el Sudoku está completo (todas las celdas llenas)
        sudoku_completo = all(all(cell != 0 for cell in row) for row in tablero)
        
        # Si está completo, verificar si es correcto
        if sudoku_completo:
            # Verificar cada celda del tablero
            sudoku_correcto = True
            for fila in range(len(tablero)):
                for columna in range(len(tablero[fila])):
                    valor = tablero[fila][columna]
                    # Verificar si el valor en esta celda es correcto
                    if not verificar_solucion(tablero, solucion, fila, columna, valor):
                        sudoku_correcto = False
                        break
                if not sudoku_correcto:
                    break
            
            if sudoku_correcto:
                # Detener todos los sonidos antes de mostrar la felicitación
                for sonido in config['sonidos_escenarios'].values():
                    sonido.stop()
                
                # Mostrar la pantalla de felicitación
                resultado = mostrar_felicitacion(config['display'])
                
                # Procesar el resultado de la pantalla de felicitación
                if resultado == 'menu':
                    return 'menu'
                elif resultado == 'salir':
                    return 'salir'
        
        # Actualizar la pantalla
        pygame.display.flip()
        config['clock'].tick(60)

def aplicar_pista(tablero, solucion, estado_juego):
    """Rellena una celda vacía con la solución como pista"""
    for fila in range(4):
        for columna in range(4):
            if tablero[fila][columna] == 0:
                tablero[fila][columna] = solucion[fila][columna]
                estado_juego['last_insertion'] = (fila, columna, solucion[fila][columna])
                estado_juego['correct_answers'] += 1
                return