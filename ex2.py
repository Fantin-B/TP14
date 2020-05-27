from PySide2.QtWidgets import *

class Window2(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Laisser un commentaire")
        self.layout = QGridLayout()

        self.label = QLabel("Laissez un commentaire")
        self.txt = QTextEdit()
        self.button1 = QPushButton("Success")
        self.button2 = QPushButton("Cancel")

        self.layout.addWidget(self.label,0,0,1,2)
        self.layout.addWidget(self.txt,1,0,1,2)
        self.layout.addWidget(self.button1,2,0,1,1)
        self.layout.addWidget(self.button2,2,1,1,1)

        self.setLayout(self.layout)

if __name__ == "__main__" :
    app = QApplication([])
    win = Window2()
    win.show()
    app.exec_()
