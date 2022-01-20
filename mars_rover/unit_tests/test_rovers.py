import unittest
from mars_rover import rovers


class TestRovers(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_check_date_empty(self):
        date = ''
        self.assertFalse(rovers.Rover.check_date(date))


if __name__ == '__main__':
    unittest.main()
