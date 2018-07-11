import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import QRex
import Repo
import LRex

class WindowNew(QtWidgets.QMainWindow):

    def __init__(self):
        super(WindowNew, self).__init__()
        self.setGeometry(50,50,550,350)
        self.setWindowTitle("FuncRex - Home")

        lbl_background = QtWidgets.QLabel(self)
        lbl_background.setPixmap(QPixmap("fr.jpg"))
        lbl_background.move(0,0)
        lbl_background.resize(550,350)

        lbl_Logo = QtWidgets.QLabel(self)
        lbl_Logo.setPixmap(QPixmap("frtitle.png"))
        #lbl_Logo.setText("Welcome to FuncRex")
        lbl_Logo.move(85,15)
        lbl_Logo.resize(400,100)
        #font = QtGui.QFont("Calibri", 32)
        #lbl_Logo.setFont(font)

        btn_linrex = QtWidgets.QPushButton("<-- Launch LinRex", self)
        btn_linrex.clicked.connect(self.launch_linRex)
        btn_linrex.move(18, 180)
        btn_linrex.resize(230,40)

        btn_quadrex = QtWidgets.QPushButton("Launch QuadRex ---> ", self)
        btn_quadrex.clicked.connect(self.launch_quadRex)
        btn_quadrex.move(250,180)
        btn_quadrex.resize(230, 40)

        btn_launchRepository = QtWidgets.QPushButton("View Stored Functions (Launch Function Repository) --> ", self)
        btn_launchRepository.clicked.connect(self.launch_repository)
        btn_launchRepository.move(18, 240)
        btn_launchRepository.resize(460,40)



        self.show()

    def launch_linRex(self):
        """
        This Method is supposed to launch LinRex Window
        :return: None
        """
        self.WindowL = LRex.LRexClass()
        self.WindowL.show()
        self.WindowL.setWindowTitle("LinRex - Home")

    def launch_quadRex(self):
        """
        This Method is supposed to launch QuadRex Window
        :return: None
        """
        self.WindowQ = QRex.QRexClass()
        self.WindowQ.show()
        #self.WindowQ.setGeometry(215, 215, 500, 300)
        self.WindowQ.setWindowTitle("QuadRex - Home")
        #self.close()

    def launch_repository(self):
        """
        This Method is supposed to launch Function Repository Window
        :return: None
        """
        self.WindowR = Repo.Repository()
        self.WindowR.show()
        self.WindowR.setWindowTitle("FuncRex - View Stored Functions - Function Repository ")







