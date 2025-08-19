import numpy as np
import unittest
from IPython.display import Markdown, display

import __main__

def printmd(string):
    display(Markdown(string))

# Test case cell parameters for Rhodonite:
a, b, c = 0.9758, 10.499, 12.205
alpha, beta, gamma = (np.radians(108.58), np.radians(102.92),
                      np.radians(82.52))
cellparams = a, b, c, alpha, beta, gamma
V = 115.28630541243658

class Tests(unittest.TestCase):

    def check_V(self, calc_V):
        self.assertAlmostEqual(calc_V(a, b, c, alpha, beta, gamma), V)

    def check_q(self, calc_q):
        h, k, l = 3, 1, 1
        q = 19.949015808373602
        __main__.a, __main__.b, __main__.c = a, b, c
        __main__.alpha, __main__.beta, __main__.gamma = alpha, beta, gamma
        self.assertAlmostEqual(calc_q(h, k, l), q)

    def check_f_coefs(self, read_form_factor_coefs):
        coeffs = read_form_factor_coefs()
        cZn = np.array([14.0743, 3.2655, 7.0318, 0.2333, 5.1652, 10.3163,
                        2.41, 58.7097, 1.3041])
        self.assertTrue(np.allclose(coeffs['Zn'], cZn))

    def check_form_factor(self, calc_f):
        q = 3.065272
        f = 22.696999395501315
        self.assertAlmostEqual(calc_f('Zn', q), f)

    def check_structure_factor(self, calc_absF):
        atoms = [( 'Zn', np.array((0.25, 0.25, 0.25)) ),
                 ( 'Zn', np.array((0.75, 0.75, 0.25)) ),
                 ( 'Zn', np.array((0.75, 0.25, 0.75)) ),
                 ( 'Zn', np.array((0.25, 0.75, 0.75)) ),
                 ( 'S', np.array((0.0, 0.0, 0.0)) ),
                 ( 'S', np.array((0.5, 0.5, 0.0)) ),
                 ( 'S', np.array((0.5, 0.0, 0.5)) ),
                 ( 'S', np.array((0.0, 0.5, 0.5)) ),
                ]
        hkl = np.array((3,1,1))
        __main__.a = __main__.b = __main__.c = 0.541
        __main__.alpha = __main__.beta = __main__.gamma = np.pi/2
        F = 9.2650300427526773
        self.assertAlmostEqual(calc_absF(hkl, atoms), F)

    def check_intensity_calculation(self, calc_I):
        __main__.a = __main__.b = __main__.c = 0.541
        __main__.alpha = __main__.beta = __main__.gamma = np.pi/2
        __main__.atoms = [( 'Zn', np.array((0.25, 0.25, 0.25)) ),
                          ( 'Zn', np.array((0.75, 0.75, 0.25)) ),
                          ( 'Zn', np.array((0.75, 0.25, 0.75)) ),
                          ( 'Zn', np.array((0.25, 0.75, 0.75)) ),
                          ( 'S', np.array((0.0, 0.0, 0.0)) ),
                          ( 'S', np.array((0.5, 0.5, 0.0)) ),
                          ( 'S', np.array((0.5, 0.0, 0.5)) ),
                          ( 'S', np.array((0.0, 0.5, 0.5)) ),
                         ]
        # Check for a systematic absence:
        theta, I = calc_I((2,1,0), 1.)
        self.assertAlmostEqual(I, 0.)
        # A known reflection intensity
        theta, I = calc_I((2,2,0), 1.)
        self.assertAlmostEqual(theta, 0.41431967623590099)
        self.assertAlmostEqual(I, 93055.512423882596)
        

check = Tests()
def run_check(check_name, func, hint=False):
    try:
        getattr(check, check_name)(func)
    except check.failureException as e:
        printmd('**<span style="color: red;">FAILED</span>**')
        if hint:
            print('Hint:',  e)
        return
    printmd('**<span style="color: green;">PASSED</span>**')
    
