from abc import ABC, abstractmethod
from random import choice, uniform
from parametros import (RIESGO_ATLETISMO,
                        RIESGO_CICLISMO,
                        RIESGO_GIMNASIA,
                        RIESGO_NATACION,
                        REQUERIMIENTO_ATLETISMO,
                        REQUERIMIENTO_CICLISMO,
                        REQUERIMIENTO_GIMNASIA,
                        REQUERIMIENTO_NATACION,
                        NIVEL_IMPLEMENTOS_COMPETENCIA,
                        PUNTAJE_MINIMO,
                        PONDERADOR_VEL_ATLETISMO,
                        PONDERADOR_RES_ATLETISMO,
                        PONDERADOR_MORAL_ATLETISMO,
                        PONDERADOR_VEL_CICLISMO,
                        PONDERADOR_RES_CICLISMO,
                        PONDERADOR_FLEX_CICLISMO,
                        PONDERADOR_FLEX_GIMNASIA,
                        PONDERADOR_RES_GIMNASIA,
                        PONDERADOR_MORAL_GIMNASIA,
                        PONDERADOR_VEL_NATACION,
                        PONDERADOR_RES_NATACION,
                        PONDERADOR_FLEX_NATACION)


class Deporte(ABC):

    @abstractmethod
    def validez_competencia(self):
        pass

    @abstractmethod
    def calcular_ganador(self):
        pass


class Atletismo(Deporte):

    def __init__(self):
        self.implementos = REQUERIMIENTO_ATLETISMO
        self.riesgo = RIESGO_ATLETISMO

    def validez_competencia(self, delegaciones, depor_usuario):
        condiciones_usuario = True
        condiciones_oponente = True
        depor_usuario_correcto = False
        depor_oponente_correcto = False
        depor_oponente = None
        op_lesion = uniform(0, 1)
        if op_lesion < self.riesgo:
            depor_usuario.lesionarse()
        for delegacion in delegaciones:
            if type(delegacion.entrenador).__name__ == "Usuario":
                if depor_usuario.lesionado is False:
                    depor_usuario_correcto = True
            else:
                depor_oponente = choice(delegacion.equipo)
                op_lesion = uniform(0, 1)
                if op_lesion < self.riesgo:
                    depor_usuario.lesionarse()
                if depor_oponente.lesionado is False:
                    depor_oponente_correcto = True
        validez_usuario = False
        if depor_usuario_correcto and condiciones_usuario:
            validez_usuario = True
        validez_oponente = False
        if depor_oponente_correcto and condiciones_oponente:
            validez_oponente = True
        return validez_usuario, validez_oponente, depor_oponente

    def calcular_ganador(self, depor_usuario, depor_oponente):
        punt_usuario = (PONDERADOR_VEL_ATLETISMO * depor_usuario.velocidad +
                        PONDERADOR_RES_ATLETISMO * depor_usuario.resistencia +
                        PONDERADOR_MORAL_ATLETISMO * depor_usuario.moral)
        puntaje_usuario = max(PUNTAJE_MINIMO, punt_usuario)
        punt_oponente = (PONDERADOR_VEL_ATLETISMO * depor_oponente.velocidad +
                         PONDERADOR_RES_ATLETISMO * depor_oponente.resistencia +
                         PONDERADOR_MORAL_ATLETISMO * depor_oponente.moral)
        puntaje_oponente = max(PUNTAJE_MINIMO, punt_oponente)
        if puntaje_usuario > puntaje_oponente:
            return depor_usuario
        else:
            return depor_oponente


class Ciclismo(Deporte):

    def __init__(self):
        self.implementos = REQUERIMIENTO_CICLISMO
        self.riesgo = RIESGO_CICLISMO

    def validez_competencia(self, delegaciones, depor_usuario):
        condiciones_usuario = False
        condiciones_oponente = False
        depor_usuario_correcto = False
        depor_oponente_correcto = False
        depor_oponente = None
        op_lesion = uniform(0, 1)
        if op_lesion < self.riesgo:
            depor_usuario.lesionado = True
        for delegacion in delegaciones:
            if type(delegacion.entrenador).__name__ == "Usuario":
                if depor_usuario.lesionado is False:
                    depor_usuario_correcto = True
                if (
                    delegacion.implementos_deportivos > NIVEL_IMPLEMENTOS_COMPETENCIA and
                    delegacion.implementos_medicos > NIVEL_IMPLEMENTOS_COMPETENCIA
                        ):
                    condiciones_usuario = True
            else:
                depor_oponente = choice(delegacion.equipo)
                op_lesion = uniform(0, 1)
                if op_lesion < self.riesgo:
                    depor_oponente.lesionado = True
                if depor_oponente.lesionado is False:
                    depor_oponente_correcto = True
                if (
                    delegacion.implementos_deportivos > NIVEL_IMPLEMENTOS_COMPETENCIA and
                    delegacion.implementos_medicos > NIVEL_IMPLEMENTOS_COMPETENCIA
                        ):
                    condiciones_oponente = True
        validez_usuario = False
        if depor_usuario_correcto and condiciones_usuario:
            validez_usuario = True
        validez_oponente = False
        if depor_oponente_correcto and condiciones_oponente:
            validez_oponente = True
        return validez_usuario, validez_oponente, depor_oponente

    def calcular_ganador(self, depor_usuario, depor_oponente):
        punt_usuario = (PONDERADOR_VEL_CICLISMO * depor_usuario.velocidad +
                        PONDERADOR_RES_CICLISMO * depor_usuario.resistencia +
                        PONDERADOR_FLEX_CICLISMO * depor_usuario.flexibilidad)
        puntaje_usuario = max(PUNTAJE_MINIMO, punt_usuario)
        punt_oponente = (PONDERADOR_VEL_CICLISMO * depor_oponente.velocidad +
                         PONDERADOR_RES_CICLISMO * depor_oponente.resistencia +
                         PONDERADOR_FLEX_CICLISMO * depor_oponente.flexibilidad)
        puntaje_oponente = max(PUNTAJE_MINIMO, punt_oponente)
        if puntaje_usuario > puntaje_oponente:
            return depor_usuario
        else:
            return depor_oponente


