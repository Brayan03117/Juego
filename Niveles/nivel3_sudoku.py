import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from src.textos import dibujar_label_texto

def crear_tablero_sudoku():
    tablero = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    # Tablero original 
    solucion = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
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
    """Dibuja el tablero de Sudoku 9x9 en la pantalla"""
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, config['display'][0], 0, config['display'][1])
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)

    cell_size = 40
    board_width = 9 * cell_size
    board_height = 9 * cell_size
    board_x = config['display'][0] - board_width - 40
    board_y = config['display'][1] - board_height - 40

    # Fondo del tablero
    glColor4f(0.2, 0.2, 0.2, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(board_x - 10, board_y - 10)
    glVertex2f(board_x + board_width + 10, board_y - 10)
    glVertex2f(board_x + board_width + 10, board_y + board_height + 10)
    glVertex2f(board_x - 10, board_y + board_height + 10)
    glEnd()

    for row in range(9):
        for col in range(9):
            cell_x = board_x + col * cell_size
            cell_y = board_y + (8 - row) * cell_size  # fila invertida

            # Colores de fondo
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

            # Borde de celda
            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_LINE_LOOP)
            glVertex2f(cell_x, cell_y)
            glVertex2f(cell_x + cell_size, cell_y)
            glVertex2f(cell_x + cell_size, cell_y + cell_size)
            glVertex2f(cell_x, cell_y + cell_size)
            glEnd()

            # Número
            if tablero[row][col] != 0:
                if estado_juego['last_insertion'] and estado_juego['last_insertion'][0] == row and estado_juego['last_insertion'][1] == col:
                    color = (0.0, 1.0, 0.3)
                else:
                    color = (1.0, 0.9, 0.0)
                dibujar_numero_sin_fondo(
                    tablero[row][col],
                    cell_x + cell_size // 2 - 10,
                    cell_y + cell_size // 2 - 15,
                    28,
                    color
                )

    # Texto
    glColor3f(1.0, 0.8, 0.2)
    dibujar_label_texto("SUDOKU 9x9", pos_x=board_x, pos_y=board_y + board_height + 30, tam=28)

    glColor3f(0.9, 0.9, 0.9)
    dibujar_label_texto("Haz clic en una celda y presiona 1-9", pos_x=board_x, pos_y=board_y + board_height + 60, tam=18)

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