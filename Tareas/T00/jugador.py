from random import randint

from tablero import print_tablero
from parametros import RADIO_EXP

import bombas
from coordenadas import de_coordenada_a_nm, abcdario


class Jugador:

    def __init__(self):
        self.apodo = ""
        self.tablero = []

    def crear_tablero(self, filas, columnas):
        # crear un tablero vacio
        for i in range(filas):
            fila = []
            self.tablero.append(fila)
        for fila in self.tablero:
            for j in range(columnas):
                fila.append(" ")
        return

    def ubicar_barcos(self, cantidad):
        # ubicar los barcos del jugador
        while cantidad > 0:
            fila = randint(0, len(self.tablero)-1)
            celda = randint(0, len(self.tablero[0])-1)
            if self.tablero[fila][celda] == " ":
                self.tablero[fila][celda] = "B"
                cantidad -= 1
        return

    def contar_fuegos(self):
        # cuenta los barcos undidos
        cuenta_fuegos = 0
        for fila in self.tablero:
            for celda in fila:
                if celda == "F":
                    cuenta_fuegos += 1
        return cuenta_fuegos

    def lanzar_bomba(self, tablero_contrincante):
        pass


class Usuario(Jugador):

    def __init__(self):
        super().__init__()
        self.bombas_especiales = 1

    def elegir_apodo(self):
        apodo_correcto = False
        while apodo_correcto is False:
            nombre = input("Elija un apodo: ")
            if nombre.isalnum() and (len(nombre) >= 5):
                self.apodo = nombre
                apodo_correcto = True
            else:
                print("Tu apodo debe ser alfanumerico y contener al menos 5 caracteres")
                print("Pulse:\n   [0] para elegir un nuevo apodo\n   [1] para volver a inicio")
                inicio = input("Eleccion: ")
                eleccion = False
                while eleccion is False:
                    print("Ingrese una accion correcta")
                    inicio = input("Eleccion: ")
                    if inicio.isdigit() and (0 <= int(inicio) <= 1):
                        eleccion = True
                if inicio.isdigit() and int(inicio) == 1:
                    return True
        return False

    def lanzar_bomba(self, contrincante):
        tablero_contrincante = contrincante.tablero
        coord_correcta = False
        acierto = False
        fuego = False
        hit = False
        tipo_correcto = False
        fire = False
        while acierto is False:
            # verificar si el tipo de bomba ingresado es posible
            while tipo_correcto is False:
                print("\nEscoja el tipo de bomba:\n   [0] bomba regular")
                if self.bombas_especiales == 1:
                    print("  bombas especiales:\n   [1] bomba cruz\
                        \n   [2] bomba equis\n   [3] bomba diamante")
                tipo_bomba = input("\nElección de bomba: ")
                if tipo_bomba.isdigit() and (0 <= int(tipo_bomba) <= 3):
                    if (self.bombas_especiales == 1) or (int(tipo_bomba) == 0 and
                                                         self.bombas_especiales == 0):
                        tipo_correcto = True
                    else:
                        print("No te quedan bombas especiales")
                else:
                    print("INGRESE UNA ACCION CORRECTA")
            # elegir una coordenada y verificar si es posible
            while coord_correcta is False:
                print("Debe ingresar las coordenadas, de la forma letra mayuscula y numero. Ej:A0")
                coordenada = input("Ingrese la coordenada donde quiere atacar: ")
                if (len(coordenada) == 2) and (coordenada[0] in abcdario) and \
                    ((len(tablero_contrincante) - 1) >= int(coordenada[1])) and \
                        ((len(tablero_contrincante[0]) - 1) >= abcdario.index(coordenada[0])):
                    coord_correcta = True
                else:
                    print("\nINGRESE UNA COORDENADA VALIDA")
            coordenada = de_coordenada_a_nm(coordenada)
            # LANZAR TIPO DE BOMBA
            # regular
            if int(tipo_bomba) == 0:
                hit, tablero_contrincante, fuego, descubierta = \
                 bombas.regular(coordenada[0], coordenada[1], tablero_contrincante)
            # bombas especiales
            elif 1 <= int(tipo_bomba) <= 3:
                # especial cruz
                if int(tipo_bomba) == 1:
                    hit, tablero_contrincante, fuego, descubierta = \
                     bombas.cruz(coordenada[0], coordenada[1], tablero_contrincante, RADIO_EXP)
                # especial equis
                elif int(tipo_bomba) == 2:
                    hit, tablero_contrincante, fuego, descubierta = \
                     bombas.equis(coordenada[0], coordenada[1], tablero_contrincante, RADIO_EXP)
                # especial diamante
                elif int(tipo_bomba) == 3:
                    hit, tablero_contrincante, fuego, descubierta = \
                     bombas.diamante(coordenada[0], coordenada[1], tablero_contrincante, RADIO_EXP)
                self.bombas_especiales = 0
            acierto = hit
            fire = fuego
            if contrincante.contar_fuegos() == 3:
                return tablero_contrincante
            if fire:
                coord_correcta = False
                tipo_correcto = False
                acierto = False
                print("\nFuego! Repites turno\n")
                print_tablero(tablero_contrincante, self.tablero)
            elif descubierta:
                coord_correcta = False
        return tablero_contrincante


class Oponente(Jugador):

    def __init__(self):
        super().__init__()

    def lanzar_bomba(self, contrincante):
        tablero_contrincante = contrincante.tablero
        acierto = False
        while acierto is False:
            fila = randint(0, len(self.tablero)-1)
            celda = randint(0, len(self.tablero[0])-1)
            hit, tablero_contrincante, f, d = bombas.regular(fila, celda, tablero_contrincante)
            acierto = hit
        return tablero_contrincante
