from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import * #pip install pillow
#from actions import luces as lc
import math

def draw_sphere1(x, y, z, r, color):
    glPushMatrix()
    glColor3f(*color)
    glTranslatef(x, y, z)
    spheres_stack = gluNewQuadric()
    gluQuadricNormals(spheres_stack, GLU_SMOOTH)
    gluSphere(spheres_stack, r, 32, 32)
    glPopMatrix()



def draw_rectangular_prism(width, height, depth, color, translation):

    glPushMatrix()  # Guardar el estado actual de la matriz de modelo

    glColor3f(*color)
    # Aplicamos la traslación
    glTranslatef(*translation)

    # Definimos los vértices del prisma
    vertices = [
        (0, 0, 0),  # Vértice inferior izquierdo
        (width, 0, 0),  # Vértice inferior derecho
        (width, height, 0),  # Vértice superior derecho
        (0, height, 0),  # Vértice superior izquierdo
        (0, 0, depth),  # Vértice inferior izquierdo trasero
        (width, 0, depth),  # Vértice inferior derecho trasero
        (width, height, depth),  # Vértice superior derecho trasero
        (0, height, depth)  # Vértice superior izquierdo trasero
    ]
    
    # Iniciamos el dibujado del prisma
    glBegin(GL_QUADS)
    glColor3f(*color)
    # Caras del prisma
    # Frente
    glVertex3f(*vertices[0])
    glVertex3f(*vertices[1])
    glVertex3f(*vertices[2])
    glVertex3f(*vertices[3])

    # Atrás
    glVertex3f(*vertices[4])
    glVertex3f(*vertices[5])
    glVertex3f(*vertices[6])
    glVertex3f(*vertices[7])

    # Izquierda
    glVertex3f(*vertices[0])
    glVertex3f(*vertices[3])
    glVertex3f(*vertices[7])
    glVertex3f(*vertices[4])

    # Derecha
    glVertex3f(*vertices[1])
    glVertex3f(*vertices[2])
    glVertex3f(*vertices[6])
    glVertex3f(*vertices[5])

    # Arriba
    glVertex3f(*vertices[3])
    glVertex3f(*vertices[2])
    glVertex3f(*vertices[6])
    glVertex3f(*vertices[7])

    # Abajo
    glVertex3f(*vertices[0])
    glVertex3f(*vertices[1])
    glVertex3f(*vertices[5])
    glVertex3f(*vertices[4])

    # Finalizamos el dibujado del prisma
    glEnd()
    glPopMatrix()

        
def draw_cylinder(x, y, z, height, radius, slices, color):
    glPushMatrix()
    glColor3f(*color)

    # Trasladamos el cilindro a la posición de la base
    glTranslatef(x, y, z)
    # Calculamos el ángulo de cada segmento
    angle_increment = 2 * math.pi / slices
    
    # Iniciamos el dibujado
    glBegin(GL_QUAD_STRIP)
    for i in range(slices + 1):
        angle = i * angle_increment
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        # Vértice inferior
        glVertex3f(x, y, 0)
        # Vértice superior
        glVertex3f(x, y, height)
    glEnd()

    # Tapón superior
    glBegin(GL_POLYGON)
    for i in range(slices + 1):
        angle = i * angle_increment
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, height)
    glEnd()

    # Tapón inferior
    glBegin(GL_POLYGON)
    for i in range(slices + 1):
        angle = i * angle_increment
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0)
    glEnd()
    # Restauramos la matriz de transformación
    glPopMatrix()


def draw(t_x,t_y,t_z, Posimiento):
    if Posimiento == 0:
        Pos0(t_x,t_y,t_z)




def Pos0(t_x, t_y, t_z):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    
    # Cabeza
    draw_rectangular_prism(0.5, 1, 1, (0.5, 0, 1), (1 + t_x, 3.5 + t_y, 5.7 + t_z))
    
    # Pecho (más delgado)
    draw_rectangular_prism(1, 2, 3.15, (255/255, 255/255, 0/255), (0.80 + t_x, 3. + t_y, 2.5 + t_z))  # Amarillo
    
    # Copa del sombrero (centrada sobre la cabeza)
    draw_cylinder(1.25 + t_x, 4 + t_y, 6.8 + t_z, 0.5, 0.2, 32, (1, 1, 1))  # Negro

    # Ala del sombrero (parte inferior)
    draw_cylinder(1.25 + t_x, 4.0 + t_y, 6.7 + t_z, 0.1, 0.5, 32, (1, 1, 1))  
    
    # Piernas (más delgadas y color azul)
    draw_cylinder(1.25 + t_x, 3.25 + t_y, 0.5 + t_z, 2, 0.2, 32, (0/255, 0/255, 255/255))  # Azul
    draw_cylinder(1.25 + t_x, 4.75 + t_y, 0.5 + t_z, 2, 0.2, 32, (0/255, 0/255, 255/255))  # Azul
    
    # Pies
    draw_rectangular_prism(1, 0.5, 0.5, (0.0, 0.0, 0.0), (1 + t_x, 4.5 + t_y, 0 + t_z))
    draw_rectangular_prism(1, 0.5, 0.5, (0.0, 0.0, 0.0), (1 + t_x, 3 + t_y, 0 + t_z))
    
    # Hombros
    draw_sphere1(1.28 + t_x, 2.75 + t_y, 5 + t_z, 0.4, (255/255, 0/255, 0/255))  # Rojo
    draw_sphere1(1.28 + t_x, 5.25 + t_y, 5 + t_z, 0.4, (255/255, 0/255, 0/255))  # Rojo
    
    draw_cylinder(1.65 + t_x, 2.7 + t_y, 3 + t_z, height=1.75, radius=0.2, slices=32, color=(255/255, 0/255, 0/255))  # Rojo
    # Mano derecha
    draw_cylinder(1.65 + t_x, 5.3 + t_y, 3 + t_z, height=1.75, radius=0.2, slices=32, color=(255/255, 0/255, 0/255))  # Rojo

    glDisable(GL_LIGHTING) 
    glDisable(GL_LIGHT0)
    glPopMatrix()