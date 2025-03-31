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
        
    def test_nb_pizza_mock(self): 
        pizza_mock = MagicMock()
        pizza_mock.name = "Quentinho"
        self.carte.pizzas = {pizza_mock}
        self.assertEqual(self.carte.nb_pizzas(), 1)
        self.carte.pizzas = {}

    def test_add_pizza_mock(self):
        pizza_mock = MagicMock()
        pizza_mock.name = "Aymerickinho"
        self.carte.add_pizza(pizza_mock)
        self.assertIn("Aymerickinho", self.carte.pizzas)
        self.carte.pizzas = {}

    




        
    


    
