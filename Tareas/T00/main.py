import sys

from parametros import NUM_BARCOS
from tablero import print_tablero

from partida import menu_de_inicio, menu_de_juego, definir_tablero
from jugador import Usuario, Oponente
from puntajes import calcular_puntaje, agregar_puntaje


jugar_partida = True
menu_inicio = True
while jugar_partida:
    # MENU DE INICIO
    while menu_inicio:
        menu_inicio, accion = menu_de_inicio(menu_inicio)
        if accion.isdigit() and 0 == int(accion):
            jugador = Usuario()
            if jugador.elegir_apodo():
                menu_inicio = True
            else:
                menu_inicio = False
    # DEFINIR PARTIDA
    oponente = Oponente()
    oponente.apodo = "oponente"
    filas, columnas = definir_tablero()
    jugador.crear_tablero(filas, columnas)
    oponente.crear_tablero(filas, columnas)
    jugador.ubicar_barcos(NUM_BARCOS)
    oponente.ubicar_barcos(NUM_BARCOS)
    # JUGAR PARTIDA
    while jugar_partida:
        menu_de_juego(jugador, oponente)
        accion = input("\nEleccion: ")
        if accion.isdigit() and (0 <= int(accion) <= 2):
            if 0 == int(accion):
                # lanzar bombas
                jugador.lanzar_bomba(oponente)
                if oponente.contar_fuegos() != 3:
                    print("\nTURNO DE TU OPONENTE")
                    oponente.lanzar_bomba(jugador)
                    print_tablero(oponente.tablero, jugador.tablero)
            elif 1 == int(accion):
                # rendirse e ir a menu de inicio
                print("Te haz rendido, haz vuelto al inicio")
                puntaje = calcular_puntaje(jugador, oponente)
                agregar_puntaje(puntaje, "puntajes.txt")
                menu_inicio = True
                break
            elif 2 == int(accion):
                # salir del juego
                print("\nHA SALIDO DEL JUEGO")
                jugar_partida = False
                sys.exit()
        else:
            print("Ingrese una acción correcta")
        if (jugador.contar_fuegos() == 3) or (oponente.contar_fuegos() == 3):
            print("\nLA PARTIDA HA TERMINADO")
            if jugador.contar_fuegos == 3:
                print("Ha ganado tu oponente")
            else:
                print(f"Felicidades {jugador.apodo}! Haz ganado!!")
            puntaje = calcular_puntaje(jugador, oponente)
            agregar_puntaje(puntaje, "puntajes.txt")
            jugar_partida = False
            sys.exit()
