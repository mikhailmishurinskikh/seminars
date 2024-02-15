import unittest
from n2 import l_s

class Test_2(unittest.TestCase):

    def test_error1(self):
        self.assertEqual(l_s(1, 2), 'invalid values', 'should be error')
    def test_error2(self):
        self.assertEqual(l_s((1,2), (2,3,4)), 'invalid values', 'should be error')
    def test_error3(self):
        self.assertEqual(l_s((1,'2'), (3,4)), 'invalid values', 'should be error')
    def test_error4(self):
        self.assertEqual(l_s((1, 1),(1, 100)), 'invalid values', 'should be error')

    def test_usual_values1(self):
        self.assertEqual(l_s((1,2), (1,2)), (1, 0), 'should be (1,0)')
    def test_usual_values2(self):
        self.assertEqual(l_s((0, 1440, 1334, 1221, 1103, 1010),
            (1.7, 23.4, 21.7, 20.1, 18.6, 16.9)), (0.02, 1.73), 'should be (0.02,1.73)')
    def test_usual_values3(self):
        self.assertEqual(l_s((1, 100, 50),(100, 1, 50)), (-1.0, 100.66), 'should be (-1.0, 100.66) ')
    def test_strange_values(self):
        self.assertEqual(l_s((1, 1, -10),(1, 100, 2)), (4.41, 46.09), 'should be (4.41, 46.09) ')
                            
if __name__ == "__main__":
    unittest.main()
