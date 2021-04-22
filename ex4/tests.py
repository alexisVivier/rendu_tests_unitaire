import unittest
from evaluation_tests.ex4.pool_utils import PoolUtils
from unittest import TestCase
from unittest.mock import MagicMock
from utils import PoolUtils

class TestPoolV1(TestCase):
    
    def test_pool_utils(self):
        mock = MagicMock()
        mock.get_actual_temp().return_value = 20
        mock.get_last_days_temps().return_value = [20, 21, 20, 19, 24, 20, 20]
        mock.set_heater().return_value = False

        pool_utils = PoolUtils()
        
        self.assertEqual(20, pool_utils.get_actual_temp())
        self.assertEqual([20, 21, 20, 19, 24, 20, 20], pool_utils.get_last_days_temps())
        self.assertEqual(False, pool_utils.set_heater())


unittest.main()