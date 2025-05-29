import random

class Symbole:
    def __init__(self, nom, gain):
        self.nom = nom
        self.gain = gain

    def __str__(self):
        return self.nom

class MachineASous:
    def __init__(self):
        self.symboles = [
            Symbole("🍒", 4),
            Symbole("🍋", 6),
            Symbole("🔔", 10),
            Symbole("💎", 20)
        ]

    def tirer(self):
        tirage = []
        for i in range(3):
            symbole = random.choice(self.symboles)
            tirage.append(symbole)
        return tirage


    def jouer(self, mise):
        tirage = self.tirer()
        print("Résultat :", " | ".join(str(sym) for sym in tirage))

        if tirage[0].nom == tirage[1].nom == tirage[2].nom:
            gain = tirage[0].gain
            print(f"Jackpot ! Vous gagnez {gain} pièces.")
            return gain
        else:
            print("Perdu !")
            return -3

class Jeu:
    def __init__(self, solde_initial):
        self.solde = solde_initial
        self.machine = MachineASous()

    def lancer(self):
        while self.solde > 0:
            input(f"\nAppuyez sur Entrée pour jouer (pièces restantes : {self.solde})...")
            self.solde -= 1
            resultat = self.machine.jouer(1)
            if resultat > 0:
                self.solde += resultat
        print("\nVous n'avez plus de pièces. Fin de la partie.")

# Lancement du jeu
if __name__ == "__main__":
    jeu = Jeu(5)
    jeu.lancer()
