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
                glVertex3f(x, y, z)
    glEnd()

