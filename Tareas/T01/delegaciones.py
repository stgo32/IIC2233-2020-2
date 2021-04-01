from abc import ABC, abstractmethod
from random import uniform, choice
from parametros import (
            MINIMO_MORAL,
            MAXIMO_MORAL,
            MINIMO_DINERO,
            MINIMO_EXCELENCIA_RESPETO_IEEE,
            MAXIMO_EXCELENCIA_RESPETO_IEEE,
            MINIMO_EXCELENCIA_RESPETO_DCC,
            MAXIMO_EXCELENCIA_RESPETO_DCC,
            MINIMO_IMPLEMENTOS_DEP_IEEE,
            MAXIMO_IMPLEMENTOS_DEP_IEEE,
            MINIMO_IMPLEMENTOS_DEP_DCC,
            MAXIMO_IMPLEMENTOS_DEP_DCC,
            MINIMO_IMPLEMENTOS_MED_IEEE,
            MAXIMO_IMPLEMENTOS_MED_IEEE,
            MINIMO_IMPLEMENTOS_MED_DCC,
            MAXIMO_IMPLEMENTOS_MED_DCC,
            COSTO_ENTRENAR_DEPORTISTA,
            COSTO_COMPRAR_TECNOLOGIA,
            COSTO_SANAR_DEPORTISTA,
            PONDERADOR_COMPRAR_TECNOLOGIA,
            SUMADOR_EXCELENCIA_RESPETO,
            MAXIMO_ATRIBUTO_DEPORTISTA,
            BONIFICACION_MORAL,
            BONIFICACION_DINERO,
            CONT_HABILIDAD_ESP,
            COSTO_HAB_ESP
        )

# LAS DELEGACIONES NO TIENEN UN METODO competir() POR AHORA


class Delegacion(ABC):

    def __init__(self, nombre, equipo, medallas, moral, dinero):
        self.nombre = nombre
        self.entrenador = None  # instancia entrenador
        self.equipo = equipo  # list, instancias de deportistas
        self.cont_hab_esp = CONT_HABILIDAD_ESP
        self.__medallas = medallas  # int, property
        self.__moral = moral  # float, property
        self.__dinero = dinero  # int, property
        # floats entre 0 y 1, properties
        self._excelencia_respeto = None
        self._implementos_medicos = None
        self._implementos_deportivos = None

    """ Properties para todas las delegaciones """
    # promedio de las morales del equipo
    @property
    def moral(self):
        if MINIMO_MORAL > self.__moral:
            self.__moral = MINIMO_MORAL
        elif MAXIMO_MORAL < self.__moral:
            self.__moral = MAXIMO_MORAL
        return self.__moral

    @moral.setter
    def moral(self, cantidad):
        if MINIMO_MORAL > self.__moral:
            self.__moral = MINIMO_MORAL
        elif MAXIMO_MORAL < self.__moral:
            self.__moral = MAXIMO_MORAL
        self.__moral = cantidad

    @property
    def dinero(self):
        if self.__dinero < MINIMO_DINERO:
            self.__dinero = MINIMO_DINERO
        return self.__dinero

    @dinero.setter
    def dinero(self, cantidad_de_dinero):
        if cantidad_de_dinero < MINIMO_DINERO:
            self.__dinero = MINIMO_DINERO
        else:
            self.__dinero = cantidad_de_dinero

    @property
    def medallas(self):
        return self.__medallas

    # recibe medallas, cada vez aumenta excelencia_respeto en 0.01
    @medallas.setter
    def medallas(self, cantidad_de_medallas):
        if cantidad_de_medallas >= 0:
            self.excelencia_respeto += SUMADOR_EXCELENCIA_RESPETO
            self.__medallas = cantidad_de_medallas

    """ Properties abstractas de las delegaciones """
    # numero random, depende del tipo de delegacion
    @property
    @abstractmethod
    def excelencia_respeto(self):
        pass

    # numero random, depende del tipo de delegacion
    @property
    @abstractmethod
    def implementos_deportivos(self):
        pass

    # numero random, depende del tipo de delegacion
    @property
    @abstractmethod
    def implementos_medicos(self):
        pass

    """ Metodos abstractos de las delegaciones """
    # entrena un deportista del equipo
    @abstractmethod
    def entrenar_deportista(self):
        pass

    @abstractmethod
    def sanar_deportista(self):
        pass

    # habilidad especial, depende del tipo de delegacion
    @abstractmethod
    def habilidad_especial(self):
        pass

    """ Metodos para todas las delegaciones """
    def equipo_inicial(self, deportistas):
        equipo_dep = []
        for nombre in self.equipo:
            for deportista in deportistas:
                if deportista.nombre == nombre:
                    dep = deportistas.pop(deportistas.index(deportista))
                    equipo_dep.append(dep)
        self.equipo = equipo_dep

    # ficha un nuevo deportista y lo agrega al equipo
    def fichar_deportista(self, dep, deportistas):
        deportista = deportistas[dep]
        self.equipo.append(deportista)
        self.dinero -= deportista.precio
        deportistas = deportistas.pop(dep)

    # compra tec para mejorar los implementos dep y med
    def comprar_tecnologia(self):
        if self.dinero < COSTO_COMPRAR_TECNOLOGIA:
            print("No tienes suficiente dinero")
        else:
            print("Haz comprado tecnologia para tu equipo")
            print(f"Tus implementos medicos pasaron de {round(self.implementos_medicos, 2)} a "
                  f"{round(self.implementos_medicos * PONDERADOR_COMPRAR_TECNOLOGIA, 2)}")
            print(f"Tus implementos deportivos pasaron de {round(self.implementos_deportivos, 2)} a"
                  f" {round(self.implementos_deportivos * PONDERADOR_COMPRAR_TECNOLOGIA, 2)}")
            self.implementos_medicos *= PONDERADOR_COMPRAR_TECNOLOGIA
            self.implementos_deportivos *= PONDERADOR_COMPRAR_TECNOLOGIA
            self.dinero -= COSTO_COMPRAR_TECNOLOGIA


