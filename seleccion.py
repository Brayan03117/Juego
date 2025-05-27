import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from OpenGL.GLUT import GLUT_BITMAP_TIMES_ROMAN_24
from acciones.jesusL import draw as draw_jesus 
from acciones.torchic import personaje as draw_torchic
from acciones import expresiones as torchic
#from acciones.dyson import original5 as draw_dyson  
from acciones.dysonEm import dibujar_personaje as draw_dyson
# from Esenarios.escenario import draw_e  
from acciones import iluminacion  
from src.textos import dibujar_label_texto
from Esenarios import escenario as es
from src.textos import dibujar_label_texto




personaje_posiciones = [(-0.5, 6.0, 0.0), (5.0, 6.0, 0.0), (-6, 6.0, 0.0)]  # Coordenadas para la flecha
personaje_nombres = ["JESUSL", "TORCHIC", "DYSON"]  # Nombres de los personajes
seleccion_actual = 0

# Definir una función básica para renderizar texto
def renderizar_texto(texto, x, y, escala=1.0, color=(1.0, 1.0, 1.0)):
    """Función básica para renderizar texto en OpenGL"""
    glDisable(GL_LIGHTING)
    glColor3f(*color)
    glRasterPos2f(x, y)
    for caracter in texto:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(caracter))
    glEnable(GL_LIGHTING)

def dibujar(seleccion_actual, emocion):
    """Dibuja el personaje seleccionado"""
    if seleccion_actual == 0:
        if emocion == 0:
            draw_jesus(0, -3, -2.2,0)
        elif emocion == 1:
            draw_jesus(0, -3, -2.2,1)
        elif emocion == 2:
            draw_jesus(0, -3, -2.2,2)
        elif emocion == 3:
            draw_jesus(0, -3, -2.2,3)
        elif emocion == 4:
            draw_jesus(0, -3, -2.2,7)
        
 
    elif seleccion_actual == 1:
        if emocion == 0:
            draw_torchic()
        elif emocion == 1:
            torchic.draw_cejas_chad()
        elif emocion == 2:
            torchic.draw_enojado()
        elif emocion == 3:
            torchic.draw_nervioso()
        elif emocion == 4:
            torchic.draw_triste()
    elif seleccion_actual == 2:
        if emocion == 0:
            draw_dyson((-9, 2, 8), emocion="original")  # Posición local en su propio sistema
        elif emocion == 1:
            draw_dyson((-9, 2, 8), emocion="asco")
        elif emocion == 2:
            draw_dyson((-9, 2, 8), emocion="admirar")
        elif emocion == 3:
            draw_dyson((-9, 2, 8), emocion="sad")
        elif emocion == 4:
            draw_dyson((-9, 2, 8), emocion="happy")


