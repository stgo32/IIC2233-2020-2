import os

from PyQt5.QtWidgets import (
    QLabel, QApplication
)
from PyQt5.QtCore import Qt, QMimeData, pyqtSignal  # , QTimer
from PyQt5.QtGui import QPixmap, QDrag, QPainter

from parametros import p

# codigo basado en https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5


class DragChoza(QLabel):

    def __init__(self, parent, color):
        super().__init__(parent)
        self.color = color
        llave_color = 'RUTA_CHOZA_AZUL'
        imagen = os.path.join(*tuple(p.CONSTRUCCIONES[llave_color]))
        self.setPixmap(QPixmap(imagen))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < \
                QApplication.startDragDistance():
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


class DropChoza(QLabel):

    senal_colocar_choza = pyqtSignal(dict)
    senal_preguntar_por_choza = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.ubicable = True
        self.nodo = None
        self.setMinimumSize(*p.TAMANO_DROP_CHOZA)
        self.setScaledContents(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage() and self.ubicable:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage() and self.ubicable:
            self.senal_preguntar_por_choza.emit(self.nodo.valor)
            # self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
            # print('CHOZA', self.nodo.valor)
            # self.senal_colocar_choza.emit({'evento': 'Choza', 'detalles': self.nodo.valor})

    def ocupar(self, color):
        if color == 'rojo':
            color = 'roja'
        llave_color = 'RUTA_CHOZA_' + color.upper()
        imagen = os.path.join(*(p.CONSTRUCCIONES[llave_color]))
        self.setPixmap(QPixmap(imagen))


