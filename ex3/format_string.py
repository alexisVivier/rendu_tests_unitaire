import re

class FormatString():

    def format_string_with_line_breaks(slef, string, max_size):
        result = ""
        for index, char in enumerate(string):
            if char == " ":
                result += '\n'
            result += char

        print(result)


    def format_string_with_line_breaks_with_hyphen(self, string, max_size):
        lines = []
        for i in range(0, len(string), max_size):
            lines.append(string[i:i+max_size])
        return '-\n'.join(lines)