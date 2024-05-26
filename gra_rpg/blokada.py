from ekwipunek import *


class Blokada(Ekwipunek):
    def __init__(self):
        super().__init__("Blokada", "Blokada, pozwala ci zablokowac najblizszy atak przeciwnika")
    
    def uzyj(self, obiekt):
        print("Uzywasz blokady, nastepny atak przeciwnika zostanie zablokowany")
        obiekt.blok = True