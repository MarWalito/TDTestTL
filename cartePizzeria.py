from cartePizzeriaException import CartePizzeriaException
from pizza import Pizza
class CartePizzeria:
    
    def __init__(self):
        self.pizzas = {}

    def is_empty(self) -> bool:
        return len(self.pizzas) == 0

    def nb_pizzas(self) -> int:
        return len(self.pizzas)

    def add_pizza(self, pizza: Pizza):
        self.pizzas[pizza.name] = pizza

    def remove_pizza(self, pizza):
        self.pizzas.remove(pizza)

    def __repr__(self):
        return f"CartePizzeria({list(self.pizzas.values())})"