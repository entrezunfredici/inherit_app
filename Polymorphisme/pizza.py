class Pizza:
    def __init__(self, nom, ingrédients, cuit):
        self.name = nom
        self.ingrédients = ingrédients
        self.cuit = cuit

    def fabriquer(self, degats):
        self.pv -= degats
        print(f"{self.nom} a perdu {degats} PV. Il lui reste {self.pv} PV.")

    def cuire(self):
        if self.cuit:
            print("pizza déja cuite")
        else:
            self.cuit = True
        return self

    def __str__(self):
        return f"{self.nom} (PV: {self.pv}, Force: {self.force}, Intelligence: {self.intelligence}, Endurance: {self.endurance}, Mana: {self.mana})"