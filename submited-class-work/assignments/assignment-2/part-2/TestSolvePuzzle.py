from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
            board = [1,2,2,3,4]
            self.assertEqual(puzzle(board), True)

        def testCounterClockwise(self):
            board = [1,1,1]
            self.assertEqual(puzzle(board), True)

        def testMixed(self):
            board = [1,3,1,4,1]
            self.assertEqual(puzzle(board), True)
        
        def testUnsolveable(self):
            board = [0,2,1,3,2]
            self.assertEqual(puzzle(board), False)

unittest.main()