
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import QRex
import Repo
from Functions import Functions
from QuadraticFunction import QuadraticFunction
from LinearFunction import LinearFunction
from Node import Node
import pickle

class LinkedList:

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def append(self, theFunction: Functions):
        if self.size == 0:
            new_node = Node(theFunction)
            new_node.next = None
            self.front = self.back = new_node
            self.size += 1
        else:
            new_node = Node(theFunction)
            new_node.next = None
            self.back.next = new_node
            self.back = new_node
            self.size += 1

    def debug(self):
        current = self.front
        text = ""
        while current is not None:
            text += current.data.textEntered
            text += "-->"
            current = current.next
        return text

    def __str__(self):
        if self.size == 0:
            return "LIST IS EMPTY - STR"

        current = self.front
        text = ""
        while current is not None:
            text += current.data.textEntered
            text += "  -->> "
            current = current.next

        return text

    def displayDefault(self):
        if self.size == 0:
            return "<NO FUNCTIONS>"
        else:
            current = self.front
            text = ""
            while current is not None:
                text += """
    ===============================================================
    Function: {} 
    Type:  {} 
    X-Intercepts: ({}, {})
    Discriminant Value: {}
    """.format(current.data.textEntered, "Quadratic" if isinstance(current.data, QuadraticFunction) else "Linear",
               current.data.getXIntercepts()[0], current.data.getXIntercepts()[1],
               current.data.calculateDiscriminant() if isinstance(current.data, QuadraticFunction) else 0)
                current = current.next
            return text

    def search_by_textEntered(self, target: str):
        if self.size == 0:
            return "LIST IS EMPTY"
        elif self.size == 1:
            if self.front.data.textEntered == target:
                return """ 
                        ====================== FUNCTION FOUND =========================
                        Function: {} 
                        Type: {}
                        Coefficients: {}
                        """.format(self.front.data.textEntered, "QUADRATIC", self.front.data.a + " " + self.front.data.b)
        else:
            current = self.front
            while current is not None and current.data.textEntered != target:
                current = current.next

            # return "FOUND" if current else "NOT FOUND"
            return """ 
    ============================= FUNCTION FOUND ========================
    Function: {} 
    Type: {}
    Coefficients: {}
    =====================================================================
    """.format(current.data.textEntered, "QUADRATIC", str(current.data.a) + " " + str(current.data.b)) if current else "NOT FOUND"


    def removeFunction(self, textEntered: str):
        if self.size == 0:
            pass
        else:
            if self.front.data.textEntered == textEntered:
                self.front = self.front.next
                self.size -= 1
            else:
                current = self.front
                prev = None

                while current is not None and current.data.textEntered != textEntered:
                    prev = current
                    current = current.next
                if current:
                    prev.next = prev.next.next
                    self.size -= 1
                else:
                    raise Exception("This Function is not Available in the LinkedList")

    def createAllDictionary(self):
        all = {}
        if self.size == 0:
            pass
        else:
            current = self.front
            while current is not None:
                all[current.data.a] = current.data
                current = current.next
        return all

    def sortByCoefficient(self):
        all_fnc = self.createAllDictionary()
        sorted = {}
        while len(all_fnc) > 0:
            current_minimum = min(list(all_fnc.keys()))
            sorted[current_minimum] = all_fnc[current_minimum]
            del all_fnc[current_minimum]

        ple = ""
        for c in sorted:
            is_quadratic = isinstance(sorted[c], QuadraticFunction)
            ple += """
    =============================================================================
    Function: {} 
    Type: {} 
    Leading Coefficient: {}
    Slope/Discriminant Value: {}
    """.format(sorted[c].textEntered, "Quadratic" if is_quadratic else "Linear", sorted[c].a, \
                       sorted[c].calculateSlope() if not is_quadratic else sorted[c].calculateDiscriminant())

        return ple



    def sortByType(self):
        quadrex, linrex = [], []
        if self.size == 0:
            pass
        else:
            current = self.front
            while current is not None:
                if isinstance(current.data, QuadraticFunction):
                    quadrex.append(current.data)
                else:
                    linrex.append(current.data)
                current = current.next

        text = ""
        for q in quadrex:
            text += \
                """
    ===========================================================
    Function: {}
    Type: Quadratic     
    X-Intercepts: ({}, {})
    Discriminant Value: {}
        """.format(q.textEntered, q.getXIntercepts()[0], q.getXIntercepts()[1], q.calculateDiscriminant())
        for l in linrex:
            text += \
            """
    ===========================================================
    Function: {} 
    Type: Linear   
    Coefficients: {}
        """.format(l.textEntered, l.a)

        return text



    def removeType(self, typeGiven):
        if self.size == 0:
            pass
        else:
            while isinstance(self.front.data, typeGiven):
                self.front = self.front.next
            current = self.front
            prev = None
            while current is not None:
                while current is not None and not isinstance(current.data, typeGiven):
                    prev = current
                    current = current.next
                prev.next = current.next if current else None
                self.size -= 1
                current = prev.next

        return self.displayDefault()


        # if self.size == 0:
        #     pass
        # else:
        #     while isinstance(self.front.data, type):
        #         self.front = self.front.next
        #     current = self.front
        #     while current is not None:
        #         prev = None
        #         while current is not None and not isinstance(current.data, type):
        #             prev = current
        #             current = current.next
        #         prev.next = current.next if current else None
        #         #current = current.next if current else None
        # text = self.displayDefault()
        # return text

    def search(self, target):
        if self.size != 0:
            current = self.front
            while current is not None:
                print(current.data.textEntered, target)
                if str(current.data.textEntered) == target:
                    return """
        ======================== Function Found ========================
        Function: {} 
        Type: {} 
        Leading Coefficients: {}
        ================================================================
        """.format(current.data.textEntered, "Quadratic" if isinstance(current.data, QuadraticFunction) else "Linear", current.data.a)
                current = current.next

            return "FUNCTION NOT FOUND"



if __name__ == "__main__":
    print("LinkedList part is working")

    myLL = LinkedList()
    print(myLL.size)
    q = QuadraticFunction("4x^2 + 16x + 2")
    myLL.append(q)
    q1 = QuadraticFunction("2x^2 + 15x + 1")
    myLL.append(q1)
    q2 = QuadraticFunction("6x^2 + 11x + 2")
    myLL.append(q2)
    q3 = LinearFunction("x + 2")
    myLL.append(q3)
    myLL.sortByCoefficient()












   # One time for putting the Linked List

   #theLL = LinkedList()
   #pickle_out = open("putfilenamehere.pickle", "wb")
   #pickle.dump(theLL, pickle_out)
   #pickle_out.close()

   #pickle_in = open("putfilenamehere.pickle", "rb")
   #the = pickle.load(pickle_in)
   #print(the)






