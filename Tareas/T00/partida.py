import sys

from tablero import print_tablero

from puntajes import ver_ranking_puntajes


# configurar el tamaño del tablero
def definir_tablero():
    correcto = False
    print("\nESCOJA EL TAMAÑO DEL TABLERO:")
    while correcto is False:
        filas = input("   Filas [3, 15]: ")
        columnas = input("   Columnas [3, 15]: ")
        if filas.isdigit() and columnas.isdigit():
            if 3 <= int(filas) <= 15 and 3 <= int(columnas) <= 15:
                correcto = True
                continue
        print("Ambos deben ser enteros entre 3 y 15")
    filas = int(filas)
    columnas = int(columnas)
    return filas, columnas


# menu inicio
def menu_de_inicio(jugar_partida):
    print("\n**** MENÚ DE INICIO ****\nPulse:\n   [0] para iniciar una partida\
        \n   [1] para ver ranking de puntajes\n   [2] para salir del programa")
    accion = input("\nElección: ")
    # iniciar partida
    if accion.isdigit():
        if 0 == int(accion):
            print("\nHa iniciado una nueva partida\n")
            return jugar_partida, accion
        # ver ranking de puntajes
        elif 1 == int(accion):
            ver_ranking_puntajes("puntajes.txt")
            input("\n[0] Volver a inicio: ")
            pass
        # salir del juego
        elif 2 == int(accion):
            print("\nHA SALIDO DEL JUEGO")
            sys.exit()
            jugar_partida = False
        else:
            print("\nINGRESE UNA ACCION CORRECTA:\n")
    else:
        print("\nINGRESE UNA ACCION CORRECTA:\n")
    return jugar_partida, accion


# menu de juego
def menu_de_juego(jugador, oponente):
    print("\n**** MENÚ DE JUEGO ****\n")
    print_tablero(oponente.tablero, jugador.tablero)
    print("\n \nPulse:\n   [0] para lanzar una bomba\
        \n   [1] para rendirse y volver a inicio\n   [2] para salir del programa")
    return
