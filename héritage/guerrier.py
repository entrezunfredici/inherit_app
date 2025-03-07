from inherit_app.héritage.personnage import Personnage, PeutJeterUnSort

class Guerrier(Personnage):
    def __init__(self, nom, pv, force, intelligence, endurance, mana):
        super().__init__(nom, pv, force, intelligence, endurance, mana)

    def frapper(self):
        if self.endurance > 0:
            degats = self.endurance * 2
            self.endurance -= 1
            print(f"{self.nom} frappe avec une force de {degats} points de dégâts!")
            return degats
        else:
            print(f"{self.nom} n'a plus d'endurance pour frapper.")
            return 0
