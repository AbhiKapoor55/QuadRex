

import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from QuadraticFunction import QuadraticFunction
from LinearFunction import LinearFunction

class LRexClass(QtWidgets.QMainWindow):

    def __init__(self):
        super(LRexClass, self).__init__()
        self.setGeometry(260,180,720,380)
        self.setWindowTitle("LinRex - Home")

        lbl_background = QtWidgets.QLabel(self)
        lbl_background.setPixmap(QPixmap("blue.jpg"))
        lbl_background.resize(950,500)
        lbl_background.move(0,0)

        self.lbl_enter = QtWidgets.QLabel(self)
        self.lbl_enter.resize(300,30)
        self.lbl_enter.move(20,350)
        self.lbl_enter.setText("<font color='white'>Enter Linear Function :</font>")

        font = QtGui.QFont()
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(15)
        self.lbl_enter.setFont(font)

        self.entry = QtWidgets.QLineEdit(self)
        self.entry.resize(300,18)
        self.entry.move(230,358)

        lbl_logo = QtWidgets.QLabel(self)
        lbl_logo.setGeometry(200,40,270,50)
        lbl_logo.setPixmap(QtGui.QPixmap("lrex.png"))

        btn_calculate = QtWidgets.QPushButton("Calculate", self)
        btn_calculate.move(540,351)
        btn_calculate.resize(140,35)
        btn_calculate.clicked.connect(self.calculate)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.resize(720,20)
        self.progress.move(0,330)

        self.lbl_show_y_ints = QtWidgets.QLabel(self)
        self.lbl_show_y_ints.setText(" ")
        self.lbl_show_y_ints.move(40,150)
        self.lbl_show_y_ints.resize(290,30)

        self.lbl_show_textEntered = QtWidgets.QLabel(self)
        self.lbl_show_textEntered.setText(" ")
        self.lbl_show_textEntered.move(330,150)
        self.lbl_show_textEntered.resize(290,30)

        self.lbl_show_x_ints = QtWidgets.QLabel(self)
        self.lbl_show_x_ints.setText(" ")
        self.lbl_show_x_ints.move(40, 200)
        self.lbl_show_x_ints.resize(290, 30)

        self.lbl_copyright = QtWidgets.QLabel(self)
        self.lbl_copyright.move(530, 5)
        self.lbl_copyright.resize(200,30)
        self.lbl_copyright.setText("<font color='white'>© Copyright Abhi Kapoor 2018</font>");

        btn_exit = QtWidgets.QPushButton("<-- Back", self)
        btn_exit.move(5,5)
        btn_exit.resize(100,30)
        btn_exit.clicked.connect(self.back)

        self.lbl_show_slope = QtWidgets.QLabel(self)
        self.lbl_show_slope.setText("")
        self.lbl_show_slope.move(40,250)
        self.lbl_show_slope.resize(350,30)


        self.show()

    def back(self):
        self.close()

    def calculate(self):
        completed = 0
        self.lbl_enter.setText("<font color='white'>Loading...</font>")

        while completed < 100:
            completed += 0.00001
            self.progress.setValue(completed)

        self.lbl_enter.setText("Enter Linear Function :")

        theFunction = LinearFunction(self.entry.text())
        print(theFunction)

        yi = "Y-Intercepts are: ({}, {})".format(theFunction.getYIntercepts()[0], theFunction.getYIntercepts()[1])
        si = "Slope: {}".format(theFunction.calculateSlope())

        self.lbl_show_y_ints.setText("Y-Intercept: ({},{})".format(theFunction.getYIntercepts()[0], theFunction.getYIntercepts()[1]))
        self.lbl_show_slope.setText("Slope: {}".format(theFunction.calculateSlope()))
        self.lbl_show_x_ints.setText("X-Intercept: ({},{})".format(theFunction.getXIntercepts()[0], theFunction.getXIntercepts()[1]))
        self.lbl_show_textEntered.setText("Function: {}".format(theFunction.textEntered))

        self.lbl_show_y_ints.repaint()
        self.lbl_show_slope.repaint()
        self.lbl_show_x_ints.repaint()
        self.lbl_show_textEntered.repaint()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = LRexClass()

    sys.exit(app.exec_())