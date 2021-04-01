from PyQt5.QtCore import QEventLoop, QTimer

# codigo basado en el ejercicio del Pou de la ayudantía 7


def dormir(segundos):
    loop = QEventLoop()
    QTimer.singleShot(segundos*1000, loop.quit)
    loop.exec_()

