import unittest
from n3 import qsort
from random import shuffle

class Test_2(unittest.TestCase):
    def test_error(self):
        self.assertEqual(qsort(['1',2]), 'error', "should be error")
    def test_error_none(self):
        self.assertEqual(qsort(None), 'error', "should be error")
    def test_empty(self):
        self.assertEqual(qsort([]), [], 'should be []')

    def test_str(self):
        self.assertEqual(qsort(['a', 'c', 'b']), ['a', 'b', 'c'], 'should be a, b, c')
    def test_int(self):
        self.assertEqual(qsort([4, 2, 1, 3]), [1, 2, 3, 4], 'should be 1, 2, 3, 4')
    def test_float(self):
        self.assertEqual(qsort([4.1, 2.0, 1, 3]), [1, 2.0, 3, 4.1], 'should be 1, 2, 3, 4')
    def test_reverse_array(self):
        array = [i for i in range(100, 0, -1)]
        self.assertEqual(qsort(array), [i for i in range(1, 101)], 'should be 1, 2, .., 100')
    def test_sort_array(self):
        array = [i for i in range(1, 101)]
        self.assertEqual(qsort(array), array, 'should be 1, 2, .., 100')
    def test_random_array(self):
        array = [i for i in range(1, 101)]
        sh_array = array+[]
        shuffle(sh_array)
        self.assertEqual(qsort(sh_array), array, 'should be 1, 2, .., 100')

if __name__ == '__main__': unittest.main()

