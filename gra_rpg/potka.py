from ekwipunek import *

class Potka(Ekwipunek):
    def __init__(self):
        self.leczenie = 30
        super().__init__("Potka", f"Potka lecznicza, zwieksza twoje hp  o {self.leczenie}")
        

    def uzyj(self, obiekt):
        print(f"Uzywasz potki, twoje hp zwieksza sie o {self.leczenie}")
        obiekt.hp += self.leczenie