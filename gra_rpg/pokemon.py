from random import *

class Pokemon:
    def __init__(self,cp,zywiol,nazwa,procent):
        self.cp = cp
        self.zywiol = zywiol
        self.nazwa = nazwa
        self.procent = procent
        self.kondycja = 100 
    
    def __str__(self):
        return f" nazwa : {self.nazwa}, cp: {self.cp}, zywiol : {self.zywiol}, szansa na zlapanie : {self.procent} procent, kondycja: {self.kondycja}"

    def zlap(self):
        z = randint(1,100)
        if z <= self.procent:
            print("Udało ci sie zlapac pokemona")
            return True
        else:
            print("Niestety pokemon ci uciekl")
            return False





