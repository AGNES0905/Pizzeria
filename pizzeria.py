# Classe Pizza : représente une pizza avec un nom, une liste d'ingrédients et un prix
class Pizza:
    def __init__(self, nom, ingredients, prix):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

    def __str__(self):
        return f"{self.nom} - Ingrédients: {', '.join(self.ingredients)} - Prix: {self.prix}€"


# Classe CartePizzeriaException : exception personnalisée pour la carte de la pizzeria
class CartePizzeriaException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Classe CartePizzeria : représente la carte de la pizzeria
class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    # Vérifie si la carte est vide
    def is_empty(self):
        return len(self.pizzas) == 0

    # Retourne le nombre de pizzas dans la carte
    def nb_pizzas(self):
        return len(self.pizzas)

    # Ajoute une pizza à la carte
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    # Retire une pizza de la carte par son nom
    def remove_pizza(self, name):
        pizza_to_remove = None
        for pizza in self.pizzas:
            if pizza.nom == name:
                pizza_to_remove = pizza
                break
        
        if pizza_to_remove is None:
            raise CartePizzeriaException(f"La pizza '{name}' n'existe pas sur la carte.")
        else:
            self.pizzas.remove(pizza_to_remove)
            print(f"La pizza '{name}' a été retirée de la carte.")
