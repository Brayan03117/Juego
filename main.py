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
            # Loop for character and level selection
            while True:
                personaje_seleccionado = seleccion_personaje()
                if personaje_seleccionado == "back":
                    # Go back to main menu (pantalla_inicial)
                    break # Break out of the inner character/level selection loop

                print(f"Seleccionaste el personaje {personaje_seleccionado}")

                # After selecting the character, show level selection
                nivel_seleccionado = seleccion_nivel(personaje_seleccionado)
                if nivel_seleccionado == "back":
                    # Go back to character selection
                    continue # Continue the inner character/level selection loop

                print(f"Seleccionaste el nivel {nivel_seleccionado}")

                # Start the game automatically after selecting level
                if personaje_seleccionado is not None and nivel_seleccionado is not None:
                    print(f"Iniciando juego con personaje {personaje_seleccionado} en nivel {nivel_seleccionado}")

                    # Variable to control if the level should restart
                    reiniciar_nivel = True
                    go_back_to_level_selection = False # Flag for going back to level selection

                    while reiniciar_nivel:
                        # Load the corresponding level
                        if nivel_seleccionado == "nivel1":
                            resultado = iniciar_nivel1(personaje_seleccionado)
                        elif nivel_seleccionado == "nivel2":
                            resultado = iniciar_nivel2(personaje_seleccionado)
                        elif nivel_seleccionado == "nivel3":
                            resultado = iniciar_nivel3(personaje_seleccionado)
                        # You can add more levels here in the future

                        # Process the level result
                        if resultado == "salir":
                            sys.exit()  # Close the game completely with Esc
                        elif resultado == "menu" or resultado == "gameover":
                            reiniciar_nivel = False  # Return to main menu with Enter or in case of Game Over
                        elif resultado == "reiniciar":
                            reiniciar_nivel = True  # Restart the current level with Space (only during the game)
                        elif resultado == "back":
                            reiniciar_nivel = False # Exit the level loop
                            go_back_to_level_selection = True # Set flag to go back to level selection
                        else:
                            reiniciar_nivel = False  # By default, return to main menu

                    # After the level loop, check if we need to go back to level selection
                    if go_back_to_level_selection:
                        continue # Continue the inner character/level selection loop (will call seleccion_nivel again)
                    else:
                        break # Break out of the inner character/level selection loop (will go back to main menu)

        elif opcion == "salir":
            break

if __name__ == "__main__":
    main()