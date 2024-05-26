from postac import *

class Superman(Postac):
    def __init__(self):
        self.mana = 120
        self.laser = 45
        self.ile_laser = 0
        super().__init__("Superman", 15, 250, "dobry")
    
    def zaatakuj(self, cel):
        if self.ile_laser > 0:
            print("ogien laseru zadaje 5hp")
            cel.hp-=5
        if (self.mana < 30):
            print("wykonujesz zwykly atak")
            super().zaatakuj(cel)
        else:
            print("wybierz sposob ataku: 1 - zwykly, 2 - laser (koszt - 30 many)")
            w = int(input("wybor: "))
            while w != 1 and w != 2:
                print("nieprawidlowy wybor. sprobuj jeszcze raz")
                w = input("wybor: ")
            if w == 1:
                print("wybrales zwykly atak")
                super().zaatakuj(cel)
            else:
                print("wybrales atak laserem")
                self.zaatakuj_laserem(cel)



    def zaatakuj_laserem(self, cel):
        self.mana -= 30
        self.ile_laser += 3
        cel.przyjmij_atak(self.laser)
  
         
