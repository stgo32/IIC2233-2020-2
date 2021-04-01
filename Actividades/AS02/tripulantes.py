import random
import time
from threading import Thread, Event, Lock, Timer

from parametros import (PROB_IMPOSTOR, PROB_ARREGLAR_SABOTAJE,
                        TIEMPO_ENTRE_TAREAS, TIEMPO_TAREAS, TIEMPO_SABOTAJE,
                        TIEMPO_ENTRE_ACCIONES, TIEMPO_ESCONDITE)

from funciones import (elegir_accion_impostor, print_progreso, print_anuncio,
                       print_sabotaje, cargar_sabotajes, print_explosión)


class Tripulante(Thread):

    def __init__(self, color, tareas, evento_sabotaje, diccionario_tareas):
        # No modificar
        super().__init__(daemon=True)
        self.color = color
        self.tareas = tareas
        self.esta_vivo = True
        self.diccionario_tareas = diccionario_tareas
        self.evento_sabotaje = evento_sabotaje
        # Si quieres agregar lineas, hazlo desde aca

    def run(self):
        while True:
            if self.esta_vivo and len(self.tareas) > 0:
                prob = random.uniform(0, 1)
                while self.evento_sabotaje:
                    if prob < PROB_ARREGLAR_SABOTAJE:
                        self.arreglar_sabotaje()
                    else:
                        time.sleep(TIEMPO_ENTRE_TAREAS)
                if not self.evento_sabotaje:
                    self.hacer_tarea()
                    time.sleep(TIEMPO_ENTRE_TAREAS)


    def hacer_tarea(self):
        tarea = random.choice(self.tareas)
        tarea = self.diccionario_tareas[tarea]
        if not tarea["realizado"]:
            with tarea["lock"]:
                tiempo = random.randint(0, TIEMPO_TAREAS)
                tiempo /= 5
                for i in range(5):
                    if self.esta_vivo is not False:
                        time.sleep(tiempo)
                        tar = tarea["nombre"]
                        print_progreso(self.color, "Realizando "+tar, i)
                if self.esta_vivo is not False:
                    tarea["realizado"] = True
                    for t in self.tareas:
                        if t == tarea["nombre"]:
                            self.tareas.pop(self.tareas.index(t))


    def arreglar_sabotaje(self):
        tiempo = random.randint(TIEMPO_SABOTAJE[0], TIEMPO_SABOTAJE[1])
        tiempo /= 4
        print_anuncio(self.color, "Arreglando sabotaje")
        for i in range(4):
            if self.esta_vivo:
                time.sleep(tiempo)
                print_progreso(self.color, f"Arreglando sabotaje", i)
        if self.esta_vivo:
            self.evento_sabotaje.clear()






class Impostor(Tripulante):

    def __init__(self, color, tareas, evento_sabotaje, diccionario_tareas, tripulantes, evento_termino):
        # No modificar
        super().__init__(color, tareas, evento_sabotaje, diccionario_tareas)
        self.tripulantes = tripulantes
        self.evento_termino = evento_termino
        self.sabotajes = cargar_sabotajes()
        # Si quieres agregar lineas, hazlo desde aca

    def run(self):
        vivos = True
        while self.evento_termino is False and vivos:
            accion = elegir_accion_impostor()
            if accion == "Matar":
                self.matar_jugador()
            elif accion == "Sabotear":
                self.sabotear()
            elif accion == "Esconderse":
                time.sleep(TIEMPO_ESCONDITE)
            for t in self.tripulantes:
                if t.esta_vivo is False:
                    vivos = False
            time.sleep(TIEMPO_ENTRE_ACCIONES)
        

    def matar_jugador(self):
        tripulante = random.choice(self.tripulantes)
        self.tripulantes(self.tripulantes.index(tripulante)).esta_vivo = False
        self.tripulantes.pop(self.tripulantes.index(tripulante))
        print_anuncio(tripulante.color, "Ha muerto")

    def sabotear(self):
        if not self.evento_sabotaje:
            sabotaje = random.choice(self.sabotajes)
            tiempo = random.randint(TIEMPO_SABOTAJE[0], TIEMPO_SABOTAJE[1])
            timer_sabotaje = Timer(tiempo, self.terminar_sabotaje)
            timer_sabotaje.start()
            self.evento_sabotaje.set()
            print_sabotaje(sabotaje)

    def terminar_sabotaje(self):
        if self.evento_sabotaje:
            for t in self.tripulantes:
                t.esta_vivo = False
            print_explosión()


if __name__ == "__main__":
    print("\n" + " INICIANDO PRUEBA DE TRIPULANTE ".center(80, "-") + "\n")
    # Se crea un diccionario de tareas y un evento sabotaje de ejemplos.
    ejemplo_tareas = {
            "Limpiar el filtro de oxigeno": {
                "lock": Lock(),
                "realizado": False,
                "nombre": "Limpiar el filtro de oxigeno"
            }, 
            "Botar la basura": {
                "lock": Lock(),
                "realizado": False,
                "nombre":  "Botar la basura"
            }
        }
    ejemplo_evento = Event()

    # Se intancia un tripulante de color ROJO
    rojo = Tripulante("Rojo", list(ejemplo_tareas.keys()), ejemplo_evento, ejemplo_tareas)

    rojo.start()

    time.sleep(5)
    # ==============================================================
    # Descomentar las siguientes lineas para probar el evento sabotaje.

    # print(" HA COMENZADO UN SABOTAJE ".center(80, "*"))
    # ejemplo_evento.set()

    rojo.join()

    print("\n-" + "="*80 + "\n")
    print(" PRUEBA DE TRIPULANTE TERMINADA ".center(80, "-"))
    if sum((0 if x["realizado"] else 1 for x in ejemplo_tareas.values())) > 0:
        print("El tripulante no logró completar todas sus tareas. ")
    elif ejemplo_evento.is_set():
        print("El tripulante no logró desactivar el sabotaje")
    else:
        print("El tripulante ha GANADO!!!")
