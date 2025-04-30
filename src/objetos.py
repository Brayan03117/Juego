import math
from OpenGL.GL import *
from OpenGL.GLU import *
# ========================
# Funciones Base para torchic
# ========================
def draw_sphere(position, radius, slices=16, stacks=16):
    x, y, z = position
    glPushMatrix()
    glTranslatef(x, z, -y)
    quad = gluNewQuadric()
    gluSphere(quad, radius, slices, stacks)
    gluDeleteQuadric(quad)
    glPopMatrix()

def draw_cylinder(start, end, radius, slices=16):
    from numpy import array, cross, linalg

    start = array([start[0], start[2], -start[1]])
    end = array([end[0], end[2], -end[1]])

    direction = end - start
    length = linalg.norm(direction)
    direction = direction / length

    up = array([0, 0, 1])
    axis = cross(up, direction)
    angle = math.degrees(math.acos(max(min(direction @ up, 1), -1)))

    glPushMatrix()
    glTranslatef(*start)
    if linalg.norm(axis) > 0.0001:
        glRotatef(angle, *axis)

    quad = gluNewQuadric()
    gluCylinder(quad, radius, radius, length, slices, 1)
    gluDeleteQuadric(quad)
    glPopMatrix()

def draw_param_surface(fx, fy, fz, u_range, t_range, u_steps=20, t_steps=10):
    du = (u_range[1] - u_range[0]) / u_steps
    dt = (t_range[1] - t_range[0]) / t_steps

    glBegin(GL_QUADS)
    for i in range(u_steps):
        for j in range(t_steps):
            u = u_range[0] + i * du
            t = t_range[0] + j * dt

            for du_offset, dt_offset in [(0,0), (du,0), (du,dt), (0,dt)]:
                uu = u + du_offset
                tt = t + dt_offset
                x = fx(uu, tt)
                y = fz(uu, tt)
                z = -fy(uu, tt)

                # Normal aproximada: radial desde el centro
                magn = (x**2 + y**2 + z**2) ** 0.5
                if magn == 0:
                    nx, ny, nz = 0, 0, 1
                else:
                    nx, ny, nz = x / magn, y / magn, z / magn

                glNormal3f(nx, ny, nz)
                glVertex3f(x, y, z)
    glEnd()

def draw_pyramid(position, base_size=2.0, height=2.0):
    x, y, z = position
    hs = base_size / 2  # Half size (para los vértices)
    
    glPushMatrix()
    glTranslatef(x, height / 2 + y, -z)  # ¡Aquí está el ajuste clave de altura!

    glBegin(GL_TRIANGLES)
    # Caras laterales
    # Frente    
    glNormal3f(0, 0.707, 0.707)
    glVertex3f(0.0, height / 2, 0.0)           # Punta
    glVertex3f(-hs, -height / 2, hs)           # Base izquierda
    glVertex3f(hs, -height / 2, hs)            # Base derecha

    # Derecha
    glNormal3f(0.707, 0.707, 0)
    glVertex3f(0.0, height / 2, 0.0)
    glVertex3f(hs, -height / 2, hs)
    glVertex3f(hs, -height / 2, -hs)

    # Atrás
    glNormal3f(0, 0.707, -0.707)
    glVertex3f(0.0, height / 2, 0.0)
    glVertex3f(hs, -height / 2, -hs)
    glVertex3f(-hs, -height / 2, -hs)

    # Izquierda
    glNormal3f(-0.707, 0.707, 0)
    glVertex3f(0.0, height / 2, 0.0)
    glVertex3f(-hs, -height / 2, -hs)
    glVertex3f(-hs, -height / 2, hs)
    glEnd()

    # Base (cuadrado)
    glBegin(GL_QUADS)
    glNormal3f(0, -1, 0)
    glVertex3f(-hs, -height / 2, hs)
    glVertex3f(hs, -height / 2, hs)
    glVertex3f(hs, -height / 2, -hs)
    glVertex3f(-hs, -height / 2, -hs)
    glEnd()

    glPopMatrix()



def draw_cube(position, size=2.0):
    x, y, z = position
    hs = size / 2  # half size
    glPushMatrix()
    glTranslatef(x, z + hs, -y)  # ajustamos altura
    glBegin(GL_QUADS)

    # Cara frontal
    glNormal3f(0, 0, 1)
    glVertex3f(-hs, -hs, hs)
    glVertex3f(hs, -hs, hs)
    glVertex3f(hs, hs, hs)
    glVertex3f(-hs, hs, hs)

    # Cara trasera
    glNormal3f(0, 0, -1)
    glVertex3f(hs, -hs, -hs)
    glVertex3f(-hs, -hs, -hs)
    glVertex3f(-hs, hs, -hs)
    glVertex3f(hs, hs, -hs)

    # Cara izquierda
    glNormal3f(-1, 0, 0)
    glVertex3f(-hs, -hs, -hs)
    glVertex3f(-hs, -hs, hs)
    glVertex3f(-hs, hs, hs)
    glVertex3f(-hs, hs, -hs)

    # Cara derecha
    glNormal3f(1, 0, 0) 
    glVertex3f(hs, -hs, hs)
    glVertex3f(hs, -hs, -hs)
    glVertex3f(hs, hs, -hs)
    glVertex3f(hs, hs, hs)

    # Cara superior
    glNormal3f(0, 1, 0)
    glVertex3f(-hs, hs, hs)
    glVertex3f(hs, hs, hs)
    glVertex3f(hs, hs, -hs)
    glVertex3f(-hs, hs, -hs)

    # Cara inferior
    glNormal3f(0, -1, 0)
    glVertex3f(-hs, -hs, -hs)
    glVertex3f(hs, -hs, -hs)
    glVertex3f(hs, -hs, hs)
    glVertex3f(-hs, -hs, hs)

    glEnd()
    glPopMatrix()
