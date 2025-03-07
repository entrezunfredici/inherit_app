from inherit_app.héritage.personnage import Personnage

class Mage(Personnage):
    def __init__(self, nom, pv, force, intelligence, endurance, mana):
        super().__init__(nom, pv, force, intelligence, endurance, mana)

    def attaque(self):
        super().attaquer()
        self.mana = self.mana - 10
