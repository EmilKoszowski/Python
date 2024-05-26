from postac import *
from random import *
from blokada import *

class Lustrzaniec(Postac):
    def __init__(self):
        self.koszt_ucieczki = 45
        super().__init__("Lustrzaniec", "zalezy od godziny" , 100 , "ciemna")
        self.nagroda = 45
        self.odbicie = True
        b = Blokada()
        self.ekwipunek.append(b)
    

    def zaatakuj(self, cel):
        losowanie = randint(0,1)
        if losowanie == 0:
            print("Lustrzaniec odbije twoj nastepny atak")
            self.odbicie = True
        sila = abs(12 - self.godzina) * 3
        cel.przyjmij_atak(sila)
  
    

    def przyjmij_atak(self, sila):
        self.hp -= sila
    
