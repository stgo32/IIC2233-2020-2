from sys import exit
from parametros import DIAS_COMPETENCIA, CONT_HABILIDAD_ESP, COSTO_HAB_ESP


class Menu:

    def __init__(self):
        self.campeonato = None  # instancia de campeonato
        self.usuario = None  # instancia entrenador
        self.lista_deportistas = []

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

    def inicio(self, bool_inicio):
        print("\n**** MENU DE INICIO ****")
        print("\nPulse:")
        print("   [0]  Para comenzar una nueva partida")
        print("   [1]  Para salir el programa\n")
        accion = self.input(2)
        if accion == 0:
            # comenzar partida
            resultados = open("resultados.txt", "w")
            resultados.write("RESULTADOS DIA A DIA DCCUMBRE OLIMPICA"
                             "\n________________________________________")
            resultados.close()
            bool_inicio = False
        elif accion == 1:
            # salir
            print("\nHa salido del programa")
            exit()
        return bool_inicio

    def principal(self):
        menu_principal = True
        while menu_principal:
            if self.campeonato.dia_actual > DIAS_COMPETENCIA:
                print("\nDCCumbre Olimpica a llegado a su fin")
                if (self.campeonato.delegaciones[0].medallas >
                        self.campeonato.delegaciones[1].medallas):
                    print(f"Ha ganado {self.campeonato.delegaciones[0].nombre}!!")
                elif (self.campeonato.delegaciones[0].medallas <
                      self.campeonato.delegaciones[1].medallas):
                    print(f"Ha ganado {self.campeonato.delegaciones[1].nombre}!!")
                else:

                    print("Ambas delegaciones han empatado")
                delegacion1 = self.campeonato.delegaciones[0]
                delegacion2 = self.campeonato.delegaciones[1]
                print("\nMedallero:")
                print(f"Deporte      |   {delegacion1.nombre}  |   {delegacion2.nombre}")
                a = self.campeonato.medallero[delegacion1.nombre]["Atletismo"]
                b = self.campeonato.medallero[delegacion2.nombre]["Atletismo"]
                print(f"Atletismo     {a:^15d} {b:^15d}")
                a = self.campeonato.medallero[delegacion1.nombre]["Ciclismo"]
                b = self.campeonato.medallero[delegacion2.nombre]["Ciclismo"]
                print(f"Ciclismo      {a:^15d} {b:^15d}")
                a = self.campeonato.medallero[delegacion1.nombre]["Gimnasia"]
                b = self.campeonato.medallero[delegacion2.nombre]["Gimnasia"]
                print(f"Gimnasia      {a:^15d} {b:^15d}")
                a = self.campeonato.medallero[delegacion1.nombre]["Natacion"]
                b = self.campeonato.medallero[delegacion2.nombre]["Natacion"]
                print(f"Natacion      {a:^15d} {b:^15d}")
                print("\nPulse: [0]  Para volver al menu de inicio")
                # actualizar puntajes.txt
                accion = self.input(1)
                self.inicio(bool_inicio=True)
            print("\n**** MENU PRINCIPAL ****")
            print(f"\nPulse:                                     ${self.usuario.delegacion.dinero}")
            print("   [0]  Para ir al menu de entrenador")
            print("   [1]  Para simular competencias")
            print("   [2]  Para mostrar estado")
            print("   [3]  Para volver a inicio")
            print("   [4]  Para salir el programa\n")
            accion = self.input(5)
            if accion == 0:
                # menu entrenador
                self.menu_entrenador(self.usuario)
            if 1 <= accion <= 2:
                if accion == 1:
                    # simular cmpetencias
                    self.campeonato.simular_competencias()
                elif accion == 2:
                    # mostrar estado
                    self.campeonato.estado_competencia()
                print("\nPulse: [0]  Para volver al menu principal")
                accion = self.input(1)
                menu_principal = True
            elif accion == 3:
                # volver a inicio
                menu_principal = False
                menu_inicio = True
                return menu_principal, menu_inicio
            elif accion == 4:
                # salir
                print("\nHa salido del programa")
                exit()

    def menu_entrenador(self, entrenador):
        menu_entrenador = True
        while menu_entrenador:
            print("\n**** MENU DE ENTRENADOR ****")
            print(f"\nPulse:                                     ${self.usuario.delegacion.dinero}")
            print("   [0]  Para fichar un jugador")
            print("   [1]  Para entrenar un jugador")
            print("   [2]  Para sanar un jugador")
            print("   [3]  Para comprar tecnologia")
            print("   [4]  Para usar habilidad especial")
            print("   [5]  Para volver al menu principal")
            print("   [6]  Para salir del programa")
            accion = self.input(7)
            if 0 <= accion <= 4:
                if accion == 0:
                    # fichar jugador
                    entrenador.fichar_deportista(self.lista_deportistas)
                elif accion == 1:
                    # entrenar jugador
                    entrenador.entrenar_deportista()
                elif accion == 2:
                    # sanar lesion
                    entrenador.sanar_deportista()
                elif accion == 3:
                    # comprar tecnologia
                    entrenador.delegacion.comprar_tecnologia()
                elif accion == 4:
                    # habilidad especial
                    if entrenador.delegacion.dinero >= COSTO_HAB_ESP:
                        if entrenador.delegacion.cont_hab_esp == CONT_HABILIDAD_ESP:
                            self.campeonato = \
                                entrenador.delegacion.habilidad_especial(self.campeonato)
                        else:
                            print("\nSolo esta permitido usar una vez la habilidad especial")
                    else:
                        print("\n No tienes dinero suficiente")
                print("\nPulse: [0]  Para volver al menu entrenador")
                accion = self.input(1)
                menu_entrenador = True
            elif accion == 5:
                # volver
                menu_entrenador = False
                self.principal()
            elif accion == 6:
                # salir
                print("\nHa salido del programa")
                exit()
