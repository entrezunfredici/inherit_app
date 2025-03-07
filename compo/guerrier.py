from inherit_app.compo.container import Container

class Guerrier(Container):
    def __init__(self, nom, pv, force, intelligence, endurance, mana):
        super().__init__(nom, pv, force, intelligence, endurance, mana)

    Container.__init__()
    self.frapper(cible, force)