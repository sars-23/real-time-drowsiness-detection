import unittest

from geometry import calculate_ear, calculate_mar


class GeometryTests(unittest.TestCase):
    def test_ear_for_symmetric_eye(self):
        eye = [(0, 0), (1, 2), (3, 2), (4, 0), (3, -2), (1, -2)]
        self.assertAlmostEqual(1.0, calculate_ear(eye))

    def test_mar_for_open_mouth(self):
        mouth = [(0, 3), (0, 1), (2, 3), (2, 1), (0, 0), (4, 0)]
        self.assertAlmostEqual(0.5, calculate_mar(mouth))

    def test_rejects_zero_denominator(self):
        with self.assertRaises(ValueError):
            calculate_ear([(0, 0)] * 6)

    def test_rejects_invalid_landmarks(self):
        with self.assertRaises(ValueError):
            calculate_mar([(0, 0)] * 5)
        with self.assertRaises(ValueError):
            calculate_ear([(0, 0), (1, 1), (1, 1), (2, 2), (1, 1), ("x", 1)])


if __name__ == "__main__":
    unittest.main()
