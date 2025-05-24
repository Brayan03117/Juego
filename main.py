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
            while True:
                personaje_seleccionado = seleccion_personaje()
                if personaje_seleccionado == "back":
                    break 
                print(f"Seleccionaste el personaje {personaje_seleccionado}")

                nivel_seleccionado = seleccion_nivel(personaje_seleccionado)
                if nivel_seleccionado == "back":
                    continue 
                print(f"Seleccionaste el nivel {nivel_seleccionado}")

                if personaje_seleccionado is not None and nivel_seleccionado is not None:
                    print(f"Iniciando juego con personaje {personaje_seleccionado} en nivel {nivel_seleccionado}")

                    reiniciar_nivel = True
                    go_back_to_level_selection = False 

                    while reiniciar_nivel:
                        if nivel_seleccionado == "nivel1":
                            resultado = iniciar_nivel1(personaje_seleccionado)
                        elif nivel_seleccionado == "nivel2":
                            resultado = iniciar_nivel2(personaje_seleccionado)
                        elif nivel_seleccionado == "nivel3":
                            resultado = iniciar_nivel3(personaje_seleccionado)

                        if resultado == "salir":
                            sys.exit()  
                        elif resultado == "menu" or resultado == "gameover":
                            reiniciar_nivel = False  
                        elif resultado == "reiniciar":
                            reiniciar_nivel = True 
                        elif resultado == "back":
                            reiniciar_nivel = False 
                            go_back_to_level_selection = True
                            reiniciar_nivel = False  

                    if go_back_to_level_selection:
                        continue 
                        break 

        elif opcion == "salir":
            break

if __name__ == "__main__":
    main()