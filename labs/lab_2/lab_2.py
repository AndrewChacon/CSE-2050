import math

class Polygon:
    def __init__(self, nbr_sides: int):
        self.nbr_sides = nbr_sides

    def whoamI(self):
        return "Triangle" if self.nbr_sides == 3 else "Rectangle"

    def howmanysides(self):
        return self.nbr_sides

    def area(self):
        return "No area"

    def perimeter(self):
        return "No perimeter"

class Rectangle(Polygon):

    def __init__(self, breadth, length):
        super().__init__(4)

        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth * self.length

    def perimeter(self):
        return (self.breadth + self.length) * 2

class Triangle(Polygon):

    def __init__(self,a ,b, c):
        super().__init__(3)

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shape1 = Rectangle(5, 5)
shape2 = Triangle(5, 5, 5)


if __name__ == '__main__':

    print('\nShape:', shape1.whoamI())
    print('Number of sides:', shape1.howmanysides())
    print('Breadth:', shape1.breadth)
    print('Length:', shape1.length)
    print('Area:', shape1.area())
    print('Perimeter:', shape1.perimeter())

    print('\nShape:', shape2.whoamI())
    print('Number of sides:', shape2.howmanysides())
    print('Side A:', shape2.a)
    print('Side B:', shape2.b)
    print('Side C:', shape2.c)
    print('Area:', shape2.area())
    print('Perimeter:', shape2.perimeter())