class IEEEsparta(Delegacion):

    def __init__(self, nombre, equipo, medallas, moral, dinero):
        super().__init__(nombre, equipo, medallas, moral, dinero)
        self._excelencia_respeto = uniform(MINIMO_EXCELENCIA_RESPETO_IEEE,
                                           MAXIMO_EXCELENCIA_RESPETO_IEEE)
        self._implementos_deportivos = uniform(MINIMO_IMPLEMENTOS_DEP_IEEE,
                                               MAXIMO_IMPLEMENTOS_DEP_IEEE)
        self._implementos_medicos = uniform(MINIMO_IMPLEMENTOS_MED_IEEE,
                                            MAXIMO_IMPLEMENTOS_MED_IEEE)

    # float random entre 0.4 y 0.8
    @property
    def excelencia_respeto(self):
        return self._excelencia_respeto

    @excelencia_respeto.setter
    def excelencia_respeto(self, cantidad):
        if cantidad < MINIMO_EXCELENCIA_RESPETO_IEEE:
            self._excelencia_respeto = MINIMO_EXCELENCIA_RESPETO_IEEE
        elif cantidad > MAXIMO_EXCELENCIA_RESPETO_IEEE:
            self._excelencia_respeto = MAXIMO_EXCELENCIA_RESPETO_IEEE
        else:
            self._excelencia_respeto = cantidad

    # float random entre 0.3 y 0.7
    @property
    def implementos_deportivos(self):
        return self._implementos_deportivos

    @implementos_deportivos.setter
    def implementos_deportivos(self, cantidad):
        if cantidad < MINIMO_IMPLEMENTOS_DEP_IEEE:
            self._implementos_deportivos = MINIMO_IMPLEMENTOS_DEP_IEEE
        elif cantidad > MAXIMO_IMPLEMENTOS_DEP_IEEE:
            self._implementos_deportivos = MAXIMO_IMPLEMENTOS_DEP_IEEE
        else:
            self._implementos_deportivos = cantidad

    # float random entre 0.2 y 0.6
    @property
    def implementos_medicos(self):
        return self._implementos_medicos

    @implementos_medicos.setter
    def implementos_medicos(self, cantidad):
        if cantidad < MINIMO_IMPLEMENTOS_MED_IEEE:
            self._implementos_medicos = MINIMO_IMPLEMENTOS_MED_IEEE
        elif cantidad > MAXIMO_IMPLEMENTOS_MED_IEEE:
            self._implementos_medicos = MAXIMO_IMPLEMENTOS_MED_IEEE
        else:
            self._implementos_medicos = cantidad

    # sube al maximo la moral del equipo
    def habilidad_especial(self, campeonato):
        self.dinero -= COSTO_HAB_ESP
        for i in range(len(self.equipo)):
            self.equipo[i].moral = MAXIMO_ATRIBUTO_DEPORTISTA
        print("\nIEEEsparta ha realizado un GRITO DE GUERRA!!!\nHan mejorado su moral al maximo")
        self.cont_hab_esp -= 1
        return campeonato

    # entrena deportista segun formula, se pondera por 1.7
    def entrenar_deportista(self, deportista, atributo):
        deportista = self.equipo[deportista]
        deportista.entrenar(atributo, True)
        self.dinero -= COSTO_ENTRENAR_DEPORTISTA
        if atributo == 0:
            atributo = "velocidad"
            print(f"{deportista.nombre} ha entrenado {atributo}, ahora es {deportista.velocidad}")
        elif atributo == 1:
            atributo = "resistencia"
            print(f"{deportista.nombre} ha entrenado {atributo}, ahora es {deportista.resistencia}")
        elif atributo == 2:
            atributo = "flexibilidad"
            print(f"{deportista.nombre} ha entrenado {atributo}, ahora es {deportista.flexibilidad}"
                  )

    # sana lesiones de algun deportista del equipo
    def sanar_deportista(self, deportista):
        condicion = deportista.moral * (self.implementos_medicos + self.excelencia_respeto)
        probabilidad = round(min(1, max(0, condicion / 200)), 1)
        oportunidad = uniform(0, 1)
        if oportunidad <= probabilidad:
            deportista.lesionado = False
            print(f"{deportista.nombre} ha sido sanado")
        else:
            print(f"Lamentablemente tomara mas tiempo que {deportista.nombre} se mejore")
        self.dinero -= COSTO_SANAR_DEPORTISTA


