from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QTextBrowser, QTextEdit
from PyQt6.QtCore import pyqtSlot


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.dez_label =QLabel("Zahlen im Dezimalsystem zwichen 0 und 9999:", self)
        self.hexa_label = QLabel("Sechstellige Hexadezimalwerte: ", self)
        self.binaer_label = QLabel("Binärzahlen, zwischen 2**2 und 2**10: ", self)
        self.char_label = QLabel("Nur Buchstaben (a-z, A-Z): ", self)
        self.upper_char_label = QLabel("Eingabe von Groß- und Kleinbuchstaben, welche in Großbuchstaben umgewandelt werden:", self)

        self.dez_edit = QLineEdit(self)
        self.dez_edit.setInputMask("9000")
        self.hexa_edit = QLineEdit(self)
        self.hexa_edit.setInputMask(">HHHHHH")
        self.binär_edit = QLineEdit(self)
        self.binär_edit.setInputMask("BBbbbbbbb")
        self.char_edit = QLineEdit(self)
        self.char_edit.setInputMask("A")
        self.upper_char_edit = QLineEdit(self)
        self.upper_char_edit.setInputMask(">A")

        self.browser =QTextBrowser()

        self.dez_edit.textChanged.connect(self.text_Cahnged)
        self.dez_edit.inputRejected.connect(self.text_rejektet)
        self.dez_edit.editingFinished.connect(self.text_finished)

        layout = QGridLayout(self)
        layout.addWidget(self.dez_label, 1, 1)
        layout.addWidget(self.dez_edit, 1, 2)
        layout.addWidget(self.hexa_label, 2, 1)
        layout.addWidget(self.hexa_edit, 2, 2)
        layout.addWidget(self.binaer_label, 3, 1)
        layout.addWidget(self.binär_edit, 3, 2)
        layout.addWidget(self.char_label, 4, 1)
        layout.addWidget(self.char_edit, 4, 2)
        layout.addWidget(self.upper_char_label, 5, 1)
        layout.addWidget(self.upper_char_edit, 5, 2)
        layout.addWidget(self.browser, 6, 1)

    @pyqtSlot(str)
    def text_Cahnged(self, text_from_signal):
        self.browser.append("changed event" + text_from_signal)

    @pyqtSlot()
    def text_rejektet(self):
        self.browser.append("rejectet")

    @pyqtSlot()
    def text_finished(self):
        self.browser.append("finished")

        text = self.dez_edit.text()
        self.browser.append(text + "finished text")

