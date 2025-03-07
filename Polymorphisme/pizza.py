class Pizza:
    def __init__(self, pâte, nom, ingrédients, cuit):
        self.name = nom
        self.ingrédients = ingrédients
        self.cuit = cuit
        self.pâte = pâte

    def cuire(self):
        if self.cuit:
            print("pizza déja cuite")
        else:
            self.cuit = True
        return self

    def __str__(self):
        return f"{self.nom} (PV: {self.pv}, Force: {self.force}, Intelligence: {self.intelligence}, Endurance: {self.endurance}, Mana: {self.mana})"