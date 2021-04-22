from heater import Heater
import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from utils import PoolUtils

class TestPoolV1(TestCase):
    
    def test_pool_utils(self):

        # On créé le mock
        mock = MagicMock()

        # On set les valeurs de retour attendues
        mock.get_actual_temp.return_value = 20
        mock.get_last_days_temps.return_value = [20, 21, 20, 19, 24, 20, 20]
        mock.set_heater.return_value = False

        # On instancie le heater  
        heater = Heater(functions=mock)
        
        # On lance les tests
        self.assertEqual(20, heater.pool_utils.get_actual_temp())
        self.assertEqual([20, 21, 20, 19, 24, 20, 20], heater.pool_utils.get_last_days_temps())
        self.assertEqual(False, heater.pool_utils.set_heater())


unittest.main()