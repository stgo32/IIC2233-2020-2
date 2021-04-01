from random import randint


class Jugador:

    def __init__(self, nombre, ide, color):
        self.nombre = nombre
        self.id = ide
        self.color = color

        self.chozas = []  # lista de nodos
        self.materias_primas = {
            'arcilla': 0,
            'madera': 0,
            'trigo': 0
        }

    def sumar_materias_primas(self, nodo, ganancia):
        print('ganancia', ganancia)
        for materia_prima in nodo.materias_primas:
            if materia_prima == 'arcilla':
                self.materias_primas['arcilla'] += ganancia
            elif materia_prima == 'madera':
                self.materias_primas['madera'] += ganancia
            elif materia_prima == 'trigo':
                self.materias_primas['trigo'] += ganancia

        return self.materias_primas

    def restar_materias_primas(self, nodo, costo):
        self.materias_primas['arcilla'] -= costo['arcilla']
        self.materias_primas['madera'] -= costo['madera']
        self.materias_primas['trigo'] -= costo['trigo']
        return self.materias_primas


class Usuario(Jugador):

    def __init__(self, nombre, ide, color):
        super().__init__(nombre, ide, color)

        self.lanzo_dados = False
        self.actuo = False

        self.puntos_victoria = 0

        print('mp usuario jug.py', self.materias_primas)

    def ubicar_choza_inicial(self, tablero, ganancia):
        ubicar_choza = False
        contador = 0

        while ubicar_choza is False:
            contador = 0
            nodo_elejido = randint(0, len(tablero.lista_nodos)-1)
            nodo_elejido = tablero.lista_nodos[nodo_elejido]
            nodos_vecinos = nodo_elejido.vecinos

            if nodo_elejido.choza.ubicable:
                contador += 1
            for nodo in nodos_vecinos:
                if nodo.choza.ubicable:
                    contador += 1
                else:
                    pass
            if contador == len(nodos_vecinos) + 1:
                ubicar_choza = True

        nodo_elejido.ubicar_choza(self.color)
        self.chozas.append(nodo_elejido)

        self.materias_primas = self.sumar_materias_primas(nodo_elejido, ganancia)

        return {
            'evento': 'Choza inicial',
            'detalles': {
                'jugador': self.nombre,
                'nodo': nodo_elejido.valor,
                'materias_primas_jugador': self.materias_primas
                }
            }

    def preguntar_por_choza(self, costo_choza):
        ''' costo_choza: dict con costo en materias primas por una choza '''
        if (
            self.materias_primas['arcilla'] >= costo_choza['arcilla'] and
            self.materias_primas['madera'] >= costo_choza['madera'] and
            self.materias_primas['trigo'] >= costo_choza['trigo']
        ):
            return True
        else:
            return False
