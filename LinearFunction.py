
from sympy.solvers import solve
from sympy import Symbol
from Functions import Functions

class LinearFunction(Functions):

    def __init__(self, textEntered: str):
        # x + 4
        # 3x + 17
        self.textEntered = textEntered
        if "+" in textEntered:
            l = textEntered.split("+")
            first = l[0]
            print(l)
            if l[0].find("x") != 0:
                self.a = int(l[0][:l[0].find("x")])
            else:
                self.a = 1
            self.c = int(l[1])
        elif "-" in textEntered:
            l = textEntered.split("-")
            first = l[0]
            if l[0].find("x") != 0:
                self.a = int(l[0][:l[0].find("x")])
            else:
                self.a = 1
            self.c = int(l[1])
        else:
            l = textEntered.split()
            if l[0].find("x") != 0 :
                self.a = int(l[0][:l[0].find("x")])
            else:
                self.a = 1
            self.c = 0

    def __str__(self):
        return "A: {}, C: {}".format(self.a, self.c)

    def getYIntercepts(self):
        return (0, self.c)

    def getXIntercepts(self):
        x = Symbol("x")
        answer = solve(self.a * x + self.c, x)
        return (answer[0], 0)

    def calculateSlope(self):
        return self.a


if __name__ == "__main__":
    print(LinearFunction("4x + 2").getXIntercepts())







