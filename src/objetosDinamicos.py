# objetosDinamicos.py

from OpenGL.GL import *
from src import objetos as obj
import random

objetos_dinamicos = []
objetos = []
velocidad_caida = 0.02  # velocidad con la que los objetos bajan

def generar_objetos_dinamicos():
    """Genera dos objetos 3D dinámicos con coordenadas aleatorias donde z=0"""
    global objetos_dinamicos
    objetos_dinamicos = []  # Reinicia lista

    tipos = ["tiempo", "errores"]
    for tipo in tipos:
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = 0  # z fijo
        objeto = {
            "tipo": tipo,
            "pos": (x, y, z),
            "radio": 1.5
        }
        objetos_dinamicos.append(objeto)

def obtener_objetos_dinamicos():
    return objetos_dinamicos

def dibujar_objetos_dinamicos():
    """Dibuja los objetos dinámicos con formas diferentes"""
    for obj_data in objetos_dinamicos:
        x, y, z = obj_data["pos"]
        glPushMatrix()
        glTranslatef(x, y, z)
        if obj_data["tipo"] == "tiempo":
            glColor3f(0.0, 0.7, 1.0)  # Azul claro
            obj.draw_cube((0, 0, 0))  # Representa más tiempo
        elif obj_data["tipo"] == "errores":
            glColor3f(1.0, 0.5, 0.0)  # Naranja
            obj.draw_pyramid((0, 0, 0))  # Representa reducción de errores
        glPopMatrix()



