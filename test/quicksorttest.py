import unittest
import main

class quickSortTest(unittest.TestCase):
    def test_normal(self):
        expect = [1, 2, 3, 4]
        x = main.Sort([3, 4, 2, 1]).QUICKSORT()
        self.assertEqual(expect, x)
    def test_same(self):
        expect = [27, 27, 27]
        x = main.Sort([27, 27, 27]).QUICKSORT()
        self.assertEqual(expect, x)
    def test_normal_double(self):
        expect = [0.1, 0.2, 0.3]
        x = main.Sort([0.2, 0.1, 0.3]).QUICKSORT()
        self.assertEqual(expect, x)
    def test_normal_neg(self):
        expect = [-0.1, 0, 0.1]
        x = main.Sort([-0.1, 0, 0.1]).QUICKSORT()
        self.assertEqual(expect, x)
    def test_empty(self):
        expect = []
        x= main.Sort([]).QUICKSORT()
        self.assertEqual(expect, x)

if __name__ == '__main__':
    unittest.main()
