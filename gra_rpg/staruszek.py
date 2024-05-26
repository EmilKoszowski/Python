from postac import *
from random import *
from laska import *

class Staruszek(Postac):
    def __init__(self):
        self.koszt_ucieczki = 40
        super().__init__("Staruszek", 15 , 120 , "ciemna")
        self.laska = False
        self.nagroda = 50
        l = Laska()
        self.ekwipunek.append(l)
    

    def przyjmij_atak(self, sila):
        losowanie = randint(0,1)
        if self.laska==True:
            if losowanie == 1:
                print("Nie trafiles przeciwnika bo ogłuszył cie")
            else:
                print("Fartem trafiles przeciwnika pomimo uderzenia laska") 
                self.hp -= sila
            self.laska = False
        else:
            self.hp -= sila
    
    def zaatakuj(self,cel):
        losowanie = randint(0,1)
        if losowanie == 0:
            print("Staruszek uderzyl cie swoja laska kreci ci sie w glowie masz 50% szans na trafienie go")
            self.laska = True
        super().zaatakuj(cel)
    