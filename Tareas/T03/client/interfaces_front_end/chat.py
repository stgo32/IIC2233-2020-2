import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel)
from PyQt5.QtCore import pyqtSignal


# basado en chat_widget.py de AF05
class VentanaChat(QWidget):
    """
    Este widget contiene el chat y sus elementos interactivos.
    """

    senal_enviar_texto = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):
        self.setWindowTitle('Chat DCColonos')
        self.setMinimumSize(300, 300)

        # Main widget declaration
        self.text_area = QTextEdit(self)
        self.main_vertical_layout = QVBoxLayout(self)
        self.input_horizontal_layout = QHBoxLayout()
        self.line_input = QLineEdit(self)
        self.send_button = QPushButton(self)
        self.feedback_label = QLabel(self)

        # Add widgets to layout
        self.main_vertical_layout.addWidget(self.text_area)
        self.input_horizontal_layout.addWidget(self.line_input)
        self.input_horizontal_layout.addWidget(self.send_button)
        self.main_vertical_layout.addLayout(self.input_horizontal_layout)
        self.main_vertical_layout.addWidget(self.feedback_label)

        self.text_area.setReadOnly(True)

    def __retranslate_ui(self):
        self.send_button.setText("Send")

    def __connect_events(self):
        self.send_button.clicked.connect(self.send_text)
        self.line_input.returnPressed.connect(self.send_text)
        self.send_button.setAutoDefault(True)

    def add_message(self, text):
        self.text_area.setText(self.text_area.toPlainText() + "\n" + text)

    def send_text(self):
        """
        Enviar diccionario conteniendo el texto dentro de line_input al backend.
        """
        text = self.line_input.text()
        self.line_input.setText("")
        if text.strip():
            dict_ = {
                "evento": "Mensaje chat",
                "detalles": text
            }
            self.senal_enviar_texto.emit(dict_)


if __name__ == "__main__":
    app = QApplication([])
    window = VentanaChat()
    window.show()
    sys.exit(app.exec_())
