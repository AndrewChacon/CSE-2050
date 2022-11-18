from hw5 import solveable, valid_moves
import unittest

class TestValidMoves(unittest.TestCase):
        def testValidMoves(self):
                """Tests that valid_moves returns correct positions"""
                # 'k' denotes a knight
                # 'x' denotes possible moves
                # Positions should be given in (row, column) tuples
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - x - - - - - -
                #6 - - x - - - - -
                #7 k - - - - - - -
                # TODO: Fill in the data to test valid_moves on the board above
                k_idx = (7,0)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), 2)

                # TODO: Write tests for valid_moves for the following boards
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - x - - - - -
                #2 - x - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx = (0,0)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)


                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - k
                #1 - - - - - x - -
                #2 - - - - - - x -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx = (0, 7)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)


                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - x -
                #6 - - - - - x - -
                #7 - - - - - - - k
                k_idx = (7, 7)
                expected_valid_moves = 2
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)


                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx = (3, 3)
                expected_valid_moves = 8
                self.assertEqual(len(valid_moves(k_idx)), expected_valid_moves)


class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
            p_idx = {(1,0), (6,7), (2,5)}
            k_idx = (0, 1)

            self.assertEqual(solveable(p_idx,k_idx), False)

            p_idx = {(3, 0), (6,3), (3,4)}
            k_idx = (1,1)

            self.assertEqual(solveable(p_idx,k_idx), False)
        def testSolveableSimple(self):
            p_idx = {(2,5), (4,6), (6,7)}
            k_idx = (1,3)

            self.assertEqual(solveable(p_idx,k_idx), True)

            p_idx = {(5,5), (3,6), (2,4)}
            k_idx = (0,3)

            self.assertEqual(solveable(p_idx, k_idx), True)

        def testSolveableHard(self):
            p_idx = {(0,3), (5,7), (3,6), (1,5), (4,5)}
            k_idx = (2,4)

            self.assertEqual(solveable(p_idx, k_idx), True)

            p_idx = {(5,4), (6,6), (4,5), (0,0), (2,1), (3,3)}
            k_idx = (1,2)
            
            self.assertEqual(solveable(p_idx, k_idx), True)


unittest.main()
