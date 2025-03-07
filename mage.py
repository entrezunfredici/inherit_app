from personnage import Personnage

class Mage(Personnage):
    Personnage.PV = 100
    Personnage.intelligence = 50
    Personnage.force = 150
    Personnage.name = "kévin"
    mana = 100

    def attaque(self):
        super().attaquer()
        self.mana = self.mana - 10
