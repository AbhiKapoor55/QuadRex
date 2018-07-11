
from Functions import Functions

class QuadraticFunction(Functions):
    """
    This class represents Quadratic Functions
    """

    def __init__(self, textEntered: str):
        """
        Initializes a new Quadratic Function with up to 3 coefficients
        """
        self.textEntered = textEntered

        split = textEntered.split()
        if len(split) == 5:
            self.determineA(split[0])
            self.determineB(split)
            self.determineC(split)
        elif len(split) == 3:
            self.determineA(split[0])
            self.determineB(split)
        elif len(split) == 1:
            self.determineA(split[0])
        else:
            raise Exception("Length was Not 1, 3, or 5")

    def determineA(self, first: str):

        x2_index = first.find("x^2")
        if x2_index == 0:
            self.a = 1
        else:
            coefficient_one = first[:x2_index]
            if coefficient_one.find("-") >= 0:
                self.a = int(first[1:x2_index]) * -1
            else:
                self.a = int(first[:x2_index])

    def determineB(self, split):
        x_index = split[2].find("x")
        if x_index < 0:
            self.b = 0
            self.c = int(split[2]) * -1 if split[1] == "-" else int(split[2])
        elif x_index == 0:
            self.b = 1
            self.c = 0
        else:
            self.b = int(split[2][:x_index]) * -1 if split[1] == "-" else int(split[2][:x_index])
            self.c = 0

    def determineC(self, split):
        self.c = int(split[4]) * -1 if split[3] == "-" else int(split[4])

    def __str__(self):
        return "A: {}, B: {}, C: {}".format(self.a, self.b, self.c)

    def calculateDiscriminant(self):
        """
        Returns the Discriminant value of this Quadratic Function
        :return: int
        """
        return self.b ** 2 - (4 * self.a * self.c)

    def getNumOfRoots(self):
        """
        Returns the number of real roots this Quadratic Function has
        :return: int
        """
        return 1 if self.calculateDiscriminant() == 0 else 2

    def getXIntercepts(self):
        """
        Returns a Tuple containing the two x-intercepts of this Quadratic Function
        :return: Tup(int, int)
        """
        p1 = -1 * self.b
        p2 = self.calculateDiscriminant() ** 0.5
        denom = 2 * self.a

        root_one = (p1 + p2) / denom
        root_two = (p1 - p2) / denom

        return (round(root_one, 4), round(root_two, 4))

    def getYIntercepts(self):
        """
        Returns a Tuple containing the y-intercept of this Quadratic Function
        :return: Tup(int, int)
        """
        return (0, self.c) if isinstance(self.c, int) else (0,0)

    def getLineOfSymmetryEquation(self):
        """
        Returns the equation of the Line of Symmetry of this Quadratic Function
        :return: int
        """
        return (-1 * self.b) / (2 * self.a)

    def getVertexCoordinates(self):
        """
        Return the coordinates of the Vertex of this Quadratic Function as a Tuple
        :return: Tup(int, int)
        """
        x_coord = round(self.getLineOfSymmetryEquation(), 4)
        p1 = (x_coord ** 2) * self.a
        p2 = x_coord * self.b if isinstance(self.b, int) else 0
        y_coord = round(p1 + p2 + self.c, 4)

        return (x_coord, y_coord)


if __name__ == "__main__":
    print(QuadraticFunction("7x^2 + 12x + 6"))
    print(QuadraticFunction("2x^2 + 15x + 6").getVertexCoordinates())