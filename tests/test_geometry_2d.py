import unittest

from src.geometry_2d import calculate_endpoint, calculate_two_link_endpoint

class TestGeometry2D(unittest.TestCase):

    def test_calculate_endpoint(self):
        # Test at 0 degrees
        x, y = calculate_endpoint(10, 0)
        self.assertAlmostEqual(x, 10, places=6)
        self.assertAlmostEqual(y, 0, places=6)

        # Test at 90 degrees
        x, y = calculate_endpoint(10, 90)
        self.assertAlmostEqual(x, 0, places=6)
        self.assertAlmostEqual(y, 10, places=6)

        # Test at 180 degrees
        x, y = calculate_endpoint(10, 180)
        self.assertAlmostEqual(x, -10, places=6)
        self.assertAlmostEqual(y, 0, places=6)

        # Test at 270 degrees
        x, y = calculate_endpoint(10, 270)
        self.assertAlmostEqual(x, 0, places=6)
        self.assertAlmostEqual(y, -10, places=6)

    def test_two_link_straight_horizontal(self):
        joint1, endpoint = calculate_two_link_endpoint(10, 5, 0, 0)

        self.assertAlmostEqual(joint1[0], 10, places=6)
        self.assertAlmostEqual(joint1[1], 0, places=6)
        self.assertAlmostEqual(endpoint[0], 15, places=6)
        self.assertAlmostEqual(endpoint[1], 0, places=6)

    def test_two_link_straight_vertical(self):
        joint1, endpoint = calculate_two_link_endpoint(10, 5, 90, 0)

        self.assertAlmostEqual(joint1[0], 0, places=6)
        self.assertAlmostEqual(joint1[1], 10, places=6)
        self.assertAlmostEqual(endpoint[0], 0, places=6)
        self.assertAlmostEqual(endpoint[1], 15, places=6)

    def test_two_link_at_30_degrees(self):
        joint1, endpoint = calculate_two_link_endpoint(10, 5, 30, 0)

        self.assertAlmostEqual(joint1[0], 8.660254, places=5)
        self.assertAlmostEqual(joint1[1], 5, places=6)
        self.assertAlmostEqual(endpoint[0], 12.990381, places=5)
        self.assertAlmostEqual(endpoint[1], 7.5, places=6)

    def test_two_link_with_positive_angles(self):
        joint1, endpoint = calculate_two_link_endpoint(10, 5, 45, 30)

        self.assertAlmostEqual(joint1[0], 7.071068, places=5)
        self.assertAlmostEqual(joint1[1], 7.071068, places=5)
        self.assertAlmostEqual(endpoint[0], 8.365163, places=5)
        self.assertAlmostEqual(endpoint[1], 11.900697, places=5)

    def test_two_link_with_negative_relative_angle(self):
        joint1, endpoint = calculate_two_link_endpoint(10, 5, 90, -45)

        self.assertAlmostEqual(joint1[0], 0, places=6)
        self.assertAlmostEqual(joint1[1], 10, places=6)
        self.assertAlmostEqual(endpoint[0], 3.535534, places=5)
        self.assertAlmostEqual(endpoint[1], 13.535534, places=5)

if __name__ == "__main__":
    unittest.main()
