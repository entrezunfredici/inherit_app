from pizza import Pizza
from pizzayolo import Pizzayolo

pâte = "pâte a pizza"
ingrédients = {
    "Reine": [
        "sauce tomate",
        "champignons",
        "jambon",
        "fromage rappé"
    ],
    "Chorizo": [
        "sauce tomate",
        "Chorizo",
        "fromage rapé",
        "origan",
        "poivron",
        "champignons",
        "mozzarella",
        "crème liquide",
        "basillic"
    ],
    "Regina": [
        "jambon",
        "champignon"
    ]
}

class Commande(Pizza):
    def add_pizza(self, nom_pizza):
        self.pizza.append(Pizza.__init__(self, pâte, nom_pizza, ingrédients[nom_pizza], False))

    def do_commande(self, pizza):
        mario = Pizzayolo.__init__("mario")
        for pizza in self.pizza:
            mario.cuire_pizza(pizza)
