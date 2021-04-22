import unittest
from unittest import result
from string_manipulation import StringManipulation

class TestEx1(unittest.TestCase):
    def test_list_to_string(self):
        string_manipulation = StringManipulation()
        array = ["Hello", "world"]
        result = string_manipulation.list_to_string(array)
        self.assertEqual(result, "Hello world")


    def test_list_average(self):
        string_manipulation = StringManipulation()
        array = [2, 2, 2, 2]
        result = string_manipulation.list_average(array)
        self.assertEqual(result, 2)
        


# if __main__ == "__main__":
unittest.main()