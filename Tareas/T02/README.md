# Tarea 02: DCCumbia :penguin:


## Consideraciones generales :octocat:

La Tarea tine la mayoría de los requerimientos implementados y funciona en la mayoría de los casos como se pide, pero **no** está implementada la flecha hielo y hay un ```bug``` con la aprobación que no logré encontrar, el cual en muy pocas ocaciones la aprobación es superior al mínimo y la ventana de resumen dice que ha perdido, pero la de juego permite seguir jugando.

### Cosas implementadas y no implementadas :white_check_mark: :x:

1. **Ventana de Inicio:**
    1. Hecha completa.
2. **Ventana de Ranking:**
    1. Hecha completa.
3. **Ventana de Juego:**
    1. Generales: hecha completa.
    2. Fase de pre-ronda: hecha completa.
    3. Fase de ronda: hecha completa.
    4. Fase de post-ronda: como mencione anteriormente, hay un ```bug``` con la aprobación en ocaciones muy puntuales, pero a parte de eso funciona bien. 
4. **Mecánicas:**
    1. Pingüirín: hecha completa.
    2. Flechas: Funciona todo como se pide, solo que no se implementó la flecha hielo.
5. **Funcionalidades Extra:**
    1. Pausa: hecha completa.
    2. M+O+N: hecha completa.
    3. N+I+V: hecha completa.
6. **General:**
    1. Modularización: hecha completa.
    2. Modelación: hecha completa.
    3. Archivos: hecha completa.
    4. Parámetros: hecha completa.
7. **Bonus:**
No se implementó ningún bonus.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales que deben estar contenidos en una carpeta llamada ```T02```:
1. ```parametros.py```
2. ```front_end``` directorio que contiene a:
    1. ```front_inicio.py``` 
    2. ```front_juego.py```
    3. ```front_ranking.py```
    4. ```front_resumen.py```
3. ```back_end``` directorio que contiene a:
    1. ```back_ranking.py``` 
    2. ```funciones.py```
    3. ```partida.py```
    4. ```pinguirines.py```
    5. ```zona_de_ritmo.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: librería que se utilizó en todos los módulos excepto en ```parametros.py```. Se usaron las funciones ```path``` y ```exit```.
2. ```os```: ```path``` en ```parametros.py```
3. ```random```: ```randint```, ```random``` en ```zona_de_ritmo.py``` 
2. ```PyQt5```: librería que se utiliza en  ```main.py``` y en todos los archivos de ```front_end``` y ```back_end``` y que **debe** ser instalada. Se detallan las funciones utilizadas por módulos:
    1. ```QtCore```: ```QObject```, ```pyqtSignal```, ```QEventLoop```, ```QTimer```, ```Qt```, ```QMimeData```, ```QUrl```
    2. ```QtGui```: ```QPixmap```, ```QDrag```, ```QImage```, ```QPainter```, ```QKeySequence```
    3. ```QtWidgets```: ```QWidget```, ```QLabel```, ```QLineEdit```, ```QApplication```, ```QComboBox```, ```QFormLayout```, ```QPushButton```, ```QHBoxLayout```, ```QVBoxLayout```, ```QLineEdit```, ```QErrorMessage```, ```QComboBox```, ```QProgressBar```, ```QShortcut```   
    4. ```QMultimedia```: ```QMediaContent```, ```QMediaPlayer```  


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```front_inicio.py```: Contiene a ```fInicio```, despliega la ventana de inicio.
2. ```front_juego.py```: Contiene a ```fJuego```, despliega la ventana de juego.
3. ```front_ranking.py```: Contiene a ```fRanking```, despliega la ventana de ranking.
4. ```front_resumen.py```: Contiene a ```fResumen```, despliega la ventana de resumen.
5. ```back_ranking.py```: Contiene a ```bRanking```, y contiene la lógica de la ventana de ranking.
6. ```funciones.py```: Contiene a la función ```dormir```.
7. ```partida.py```: contiene la lógica de todo el juego, por lo que involucra a todas las ventanas y contiene a la clase ```Partida```.
8. ```pinguirines.py```: contiene a las clases ```DragPingu``` y ```DropPingu``` y contiene la lógica de los pingüirines.
9. ```zona_de_ritmo.py```: contiene a las clases ```Flecha```, ```CapturaFlechas``` y ```CreadorFlechas```. Sirve para que la ```Partida``` delegue algunos de sus deberes.
10. ```parametros.py```: contiene parametros que se son constantes para todo el juego.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. La aprobación no puede ser negativa. 
2. Es posible poner un máximo de 20 pingüirines en la pista de baile, dado que la clase ```DragPingu``` necesita que estén instanciados objetos ```DropPingu``` en la pista.
3. Los cheatcodes fueron hechos con ```QShortcut```, por lo que las teclas **deben** ser apretadas en orden mientras se mantienen presionadas.
4. Las ventanas se estilizaron con ```css```, por lo que si se tiene problemas visuales, en ```parametros.py``` en la linea 233 está ```APP_STYLE_SHEET``` y sólo se debe comentar la linea 24 de ```main.py``` para deshabilitarlo.
5. Supuse que el tipo de paso (simple, doble o triple) de las flechas se determina de forma aleatoria.
6. Supuse que los pasos múltiples **no** puden ser combinados, por ejemplo, no pueden haber flechas normales y doradas en un mismo paso.
7. Las canciones se reproducen con ```QMediaPlayer```. He escuchado que esta clase tiene problemas con sistemas operativos IOS.
8. Si se tiene problemas con la importación es porque es necesaria una carpteta llamada T02 que contenga todos los módulos y directorios mencionados. Dado que, para las rutas relativas se utilizó ```path``` de ```sys```.  


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5: se usó como base para el archivo ```pinguirines.py```
2. codigo de ```Flecha``` en ```zona_de_ritmo.py``` inspirado en el ultimo ejemplo del primer notebook de la semana 10 (el de las comidas)
3. https://stackoverflow.com/questions/7176951/how-to-get-multiple-key-presses-in-single-event: se usó como base para la captura de multiples teclas en ```front_juego.py```
4. En ```funciones.py```, ```dormir``` está basado en el ejercicio del Pou de la ayudantía 7.
