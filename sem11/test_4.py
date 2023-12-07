import unittest
from n4 import decode, Caesar

class Test_4(unittest.TestCase):
    def test_int(self):
        self.assertEqual(decode(168373, 5), '168373', "should be 168373")
    def test_error(self):
        self.assertEqual(decode('some text','r'), 'error', 'should be error')
    def test_empty_str(self):
        self.assertEqual(decode('', 1), '', 'should be empty str')

    def test_strange_key(self):
        self.assertEqual(decode('абвгд', 100), 'яабвг' ,'should be')
    def test_null_key(self):
        self.assertEqual(decode('текст', 0), 'текст', 'should be текст')
    def test_usual(self):
        self.assertEqual(decode('сх нсусднл жс рн', 3), 'от коробки до нк', 'should be от коробки до нк')
    def test_usual2(self):
        self.assertEqual(decode('Фхузхесснцч фхнъуинч ж ёнёрнучйпш: — Зий ёнёрнучйпехб? — Ж ехънжй. — Хемехънжнхшочй, фулершоцче.', 5), 'Программист приходит в библиотеку: — Где библиотекарь? — В архиве. — Разархивируйте, пожалуйста.','should be anecdote')

if __name__ == '__main__': unittest.main()
