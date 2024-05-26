czy_pokeball = False

class Item:
    def __init__(self, opis):
        self.opis = opis
    
    def uzyj(self, lista_pok):
        print(f"uzywasz itemu {self.opis}")


class Pokeball(Item):
    def __init__(self):
        super().__init__("Pokaball: Masz 100-procentowa szanse na zlapanie nastepnego pokemona")
    
    def uzyj(self, lista_pok):
        czy_pokeball = True
        super().uzyj(lista_pok)

class Owoc(Item):
    def __init__(self):
        super().__init__("Owoc - leczy wszystkie pokemony dodajac po 10 kondycji")
    
    def uzyj(self, lista_pok):
        for i in range(len(lista_pok)):
            lista_pok[i].kondycja = min(100,  lista_pok[i].kondycja+10)
        super().uzyj(lista_pok)