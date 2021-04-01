from os import path

# posiciones base
ALTO_ZONA_ESTCA = 150
BORDE_IZQUIERDA = 5
BORDE_INFERIOR = 10
MIN_WIDTH_TIENDA = 250
MAX_WIDTH_BARRA = 250
MAX_WIDTH_COMBO = 250
MAX_WIDTH_BOTON_RANKING = 200
SET_GEO_BOTON_RANKING = (120, 460, 200, 30)
SET_GEO_LABEL_PERDIDA = (30, 410, 400, 40)
MAX_WIDTH_BOTON_RESUMEN = 250
MIN_WIDTH_BOTON_RESUMEN = 200
SET_GEO_BOTON_RESUMEN = (120, 460, 150, 30)
MIN_SIZE_INICIO = (500, 500)
MIN_SIZE_RANKING = (500, 500)
MIN_SIZE_JUEGO = (1600, 900)
MIN_SIZE_RESUMEN = (500, 500)
PUFFLE_SET_GEO = (170, 250, 150, 120)

# prbabilidad de flechas
PROB_FLECHA_NORMAL = 0.75
PROB_FLECHA_X2 = 0.15
PROB_FLECHA_DORADA = 0.05
PROB_FLECHA_HIELO = 0.05

# probabilidad de pasos
PROB_PASO_SIMPLE = 0.7
PROB_PASO_DOBLE_AFICIONADO = 0.3
PROB_PASO_DOBLE_MAESTRO = 0.25
PROB_PASO_TRIPLE = 0.05

# tamaños de imagenes
LOGO_SIZE = (429, 433)
FONDO_SIZE = (2301, 2357)
MAX_TAMANO_FLECHA = 70

# tiempos dificultades
GENERADOR_PASOS_PRINCIPIANTE = 1000
DURACION_PRINCIPIANTE = 30
GENERADOR_PASOS_AFICIONADO = 750
DURACION_AFICIONADO = 45
GENERADOR_PASOS_MAESTRO = 500
DURACION_MAESTRO = 60

# velocidades flechas
VELOCIDAD_FLECHA = 17

# puntajes
PUNTOS_FLECHA = 10
PUNTAJES_A_MOSTRAR = 5
CANTIDAD_PUNTAJES_RANKING = 5
FACTOR_FLECHAS_X2 = 2
FACTOR_FLECHAS_DORADAS = 10

# aprobacion
APROBACION_PRINCIPIANTE = 30
APROBACION_AFICIONADO = 50
APROBACION_MAESTRO = 70
MINIMO_APROBACION = 0

# dinero
MINIMO_DINERO = 0
PRECIO_PINGUIRIN = 500
DINERO_INICIAL = 700
DINERO_TRAMPA = 1000000

# key de teclas
FLECHA_IZQUIERDA = 65
FLECHA_ARRIBA = 87
FLECHA_ABAJO = 83
FLECHA_DERECHA = 68

# rutas
RUTA_RANKING = path.join('ranking.txt')
RUTA_LOGO = path.join('sprites', 'logo.png')
RUTA_FONDO = path.join('sprites', 'fondos', 'fondo.png')

RUTA_FLECHA_RITMO_LEFT = path.join('sprites', 'flechas', 'left_7.png')
RUTA_FLECHA_RITMO_UP = path.join('sprites', 'flechas', 'up_7.png')
RUTA_FLECHA_RITMO_DOWN = path.join('sprites', 'flechas', 'down_7.png')
RUTA_FLECHA_RITMO_RIGHT = path.join('sprites', 'flechas', 'right_7.png')

RUTA_FLECHA_NORMAL_LEFT = path.join('sprites', 'flechas', 'left_1.png')
RUTA_FLECHA_NORMAL_UP = path.join('sprites', 'flechas', 'up_1.png')
RUTA_FLECHA_NORMAL_DOWN = path.join('sprites', 'flechas', 'down_1.png')
RUTA_FLECHA_NORMAL_RIGHT = path.join('sprites', 'flechas', 'right_1.png')

RUTA_FLECHA_X2_LEFT = path.join('sprites', 'flechas', 'left_4.png')
RUTA_FLECHA_X2_UP = path.join('sprites', 'flechas', 'up_4.png')
RUTA_FLECHA_X2_DOWN = path.join('sprites', 'flechas', 'down_4.png')
RUTA_FLECHA_X2_RIGHT = path.join('sprites', 'flechas', 'right_4.png')

