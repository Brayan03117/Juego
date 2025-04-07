import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_text(text, PosX, PosY, PosZ, SizeFont, R, G, B, RB, GB, BB):
    font = pygame.font.Font(None, SizeFont)
    text_surface = font.render(text, True, (R, G, B), (RB, GB, BB))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    
    glRasterPos3d(PosX, PosY, PosZ)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), 
                GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def draw_fixed_text():
    # Configurar para dibujo 2D
    glDisable(GL_DEPTH_TEST)  # Desactivar depth test para que el texto siempre esté visible
    
    # Dibujar todos los elementos del menú
    draw_text("Menu", 50, 50, 0, 36, 255, 255, 255, 0, 0, 0)
    draw_text("O. Original", 50, 100, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("1. Admiración", 50, 130, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("2. Enojo colisión", 50, 160, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("3. Feliz", 50, 190, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("4. Triste", 50, 220, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("5. Guiño", 50, 250, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("6. Dormir", 50, 280, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("7. Asco", 50, 310, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("W,A,S,D,x,z Movimiento de camara", 50, 340, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("Raton zoom", 50, 370, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("P. Reproducir musica de fondo", 50, 400, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("M. Detener musica de fondo", 50, 430, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("Esc. Salir", 50, 460, 0, 24, 255, 255, 255, 0, 0, 0)
    draw_text("8. Acerca de:", 50, 490, 0, 24, 255, 255, 255, 0, 0, 0)
    
    glEnable(GL_DEPTH_TEST)  # Reactivar depth test

def draw_AcercaDe():
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(0, 0, 0) 
    draw_text("Florencio Arzate Milton", 50, 520, 0, 24, 255, 255, 255, 0, 0, 0)
    glPopMatrix()

def draw_colision1():
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(0, 0, 0)   
    draw_text("Impacto inminente", 300, 500, 0, 24, 255, 255, 255, 0, 0, 0)
    glPopMatrix()

def draw_colision2():
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(0, 0, 0) 
    draw_text("Impacto esquivable", 100, 300, 0, 24, 255, 255, 255, 0, 0, 0)
    glPopMatrix()