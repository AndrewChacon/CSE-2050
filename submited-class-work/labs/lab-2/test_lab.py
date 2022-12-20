import unittest
from lab_2 import Polygon, Triangle, Rectangle

class test_lab(unittest.TestCase):
    def test_init(self):

        a1 = Polygon(3);
        self.assertEqual(a1.whoamI(),"Triangle")
        self.assertEqual(a1.howmanysides(), 3)
        a2 = Polygon(4);
        self.assertEqual(a2.whoamI(),"Rectangle")
        self.assertEqual(a2.howmanysides(), 4)

    def test_area(self):
        a1 = Polygon(3);
        self.assertEqual(a1.area(), "No area")
        r1 = Rectangle(5, 5)
        r2 = Triangle(5, 5, 5)
        self.assertEqual(r1.area(), 25)
        self.assertEqual(r2.area(), 10.825317547305483)

    def test_perimeter(self):
        a1 = Polygon(3);
        self.assertEqual(a1.perimeter(), "No perimeter")
        r1 = Rectangle(5, 5)
        r2 = Triangle(5, 5, 5)
        self.assertEqual(r1.perimeter(), 20)
        self.assertEqual(r2.perimeter(), 15)

if (__name__ == '__main__'):
    unittest.main()
