import unittest, my_math
from subprocess import Popen, PIPE

class ProductTestCase(unittest.TestCase):
    def testIntegers(self):
        for x in range(-10,10):
            for y in range(-10,10):
                p = my_math.product(x,y)
                self.assertTrue(p==x*y,'Interger multiplication failed')

    def testFloats(self):
        for x in range(-10,10):
            for y in range(-10,10):
                x = x/10.0
                y = y/10.0
                p = my_math.product(x,y)
                self.assertTrue(p == x*y, 'Float multiplication failed')

    def testWithPyLint(self):
        cmd = 'pylint', 'rn', 'my_math'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(str(pylint.stdout.read()),'')
        
    def product(factor1, factor2):
        'The product of two numbers'
        return factor1 * factor2
    
if __name__ == "__main__": unittest.main()
 