class DCCrotona(Delegacion):

    def __init__(self, nombre, equipo, medallas, moral, dinero):
        super().__init__(nombre, equipo, medallas, moral, dinero)
        self._excelencia_respeto = uniform(MINIMO_EXCELENCIA_RESPETO_DCC,
                                           MAXIMO_EXCELENCIA_RESPETO_DCC)
        self._implementos_deportivos = uniform(MINIMO_IMPLEMENTOS_DEP_DCC,
                                               MAXIMO_IMPLEMENTOS_DEP_DCC)
        self._implementos_medicos = uniform(MINIMO_IMPLEMENTOS_MED_DCC,
                                            MAXIMO_IMPLEMENTOS_MED_DCC)

    # float random entre 0.3 y 0.7
    @property
    def excelencia_respeto(self):
        return self._excelencia_respeto

    @excelencia_respeto.setter
    def excelencia_respeto(self, cantidad):
        if cantidad < MINIMO_EXCELENCIA_RESPETO_DCC:
            self._excelencia_respeto = MINIMO_EXCELENCIA_RESPETO_DCC
        elif cantidad > MAXIMO_EXCELENCIA_RESPETO_DCC:
            self._excelencia_respeto = MAXIMO_EXCELENCIA_RESPETO_DCC
        else:
            self._excelencia_respeto = cantidad

    # float random entre 0.2 y 0.6
    @property
    def implementos_deportivos(self):
        return self._implementos_deportivos

    @implementos_deportivos.setter
    def implementos_deportivos(self, cantidad):
        if cantidad < MINIMO_IMPLEMENTOS_DEP_DCC:
            self._implementos_deportivos = MINIMO_IMPLEMENTOS_DEP_DCC
        elif cantidad > MAXIMO_IMPLEMENTOS_DEP_DCC:
            self._implementos_deportivos = MAXIMO_IMPLEMENTOS_DEP_DCC
        else:
            self._implementos_deportivos = cantidad

    # float random entre 0.4 y 0.8
    @property
    def implementos_medicos(self):
        return self._implementos_medicos

    @implementos_medicos.setter
    def implementos_medicos(self, cantidad):
        if cantidad < MINIMO_IMPLEMENTOS_MED_DCC:
            self._implementos_medicos = MINIMO_IMPLEMENTOS_MED_DCC
        elif cantidad > MAXIMO_IMPLEMENTOS_MED_DCC:
            self._implementos_medicos = MAXIMO_IMPLEMENTOS_MED_DCC
        else:
            self._implementos_medicos = cantidad

    # medalla de forma inmediata
    def habilidad_especial(self, campeonato):
        self.dinero -= COSTO_ENTRENAR_DEPORTISTA
        deportista = choice(self.equipo)
        deportista.moral += BONIFICACION_MORAL * 2
        self.dinero += BONIFICACION_DINERO
        self.medallas += 1
        campeonato.medallero[self.nombre]["Atletismo"] += 1
        self.equipo[self.equipo.index(deportista)] = deportista
        print("\nDCCrotona es muy popular, ha recibido una MEDALLA DE FORMA INMEDIATA!!")
        self.cont_hab_esp -= 1
        return campeonato

    # entrena deportista segun formula
    def entrenar_deportista(self, deportista, atributo):
        deportista = self.equipo[deportista]
        deportista.entrenar(atributo, False)
        self.dinero -= COSTO_ENTRENAR_DEPORTISTA
        if atributo == 0:
            atributo = "velocidad"
            print(f"{deportista.nombre} ha entrenado {atributo}, ahora es {deportista.velocidad}")
        elif atributo == 1:
            atributo = "resistencia"
            print(f"{deportista.nombre} ha entrenado {atributo}, ahora es {deportista.resistencia}")
        elif atributo == 2:
            atributo = "flexibilidad"
            print(f"{deportista.nombre} ha entrenado {atributo}, ahora es {deportista.flexibilidad}"
                  )

    # sana lesiones de algun deportista del equipo
    def sanar_deportista(self, deportista):
        condicion = deportista.moral * (self.implementos_medicos + self.excelencia_respeto)
        probabilidad = round(min(1, max(0, condicion / 200)), 1)
        oportunidad = uniform(0, 1)
        if oportunidad <= probabilidad:
            deportista.lesionado = False
            print(f"{deportista.nombre} ha sido sanado")
        else:
            print(f"Lamentablemente tomara mas tiempo que {deportista.nombre} se mejore")
        self.dinero -= 2 * COSTO_SANAR_DEPORTISTA
