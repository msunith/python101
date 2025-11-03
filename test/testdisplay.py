
import unittest
from src.app.app import display

# Unit tests
class TestDisplay(unittest.TestCase):
    def test_display(self):
        r = display()
        self.assertEqual(r,None)

# Run the unit tests
if __name__ == '__main__':
    unittest.main()

