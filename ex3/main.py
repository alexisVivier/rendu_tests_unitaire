from format_string import FormatString
import unittest

class TestEx3(unittest.TestCase):
    
    # def test_format_string_with_line_breaks_and_hyphen(self):
    #     format_string = FormatString()
    #     result = format_string.format_string_with_line_breaks_with_hyphen("J’aimerai découper cette ligne:\nCette ligne est beaucoup trop longue alors je souhaite la découper", 20)
    #     self.assertEqual(result, "J’aimerai découper c-\nette ligne:\nCette li-\ngne est beaucoup tro-\np longue alors je so-\nuhaite la découper\n.")

    def test_format_string_with_line_breaks(self):
        format_string = FormatString()
        result = format_string.format_string_with_line_breaks("J’aimerai découper cette ligne:\nCette ligne est beaucoup trop longue alors je souhaite la découper", 20)



unittest.main()