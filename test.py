import unittest
from solution import visible_area
import random


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

    def test_boundary_conditions(self):
        mountains = [{'left': 0, 'right': 100000, 'height': 50000}]
        self.assertEqual(visible_area(mountains), 2500000000)

    def test_hidden_mountain(self):
        mountains = [
            {'left': 0, 'right': 6, 'height': 3},
            {'left': 2, 'right': 4, 'height': 1}
        ]
        self.assertEqual(visible_area(mountains), 9)

    def test_random_mountains_consistency(self):
        random.seed(42)
        mountains = []
        for _ in range(10):
            height = random.randint(1, 50000)
            left = random.randint(0, 100000 - 2 * height)
            right = left + 2 * height
            mountains.append({'left': left, 'right': right, 'height': height})
        area1 = visible_area(mountains)

        random.seed(42)
        mountains = []
        for _ in range(10):
            height = random.randint(1, 50000)
            left = random.randint(0, 100000 - 2 * height)
            right = left + 2 * height
            mountains.append({'left': left, 'right': right, 'height': height})
        area2 = visible_area(mountains)

        self.assertEqual(area1, area2)


if __name__ == '__main__':
    unittest.main()
