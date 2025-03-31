import unittest
from unittest.mock import MagicMock
from cartePizzeria import CartePizzeria
from cartePizzeriaException import CartePizzeriaException
from pizza import Pizza

class TestCartePizzeria(unittest.TestCase): 
    def setUp(self):
        self.carte = CartePizzeria()

    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty()) 
    
    def test_nb_pizza(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)
    
