import sys
sys.path.append('..')

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QApplication, QComboBox, QFormLayout
)
from PyQt5.QtCore import Qt, QMimeData, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QDrag, QImage, QPainter

from T02.back_end.funciones import dormir
from T02.parametros import TIPOS_PINGUIRINES, DINERO_INICIAL

# codigo basado en https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5


class DragPingu(QLabel):

    senal_enviar_color_pingu = pyqtSignal(str)

    def __init__(self, parent, color):
        super().__init__(parent)
        self.color = color
        imagen = TIPOS_PINGUIRINES[str(color)]['neutro']
        self.setPixmap(QPixmap(imagen))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
            self.senal_enviar_color_pingu.emit(self.color)

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setImageData(self.pixmap().toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)


class DropPingu(QLabel):

    senal_get_color_pingu = pyqtSignal(QLabel)
    senal_gastar_dinero = pyqtSignal()

    def __init__(self, parent, index):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.color = None
        self.index = index
        self.setScaledContents(True)
        self.dinero = DINERO_INICIAL

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage() and self.color is None and self.dinero >= 500:
            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
            self.senal_get_color_pingu.emit(self)
            self.senal_gastar_dinero.emit()

    def bailar(self, columnas):
        if self.color is not None:
            if columnas == [0]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['left']
            elif columnas == [1]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['up']
            elif columnas == [2]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['down']
            elif columnas == [3]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['right']
            elif columnas == [0, 1] or columnas == [1, 0]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['up_left']
            elif columnas == [0, 2] or columnas == [2, 0]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['down_left']
            elif columnas == [0, 3] or columnas == [3, 0]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['cuatro']
            elif columnas == [1, 2] or columnas == [2, 1]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['cuatro']
            elif columnas == [1, 3] or columnas == [3, 1]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['up_right']
            elif columnas == [2, 3] or columnas == [3, 2]:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['down_right']
            elif len(columnas) == 3:
                imagen = TIPOS_PINGUIRINES[str(self.color)]['tres']

            self.setPixmap(QPixmap(imagen))
            
            self.timer = QTimer(self)
            self.timer.setSingleShot(True)
            self.timer.setInterval(150)
            self.timer.timeout.connect(self.posicion_neutra)
            self.timer.start()

    def posicion_neutra(self):
        imagen = TIPOS_PINGUIRINES[self.color]['neutro']
        self.setPixmap(QPixmap(imagen))
