# Tarea 03: DCColonos :rice_scene:


## Consideraciones generales :octocat:

La tarea tiene implementado un sistemas de trunos que: lanza los dados y reparte las materias primas correspondientes, permite adquerir chozas o pasar en caso de no tener suficientes materias perimas y luego con el botón de terminar turno pasar al turno siguiente. Lamentablemente, a mi parecer, una arquitectura cliente-servidor deficiente a veces produce un ```bug``` cuando se conectan 4 jugadores. Este consiste en que no se coloca la última choza inicial por lo que nunca inicia el sistema de turnos, destacar que la arquitectura cliente-servidor puede no necesariamente la causa de lo que pasa, sino que también puede ser que dado que el tablero es pequeño no quedan más espacios disponibles para la última choza por lo que el programa se frena.

### Cosas implementadas y no implementadas :white_check_mark: :x:

1. **Networking:**
    1. Protocolo: hecha completa.
    2. Correcto uso de sockets: hecha completa.
    3. Conexión: hecha completa.
    4. Manejo de clientes: se controla de buena forma la desconexión de algún cliente o del servidor, pero el sistema de turnos se ve interrumpido.
2. **Arquitectura cliente-servidor:**
    1. Roles: considero que le di muchas facultades a los clientes. Pero el flujo del juego es consistente al enunciado.
    2. Consistencia: el juego se actualiza como se pide, el único error es el ```bug``` mencionado que se produce al iniciar la partida.
    3. Logs: hecha completa.
3. **Manejo de bytes:**
    1. Codificación: no se cumple al pie de la letra el protocolo especificado en el enunciado dado que trajo problemas en la implementación de la mensajería cliente-servidor.
    2. Decodificación: no se cumple al pie de la letra el protocolo especificado en el enunciado dado que trajo problemas en la implementación de la mensajería cliente-servidor.
    3. Integración: hecha completa.
4. **Interfaz gráfica:**
    1. Integración: hecha completa.
    2. Sala de espera: no es posible avisar que la partida ya ha comenzado cuendo se conecta otro cliente.
    3. Sala de juego: no se implementan las cartas de desarrollo ni el intercambio. Todo lo demás funciona acorde al enunciado.
    4. Fin de partida: no se implementa un botón que redirija a la sala de espera.
5. **Grafo:**
    1. Archivo: hecha completa.
    2. Modelación: hecha completa
    3. Funcionalidades: no se implementan las carreteras. Es correcta la implementacón de las chozas.
6. **Reglas DCColonos:**
    1. Inicio del juego: hecha completa.
    2. Lanzamiento dados: hecha completa.
    3. Se imlpementa la adquisición de chozas y se calculan correctamente los puntos de victoria.
    4. Término del juego: hecha completa.
7. **General:**
    1. Parámetros (json): hecha completa.
    2. Grafo (json): hecha completa.
    3. Generador de mazos: no se implementa.
8. **Bonus:**
    1. Chat: se implementa un botón que despliega una ventana de chat.


## Ejecución :computer:
Para la ejecución del programa se crearon dos directorios: ```client``` y ```server```. En estos se debe ejecutar el archivo ```main.py``` independientemente, primero ejecutando el del servidor. Se pueden abrir ```MAX_JUGADORES_PARTIDA``` clientes.
Fueron entregados archivos externos para la realización de la tarea, y para su correcta ejecución estos archivos deben ubicarse en los siguientes directorios: ```grafo.json``` debe ubicarse en ```server``` y ```generador_grilla.py y sprites``` deben ubicarse en ```cliente```.

1. ```client``` directorio que contiene a:
    1. ```main.py```
    2. ```client.py```
    3. ```interfaz.py```
    4. ```parametros.py```
    5. ```parametros.json```
    6. ```interfaces_back_end```, directorio que contiene a:
        1. ```jugador.py```
        2. ```sala_de_espera.py```
        3. ```sala_de_juego.py```
        4. ```tablero.py```
    7. ```interfaces_front_end```, directorio que contiene a:
        1. ```chat.py```
        2. ```chozas.py```
        3. ```fin_de_partida.py```
        4. ```sala_de_espera.py```
        5. ```sala_de_juego```
    8. ```sprites_adicionales```, directorio que contiene sprites adicionales a los entregados.
