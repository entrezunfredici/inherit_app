class Personnage:
    def __init__(self, nom, pv, force, intelligence, endurance, mana):
        self.nom = nom
        self.pv = pv
        self.force = force
        self.intelligence = intelligence
        self.endurance = endurance
        self.mana = mana

    def prendre_degats(self, degats):
        self.pv -= degats
        print(f"{self.nom} a perdu {degats} PV. Il lui reste {self.pv} PV.")

    def est_vivant(self):
        return self.pv > 0

    def __str__(self):
        return f"{self.nom} (PV: {self.pv}, Force: {self.force}, Intelligence: {self.intelligence}, Endurance: {self.endurance}, Mana: {self.mana})"
