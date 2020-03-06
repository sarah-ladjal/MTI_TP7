import sys
class Compte(object):
    pass
class Vendeur(Compte):
    def draw(self): print("Vendeur.draw")

    def erase(self): print("Vendeur.erase")

class Visiteur(Compte):
    def draw(self): print("Visiteur.draw")

    def erase(self): print("Visiteur.erase")

class Gestionnaire(Compte):
    def draw(self): print("Gestionnaire.draw")

    def erase(self): print("Gestionnaire.erase")

class CompteFactory:
    @staticmethod
    def createCompte(type):
        if type == "Vendeur":
            return Vendeur()
        elif type == "Visiteur":
            return Visiteur()
        if type == "Gestionnaire":
            return Gestionnaire()

        else:
            print("Bad Compte creation: " + type)
    #sys.exit()



if __name__ == "__main__":
    for type in ("Vendeur", "Visiteur" ,"Gestionnaire"):
        compte = CompteFactory.createCompte(type)
        compte.draw()
        compte.erase()