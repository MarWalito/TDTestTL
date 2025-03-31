class Pizza:
    
    def __init__(self, name: str, ingredients: list, price: float):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __repr__(self):
        return f"Pizza({self.name}, {self.ingredients}, {self.price}€)"