RUTA_FLECHA_DORADA_LEFT = path.join('sprites', 'flechas', 'left_2.png')
RUTA_FLECHA_DORADA_UP = path.join('sprites', 'flechas', 'up_2.png')
RUTA_FLECHA_DORADA_DOWN = path.join('sprites', 'flechas', 'down_2.png')
RUTA_FLECHA_DORADA_RIGHT = path.join('sprites', 'flechas', 'right_2.png')

RUTA_FLECHA_HIELO_LEFT = path.join('sprites', 'flechas', 'left_8.png')
RUTA_FLECHA_HIELO_UP = path.join('sprites', 'flechas', 'up_8.png')
RUTA_FLECHA_HIELO_DOWN = path.join('sprites', 'flechas', 'down_8.png')
RUTA_FLECHA_HIELO_RIGHT = path.join('sprites', 'flechas', 'right_8.png')

TIPOS_FLECHAS = {
    'normal': [RUTA_FLECHA_NORMAL_LEFT, RUTA_FLECHA_NORMAL_UP, RUTA_FLECHA_NORMAL_DOWN,
               RUTA_FLECHA_NORMAL_RIGHT],
    'x2': [RUTA_FLECHA_X2_LEFT, RUTA_FLECHA_X2_UP, RUTA_FLECHA_X2_DOWN, RUTA_FLECHA_X2_RIGHT],
    'dorada': [RUTA_FLECHA_DORADA_LEFT, RUTA_FLECHA_DORADA_UP, RUTA_FLECHA_DORADA_DOWN,
               RUTA_FLECHA_DORADA_RIGHT],
    'hielo': [RUTA_FLECHA_HIELO_LEFT, RUTA_FLECHA_HIELO_UP, RUTA_FLECHA_HIELO_DOWN,
              RUTA_FLECHA_HIELO_RIGHT]
}

RUTA_CANCION_1 = path.join('songs', 'cancion_1.wav')
RUTA_CANCION_2 = path.join('songs', 'cancion_2.wav')

# amarillo
RUTA_AMARILLO_D_R = path.join('sprites', 'pinguirin_amarillo', 'amarillo_abajo_derecha.png')
RUTA_AMARILLO_D_L = path.join('sprites', 'pinguirin_amarillo', 'amarillo_abajo_izquierda.png')
RUTA_AMARILLO_D = path.join('sprites', 'pinguirin_amarillo', 'amarillo_abajo.png')
RUTA_AMARILLO_U_R = path.join('sprites', 'pinguirin_amarillo', 'amarillo_arriba_derecha.png')
RUTA_AMARILLO_U_L = path.join('sprites', 'pinguirin_amarillo', 'amarillo_arriba_izquierda.png')
RUTA_AMARILLO_U = path.join('sprites', 'pinguirin_amarillo', 'amarillo_arriba.png')
RUTA_AMARILLO_4 = path.join('sprites', 'pinguirin_amarillo', 'amarillo_cuatro_flechas.png')
RUTA_AMARILLO_R = path.join('sprites', 'pinguirin_amarillo', 'amarillo_derecha.png')
RUTA_AMARILLO_L = path.join('sprites', 'pinguirin_amarillo', 'amarillo_izquierda.png')
RUTA_AMARILLO_NEUTRO = path.join('sprites', 'pinguirin_amarillo', 'amarillo_neutro.png')
RUTA_AMARILLO_3 = path.join('sprites', 'pinguirin_amarillo', 'amarillo_tres_flechas.png')

RUTAS_AMARILLO = {
    'down_right': RUTA_AMARILLO_D_R, 'down_left': RUTA_AMARILLO_D_L, 'down': RUTA_AMARILLO_D,
    'up_right': RUTA_AMARILLO_U_R, 'up_left': RUTA_AMARILLO_U_L, 'up': RUTA_AMARILLO_U,
    'cuatro': RUTA_AMARILLO_4, 'right': RUTA_AMARILLO_R, 'left': RUTA_AMARILLO_L,
    'neutro': RUTA_AMARILLO_NEUTRO, 'tres': RUTA_AMARILLO_3
}

