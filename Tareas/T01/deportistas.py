from parametros import (
                MINIMO_ATRIBUTO_DEPORTISTA,
                MAXIMO_ATRIBUTO_DEPORTISTA,
                PUNTOS_ENTRENAMIENTO,
                PONDERADOR_ENTRENAMIENTO_IEEE
            )


class Deportista:

    def __init__(self, nombre, vel, res, flex, moral, lesion, precio):
        self.nombre = nombre  # str
        self._velocidad = vel  # int
        self._resistencia = res  # int
        self._flexibilidad = flex  # int
        self._moral = moral  # int
        self._lesionado = lesion  # bool
        self.precio = precio  # int

    @property
    def lesionado(self):
        if self._lesionado == "True":
            return True
        if self._lesionado == "False":
            return False
        return self._lesionado

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, mejora):
        if mejora < MINIMO_ATRIBUTO_DEPORTISTA:
            self._velocidad = MINIMO_ATRIBUTO_DEPORTISTA
        elif mejora > MAXIMO_ATRIBUTO_DEPORTISTA:
            self._velocidad = MAXIMO_ATRIBUTO_DEPORTISTA
        else:
            self._velocidad = mejora

    @property
    def resistencia(self):
        return self._resistencia

    @resistencia.setter
    def resistencia(self, mejora):
        if mejora < MINIMO_ATRIBUTO_DEPORTISTA:
            self._resistencia = MINIMO_ATRIBUTO_DEPORTISTA
        elif mejora > MAXIMO_ATRIBUTO_DEPORTISTA:
            self._resistencia = MAXIMO_ATRIBUTO_DEPORTISTA
        else:
            self._resistencia = mejora

    @property
    def flexibilidad(self):
        return self._flexibilidad

    @flexibilidad.setter
    def flexibilidad(self, mejora):
        if mejora < MINIMO_ATRIBUTO_DEPORTISTA:
            self._flexibilidad = MINIMO_ATRIBUTO_DEPORTISTA
        elif mejora > MAXIMO_ATRIBUTO_DEPORTISTA:
            self._flexibilidad = MAXIMO_ATRIBUTO_DEPORTISTA
        else:
            self._flexibilidad = mejora

    @property
    def moral(self):
        return self._moral

    @moral.setter
    def moral(self, mejora):
        if mejora < MINIMO_ATRIBUTO_DEPORTISTA:
            self._moral = MINIMO_ATRIBUTO_DEPORTISTA
        elif mejora > MAXIMO_ATRIBUTO_DEPORTISTA:
            self._moral = MAXIMO_ATRIBUTO_DEPORTISTA
        else:
            self._moral = mejora

    def entrenar(self, atributo, ponderador):
        if atributo == 0:
            if self.velocidad == MAXIMO_ATRIBUTO_DEPORTISTA:
                print("Este atributo ya esta al maximo")
            else:
                if ponderador:
                    self.velocidad += (PUNTOS_ENTRENAMIENTO * PONDERADOR_ENTRENAMIENTO_IEEE)
                else:
                    self.velocidad += PUNTOS_ENTRENAMIENTO
        elif atributo == 1:
            if self.resistencia == MAXIMO_ATRIBUTO_DEPORTISTA:
                print("Este atributo ya esta al maximo")
            else:
                if ponderador:
                    self.resistencia += (PUNTOS_ENTRENAMIENTO * PONDERADOR_ENTRENAMIENTO_IEEE)
                else:
                    self.resisitencia += PUNTOS_ENTRENAMIENTO
        elif atributo == 2:
            if self.flexibilidad == MAXIMO_ATRIBUTO_DEPORTISTA:
                print("Este atributo ya esta al maximo")
            else:
                if ponderador:
                    self.flexibilidad += (PUNTOS_ENTRENAMIENTO * PONDERADOR_ENTRENAMIENTO_IEEE)
                else:
                    self.flexibilidad += PUNTOS_ENTRENAMIENTO

    def lesionarse(self):
        self.lesionado = True


if __name__ == "__main__":
    pass
