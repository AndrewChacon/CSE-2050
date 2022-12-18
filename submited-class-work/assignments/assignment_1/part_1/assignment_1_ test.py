# import unittest
# from ADT import Stack_L, Queue_L, Stack_LL, Queue_LL

# class TestStackL(unittest.TestCase):

#     def test_init(self):
#         s = Stack_L()

#     def test_length(self):
#         s = Stack_L()
#         self.assertEqual(s.__len__(), 0)









import unittest
from Fitting import fit_data, const, lin, quad

class Test_functions(unittest.TestCase):
    def test_const(self):
        # y = 3
        x = [0, 1, 2, 3]
        y = [3, 3, 3, 3]
        
        for i in range(len(x)):
            self.assertEqual(const(x[i], 3), y[i])

    def test_lin(self):
        # y = 1*x + 0
        x = [0, 1, 2, 3]
        y = [0, 1, 2, 3]
        for i in range(len(x)):
            self.assertEqual(lin(x[i], 1, 0), y[i])

    def test_quad(self):
        # y = 1*x**2 + 1
        x = [0, 1, 2, 3]
        y = [1, 2, 5, 10]
        for i in range(len(x)):
            self.assertEqual(quad(x[i], 1, 0, 1), y[i])



class Test_fit_data(unittest.TestCase):
    def test_exact_const(self):
        # exact fit 
        #y^
        # |
        # |
        # |····
        # |---------> x

        x = [0, 1, 2, 3]
        y = [1, 1, 1, 1]

        params_expected = [1]   # y = 1
        rmse_expected = 0       # exact fit


        # note that we use AlmostEqual to account for any floating point round off
        params, rmse, y = fit_data(const, x, y)
        self.assertAlmostEqual(params[0], 1, 3)         # equal within 3 decimals
        self.assertAlmostEqual(rmse, rmse_expected, 3)  # equal within 3 decimals

    def test_almost_const(self):
        # almost fit
        #y^
        # |
        # | ·
        # |·  ·
        # |--·--------> x
        x = [0, 1, 2, 3]
        y = [1, 2, 0, 1]
        params = [1] # should still fit to y = 1
        
        # sq error: (1-1)**2 + (1-2)**2 + (1-0)**2 + (1-1)**2 = 2
        # Mean sq error: 2/4 = 0.5
        # Root MSE = sqrt(1/2) ~ 0.707
        rmse_expected = 0.707


        params, rmse, y = fit_data(const, x, y)
        self.assertAlmostEqual(params[0], 1)
        self.assertAlmostEqual(rmse, rmse_expected, 3) # equal to 3 decimals

    def test_exact_lin(self):
        # exact fit 
        #y^
        # |   ·
        # |  ·
        # | ·
        # |·--------> x

        x = [0, 1, 2, 3]
        y = [0, 1, 2, 3]

        params_expected = [1, 0]    # y = 1*x + 0
        rmse_expected = 0           # exact fit


        # note that we use AlmostEqual to account for any floating point round off
        params, rmse, y = fit_data(lin, x, y)
        self.assertAlmostEqual(params[0], 1, 3)         # equal within 3 decimals
        self.assertAlmostEqual(params[1], 0, 3)         # equal within 3 decimals
        self.assertAlmostEqual(rmse, rmse_expected, 3)  # equal within 3 decimals

    def test_almost_lin(self):
        #y^
        # |   
        # |  ··
        # |·· 
        # |---------> x

        x = [0, 1, 2, 3]
        y = [1, 1, 2, 2]


if (__name__ == '__main__'):
    unittest.main()