# celeste
RUTA_CELESTE_D_R = path.join('sprites', 'pinguirin_celeste', 'celeste_abajo_derecha.png')
RUTA_CELESTE_D_L = path.join('sprites', 'pinguirin_celeste', 'celeste_abajo_izquierda.png')
RUTA_CELESTE_D = path.join('sprites', 'pinguirin_celeste', 'celeste_abajo.png')
RUTA_CELESTE_U_R = path.join('sprites', 'pinguirin_celeste', 'celeste_arriba_derecha.png')
RUTA_CELESTE_U_L = path.join('sprites', 'pinguirin_celeste', 'celeste_arriba_izquierda.png')
RUTA_CELESTE_U = path.join('sprites', 'pinguirin_celeste', 'celeste_arriba.png')
RUTA_CELESTE_4 = path.join('sprites', 'pinguirin_celeste', 'celeste_cuatro_flechas.png')
RUTA_CELESTE_R = path.join('sprites', 'pinguirin_celeste', 'celeste_derecha.png')
RUTA_CELESTE_L = path.join('sprites', 'pinguirin_celeste', 'celeste_izquierda.png')
RUTA_CELESTE_NEUTRO = path.join('sprites', 'pinguirin_celeste', 'celeste_neutro.png')
RUTA_CELESTE_3 = path.join('sprites', 'pinguirin_celeste', 'celeste_tres_flechas.png')

RUTAS_CELESTE = {
    'down_right': RUTA_CELESTE_D_R, 'down_left': RUTA_CELESTE_D_L, 'down': RUTA_CELESTE_D,
    'up_right': RUTA_CELESTE_U_R, 'up_left': RUTA_CELESTE_U_L, 'up': RUTA_CELESTE_U,
    'cuatro': RUTA_CELESTE_4, 'right': RUTA_CELESTE_R, 'left': RUTA_CELESTE_L,
    'neutro': RUTA_CELESTE_NEUTRO, 'tres': RUTA_CELESTE_3
}

# morado
RUTA_MORADO_D_R = path.join('sprites', 'pinguirin_morado', 'morado_abajo_derecha.png')
RUTA_MORADO_D_L = path.join('sprites', 'pinguirin_morado', 'morado_abajo_izquierda.png')
RUTA_MORADO_D = path.join('sprites', 'pinguirin_morado', 'morado_abajo.png')
RUTA_MORADO_U_R = path.join('sprites', 'pinguirin_morado', 'morado_arriba_derecha.png')
RUTA_MORADO_U_L = path.join('sprites', 'pinguirin_morado', 'morado_arriba_izquierda.png')
RUTA_MORADO_U = path.join('sprites', 'pinguirin_morado', 'morado_arriba.png')
RUTA_MORADO_4 = path.join('sprites', 'pinguirin_morado', 'morado_cuatro_flechas.png')
RUTA_MORADO_R = path.join('sprites', 'pinguirin_morado', 'morado_derecha.png')
RUTA_MORADO_L = path.join('sprites', 'pinguirin_morado', 'morado_izquierda.png')
RUTA_MORADO_NEUTRO = path.join('sprites', 'pinguirin_morado', 'morado_neutro.png')
RUTA_MORADO_3 = path.join('sprites', 'pinguirin_morado', 'morado_tres_flechas.png')

RUTAS_MORADO = {
    'down_right': RUTA_MORADO_D_R, 'down_left': RUTA_MORADO_D_L, 'down': RUTA_MORADO_D,
    'up_right': RUTA_MORADO_U_R, 'up_left': RUTA_MORADO_U_L, 'up': RUTA_MORADO_U,
    'cuatro': RUTA_MORADO_4, 'right': RUTA_MORADO_R, 'left': RUTA_MORADO_L,
    'neutro': RUTA_MORADO_NEUTRO, 'tres': RUTA_MORADO_3
}

# rojo
RUTA_ROJO_D_R = path.join('sprites', 'pinguirin_rojo', 'rojo_abajo_derecha.png')
RUTA_ROJO_D_L = path.join('sprites', 'pinguirin_rojo', 'rojo_abajo_izquierda.png')
RUTA_ROJO_D = path.join('sprites', 'pinguirin_rojo', 'rojo_abajo.png')
RUTA_ROJO_U_R = path.join('sprites', 'pinguirin_rojo', 'rojo_arriba_derecha.png')
RUTA_ROJO_U_L = path.join('sprites', 'pinguirin_rojo', 'rojo_arriba_izquierda.png')
RUTA_ROJO_U = path.join('sprites', 'pinguirin_rojo', 'rojo_arriba.png')
RUTA_ROJO_4 = path.join('sprites', 'pinguirin_rojo', 'rojo_cuatro_flechas.png')
RUTA_ROJO_R = path.join('sprites', 'pinguirin_rojo', 'rojo_derecha.png')
RUTA_ROJO_L = path.join('sprites', 'pinguirin_rojo', 'rojo_izquierda.png')
RUTA_ROJO_NEUTRO = path.join('sprites', 'pinguirin_rojo', 'rojo_neutro.png')
RUTA_ROJO_3 = path.join('sprites', 'pinguirin_rojo', 'rojo_tres_flechas.png')

