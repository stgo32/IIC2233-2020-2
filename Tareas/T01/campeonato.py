from deportes import Atletismo, Ciclismo, Gimnasia, Natacion
from archivosExternos import actualizar_resultados
from parametros import (DIA_INICIAL,
                        DIA,
                        DESCUENTO_MORAL,
                        DESCUENTO_EXCELENCIA_RESPETO,
                        BONIFICACION_MORAL,
                        BONIFICACION_DINERO)


class Campeonato:

    def __init__(self):
        self.dia_actual = DIA_INICIAL + DIA
        self.delegaciones = []  # lista con instancias de delegaciones
        self.deportes = {
            "Atletismo": Atletismo(),
            "Ciclismo": Ciclismo(),
            "Gimnasia": Gimnasia(),
            "Natacion": Natacion()
                        }
        self.medallero = {
            "IEEEsparta": {
                "Atletismo": 0,
                "Ciclismo": 0,
                "Gimnasia": 0,
                "Natacion": 0
                           },
            "DCCrotona": {
                "Atletismo": 0,
                "Ciclismo": 0,
                "Gimnasia": 0,
                "Natacion": 0
                          }}

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

    def competir(self, deporte):
        for delegacion in self.delegaciones:
            if type(delegacion.entrenador).__name__ == "Usuario":
                print(f"\nEscoja el deportista para {type(deporte).__name__}")
                for deportista in delegacion.equipo:
                    print(f"   [{delegacion.equipo.index(deportista)}]  {deportista.nombre}, "
                          f"vel: {deportista.velocidad}, res: {deportista.resistencia}, flex: "
                          f"{deportista.flexibilidad}, moral: {deportista.moral}, lesion: "
                          f"{deportista.lesionado}")
                dep = self.input(len(delegacion.equipo))
                depor_usuario = delegacion.equipo[dep]
        depor_lesion_usuario = True
        while depor_lesion_usuario:
            if depor_usuario.lesionado:
                print(f"{depor_usuario.nombre} esta lesionado. ¿Seguro que quieres continuar?")
                print("   [0]  si")
                print("   [1]  no")
                accion = self.input(2)
                if accion == 0:
                    depor_lesion_usuario = False
                else:
                    print("Vuelva a escojer un deportista")
                    dep = self.input(len(delegacion.equipo))
                    depor_usuario = delegacion.equipo[dep]
            else:
                depor_lesion_usuario = False
        validez_usuario, validez_oponente, depor_oponente = deporte.validez_competencia(
            self.delegaciones,
            depor_usuario
                )
        if validez_usuario and validez_oponente:
            ganador = deporte.calcular_ganador(depor_usuario, depor_oponente)
            if ganador == depor_usuario:
                perdedor = depor_oponente
            else:
                perdedor = depor_usuario
        elif validez_usuario and not validez_oponente:
            ganador = depor_usuario
            perdedor = depor_oponente
        elif validez_oponente and not validez_usuario:
            ganador = depor_oponente
            perdedor = depor_usuario
        else:
            ganador = False
            perdedor = False
        return ganador, perdedor

    def simular_competencias(self):
        self.dia_actual += DIA
        dia = open("resultados.txt", "a")
        dia.write(f"\nDia: {self.dia_actual}")
        dia.close()

        ganador, perdedor = self.competir(self.deportes["Atletismo"])
        print("\nResultados de Atletismo:")
        if ganador is not False and perdedor is not False:
            for delegacion in self.delegaciones:
                if ganador in delegacion.equipo:
                    deleg_ganadora = delegacion
                    self.medallero[delegacion.nombre]["Atletismo"] += 1
                else:
                    deleg_perdedora = delegacion
            self.premiar_ganadores(deleg_ganadora, ganador)
            self.castigar_perdedores(deleg_perdedora, perdedor)
        else:
            print("Ha habido un empate")
        if ganador is False:
            deleg_ganadora = False
        actualizar_resultados(ganador, deleg_ganadora, "Atletismo", "resultados.txt")

        ganador, perdedor = self.competir(self.deportes["Ciclismo"])
        print("\nResultados de Ciclismo:")
        if ganador is not False and perdedor is not False:
            for delegacion in self.delegaciones:
                if ganador in delegacion.equipo:
                    deleg_ganadora = delegacion
                    self.medallero[delegacion.nombre]["Ciclismo"] += 1
                else:
                    deleg_perdedora = delegacion
            self.premiar_ganadores(deleg_ganadora, ganador)
            self.castigar_perdedores(deleg_perdedora, perdedor)
        else:
            print("Ha habido un empate")
        if ganador is False:
            deleg_ganadora = False
        actualizar_resultados(ganador, deleg_ganadora, "Ciclismo", "resultados.txt")

        ganador, perdedor = self.competir(self.deportes["Gimnasia"])
        print("\nResultados de Gimnasia:")
        if ganador is not False and perdedor is not False:
            for delegacion in self.delegaciones:
                if ganador in delegacion.equipo:
                    deleg_ganadora = delegacion
                    self.medallero[delegacion.nombre]["Gimnasia"] += 1
                else:
                    deleg_perdedora = delegacion
            self.premiar_ganadores(deleg_ganadora, ganador)
            self.castigar_perdedores(deleg_perdedora, perdedor)
        else:
            print("Ha habido un empate")
        if ganador is False:
            deleg_ganadora = False
        actualizar_resultados(ganador, deleg_ganadora, "Gimnasia", "resultados.txt")

        ganador, perdedor = self.competir(self.deportes["Natacion"])
        print("\nResultados de Natacion:")
        if ganador is not False and perdedor is not False:
            for delegacion in self.delegaciones:
                if ganador in delegacion.equipo:
                    deleg_ganadora = delegacion
                    self.medallero[delegacion.nombre]["Natacion"] += 1
                else:
                    deleg_perdedora = delegacion
            self.premiar_ganadores(deleg_ganadora, ganador)
            self.castigar_perdedores(deleg_perdedora, perdedor)
        else:
            print("Ha habido un empate")
        if ganador is False:
            deleg_ganadora = False
        actualizar_resultados(ganador, deleg_ganadora, "Natacion", "resultados.txt")
        asteriscos = open("resultados.txt", "a")
        asteriscos.write("\n*****************************************")
        asteriscos.close()
        self.dia_actual += DIA

    def premiar_ganadores(self, delegacion, deportista):
        if delegacion.nombre == "DCCrotona":
            deportista.moral += BONIFICACION_MORAL * 2
        else:
            deportista.moral += BONIFICACION_MORAL
        delegacion.dinero += BONIFICACION_DINERO
        delegacion.medallas += 1
        print(f"Felicidades a {deportista.nombre}!! Se lleva el ORO!!")

    def castigar_perdedores(self, delegacion, deportista):
        delegacion.excelencia_respeto -= DESCUENTO_EXCELENCIA_RESPETO
        print(f"Una lastima, {deportista.nombre} ha perdido")
        if delegacion.nombre == "IEEEsparta":
            deportista.moral -= 2 * DESCUENTO_MORAL
        else:
            deportista.moral -= DESCUENTO_MORAL

    def calcular_moral(self, delegacion):
        suma_morales = 0
        for deportista in delegacion.equipo:
            suma_morales += deportista.moral
        promedio = suma_morales / len(delegacion.equipo)
        delegacion.moral = promedio
        return delegacion.moral

    # mostrar estado campeonato --> en menus.py
    def estado_competencia(self):
        delegacion1 = self.delegaciones[0]
        delegacion2 = self.delegaciones[1]
        print("\n                ESTADO DE LAS DELEGACIONES Y DEPORTISTAS")
        print("___________________________________________________________________________")
        print(f"{delegacion1.nombre}")
        print(f"Entrenador: {delegacion1.entrenador.apodo}")
        print(f"Moral del equipo: {round(self.calcular_moral(delegacion1), 2)}")
        print(f"Medallas: {delegacion1.medallas}")
        print(f"Dinero: ${delegacion1.dinero}\n")
        print(f"Excelencia y respeto: {round(delegacion1.excelencia_respeto, 2)}")
        print(f"Implementos deportivos: {round(delegacion1.implementos_deportivos, 2)}")
        print(f"Implementos medicos: {round(delegacion1.implementos_medicos, 2)}\n")
        print("Equipo deportivo:")
        print("Nombre        |  Velocidad   | Resistencia  | Flexibilidad |  Lesion")
        for deportista in delegacion1.equipo:
            print(f"{deportista.nombre:15.15s}"
                  f"{deportista.velocidad:8.1f}"
                  f"{deportista.resistencia:15.1f}"
                  f"{deportista.flexibilidad:15.1f}"
                  f"{str(deportista.lesionado):^25.25s}")
        print("***************************************************************************")
        print(f"{delegacion2.nombre}")
        print(f"Entrenador: {delegacion2.entrenador.apodo}")
        print(f"Moral del equipo: {round(self.calcular_moral(delegacion2), 2)}")
        print(f"Medallas: {delegacion2.medallas}")
        print(f"Dinero: ${delegacion2.dinero}\n")
        print(f"Excelencia y respeto: {round(delegacion2.excelencia_respeto, 2)}")
        print(f"Implementos deportivos: {round(delegacion2.implementos_deportivos, 2)}")
        print(f"Implementos medicos: {round(delegacion2.implementos_medicos, 2)}\n")
        print("Equipo deportivo:")
        print("Nombre        |  Velocidad   | Resistencia  | Flexibilidad |  Lesion")
        for deportista in delegacion2.equipo:
            print(f"{deportista.nombre:15.15s}"
                  f"{deportista.velocidad:8.1f}"
                  f"{deportista.resistencia:15.1f}"
                  f"{deportista.flexibilidad:15.1f}"
                  f"{str(deportista.lesionado):^25.25s}")
        print("___________________________________________________________________________")
        print(f"Dia {self.dia_actual + 1} : Entrenamiento")
        print("\nMedallero:")
        print(f"Deporte      |   {delegacion1.nombre}  |   {delegacion2.nombre}")
        a = self.medallero[delegacion1.nombre]["Atletismo"]
        b = self.medallero[delegacion2.nombre]["Atletismo"]
        print(f"Atletismo     {a:^15d} {b:^15d}")
        a = self.medallero[delegacion1.nombre]["Ciclismo"]
        b = self.medallero[delegacion2.nombre]["Ciclismo"]
        print(f"Ciclismo      {a:^15d} {b:^15d}")
        a = self.medallero[delegacion1.nombre]["Gimnasia"]
        b = self.medallero[delegacion2.nombre]["Gimnasia"]
        print(f"Gimnasia      {a:^15d} {b:^15d}")
        a = self.medallero[delegacion1.nombre]["Natacion"]
        b = self.medallero[delegacion2.nombre]["Natacion"]
        print(f"Natacion      {a:^15d} {b:^15d}")
        print("___________________________________________________________________________")
