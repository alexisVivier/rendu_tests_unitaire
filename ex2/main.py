import unittest
from leap_year import LeapYear

# class TestEx2V1(unittest.TestCase):

#     def test_is_leap_year(self):
#         leap_year = LeapYear()
#         result = leap_year.is_leap_year_v1(2016)
#         self.assertEqual(result, True)

class TestEx2V2(unittest.TestCase):

    # On teste pour une année bissextile
    def test_is_leap_year_true(self):
        leap_year = LeapYear()
        result = leap_year.is_leap_year_v2(2016)
        self.assertEqual(result, True)

    # On teste pour une année non bissextile
    def test_is_leap_year_false(self):
        leap_year = LeapYear()
        result = leap_year.is_leap_year_v2(2015)
        self.assertEqual(result, False)


# if __main__ == "__main__":
unittest.main()