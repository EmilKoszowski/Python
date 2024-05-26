from ekwipunek import *

class Laska(Ekwipunek):
    def __init__(self):
        super().__init__("Laska", "Magiczna laska - pozwala ci ogluszyc przeciwnika, ktory bedzie mial przez to 50 procent szans ma trafienie cie w najblizszym ataku")
    
    def uzyj(self, obiekt):
        print("Uzywasz laski. Przeciwnik bedzie mial 50 procent szans w najblizszym ataku")
        obiekt.laska = True