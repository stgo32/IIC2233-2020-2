import os

from cargar_archivos import cargar_aeropuertos, cargar_conexiones
from entidades import Aeropuerto, Conexion


UMBRAL = 40000


class RedesMundiales:

    def __init__(self):
        # Estructura donde se guardaran los aeropuertos
        # Cada llave es un id y el valor es una instancia de Aeropuerto
        self.aeropuertos = {}

    def agregar_aeropuerto(self, aeropuerto_id, nombre):
        aeropuerto = Aeropuerto(aeropuerto_id, nombre)
        self.aeropuertos[aeropuerto_id] = aeropuerto

    def agregar_conexion(self, aeropuerto_id_partida, aeropuerto_id_llegada, infectados):
        if (aeropuerto_id_llegada and aeropuerto_id_partida) in self.aeropuertos:
            aeropuerto_partida = self.aeropuertos[aeropuerto_id_partida]
            if aeropuerto_id_llegada not in aeropuerto_partida.conexiones:
                conexion = Conexion(aeropuerto_id_partida, aeropuerto_id_llegada, infectados)
                aeropuerto_partida.conexiones.append(conexion)

    def cargar_red(self, ruta_aeropuertos, ruta_conexiones):

        # Primero se crean todos los aeropuertos
        for aeropuerto_id, nombre in cargar_aeropuertos(ruta_aeropuertos):
            self.agregar_aeropuerto(aeropuerto_id, nombre)

        # Después generamos las conexiones
        for id_partida, id_salida, infectados in cargar_conexiones(ruta_conexiones):
            self.agregar_conexion(id_partida, id_salida, infectados)

    def eliminar_conexion(self, conexion):
        id_partida = conexion.aeropuerto_inicio_id
        id_llegada = conexion.aeropuerto_llegada_id
        aeropuerto_inicio = self.aeropuertos.get(id_partida)
        for c in aeropuerto_inicio.conexiones:
            if c.aeropuerto_llegada_id == id_llegada:
                aeropuerto_inicio.conexiones.remove(c)
                break

    def eliminar_aeropuerto(self, aeropuerto_id):
        if aeropuerto_id not in self.aeropuertos:
            raise ValueError(f"No puedes eliminar un aeropuerto que no existe ({aeropuerto_id})")
        if self.aeropuertos[aeropuerto_id].conexiones:
            raise ValueError(f"No puedes eliminar un aeropuerto con conexiones ({aeropuerto_id})")
        del self.aeropuertos[aeropuerto_id]

    def infectados_generados_desde_aeropuerto(self, aeropuerto_id):
        # basado en dfs de notebook 3 semana 12

        if aeropuerto_id in self.aeropuertos:
            red = set()
            infectados = 0
            ae_inicial = aeropuerto_id
            stack = [aeropuerto_id]

            while len(stack) > 0:
                aeropuerto_id = stack.pop()

                if aeropuerto_id in red:
                    continue
                
                for conexion in self.aeropuertos[aeropuerto_id].conexiones:
                    infectados += conexion.infectados
                red.add(aeropuerto_id)
                
                for conexion in self.aeropuertos[aeropuerto_id].conexiones:
                    if conexion.aeropuerto_llegada_id not in red:
                        stack.append(conexion.aeropuerto_llegada_id)

            nombre = self.aeropuertos[ae_inicial].nombre
            print(f'La cantidad estimada de infectados generados por el aeropuerto '
                  f'{nombre} es de {infectados}')
            return infectados
        else:
            return 0

    def verificar_candidatos(self, ruta_aeropuertos_candidatos, ruta_conexiones_candidatas):
        # Se revisa cada aeropuerto candidato con las agregars conexiones candidatas.
        # Se elimina el aeropuerto en caso de que este genere muchos infectados
        for aeropuerto_id, nombre in cargar_aeropuertos(ruta_aeropuertos_candidatos):
            self.agregar_aeropuerto(aeropuerto_id, nombre)

        # Después generamos las conexiones
        for id_partida, id_salida, infectados in cargar_conexiones(ruta_conexiones_candidatas):
            self.agregar_conexion(id_partida, id_salida, infectados)
            # revisamos conexion
            if self.infectados_generados_desde_aeropuerto(id_partida) >= UMBRAL:
                for conexion in self.aeropuertos[id_partida].conexiones:
                    if conexion.aeropuerto_llegada_id == id_salida:
                        break
                self.eliminar_conexion(conexion)
                print(f'La conexión {conexion} rompe las reglas de seguridad')

        


if __name__ == "__main__":
    # I: Construcción de la red
    # Instanciación de la red de aeropuertos
    redmundial = RedesMundiales()
    # Carga de datos (utiliza agregar_aeropuerto y agregar_conexion)
    redmundial.cargar_red(
        os.path.join("datos", "aeropuertos.txt"),
        os.path.join("datos", "conexiones.txt"),
    )

    # II: Consultas sobre la red
    # Verificar si conteo de infectados funciona
    # Para el aeropuerto 8 debería ser 2677
    redmundial.infectados_generados_desde_aeropuerto(8)
    # Para el aeropuerto 7 debería ser 10055
    redmundial.infectados_generados_desde_aeropuerto(7)
    # Para el aeropuerto 12 debería ser 30000
    redmundial.infectados_generados_desde_aeropuerto(4)

    # III: Simulación sobre la red
    # Utilizamos lo que hemos hecho para aplicar los cambios sobre la red
    redmundial.verificar_candidatos(
        os.path.join("datos", "aeropuertos_candidatos.txt"),
        os.path.join("datos", "conexiones_candidatas.txt"),
    )
