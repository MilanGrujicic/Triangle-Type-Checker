import main
import unittest


class TestMainFunctions(unittest.TestCase):
    def test_triangle_type(self):
        self.assertEqual(main.triangle_type(3, 4, 5), "Scalene and right.")

    def test_is_right_triangle(self):
        self.assertEqual(main.is_right_triangle(3, 4, 5), True)

if __name__ == "__main__":
    unittest.main()
