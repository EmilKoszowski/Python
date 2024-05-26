

class Postac:
    def __init__(self,nazwa,atak,hp, strona):
        self.nazwa = nazwa
        self.atak = atak
        self.hp = hp
        self.strona = strona
        self.odbicie = False
        self.ekwipunek = []
        self.blok = False
        self.laska = False
    
    def __str__(self):
        return f"postac - nazwa: {self.nazwa}, atak: {self.atak}. hp: {self.hp}, strona: {self.strona}"

    
    def zaatakuj(self, cel):
        if cel.odbicie==True:
            print("Lustrzaniec odbija twoj atak")
            self.hp -= self.atak
            cel.odbicie = False
            return
        cel.przyjmij_atak(self.atak)
    

    def przyjmij_atak(self, sila):
        self.hp -= sila



