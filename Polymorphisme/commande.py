from pizza import Pizza
from pizzayolo import Pizzayolo

pâte = "pâte a pizza"
ingrédients = {
    "Reine": [
        "sauce tomate",
        "champignons",
        "jambon"
    ],
    "Chorizo": [
        "sauce tomate",
        "Chorizo"
    ]
}

class Commande(Pizza):
    def add_pizza(self, nom_pizza):
        self.pizza.append(Pizza.__init__(self, pâte, nom_pizza, ingrédients[nom_pizza], False))

    def do_commande(self, pizza):
        mario = Pizzayolo.__init__("mario")
        for pizza in self.pizza:
            mario.cuire_pizza(pizza)
