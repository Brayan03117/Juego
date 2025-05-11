import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import sys

# Importar módulos segmentados del nivel 1
from Niveles.nivel2_config import inicializar_nivel
from Niveles.nivel2_sudoku import crear_tablero_sudoku, verificar_solucion, dibujar_tablero_sudoku
from Niveles.nivel2_render import renderizar_escena, actualizar_personaje
from Niveles.nivel2_eventos import manejar_eventos, manejar_movimiento

# Importar la función mostrar_felicitacion
from Transiciones.Felicitacion import mostrar_felicitacion

def iniciar_nivel2(personaje_id):
    """
    Inicia el Nivel 2 con el personaje seleccionado.
    
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
        'correct_answers': 0,
        'tiempo_inicio': pygame.time.get_ticks(),
        'tiempo_maximo': 100,
        'tiempo_restante': 100
    }
    tiempo_inicio = pygame.time.get_ticks()
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
            
        # Manejar movimiento del personaje
        manejar_movimiento(config,estado_juego)
        
        # Renderizar la escena
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - estado_juego['tiempo_inicio']) // 1000
        estado_juego['tiempo_restante'] = max(0, estado_juego['tiempo_maximo'] - tiempo_transcurrido)
        if estado_juego['tiempo_restante'] <= 0:
            for sonido in config['sonidos_escenarios'].values():
                sonido.stop()

            from Transiciones.GameOver import mostrar_game_over
            resultado = mostrar_game_over(config['display'])

            if resultado == 'menu':
                return 'menu'
            elif resultado == 'salir':
                pygame.quit()
                return 'salir'



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