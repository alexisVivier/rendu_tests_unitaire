from utils import PoolUtils

class Heater():

    def __init__(self, functions: PoolUtils):
        super().__init__()
        self.pool_utils = functions

    def init_heater(self):
        average = self.list_average(self.functions.get_last_days_temps())
        actual_temp = self.functions.get_actual_temp()
        return average > 20 and actual_temp > 25

    def list_average(self, list):
        sum = 0
        for item in list:
            sum += item
        total_items = len(list)
        return sum/total_items
