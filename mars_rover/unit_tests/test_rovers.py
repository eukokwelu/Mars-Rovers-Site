import datetime
import unittest
from rovers import Rover, Perseverance, Curiosity, Spirit, Opportunity


class TestRovers(unittest.TestCase):

    def setUp(self) -> None:
        self.pers = Perseverance()

    def test_check_date_empty(self):
        date = 'bad_date'
        self.assertFalse(self.pers.check_date(date))

    def test_check_date_datetime(self):
        date = datetime.date(2021, 3, 1)
        self.assertTrue(self.pers.check_date(date))


if __name__ == '__main__':
    unittest.main()
