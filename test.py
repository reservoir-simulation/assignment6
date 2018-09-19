#/usr/bin/env python

import unittest

from assignment6 import *

class TestSolution(unittest.TestCase):

    def test_least_squares(self):

	    kc = KozenyCarmen('poro_perm.dat')

	    A = np.array([[1, 2],[1, 4],[1, 6],[1,10]])
	    b = np.array([6, 10, 13, 22])

	    np.testing.assert_allclose(kc.least_squares(A,b), np.array([1.82857143,  1.98571429]), atol=0.001)

	    A = np.array([[1, 3],[1, 9],[1, 14],[1,10]])
	    b = np.array([6, 10, 11, 29])

    def test_fit(self):

	    kc = KozenyCarmen('poro_perm.dat')
	    
	    kc.fit()
	    
	    np.testing.assert_allclose(kc.fit(), np.array([  1.05933127e+01,   2.35173520e+04]), atol=0.001)
    
    def test_fit_through_zero(self):

	    kc = KozenyCarmen('poro_perm.dat')

	    kc.fit_through_zero()
	    
	    np.testing.assert_allclose(kc.fit_through_zero(),26133.929742741482, atol=0.001)


if __name__ == '__main__':
    unittest.main()
