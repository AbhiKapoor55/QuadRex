
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import QRex
import Repo
import pickle
from LinkedList import LinkedList
from QuadraticFunction import QuadraticFunction
from LinearFunction import LinearFunction

class Repository(QtWidgets.QMainWindow):

    def __init__(self):
        super(Repository, self).__init__()
        self.setGeometry(50,50,750,600)
        self.setWindowTitle("FuncRex - View Stored Functions")

        lbl_background = QtWidgets.QLabel(self)
        lbl_background.setPixmap(QPixmap("fr.jpg"))
        lbl_background.move(0,0)
        lbl_background.resize(750,600)

        pickle_in = open("newname.pickle", "rb")
        self.LL = pickle.load(pickle_in)
        print(self.LL.size)

        lbl_Logo = QtWidgets.QLabel(self)
        lbl_Logo.setText("Function Repository")
        lbl_Logo.move(245,45)
        lbl_Logo.resize(400,100)

        font = QtGui.QFont()
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(18)
        lbl_Logo.setFont(font)

        self.logOutput = QtWidgets.QTextEdit(self)
        self.logOutput.setReadOnly(True)
        self.logOutput.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.logOutput.setGeometry(60,140,600,300)
        self.logOutput.setText(self.LL.displayDefault())
        print(self.LL.displayDefault())

        btn_sort_coefficient = QtWidgets.QPushButton("Sort by Function Coefficient", self)
        btn_sort_coefficient.setGeometry(60,470,200,40)
        btn_sort_coefficient.clicked.connect(self.sortByCoefficient)

        btn_sort_type = QtWidgets.QPushButton("Sort by Function Type", self)
        btn_sort_type.setGeometry(270, 470, 200, 40)
        btn_sort_type.clicked.connect(self.sortType)

        btn_search = QtWidgets.QPushButton("Search... ", self)
        btn_search.setGeometry(480,470,200,40)
        btn_search.clicked.connect(self.search)

        btn_add = QtWidgets.QPushButton(" + Add New Function ", self)
        btn_add.clicked.connect(self.addFunction)
        btn_add.setGeometry(60,510,200,40)

        btn_remove = QtWidgets.QPushButton(" - Remove Function ", self)
        btn_remove.clicked.connect(self.removeFunction)
        btn_remove.setGeometry(270, 510, 200, 40)

        btn_remove_type = QtWidgets.QPushButton(" - Remove by Type", self)
        btn_remove_type.clicked.connect(self.removeByType)
        btn_remove_type.setGeometry(480,510, 200,40)
        btn_remove_type.clicked.connect(self.removeByType)

        btn_reset = QtWidgets.QPushButton(" Reset ", self)
        btn_reset.clicked.connect(self.reset)
        btn_reset.setGeometry(480, 550, 200, 40)

        self.entry = QtWidgets.QLineEdit(self)
        self.entry.setGeometry(65,555,300,30)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(60,430,600,50)

        btn_back = QtWidgets.QPushButton("<-- Back", self)
        btn_back.setGeometry(20,20,100,30)
        btn_back.clicked.connect(self.back)

        # self.logOutput.setText(self.LL.displayDefault())
        # self.logOutput.repaint()

        self.show()

    def sortType(self):
        completed = 0
        # self.lbl_enter.setText("Loading...")
        while completed < 100:
            completed += 0.00001
            self.progress.setValue(completed)

        self.logOutput.setText(self.LL.sortByType())

    def sortByCoefficient(self):
        completed = 0
        # self.lbl_enter.setText("Loading...")
        while completed < 100:
            completed += 0.00001
            self.progress.setValue(completed)

        self.logOutput.setText(self.LL.sortByCoefficient())
        self.logOutput.repaint()

    def reset(self):
        myLL = LinkedList()
        print("RESET", myLL.size)

        pickle_out = open("newname.pickle", "wb")
        pickle.dump(myLL, pickle_out)
        pickle_out.close()

    def back(self):
        self.close()

    def removeByType(self):
        completed = 0
        # self.lbl_enter.setText("Loading...")
        while completed < 100:
            completed += 0.00001
            self.progress.setValue(completed)

        typeEntered = self.entry.text()
        official_type = ""
        if typeEntered == "quadratic" or typeEntered == "Quadratic":
            official_type = QuadraticFunction
        elif typeEntered == "linear" or typeEntered == "Linear":
            official_type = LinearFunction
        elif typeEntered == "trigonometric" or typeEntered == "Trigonometric" or typeEntered == "trig" or \
            typeEntered == "Trig":
            official_type = "TrigonometricFunction"
        else:
            raise Exception("No Such Type")

        self.logOutput.setText(self.LL.removeType(official_type))
        self.logOutput.repaint()

        pickle_out = open("newname.pickle", "wb")
        pickle.dump(self.LL, pickle_out)
        pickle_out.close()

    def search(self):
        completed = 0
        # self.lbl_enter.setText("Loading...")
        while completed < 100:
            completed += 0.00001
            self.progress.setValue(completed)

        self.logOutput.setText(self.LL.search(self.entry.text().strip()))
        self.logOutput.repaint()

    def addFunction(self):
        # adds a new function to the LL
        pickle_in = open("newname.pickle", "rb")
        self.LL = pickle.load(pickle_in)

        print("ADD: LinkedList has been read, size is ", self.LL.size)

        if "x^2" in self.entry.text():
            new_func = QuadraticFunction(self.entry.text())
        else:
            new_func = LinearFunction(self.entry.text())

        self.LL.append(new_func)
        print("DEB:", self.LL.debug())
        print(self.LL)
        pickle_out = open("newname.pickle", "wb")
        pickle.dump(self.LL, pickle_out)
        pickle_out.close()

        print("ADD: Updated LinkedList has been written to file", self.LL.size)
        self.logOutput.setText(self.LL.displayDefault())
        self.logOutput.repaint()


    def removeFunction(self):
        # removes a function from the LL
        pickle_in = open("newname.pickle", "rb")
        self.LL = pickle.load(pickle_in)
        print("REMOVE: LinkedList has been read, size is ", self.LL.size)

        self.LL.removeFunction(self.entry.text())

        pickle_out = open("newname.pickle", "wb")
        pickle.dump(self.LL, pickle_out)
        pickle_out.close()
        print("REMOVE: Updated LinkedList has been written to file, size is ", self.LL.size)

        self.logOutput.setText(self.LL.displayDefault())
        self.logOutput.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = Repository()
    sys.exit(app.exec_())




