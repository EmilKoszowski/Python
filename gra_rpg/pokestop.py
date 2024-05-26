from item import *
from random import *

class Pokestop:
    def __init__(self):
        self.lista = [Pokeball(), Owoc()]
    
    def wybierz(self, lista_pok):
        w = randint(0,1)
        it = self.lista[w]
        it.uzyj(lista_pok)