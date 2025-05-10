from src.pantalla1 import pantalla_inicial
from seleccion import main as seleccion_personaje
from seleccion_nivel import seleccion_nivel
from Niveles.nivel1 import iniciar_nivel1
from Niveles.nivel2 import iniciar_nivel2
from Niveles.nivel3 import iniciar_nivel3
import sys

def main():
    personaje_seleccionado = None
    nivel_seleccionado = None
    
    while True:
        opcion = pantalla_inicial()
        if opcion == "seleccionar_personaje":
            personaje_seleccionado = seleccion_personaje()
            print(f"Seleccionaste el personaje {personaje_seleccionado}")
            
            # Después de seleccionar el personaje, mostrar la selección de nivel
            nivel_seleccionado = seleccion_nivel(personaje_seleccionado)
            print(f"Seleccionaste el nivel {nivel_seleccionado}")
            
            # Iniciar el juego automáticamente después de seleccionar nivel
            if personaje_seleccionado is not None and nivel_seleccionado is not None:
                print(f"Iniciando juego con personaje {personaje_seleccionado} en nivel {nivel_seleccionado}")
                
                # Variable para controlar si se debe reiniciar el nivel
                reiniciar_nivel = True
                
                while reiniciar_nivel:
                    # Cargar el nivel correspondiente
                    if nivel_seleccionado == "nivel1":
                        resultado = iniciar_nivel1(personaje_seleccionado)
                    elif nivel_seleccionado == "nivel2":
                        resultado = iniciar_nivel2(personaje_seleccionado)
                    elif nivel_seleccionado == "nivel3":
                        resultado = iniciar_nivel3(personaje_seleccionado)
                    # Aquí puedes agregar más niveles en el futuro
                    
                    # Procesar el resultado del nivel
                    if resultado == "salir":
                        sys.exit()  # Cerrar el juego completamente con Esc
                    elif resultado == "menu":
                        reiniciar_nivel = False  # Volver al menú principal con Enter
                    elif resultado == "reiniciar":
                        reiniciar_nivel = True  # Reiniciar el nivel actual con Espacio
                    else:
                        reiniciar_nivel = False  # Por defecto, volver al menú principal
                
        elif opcion == "salir":
            break

if __name__ == "__main__":
    main()