RUTAS_ROJO = {
    'down_right': RUTA_ROJO_D_R, 'down_left': RUTA_ROJO_D_L, 'down': RUTA_ROJO_D,
    'up_right': RUTA_ROJO_U_R, 'up_left': RUTA_ROJO_U_L, 'up': RUTA_ROJO_U,
    'cuatro': RUTA_ROJO_4, 'right': RUTA_ROJO_R, 'left': RUTA_ROJO_L,
    'neutro': RUTA_ROJO_NEUTRO, 'tres': RUTA_ROJO_3
}

# verde
RUTA_VERDE_D_R = path.join('sprites', 'pinguirin_verde', 'verde_abajo_derecha.png')
RUTA_VERDE_D_L = path.join('sprites', 'pinguirin_verde', 'verde_abajo_izquierda.png')
RUTA_VERDE_D = path.join('sprites', 'pinguirin_verde', 'verde_abajo.png')
RUTA_VERDE_U_R = path.join('sprites', 'pinguirin_verde', 'verde_arriba_derecha.png')
RUTA_VERDE_U_L = path.join('sprites', 'pinguirin_verde', 'verde_arriba_izquierda.png')
RUTA_VERDE_U = path.join('sprites', 'pinguirin_verde', 'verde_arriba.png')
RUTA_VERDE_4 = path.join('sprites', 'pinguirin_verde', 'verde_cuatro_flechas.png')
RUTA_VERDE_R = path.join('sprites', 'pinguirin_verde', 'verde_derecha.png')
RUTA_VERDE_L = path.join('sprites', 'pinguirin_verde', 'verde_izquierda.png')
RUTA_VERDE_NEUTRO = path.join('sprites', 'pinguirin_verde', 'verde_neutro.png')
RUTA_VERDE_3 = path.join('sprites', 'pinguirin_verde', 'verde_tres_flechas.png')

RUTAS_VERDE = {
    'down_right': RUTA_VERDE_D_R, 'down_left': RUTA_VERDE_D_L, 'down': RUTA_VERDE_D,
    'up_right': RUTA_VERDE_U_R, 'up_left': RUTA_VERDE_U_L, 'up': RUTA_VERDE_U,
    'cuatro': RUTA_VERDE_4, 'right': RUTA_VERDE_R, 'left': RUTA_VERDE_L,
    'neutro': RUTA_VERDE_NEUTRO, 'tres': RUTA_VERDE_3
}

TIPOS_PINGUIRINES = {
    'amarillo': RUTAS_AMARILLO,
    'celeste': RUTAS_CELESTE,
    'morado': RUTAS_MORADO,
    'rojo': RUTAS_ROJO,
    'verde': RUTAS_VERDE
}

RUTA_PUFFLE_CANGREJO = path.join('sprites', 'puffles', 'puffle_02.png')
RUTA_PUFFLE_CELESTE = path.join('sprites', 'puffles', 'puffle_06.png')

# styles sheets
STYLE_CUADROS_FLECHA_IMPAR = 'background-color: aquamarine'
STYLE_CUADROS_FLECHA_PAR = 'background-color: darkcyan'

APP_STYLE_SHEET = '''
*{
    font-family: Segoe UI Semibold, Corbel, Verdana;
    font-weight: bold;
    color: rgb(28, 46, 46);
    text-transform: uppercase;
}
QLineEdit {
    text-transform: none
}
QPushButton {
    background-color: cadetblue;
    max-width: 240px;
    margin-left: 70px;
    min-height: 30px;
    border-radius: 15px;
    border-bottom-color: darkslategray;
    border-bottom-width: 5px;
}
QPushButton:hover {
    background-color: #AFEEEE
}
QProgressBar{
    margin-right: 30px;
    border: 2px solid darkslategray;
    min-height: 25px;
    text-align: center;
    color: rgb(28, 46, 46)
}
QProgressBar::chunk {
    background-color: cadetblue;
}
QComboBox {
    margin-right: 30px;
    border: 2px solid darkslategray;
    min-height: 25px;
    color: darkcyan;
}
#hboxZonaEstca {
    max-height: 150px
}
#hboxJuego {
    max-height: 750px
}
#labelTienda {
    font-size: 23px;
    margin-left: 50px;
    margin-top: 10px;
    min-height: 50px;
}
#labelRanking {
    font-size: 23px;
    min-height: 50px;
}
#labelResumen {
    font-size: 23px;
    min-height: 50px;
}
#_labelResumen{
    margin-left: 35px
}
#_labelPuntaje {
    margin-left: 35px
}
#_labelDinero {
    margin-left: 70px
}
'''
