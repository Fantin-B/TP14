from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window3(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("Encore un titre de qualité")

        self.Icon = QIcon(r"C:\Users\Fantin\Documents\Cours ISEN\Informatique\Python\2ème Année\fr-flag.png")
        self.setWindowIcon(self.Icon)

        self.layout = QVBoxLayout()

        self.label = QLabel("Hello World")
        self.label.setAlignment(Qt.AlignCenter)

        self.barre = QProgressBar()
        self.barre.setValue(46)

        self.lineEdit = QLineEdit()

        self.Button = QPushButton("Click me :(")
        self.Button.setToolTip("que sera sera")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.Button)

        self.setLayout(self.layout)




if __name__ == "__main__" :
    app = QApplication([])
    win = Window3()
    win.show()
    app.exec_()
