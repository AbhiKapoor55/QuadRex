
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from QuadraticFunction import QuadraticFunction

class QRexClass(QtWidgets.QMainWindow):

    def __init__(self):
        super(QRexClass, self).__init__()
        self.setGeometry(260,180,720,380)
        self.setWindowTitle("QuadRex - Home")

        lbl_background = QtWidgets.QLabel(self)
        lbl_background.setPixmap(QPixmap("qreximg.jpg"))
        lbl_background.resize(950,500)
        lbl_background.move(0,0)

        lbl_logo = QtWidgets.QLabel(self)
        lbl_logo.setPixmap(QPixmap("qqq2.png"))
        lbl_logo.move(220,10)
        lbl_logo.resize(500,150)

        self.lbl_enter = QtWidgets.QLabel(self)
        self.lbl_enter.setText("Enter Quadratic Function :")
        self.lbl_enter.resize(300,30)
        self.lbl_enter.move(20,350)

        font = QtGui.QFont()
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(15)
        self.lbl_enter.setFont(font)

        self.entry = QtWidgets.QLineEdit(self)
        self.entry.resize(300,18)
        self.entry.move(230,358)

        btn_calculate = QtWidgets.QPushButton("Calculate", self)
        btn_calculate.move(540,351)
        btn_calculate.resize(140,35)
        btn_calculate.clicked.connect(self.calculateMethod)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.resize(720,20)
        self.progress.move(0,330)

        self.lbl_show_root_count = QtWidgets.QLabel(self)
        self.lbl_show_root_count.setText(" ")
        self.lbl_show_root_count.move(40,150)
        self.lbl_show_root_count.resize(290,30)

        self.lbl_copyright = QtWidgets.QLabel(self)
        self.lbl_copyright.setText("© Copyright Abhi Kapoor 2018")
        self.lbl_copyright.move(530, 5)
        self.lbl_copyright.resize(200,30)

        btn_exit = QtWidgets.QPushButton("<-- Back", self)
        btn_exit.move(5,5)
        btn_exit.resize(100,30)
        btn_exit.clicked.connect(self.back)

        self.lbl_show_x_ints = QtWidgets.QLabel(self)
        self.lbl_show_x_ints.setText("")
        self.lbl_show_x_ints.move(40,210)
        self.lbl_show_x_ints.resize(350,30)

        self.lbl_show_y_ints = QtWidgets.QLabel(self)
        self.lbl_show_y_ints.setText("")
        self.lbl_show_y_ints.move(40,270)
        self.lbl_show_y_ints.resize(320,30)

        self.vertex = QtWidgets.QLabel(self)
        self.vertex.setText("")
        self.vertex.move(470,150)
        self.vertex.resize(220,30)

        self.symmetry = QtWidgets.QLabel(self)
        self.symmetry.setText("")
        self.symmetry.move(470, 210)
        self.symmetry.resize(220,30)

        self.show()

    def back(self):
        self.close()

    def calculateMethod(self):
        # Update the Progress Bar
        completed = 0
        self.lbl_enter.setText("Loading...")
        while completed < 100:
            completed += 0.00001
            self.progress.setValue(completed)

        self.lbl_enter.setText("Enter Quadratic Function :")

        theFunction = QuadraticFunction(self.entry.text())
        print(theFunction)

        # Display all details about the entered function

        if theFunction.calculateDiscriminant() >= 0:
            self.lbl_show_root_count.setText("Num of Real Roots: {}".format(theFunction.getNumOfRoots()))
            self.lbl_show_root_count.repaint()

            xints = theFunction.getXIntercepts()
            self.lbl_show_x_ints.setText("X-Intercepts at : ({}, {}) and ({}, {})".format(xints[0], 0, xints[1], 0))
            self.lbl_show_x_ints.repaint()

            self.lbl_show_y_ints.setText("Y-Intercept at : ({}, {})".format(0, theFunction.getYIntercepts()[1]))
            self.lbl_show_y_ints.repaint()

            self.vertex.setText("Vertex At : ({}, {})".format(theFunction.getVertexCoordinates()[0],
                                                              theFunction.getVertexCoordinates()[1]))
            self.vertex.repaint()

            self.symmetry.setText("Axis of Symmetry Equation : x = {}".format(theFunction.getLineOfSymmetryEquation()))
            self.symmetry.repaint()
        else:
            self.lbl_show_root_count.setText("Error - This Function Has Imaginary Roots")
            self.lbl_show_root_count.repaint()
            self.lbl_show_x_ints.setText("")
            self.lbl_show_x_ints.repaint()
            self.lbl_show_y_ints.setText("")
            self.lbl_show_y_ints.repaint()
            self.vertex.setText("")
            self.vertex.repaint()
            self.symmetry.setText("")
            self.symmetry.repaint()

        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = QRexClass()

    sys.exit(app.exec_())

