import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from src.textos import dibujar_label_texto

def crear_tablero_sudoku():
    """Crea el tablero de Sudoku y su solución"""
    # Tablero inicial con algunas casillas llenas
    tablero = [
        [4, 0, 2, 0],
        [2, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 3, 0]
    ]
    
    # Solución del Sudoku 2x2 (4x4)
    solucion = [
        [4, 3, 2, 1],
        [2, 1, 4, 3],
        [3, 2, 1, 4],
        [1, 4, 3, 2]
    ]
    
    return tablero, solucion

def verificar_solucion(tablero, solucion, fila, columna, valor):
    """Verifica si el valor ingresado es correcto según la solución"""
    return valor == solucion[fila][columna]

def dibujar_tablero_sudoku(config, estado_juego, tablero):
    """Dibuja el tablero de Sudoku en la pantalla"""
    # Configurar para dibujo 2D
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, config['display'][0], 0, config['display'][1])
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Desactivar iluminación y prueba de profundidad para dibujo 2D
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    
    # Dibujar el tablero de Sudoku
    cell_size = 50
    board_width = 4 * cell_size
    board_height = 4 * cell_size
    board_x = config['display'][0] - board_width - 20  # Posición X (derecha)
    board_y = config['display'][1] - board_height - 20  # Posición Y (arriba)
    
    # Dibujar fondo del tablero (semi-transparente)
    glColor4f(0.2, 0.2, 0.2, 0.7)  # Gris oscuro semi-transparente
    glBegin(GL_QUADS)
    glVertex2f(board_x - 10, board_y - 10)
    glVertex2f(board_x + board_width + 10, board_y - 10)
    glVertex2f(board_x + board_width + 10, board_y + board_height + 10)
    glVertex2f(board_x - 10, board_y + board_height + 10)
    glEnd()
    
    # Dibujar celdas del tablero
    for row in range(4):
        for col in range(4):
            cell_x = board_x + col * cell_size
            cell_y = board_y + (3 - row) * cell_size  # Invertir filas para que 0,0 esté arriba
            
            # Dibujar fondo de la celda (más claro para mejor contraste)
            if estado_juego['selected_cell'] == (row, col):
                glColor4f(0.9, 0.9, 0.2, 0.7)  # Amarillo para celda seleccionada
            else:
                glColor4f(0.4, 0.4, 0.4, 0.5)  # Gris medio para celdas normales
                
            glBegin(GL_QUADS)
            glVertex2f(cell_x + 1, cell_y + 1)
            glVertex2f(cell_x + cell_size - 1, cell_y + 1)
            glVertex2f(cell_x + cell_size - 1, cell_y + cell_size - 1)
            glVertex2f(cell_x + 1, cell_y + cell_size - 1)
            glEnd()
            
            # Dibujar borde de la celda
            if estado_juego['selected_cell'] == (row, col):
                glColor3f(1.0, 1.0, 0.0)  # Amarillo para celda seleccionada
            else:
                glColor3f(1.0, 1.0, 1.0)  # Blanco para celdas normales
                
            glBegin(GL_LINE_LOOP)
            glVertex2f(cell_x, cell_y)
            glVertex2f(cell_x + cell_size, cell_y)
            glVertex2f(cell_x + cell_size, cell_y + cell_size)
            glVertex2f(cell_x, cell_y + cell_size)
            glEnd()
            
            # Dibujar valor de la celda (sin fondo negro)
            if tablero[row][col] != 0:
                # Determinar el color según si es un valor original o ingresado
                if estado_juego['last_insertion'] and estado_juego['last_insertion'][0] == row and estado_juego['last_insertion'][1] == col:
                    glColor3f(0.0, 1.0, 0.0)  # Verde brillante para la última inserción correcta
                else:
                    glColor3f(1.0, 1.0, 1.0)  # Blanco brillante para valores originales
                
                # Renderizar el número con un tamaño más grande y efecto de sombra para hacerlo más llamativo
                # Primero dibujamos una sombra
                glColor3f(0.0, 0.0, 0.0)  # Negro para la sombra
                dibujar_label_texto(str(tablero[row][col]), 
                                   pos_x=cell_x + cell_size//2 - 4, 
                                   pos_y=cell_y + cell_size//2 - 4, 
                                   tam=28)
                
                # Luego dibujamos el número en su color real
                if estado_juego['last_insertion'] and estado_juego['last_insertion'][0] == row and estado_juego['last_insertion'][1] == col:
                    glColor3f(0.0, 1.0, 0.3)  # Verde brillante para la última inserción correcta
                else:
                    glColor3f(1.0, 0.9, 0.0)  # Amarillo dorado para valores normales
                
                dibujar_label_texto(str(tablero[row][col]), 
                                   pos_x=cell_x + cell_size//2 - 5, 
                                   pos_y=cell_y + cell_size//2 - 5, 
                                   tam=28)
    
    # Dibujar instrucciones del Sudoku con colores más llamativos
    glColor3f(1.0, 0.8, 0.2)  # Color dorado para el título
    dibujar_label_texto("SUDOKU 4x4", pos_x=board_x, pos_y=board_y + board_height + 30, tam=28)
    
    glColor3f(0.9, 0.9, 0.9)  # Color blanco brillante para las instrucciones
    dibujar_label_texto("Haz clic en una celda y", pos_x=board_x, pos_y=board_y + board_height + 60, tam=18)
    dibujar_label_texto("presiona 1-4 para llenarla", pos_x=board_x, pos_y=board_y + board_height + 80, tam=18)
    
    # Restaurar estados
    glEnable(GL_DEPTH_TEST)
    if config['luz_encendida']:
        glEnable(GL_LIGHTING)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)