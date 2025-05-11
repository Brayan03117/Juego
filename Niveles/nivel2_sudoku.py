import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from src.textos import dibujar_label_texto

def crear_tablero_sudoku():
    """Crea el tablero de Sudoku y su solución"""
    # Tablero inicial con algunas casillas llenas
    tablero = [
        [4, 3, 2, 1, 5, 6],
        [6, 1, 5, 2, 0, 4],
        [5, 0, 4, 3, 2, 1],
        [3, 0, 1, 0, 4, 5],
        [2, 0, 6, 0, 1, 3],
        [1, 5, 3, 0, 0, 2]
    ]
    
    # Solución del Sudoku 2x2 (4x4)
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
    # Crear una superficie temporal con fondo transparente
    font = pygame.font.SysFont('Arial', tam, bold=True)
    text_surface = font.render(str(numero), True, (255, 255, 255))
    
    # Obtener los datos de la superficie
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    text_width, text_height = text_surface.get_size()
    
    # Guardar el estado actual
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    
    # Configurar para dibujar la textura
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    # Crear una textura temporal
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    
    # Habilitar texturas
    glEnable(GL_TEXTURE_2D)
    
    # Establecer el color (afecta a la textura)
    glColor3f(*color)
    
    # Dibujar el quad con la textura
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(pos_x, pos_y)
    glTexCoord2f(1, 0); glVertex2f(pos_x + text_width, pos_y)
    glTexCoord2f(1, 1); glVertex2f(pos_x + text_width, pos_y + text_height)
    glTexCoord2f(0, 1); glVertex2f(pos_x, pos_y + text_height)
    glEnd()
    
    # Limpiar
    glDeleteTextures(1, [texture_id])
    
    # Restaurar el estado
    glPopAttrib()

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
    board_width = 6 * cell_size
    board_height = 6 * cell_size
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
    for row in range(6):
        for col in range(6):
            cell_x = board_x + col * cell_size
            cell_y = board_y + (5 - row) * cell_size  # Invertir filas para que 0,0 esté arriba
            
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
                    color = (0.0, 1.0, 0.3)  # Verde brillante para la última inserción correcta
                else:
                    color = (1.0, 0.9, 0.0)  # Amarillo dorado para valores normales
                
                # Usar nuestra nueva función para dibujar números sin fondo
                dibujar_numero_sin_fondo(
                    tablero[row][col],
                    cell_x + cell_size//2 - 10,
                    cell_y + cell_size//2 - 15,
                    32,  # Tamaño más grande para mejor visibilidad
                    color
                )
    
    # Dibujar instrucciones del Sudoku con colores más llamativos
    glColor3f(1.0, 0.8, 0.2)  # Color dorado para el título
    dibujar_label_texto("SUDOKU 6x6", pos_x=board_x, pos_y=board_y + board_height + 30, tam=28)
    
    glColor3f(0.9, 0.9, 0.9)  # Color blanco brillante para las instrucciones
    dibujar_label_texto("Haz clic en una celda y", pos_x=board_x, pos_y=board_y + board_height + 60, tam=18)
    dibujar_label_texto("presiona 1-6 para llenarla", pos_x=board_x, pos_y=board_y + board_height + 80, tam=18)
    
    # Restaurar estados
    glEnable(GL_DEPTH_TEST)
    if config['luz_encendida']:
        glEnable(GL_LIGHTING)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def configurar_iluminacion(config):
    """Configura la iluminación del escenario"""
    # Definir posición de la luz (más alta sobre el escenario)
    posicion_luz = [0.0, 30, 0.0, 1.0]  # Aumentamos la altura (Y) para que venga más desde arriba
    
    # Configurar propiedades de la luz
    luz_ambiente = [0.6, 0.6, 0.6, 1.0]  # Aumentamos la luz ambiental para mayor brillo general
    luz_difusa = [1.0, 1.0, 1.0, 1.0]    # Máxima intensidad de luz difusa
    luz_especular = [1.0, 1.0, 1.0, 1.0]
    
    # Aplicar configuración
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)
    
    # Habilitar iluminación
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    # Configurar modelo de sombreado
    glShadeModel(GL_SMOOTH)
    
    return True