def main():
    emocion=0
    fondo_actual=0
    global seleccion_actual
    global personaje_posiciones
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sonidos/Jumper.mp3")
    pygame.mixer.music.play(-1)
    display = (800, 600)
    pygame.display.quit()
    pygame.display.init()
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    es.inicializar_fondos()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -15)    

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

    # Inicializar GLUT para renderizar texto
    glutInit()

    #iluminacion.activar_iluminacion('phong')  # Cambia el modelo de iluminación aquí

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    seleccion_actual = (seleccion_actual + 1) % len(personaje_posiciones)
                    emocion = 0
                elif event.key == pygame.K_LEFT:
                    seleccion_actual = (seleccion_actual - 1) % len(personaje_posiciones)
                    emocion = 0
                elif event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    pygame.display.quit()
                    return seleccion_actual
                elif event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    return "back"
                elif event.key == pygame.K_1:
                    fondo_actual = 1
                elif event.key == pygame.K_2:
                    fondo_actual = 2
                elif event.key == pygame.K_3:
                    fondo_actual = 3
                elif event.key == pygame.K_4:
                    fondo_actual = 4
                elif event.key == pygame.K_5:
                    fondo_actual = 5
                elif event.key == pygame.K_k:
                    if emocion <4:
                        emocion = emocion + 1
                    else:
                        emocion = 0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        iluminacion.iluminacion(0, 0, 0)  # Luz blanca
        glColor3f(1.0, 1.0, 1.0)
        

        # Dibujar JesusL
        glPushMatrix()
        es.mostrar_escenario(fondo_actual)  # Mostrar el fondo del escenario
        glTranslatef(-1.5, 0.0, 0.0)
        glRotatef(90, 1, 0, 0)  
        glRotatef(180, 0, 1, 0)  
        glRotatef(90, 0, 0, 1)  
        #glDisable(GL_LIGHTING)

        if seleccion_actual == 2 or seleccion_actual == 1:
            glEnable(GL_LIGHTING)
            glColor3f(1.0, 1.0, 1.0)  # Iluminado normal
            draw_jesus(0, -3, -2.2,8) 
        else:
            glDisable(GL_LIGHTING)
            glColor3f(0, 0, 0)  # Oscuro
            dibujar(seleccion_actual, emocion)
  
        glPopMatrix()


        # Dibujar Torchic
        glPushMatrix()
        glTranslatef(5.0, 0.0, 0.0)
        glRotatef(180, 0, 1, 0)  # Girar 180 grados en el eje Y para que mire hacia la cámara
        if seleccion_actual == 0 or seleccion_actual == 2:
            glEnable(GL_LIGHTING)
            glColor3f(1.0, 1.0, 1.0)
            draw_torchic()  # Llamar a la función de dibujo
        else:
            glDisable(GL_LIGHTING)
            glColor3f(0.2, 0.2, 0.2)
            dibujar(seleccion_actual, emocion)  # Llamar a la función de dibujo
        glPopMatrix()


        # Dibujar Dyson
        glPushMatrix()
        glTranslatef(3.0, 1.5, -4.0)      # Posición en el mundo
        glRotatef(0, 0, 1, 0) 
        if seleccion_actual == 1 or seleccion_actual == 0:
            glEnable(GL_LIGHTING)
            glColor3f(1.0, 1.0, 1.0)
            draw_dyson((-9, 2, 8),emocion="original")
        else:
            glDisable(GL_LIGHTING)
            glColor3f(0.2, 0.2, 0.2) 
            dibujar(seleccion_actual, emocion)
        glPopMatrix()


        # Dibujar flecha sobre personaje seleccionado
        glPushMatrix()
        glTranslatef(*personaje_posiciones[seleccion_actual])
        glDisable(GL_LIGHTING)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(0.0, 0.0, 0.0)   # Punto inferior (punta de la flecha)
        glVertex3f(-0.5, 1.0, 0.0)  # Izquierda
        glVertex3f(0.5, 1.0, 0.0)   # Derecha
        glEnd()
        glEnable(GL_LIGHTING)
        glPopMatrix()

        # Dibujar el nombre del personaje seleccionado en la parte inferior
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, display[0], 0, display[1])
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)
        
        # Dibujar un fondo para el texto
        glColor4f(0.0, 0.0, 0.0, 0.7)  # Negro semi-transparente
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(display[0], 0)
        glVertex2f(display[0], 50)
        glVertex2f(0, 50)
        glEnd()
        
        # Dibujar el texto del nombre con colores más llamativos
        nombre_personaje = personaje_nombres[seleccion_actual]
        
        # Usar colores diferentes según el personaje seleccionado
        if seleccion_actual == 0:  # JESUSL
            color_texto = (1.0, 0.8, 0.0)  # Dorado
            nivel_dificultad = "FÁCIL"
            color_dificultad = (0.0, 1.0, 0.0)  # Verde brillante
        elif seleccion_actual == 1:  # TORCHICH
            color_texto = (1.0, 0.5, 0.0)  # Naranja
            nivel_dificultad = "DIFÍCIL"
            color_dificultad = (1.0, 0.0, 0.0)  # Rojo brillante
        else:  # DYSON
            color_texto = (0.0, 0.8, 1.0)  # Azul claro
            nivel_dificultad = "MEDIO"
            color_dificultad = (1.0, 1.0, 0.0)  # Amarillo brillante
            
        # Usar una escala mayor para hacer el texto más grande
        renderizar_texto(f"PERSONAJE: {nombre_personaje}", display[0]/2 - 120, 30, escala=2.0, color=color_texto)
        
        # Añadir texto de dificultad con efecto parpadeante
        tiempo_actual = pygame.time.get_ticks()
        if (tiempo_actual // 500) % 2 == 0:  # Parpadeo cada 500ms
            renderizar_texto(f"DIFICULTAD: {nivel_dificultad}", display[0]/2 - 120, 10, escala=1.8, color=color_dificultad)
        
        # Restaurar matrices
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        dibujar_label_texto(f"Presiona K para ver expresiones y del 1 al 5 para ver algunos escenarios", pos_x=10, pos_y=580, tam=15)


        dibujar_label_texto("Selecciona tu personaje", pos_x=220, pos_y=550, tam=24)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
