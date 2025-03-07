class container():
    def __init__(self, nom, pv, force, intelligence, endurance, mana):
        self.nom = nom
        self.pv = pv
        self.force = force
        self.intelligence = intelligence
        self.endurance = endurance
        self.mana = mana

    def attaque(self, cible, force):
        if self.endurance > force:
            degats = self.force
            self.endurance -= force/2
            print(f"{self.nom} frappe avec une force de {degats} points de dégâts!")
            cible.pv -= degats
        else:
            print(f"{self.nom} n'a plus d'endurance pour frapper.")
            return 0

    def jeterunsort(self, cible, force):
        if self.mana > force:
            degats = self.force
            self.mana -= force/2
            print(f"{self.nom} jette un sort qui inlfide {degats} points de dégâts!")
            cible.pv -= degats
        else:
            print(f"{self.nom} n'a plus de mana pour jeter un sort.")
            return 0