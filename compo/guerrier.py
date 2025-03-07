from inherit_app.compo.container import Personnage, PeutFrapper

class Guerrier(Personnage):
    def __init__(self, nom, pv, force, intelligence):
        super().__init__(nom, pv, force, intelligence)
