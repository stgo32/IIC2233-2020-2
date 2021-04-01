import json
import math

from generador_grilla import GeneradorGrillaHexagonal

from parametros import p


#  basado en grafo de listas de adyacencia de la semana 12
class Grafo:

    def __init__(self, lista_adyacencia=None):
        self.lista_adyacencia = lista_adyacencia or {}

    def adyacentes(self, x, y):
        return y in self.lista_adyacencia[x]

    def vecinos(self, x):
        return self.lista_adyacencia[x]

    def agregar_vertice(self, x):
        self.lista_adyacencia[x] = set()

    def remover_vertice(self, x):
        self.lista_adyacencia.pop(x, None)
        for k, v in self.lista_adyacencia.items():
            if x in v:
                v.remove(x)

    def agregar_arista(self, x, y):
        if x in self.lista_adyacencia:
            self.lista_adyacencia[x].add(y)

    def remover_arista(self, x, y):
        vecinos_x = self.lista_adyacencia.get(x, set())
        if y in vecinos_x:
            vecinos_x.remove(y)

    def __repr__(self):
        texto_nodos = []
        for nodo, vecinos in self.lista_adyacencia.items():
            texto_nodos.append(f"Vecinos de {nodo}: {vecinos}.")
        return "\n".join(texto_nodos)


class Nodo:

    def __init__(self, valor, posicion):
        self.valor = valor
        self.posicion = posicion
        self.vecinos = []
        self.choza_ocupada = False
        self.choza_ubicable = True
        self.choza = None  # DropChoza
        self.materias_primas = []

    def posicion_choza(self):
        x = self.posicion[0] - p.TAMANO_DROP_CHOZA[0]/2
        y = self.posicion[1] - p.TAMANO_DROP_CHOZA[1]/2
        return (x, y)

    def ubicar_choza(self, color):
        self.choza_ocupada = True
        self.choza_ubicable = False
        self.choza.ubicable = False
        for nodo in self.vecinos:
            nodo.choza_ubicable = False
            nodo.choza.ubicable = False

        self.choza.ocupar(color)

    def __repr__(self):
        return repr(self.valor)


class Hexagono:

    def __init__(self, valor, vertices=None):
        self.valor = valor
        self.vertices = vertices or []  # lista de nodos
        self.numero = None  # int numero ficha
        self.materia_prima = None  # str materia prima

    def __repr__(self):
        return repr(self.valor)

    def posicion(self):
        nodo0 = self.vertices[0].posicion
        x = nodo0[0] - p.LARGO_ARISTA/2
        y = nodo0[1]
        return (x, y)

    def size(self):
        x = p.LARGO_ARISTA * 2
        y = math.cos(math.radians(30)) * p.LARGO_ARISTA * 2
        return (x, y)

    def ubicar_label_numero(self, label):
        x = self.posicion()[0] + p.LARGO_ARISTA - 20
        y = self.posicion()[1] + p.LARGO_ARISTA - 50
        label.move(x, y)

    def ubicar_imagen_numero(self, label):
        x = self.posicion()[0] + p.LARGO_ARISTA/2 + 5
        y = self.posicion()[1] + p.LARGO_ARISTA/2 - 10
        label.move(x, y)


class Tablero:

    def __init__(self):
        self.lista_nodos = None
        self.lista_hexagonos = None
        self.grafo_nodos = None
        self.grafo_hexagonos = None

    def generar_listas_y_grafos(self, grafos):
        self.lista_nodos = self.generar_lista_nodos(grafos)
        print(self.lista_nodos)
        self.grafo_nodos = self.generar_grafo_nodos(grafos)

        self.lista_hexagonos = self.generar_lista_hexagonos(grafos)
        self.grafo_hexagonos = self.generar_grafo_hexagonos(grafos)

    def cargar_listas_adyacencia(self, ruta):
        with open(ruta, 'rt') as archivo:
            grafos = json.load(archivo)
        return grafos

    def generar_lista_nodos(self, grafos):
        # grafos = self.cargar_listas_adyacencia(ruta_grafos)
        grilla = GeneradorGrillaHexagonal(p.LARGO_ARISTA)
        pos_nodos = grilla.generar_grilla(grafos['dimensiones_mapa'], 50, 30)
        lista_nodos = [Nodo(int(i), pos_nodos[i]) for i in pos_nodos]
        return lista_nodos

    def generar_grafo_nodos(self, grafos):
        # grafos = self.cargar_listas_adyacencia(ruta_grafos)
        for nodo in self.lista_nodos:
            for vecino in grafos['nodos'][str(nodo.valor)]:
                nodo.vecinos.append(self.lista_nodos[int(vecino)])
        lista_adyacencia = {nodo: nodo.vecinos for nodo in self.lista_nodos}
        grafo = Grafo(lista_adyacencia)
        return grafo

    def generar_lista_hexagonos(self, grafos):
        # grafos = self.cargar_listas_adyacencia(ruta_grafos)
        lista_hexagonos = [Hexagono(int(hexa)) for hexa in grafos['hexagonos']]
        return lista_hexagonos

    def generar_grafo_hexagonos(self, grafos):
        # grafos = self.cargar_listas_adyacencia(ruta_grafos)
        for hexa in self.lista_hexagonos:
            for nodo in grafos['hexagonos'][str(hexa.valor)]:
                hexa.vertices.append(self.lista_nodos[int(nodo)])
        lista_adyacencia = {h: h.vertices for h in self.lista_hexagonos}
        grafo = Grafo(lista_adyacencia)
        return grafo

    def set_materias_primas_nodos(self):
        for nodo in self.lista_nodos:
            for hexa in self.lista_hexagonos:
                if nodo in hexa.vertices:
                    nodo.materias_primas.append(hexa.materia_prima)
                    self.lista_nodos[nodo.valor] = nodo


if __name__ == "__main__":

    t = Tablero()