2. ```server``` directorio que contiene a:
    1. ```main.py```
    2. ```banco.py```
    3. ```jugador.py```
    4. ```logica.py```
    5. ```parametros.py```
    6. ```parametros.json```
    7. ```server.py```
    8. ```nombres.txt```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```:  ```shuffle,  choice, randint```
2. ```json```:  ```dumps, load, loads```
3. ```threading```:  ```Thread, Lock```
4. ```os```:  ```path```
5. ```socket```:  ```socket, AF_INET, SOCK_STREAM```
6. ```sys```:  ```exit```
7. ```math```:  ```radians, cos```
8. ```PyQt5```; **debe** ser instalada
    1. ```QtWidgets```:  ```QWidget, QLabel, QPushButton, QErrorMessage, QHBoxLayout, QVBoxLayout, QApplication, QTextEdit, QLineEdit```
    2.  ```QtCore```:  ```pyqtSignal, QSize, Qt, QMimeData, QObject```
    3. ```QtGui```:  ```QPixmap, QIcon, , QDrag, QPainter```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```client```
    1. ```client.py```: Contiene a ```Cliente```, encargado de la comunicación con el servidor.
    2. ```interfaz.py```: Contiene a ```Controlador```, encargado de controlar la interfaz del juego.
    3. ```parametros.py```: Contiene a ```Parametro, cagar_parametros, hook```, encargado de cargar los parámetros en ```parametros.json```.
    4. ```parametros.json```: Objeto ```json``` que contiene parámetros que se mantienen constantes para el cliente.
    5. ```jugador.py```: Contiene a ```Jugador, Usuario```, encargado de controlar las acciones de los jugadores en la interfaz.
    6. ```sala_de_espera.py```: Contiene a ```BackSalaEspera```, encargado de la logica de la sala de espera.
    7. ```sala_de_juego.py```: Contiene a ```BackSalaJuego```, encargado de parte de la lógica de la sala de juego.
    8. ```tablero.py```: Contiene a ```Grafo, Nodo, Hexagono, Tablero```, se encarga de la lógica del tablero del juego. Es muy relevante que en este archivo se utiliza ```GeneradorGrillaHexagonal``` de ```generador_grilla.py```, como se especificó anteriormente este último archivo **debe** ubicarse en ```client```.
    9. ```chat.py```: Contiene a ```VentanaChat```, despliega vetana de chat.
    10. ```chozas.py```: Contiene a ```DragChoza, DropChoza```, despliegan chozas en la interfaz.
    11. ```fin_de_partida.py```: Contiene a ```VentanaFinPartida```, despliega ventana fin de partida.
    12. ```sala_de_espera.py```: Contiene a ```VentanaSalaEspera```, despliega ventana de la sala de espera.
    13. ```sala_de_juego```: Contiene a ```VentanaSalaJuego```, despliega a la ventana de la sala de juego.
2. ```server```
    1. ```banco.py```: Contiene a ```Banco```, encargado de parte de la logica del juego que maneja el servidor.
    2. ```jugador.py```: Contiene a ```Jugador```, clase que modela jugadores en el servidor.
    3. ```logica.py```: Contiene a ```Logica```, se encarga de manejar los mensajes de los clientes.
    4. ```parametros.py```: Contiene a ```Parametro, cagar_parametros, hook```, encargado de cargar los parámetros en ```parametros.json```.
    5. ```parametros.json```: Objeto ```json``` que contiene parámetros que se mantienen constantes para el servidor.
    6. ```server.py```: Contiene a ```Servidor```, encargado de la comunicación con los clientes.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El máximo de jugadores está dado por el parámetro ```MAX_JUGADORES_PARTIDA``` en el cliente, en el enunciado se dice que son ```4```.
2. Se actualizan los puntos de victoria una vez que se presiona el botón 'Terminar mi turno'.
3. Los turnos son ennumerados: del -1 al 0 son turnos de preparación, y del 1 en adelante son parte del progreso del juego. En los turnos de preparación cada cliente coloca sus chozas iniciales y recibe las materias primas correspondientes.
4. En el enunciado se dice que el tablero no va a variar su tamaño, por ende me di la libertad de usar el parámetro ```LISTA_NUMEROS``` en el server para determinar los números de los hexágonos. Esta lista luego es desordenada.
5. Cree mi propio archivo ```nombres.txt``` para los nombres de los clientes.
6. Recordar que ````generador_grilla.py``` debe ubicarse en ```client```.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. ```Grafo``` fue basado en grafo de listas de adyacencia de la semana 12.
2. ```VentanaChat``` fue basado en chat_widget.py de AF05.
3. El código de ```DragChoza y DropChoza``` fue basado en: https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5.
4. ```Cliente``` fue basado en ```cliente.py``` de AF05.
5. ```Server``` fue basado en ```servidor.py``` de AF05
