import unittest
from newTrainFile import add, get_system_status

class TestCalculatorAndSystem(unittest.TestCase):

    def test_add_strings(self):
        self.assertEqual(add("Hello", "World"), "Error Text")

    def test_get_system_status(self):
        status = get_system_status()
        self.assertIsInstance(status, tuple)
        self.assertEqual(len(status), 3)


if __name__ == "__main__":
    unittest.main()

