import unittest
from solution import visible_area


class TestVisibleArea(unittest.TestCase):

    def test_basic_functionality(self):
        mountains = [
            {'left': 9, 'right': 15, 'height': 3},
            {'left': 8, 'right': 14, 'height': 3},
            {'left': 0, 'right':  6, 'height': 3},
        ]
        self.assertEqual(visible_area(mountains), 20.75)

    def test_max_qty_same_mountain(self):
        mnt_1 = {'left': 0, 'right': 6, 'height': 3}
        mountains = [mnt_1.copy() for _ in range(1000)]
        self.assertEqual(visible_area(mountains), 9)

    def test_one_mountain(self):
        mountains = [{'left': 0, 'right': 6, 'height': 3}]
        self.assertEqual(visible_area(mountains), 9)

    def test_none_mountain(self):
        mountains = []
        self.assertEqual(visible_area(mountains), 0)

    # Additional test methods for other scenarios...


if __name__ == '__main__':
    unittest.main()
