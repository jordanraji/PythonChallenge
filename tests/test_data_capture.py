import unittest

from DataCapture.DataCapture import DataCapture, Stats


class TestDataCapture(unittest.TestCase):
    def test_init(self):
        capture = DataCapture()
        self.assertIsInstance(capture.data, dict)
        self.assertEqual(capture.length, 0)
        self.assertEqual(capture.max_value, 0)
        self.assertEqual(len(capture.data), 0)

    def test_add(self):
        capture = DataCapture()
        for i in range(1, 4):
            capture.add(i)

        for i in range(3, 6):
            capture.add(i)

        self.assertEqual(capture.length, 6)
        self.assertEqual(capture.max_value, 5)
        self.assertEqual(capture.data[3].count, 2)

    def test_build_stats(self):
        capture = DataCapture()
        for i in range(1, 4):
            capture.add(i)
        stats = capture.build_stats()
        self.assertIsInstance(stats, Stats)


class TestStats(unittest.TestCase):
    def setUp(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        self.stats = capture.build_stats()

    def test_less(self):
        self.assertEqual(self.stats.less(3), 0)
        self.assertEqual(self.stats.less(4), 2)
        self.assertEqual(self.stats.less(6), 3)
        self.assertEqual(self.stats.less(9), 4)

    def test_greater(self):
        self.assertEqual(self.stats.greater(3), 3)
        self.assertEqual(self.stats.greater(4), 2)
        self.assertEqual(self.stats.greater(6), 1)
        self.assertEqual(self.stats.greater(9), 0)

    def test_between(self):
        self.assertEqual(self.stats.between(3, 6), 4)
        self.assertEqual(self.stats.between(3, 9), 5)
        self.assertEqual(self.stats.between(3, 3), 2)
        self.assertEqual(self.stats.between(4, 9), 3)
        self.assertEqual(self.stats.between(4, 6), 2)
        self.assertEqual(self.stats.between(4, 4), 1)


if __name__ == "__main__":
    unittest.main()
