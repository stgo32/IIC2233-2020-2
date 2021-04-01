from abc import ABC, abstractmethod
from parametros import COSTO_ENTRENAR_DEPORTISTA, COSTO_SANAR_DEPORTISTA


class Entrenador(ABC):

    def __init__(self):
        self.apodo = None  # str
        self.delegacion = None  # instancia de delegacion

    def input(self, cant_posibilidades):
        input_correcto = False
        cant_posibilidades -= 1
        accion = input("Eleccion: ")
        while input_correcto is False:
            if accion.isdigit() and 0 <= int(accion) <= cant_posibilidades:
                input_correcto = True
            else:
                print("INGRESE UNA ACCION VALIDA")
                accion = input("Eleccion: ")
        return int(accion)

    def elegir_apodo(self):
        apodo = input("Escoja el apodo: ")
        apodo_correcto = False
        while apodo_correcto is False:
            if apodo.isalpha():
                apodo_correcto = True
            else:
                print("El apodo debe ser alfanumerico")
                apodo = input("Escoja el apodo: ")
        self.apodo = apodo
        return self.apodo

    def elegir_delegacion(self, delegacion0, delegacion1):
        print("Escoja su delegacion")
        print("\nPulse:")
        print("   [0]  Para elegir IEEEsparta")
        print("   [1]  Para elegir DCCrotona\n")
        input_correcto = False
        accion = input("Eleccion: ")
        while input_correcto is False:
            if accion.isdigit() and 0 <= int(accion) <= 1:
                input_correcto = True
            else:
                print("INGRESE UNA ACCION VALIDA")
                accion = input("Eleccion: ")
        accion = int(accion)
        if accion == 0:
            self.delegacion = delegacion0
            return 0
        elif accion == 1:
            self.delegacion = delegacion1
            return 1

    @abstractmethod
    def fichar_deportista(self):
        pass

    @abstractmethod
    def entrenar_deportista(self):
        pass

    @abstractmethod
    def sanar_deportista(self):
        pass


class Usuario(Entrenador):

    def __init__(self):
        super().__init__()

    def fichar_deportista(self, deportistas):
        for d in deportistas:
            print(f"   [{deportistas.index(d)}]  nombre: {d.nombre}, vel: {d.velocidad}, res: "
                  f"{d.resistencia}, flex:{d.flexibilidad}, moral: {d.moral}, lesion: {d.lesionado}"
                  f", precio: ${d.precio}")
        print("\n Pulse que deportista quiere fichar")
        dep = self.input(len(deportistas))
        deportista = deportistas[dep]
        if self.delegacion.dinero >= deportista.precio:
            self.delegacion.fichar_deportista(dep, deportistas)
            print(f"Haz fichado a {deportista.nombre}")
        else:
            print("\nNo tienes suficiente dinero")

    def entrenar_deportista(self):
        if self.delegacion.dinero < COSTO_ENTRENAR_DEPORTISTA:
            print("\nNo tienes suficiente dinero")
        else:
            print("\nEscoja el deportista que quiera entrenar")
            print("Pulse:")
            for deportista in self.delegacion.equipo:
                print(f"   [{self.delegacion.equipo.index(deportista)}]  {deportista.nombre}, "
                      f"vel: {deportista.velocidad}, res: {deportista.resistencia}, flex: "
                      f"{deportista.flexibilidad}")
            deportista = self.input(len(self.delegacion.equipo))
            print("\nEscoja el atributo del deportista a entrenar")
            print("Pulse:")
            print("   [0]  velocidad")
            print("   [1]  resistencia")
            print("   [2]  flexibilidad")
            atributo = self.input(3)
            self.delegacion.entrenar_deportista(deportista, atributo)

    def sanar_deportista(self):
        if self.delegacion.dinero < COSTO_SANAR_DEPORTISTA:
            print("\nNo tienes suficiente dinero")
        else:
            print("\nEscoja el deportista que quiera sanar")
            print("Pulse:")
            for deportista in self.delegacion.equipo:
                print(f"   [{self.delegacion.equipo.index(deportista)}]  {deportista.nombre}"
                      f", lesionado: {deportista.lesionado}")
            deportista = self.input(len(self.delegacion.equipo))
            deportista = self.delegacion.equipo[deportista]
            if deportista.lesionado is False:
                print(f"No puedes sanar a {deportista.nombre}, no esta lesionado")
            else:
                print(f"{deportista.nombre}, esta llendo al medico...")
                self.delegacion.sanar_deportista(deportista)


class Oponente(Entrenador):

    def __init__(self):
        super().__init__()

    def fichar_deportista(self):
        pass

    def entrenar_deportista(self):
        pass

    def sanar_deportista(self):
        pass


if __name__ == "__main__":
    jugador = Usuario()
    print(type(jugador).__name__)
