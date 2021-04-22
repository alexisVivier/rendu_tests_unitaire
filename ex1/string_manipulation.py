class StringManipulation():

    def list_to_string(self, list):
        result = ""
        for item in list:
            if result == "" :
                result = item
            else:
                result = result + " " + item
        return result

    def list_average(self, list):
        sum = 0
        for item in list:
            sum += item
        total_items = len(list)
        return sum/total_items
