import unittest
from n1 import simple_multiplier

class Test_1(unittest.TestCase):

    def test_one(self):
        self.assertEqual(simple_multiplier(1), 1, 'should be 1')
    
    def test_null(self):
        self.assertEqual(simple_multiplier(0), 'error', 'should be error')

    def test_negative(self):
        self.assertEqual(simple_multiplier(-5), 'error', 'should be error')

    def test_usual(self):
        self.assertEqual(simple_multiplier(42), (2,3,7), 'should be error')

    def test_simple_num(self):
        self.assertEqual(simple_multiplier(97), (97), 'should be 97')
'''
    def test_big_num(self):
        self.assertEqual(simple_multiplier(878533656), (2,2,2,3,7,11,13,13,29,97),
                'should be 2,2,2,3,7,11,13,13,29,97')
'''
if __name__ == "__main__":
    unittest.main()
