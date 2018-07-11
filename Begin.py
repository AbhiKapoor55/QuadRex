import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import newwindowtest


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,350,250)
        self.setWindowTitle("FuncRex - Please Enter Password")

        label2 = QtWidgets.QLabel(self)
        label2.setPixmap(QPixmap("trynew.jpg"))
        label2.move(0,0)
        label2.resize(350,250)

        lbllogin = QtWidgets.QLabel(self)
        lbllogin.setPixmap(QPixmap("user1.png"))
        lbllogin.move(95,5)
        lbllogin.resize(200,200)

        font = QtGui.QFont()
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(15)

        lblName = QtWidgets.QLabel("A b h i    K a p o o r ", self)
        lblName.move(95,185)
        lblName.resize(185,20)
        lblName.setFont(font)

        btn = QtWidgets.QPushButton("Enter", self)
        btn.clicked.connect(self.LogIn)
        btn.move(220, 215)
        btn.resize(100, 35)

        lblLogo = QtWidgets.QLabel(self)

        lblLogo.move(10,10)
        lblLogo.resize(300,200)

        self.e1 = QtWidgets.QLineEdit(self)
        self.e1.resize(200,20)
        self.e1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.e1.move(15,220)

        self.show()

    def LogIn(self):
        password_entered = self.e1.text()

        if password_entered == "abhikap":
            print("Password Accepted")
            self.Window = newwindowtest.WindowNew()
            self.Window.show()
            self.Window.setGeometry(175, 175, 500, 300)
            self.Window.setWindowTitle("New Window")
            self.close()
        else:
            print("Password Rejected")


app = QtWidgets.QApplication(sys.argv)
GUI = Window()

sys.exit(app.exec_())