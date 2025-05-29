import random

class Roulette:
    def __init__(self):
        self.couleur = {0: "vert"}
        # Rouge si impair, noir si pair (sauf 0)
        for i in range(1, 37):
            if i % 2 != 0:
                self.couleur[i] = "rouge"
            else:
                self.couleur[i] = "noir"

    def tourner(self):
        numero = random.randint(0, 36)
        couleur = self.couleur[numero]
        print(f"La couleur tombée est... {couleur}")
        return numero, couleur

    def jouer(self, choix):
        numero, couleur = self.tourner()
        if isinstance(choix, int) and choix == numero:
            print("Gain Exact !")
            return 35
        elif choix == couleur:
            print("Gain Exact !")
            return 2
        else:
            print("Dommage...")
            return -3

solde = 5
jeu = Roulette()

while solde >= 0:
    mise = input("Choisir entre 'rouge' et 'noir' ou un numéro (0-36): ")
    gain = jeu.jouer(mise)
        
    if gain > 0:
        solde += gain
    elif gain < 0:
        solde += gain
        if solde < 0:
            print("No money mister.. Trop nul")
    if solde > 0:
        print(f"Solde actuel : {solde}")


