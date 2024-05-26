from postac import *
from random import *

class Rycerz(Postac):
    def __init__(self):
        self.tarcza = 100
        self.mana = 120
        super().__init__("rycerz", 20, 200, "dobry")
    def zaatakuj(self, cel):
        if (self.mana < 30):
            print("wykonujesz zwykly atak")
            cel.przyjmij_atak(self.atak)
        else:
            print("wybierz sposob ataku: 1 - zwykly, 2 - wezwij armie szkieletow (koszt - 30 many)")
            w = int(input("wybor: "))
            while w != 1 and w != 2:
                print("nieprawidlowy wybor. sprobuj jeszcze raz")
                w = int(input("wybor: "))
            if w == 1:
                print("wybrales zwykly atak")
                cel.przyjmij_atak(self.atak)
            else:
                print("wybrales atak armia szkieletow")
                self.armia_szkieletow(cel)
        
    
    def armia_szkieletow(self, cel):
        self.mana -= 30
        szkielety = randint(45,60)
        print(f"Przywolujesz {szkielety} szkieletow. Kazdy zabiera przeciwnikowi 1 hp")
        cel.przyjmij_atak(szkielety)
        
    
    def __str__(self):
        return f"postac - nazwa: {self.nazwa}, atak: {self.atak}. hp: {self.hp}, hp tarczy: {self.tarcza}, strona: {self.strona}"

    def przyjmij_atak(self, sila):
        if self.tarcza >= sila:
            self.tarcza -= sila
        else:
            sila2 = sila - self.tarcza
            self.tarcza = 0
            self.hp -= sila2



