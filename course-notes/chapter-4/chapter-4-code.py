# Writing Tests

class Doubler:
    def __init__(self, n):
        self._n = 2 * n

    def n(self):
        return self._n
        

x = Doubler(5)
assert(x.n() == 10)
y = Doubler(-4)
# assert(y.n() == -9) # returns assertion error



# Unit Testings with Unittest

# import unittest
# from dayoftheweek import DayOfTheWeek

# class TestDayOfTheWeek(unittest.TestCase):
#     def testinitwithabbreviation(self):
#         d = DayOfTheWeek('F')
#         self.assertEqual(d.name, 'Friday')

#         d = DayOfTheWeek('Th')
#         self.assertEqual(d.name, 'Thursday')

# unittest.main()



# Test-Driven Development

# Code with duplications

L1 = []
L2 = []

avg1 = sum(L1)/len(L1)
avg2 = sum(L2)/len(L2)

# Updated code before refactoring

if len(L1) == 0:
    avg1 = 0
else:
    avg1 = sum(L1)/len(L1)

if len(L2) == 0:
    avg2 = 0
else:
    avg2 = sum(L2)/len(L2)

# Refactored code

def avg(L):
    if len(L) == 0:
        return 0
    else:
        return sum(L) / len(L)

avg1 = avg(L1)
avg2 = avg(L2)