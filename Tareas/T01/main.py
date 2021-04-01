from menus import Menu
from campeonato import Campeonato
from delegaciones import IEEEsparta, DCCrotona
from entrenadores import Usuario, Oponente
from archivosExternos import cargar_delegaciones, cargar_deportistas


jugar_partida = True
menu_inicio = True
menu_principal = True

menu = Menu()

while jugar_partida:
    while menu_inicio:
        # INICIAR PARTIDA
        menu_inicio = menu.inicio(menu_inicio)

    # DEFINIR PARTIDA
    menu_principal = True
    campeonato = Campeonato()
    menu.campeonato = campeonato

    lista_deportistas = cargar_deportistas("deportistas.csv")
    menu.lista_deportistas = lista_deportistas

    for delegacion in cargar_delegaciones("delegaciones.csv"):
        if delegacion["Delegacion"] == "IEEEsparta":
            iee_esparta = IEEEsparta(delegacion["Delegacion"], delegacion["Equipo"],
                                     delegacion["Medallas"], delegacion["Moral"],
                                     delegacion["Dinero"])
            iee_esparta.equipo_inicial(lista_deportistas)
        elif delegacion["Delegacion"] == "DCCrotona":
            dcc_rotona = DCCrotona(delegacion["Delegacion"], delegacion["Equipo"],
                                   delegacion["Medallas"], delegacion["Moral"],
                                   delegacion["Dinero"])
            dcc_rotona.equipo_inicial(lista_deportistas)
    campeonato.delegaciones = [iee_esparta, dcc_rotona]

    jugador = Usuario()
    menu.usuario = jugador
    oponente = Oponente()

    print("Escoja su apodo")
    jugador.elegir_apodo()
    print(f"\nBienvenido {jugador.apodo} a DCCumbre Olimpica!!")

    if jugador.elegir_delegacion(iee_esparta, dcc_rotona) == 0:
        iee_esparta.entrenador = jugador
        dcc_rotona.entrenador = oponente
        oponente.delegacion = dcc_rotona
        print(f"\nIEEEsparta ha presentado a su nuevo entrenador, {jugador.apodo}\n")
    else:
        iee_esparta.entrenador = oponente
        dcc_rotona.entrenador = jugador
        oponente.delegacion = iee_esparta
        print(f"\nDCCrotona ha presentado a su nuevo entrenador, {jugador.apodo}\n")

    print("Escoja el nombre de su oponente")
    oponente.elegir_apodo()

    while menu_principal:
        menu_principal, menu_inicio = menu.principal()
