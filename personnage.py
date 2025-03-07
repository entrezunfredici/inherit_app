
def Personnage():
    PV = 0
    intelligence = 0
    force = 0
    name = ""

    def attaquer(victime, dégâts):
        victime.PV = victime.PV-dégâts
