from postac import *
from random import *
from potka import *

class Wiedzma(Postac):
    def __init__(self):
        self.koszt_ucieczki = 30
        super().__init__("Wiedzma", 10 , 100 , "ciemna")
        self.blok = False
        self.nagroda = 40
        p = Potka()
        self.ekwipunek.append(p)
    

    def zaatakuj(self, cel):
        losowanie = randint(0,1)
        if losowanie == 0:
            print("Wiedzma zblokowala twoj atak")
            self.blok = True
        super().zaatakuj(cel)
    

    def przyjmij_atak(self, sila):
        if self.blok==True:
            print("wiedzma blokuje twoj atak")
            self.blok = False
            return
        self.hp -= sila
    
