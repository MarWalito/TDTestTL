from pizza import Pizza
from cartePizzeria import CartePizzeria
from cartePizzaExperience import CartePizzeriaException

carte = CartePizzeria()
    
pizza1 = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
pizza2 = Pizza("4 Fromages", ["mozzarella", "bleu", "parmesan", "chèvre"], 11.0)

carte.add_pizza(pizza1)
carte.add_pizza(pizza2)

print(carte)
print("Nombre de pizzas:", carte.nb_pizzas())

carte.remove_pizza("Margherita")  
print("Après suppression:", carte)

try:
    carte.remove_pizza("Pepperoni")
except CartePizzeriaException as error:
    print(error)