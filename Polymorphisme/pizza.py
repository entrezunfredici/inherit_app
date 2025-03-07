class Pizza:
    def __init__(self, pâte, nom, ingrédients, cuit):
        self.name = nom
        self.ingrédients = ingrédients
        self.cuit = cuit
        self.pâte = pâte

    def cuire(self):
        self.cuit = True