class Gimnasia(Deporte):

    def __init__(self):
        self.implementos = REQUERIMIENTO_GIMNASIA
        self.riesgo = RIESGO_GIMNASIA

    def validez_competencia(self, delegaciones, depor_usuario):
        condiciones_usuario = False
        condiciones_oponente = False
        depor_usuario_correcto = False
        depor_oponente_correcto = False
        depor_oponente = None
        op_lesion = uniform(0, 1)
        if op_lesion < self.riesgo:
            depor_usuario.lesionarse()
        for delegacion in delegaciones:
            if type(delegacion.entrenador).__name__ == "Usuario":
                if depor_usuario.lesionado is False:
                    depor_usuario_correcto = True
                if (
                    delegacion.implementos_deportivos > NIVEL_IMPLEMENTOS_COMPETENCIA and
                    delegacion.implementos_medicos > NIVEL_IMPLEMENTOS_COMPETENCIA
                        ):
                    condiciones_usuario = True
            else:
                depor_oponente = choice(delegacion.equipo)
                op_lesion = uniform(0, 1)
                if op_lesion < self.riesgo:
                    depor_oponente.lesionarse()
                if depor_oponente.lesionado is False:
                    depor_oponente_correcto = True
                if (
                    delegacion.implementos_deportivos > NIVEL_IMPLEMENTOS_COMPETENCIA and
                    delegacion.implementos_medicos > NIVEL_IMPLEMENTOS_COMPETENCIA
                        ):
                    condiciones_oponente = True
        validez_usuario = False
        if depor_usuario_correcto and condiciones_usuario:
            validez_usuario = True
        validez_oponente = False
        if depor_oponente_correcto and condiciones_oponente:
            validez_oponente = True
        return validez_usuario, validez_oponente, depor_oponente

    def calcular_ganador(self, depor_usuario, depor_oponente):
        punt_usuario = (PONDERADOR_FLEX_GIMNASIA * depor_usuario.flexibilidad +
                        PONDERADOR_RES_GIMNASIA * depor_usuario.resistencia +
                        PONDERADOR_MORAL_GIMNASIA * depor_usuario.moral)
        puntaje_usuario = max(PUNTAJE_MINIMO, punt_usuario)
        punt_oponente = (PONDERADOR_FLEX_GIMNASIA * depor_oponente.flexibilidad +
                         PONDERADOR_RES_GIMNASIA * depor_oponente.resistencia +
                         PONDERADOR_MORAL_GIMNASIA * depor_oponente.moral)
        puntaje_oponente = max(PUNTAJE_MINIMO, punt_oponente)
        if puntaje_usuario > puntaje_oponente:
            return depor_usuario
        else:
            return depor_oponente


class Natacion(Deporte):

    def __init__(self):
        self.implementos = REQUERIMIENTO_NATACION
        self.riesgo = RIESGO_NATACION

    def validez_competencia(self, delegaciones, depor_usuario):
        condiciones_usuario = True
        condiciones_oponente = True
        depor_usuario_correcto = False
        depor_oponente_correcto = False
        depor_oponente = None
        op_lesion = uniform(0, 1)
        if op_lesion < self.riesgo:
            depor_usuario.lesionarse()
        for delegacion in delegaciones:
            if type(delegacion.entrenador).__name__ == "Usuario":
                if depor_usuario.lesionado is False:
                    depor_usuario_correcto = True
            else:
                depor_oponente = choice(delegacion.equipo)
                op_lesion = uniform(0, 1)
                if op_lesion < self.riesgo:
                    depor_oponente.lesionarse()
                if depor_oponente.lesionado is False:
                    depor_oponente_correcto = True
        validez_usuario = False
        if depor_usuario_correcto and condiciones_usuario:
            validez_usuario = True
        validez_oponente = False
        if depor_oponente_correcto and condiciones_oponente:
            validez_oponente = True
        return validez_usuario, validez_oponente, depor_oponente

    def calcular_ganador(self, depor_usuario, depor_oponente):
        punt_usuario = (PONDERADOR_VEL_NATACION * depor_usuario.velocidad +
                        PONDERADOR_RES_NATACION * depor_usuario.resistencia +
                        PONDERADOR_FLEX_NATACION * depor_usuario.flexibilidad)
        puntaje_usuario = max(PUNTAJE_MINIMO, punt_usuario)
        punt_oponente = (PONDERADOR_VEL_NATACION * depor_oponente.velocidad +
                         PONDERADOR_RES_NATACION * depor_oponente.resistencia +
                         PONDERADOR_FLEX_NATACION * depor_oponente.flexibilidad)
        puntaje_oponente = max(PUNTAJE_MINIMO, punt_oponente)
        if puntaje_usuario > puntaje_oponente:
            return depor_usuario
        else:
            return depor_oponente
