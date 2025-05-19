import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from src.textos import dibujar_label_texto

def crear_tablero_sudoku():
    """Crea el tablero de Sudoku y su solución para el Nivel 3"""
    # Tablero inicial para Nivel 3 (puede ser el mismo o diferente)
    tablero = [
        [4, 3, 2, 1, 5, 6],
        [6, 1, 5, 2, 0, 4],
        [5, 0, 4, 3, 2, 1],
        [3, 0, 1, 0, 4, 5],
        [2, 0, 6, 0, 1, 3],
        [1, 5, 3, 0, 0, 2]
    ]
    
    # Solución del Sudoku para Nivel 3
    solucion = [
        [4, 3, 2, 1, 5, 6],
        [6, 1, 5, 2, 3, 4],
        [5, 6, 4, 3, 2, 1],
        [3, 2, 1, 6, 4, 5],
        [2, 4, 6, 5, 1, 3],
        [1, 5, 3, 4, 6, 2]
    ]
    
    return tablero, solucion

def verificar_solucion(tablero, solucion, fila, columna, valor):
    """Verifica si el valor ingresado es correcto según la solución"""
    return valor == solucion[fila][columna]

def dibujar_numero_sin_fondo(numero, pos_x, pos_y, tam, color=(1.0, 1.0, 1.0)):
    """Dibuja un número sin fondo negro utilizando líneas OpenGL"""
    font = pygame.font.SysFont('Arial', tam, bold=True)
    text_surface = font.render(str(numero), True, (255, 255, 255))
    
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    text_width, text_height = text_surface.get_size()
    
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    
    glEnable(GL_TEXTURE_2D)
    glColor3f(*color)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(pos_x, pos_y)
    glTexCoord2f(1, 0); glVertex2f(pos_x + text_width, pos_y)
    glTexCoord2f(1, 1); glVertex2f(pos_x + text_width, pos_y + text_height)
    glTexCoord2f(0, 1); glVertex2f(pos_x, pos_y + text_height)
    glEnd()
    
    glDeleteTextures(1, [texture_id])
    glPopAttrib()

def dibujar_tablero_sudoku(config, estado_juego, tablero):
    """Dibuja el tablero de Sudoku en la pantalla"""
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, config['display'][0], 0, config['display'][1])
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    glDisable(GL_LIGHTING) # Desactivar iluminación general para el HUD
    glDisable(GL_DEPTH_TEST)
    
    cell_size = 50
    board_width = 6 * cell_size
    board_height = 6 * cell_size
    board_x = config['display'][0] - board_width - 20  
    board_y = config['display'][1] - board_height - 20 
    
    glColor4f(0.2, 0.2, 0.2, 0.7)  
    glBegin(GL_QUADS)
    glVertex2f(board_x - 10, board_y - 10)
    glVertex2f(board_x + board_width + 10, board_y - 10)
    glVertex2f(board_x + board_width + 10, board_y + board_height + 10)
    glVertex2f(board_x - 10, board_y + board_height + 10)
    glEnd()
    
    for row in range(6):
        for col in range(6):
            cell_x = board_x + col * cell_size
            cell_y = board_y + (5 - row) * cell_size  
            
            if estado_juego['selected_cell'] == (row, col):
                glColor4f(0.9, 0.9, 0.2, 0.7)  
            else:
                glColor4f(0.4, 0.4, 0.4, 0.5)  
                
            glBegin(GL_QUADS)
            glVertex2f(cell_x + 1, cell_y + 1)
            glVertex2f(cell_x + cell_size - 1, cell_y + 1)
            glVertex2f(cell_x + cell_size - 1, cell_y + cell_size - 1)
            glVertex2f(cell_x + 1, cell_y + cell_size - 1)
            glEnd()
            
            if estado_juego['selected_cell'] == (row, col):
                glColor3f(1.0, 1.0, 0.0)  
            else:
                glColor3f(1.0, 1.0, 1.0)  
                
            glBegin(GL_LINE_LOOP)
            glVertex2f(cell_x, cell_y)
            glVertex2f(cell_x + cell_size, cell_y)
            glVertex2f(cell_x + cell_size, cell_y + cell_size)
            glVertex2f(cell_x, cell_y + cell_size)
            glEnd()
            
            if tablero[row][col] != 0:
                if estado_juego['last_insertion'] and estado_juego['last_insertion'][0] == row and estado_juego['last_insertion'][1] == col:
                    color = (0.0, 1.0, 0.3)  
                else:
                    color = (1.0, 0.9, 0.0)  
                
                dibujar_numero_sin_fondo(
                    tablero[row][col],
                    cell_x + cell_size//2 - 10,
                    cell_y + cell_size//2 - 15,
                    32,  
                    color
                )
    
    glColor3f(1.0, 0.8, 0.2)  
    dibujar_label_texto("SUDOKU 6x6", pos_x=board_x, pos_y=board_y + board_height + 30, tam=28)
    
    glColor3f(0.9, 0.9, 0.9)  
    dibujar_label_texto("Haz clic en una celda y", pos_x=board_x, pos_y=board_y + board_height + 60, tam=18)
    dibujar_label_texto("presiona 1-6 para llenarla", pos_x=board_x, pos_y=board_y + board_height + 80, tam=18)
    
    glEnable(GL_DEPTH_TEST)
    # La iluminación se reactiva (si es necesario) en el bucle principal de renderizado del nivel
    # después de dibujar todos los elementos 2D.
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

# La función configurar_iluminacion no es necesaria aquí, se maneja en config o render principal.