from random import *

class Kasyno:
    def __init__(self, mana):
        self.pieniadze = mana

    
    def ruletka(self):
        print("O ile chcesz zagrac?")
        x = self.pieniadze + 1
        while (x>self.pieniadze):
            x = int(input("wprowadz liczbe: "))
            if (x>self.pieniadze):
                print("Nie stac cie, wprowadz inna liczbe")
        
        print("wybierz kolor: 1 - czerwony (szansa na trafienie 48%, wygrana 2*zaklad), 2 - czarny (szansa na trafienie 48%, wygrana 2*zaklad), 3 - zielony (szansa na trafienie 4%, wygrana 100*zaklad). ")
        wybor = int(input("wybor: "))
        while wybor!=1 and wybor!=2 and wybor!=3:
            print("niepoprawny wybor")
            wybor = int(input("wybor: "))
        
        if wybor==1:
            print("wybrales kolor czerwony")
            m = 2
        elif wybor==2:
            print("wybrales kolor czarny")
            m = 2
        else:
            print("wybrales kolor zielony")
            m = 100
        los = randint(1,100)
        if los<48:
            los=1
        elif los<97:
            los=2
        else:
            los=3
        
        if wybor == los:
            print("Wygrales!!!!!")
            self.pieniadze += x*m-x
        else:
            print("przegrales")
            self.pieniadze-=x        


    def maszyna(self):
        print("O ile chcesz zagrac?")
        x = self.pieniadze + 1
        while (x>self.pieniadze):
            x = int(input("wprowadz liczbe: "))
            if (x>self.pieniadze):
                print("Nie stac cie, wprowadz inna liczbe")
        print("zasady: losowane sa 3liczby z zakresu 1-3. Jezeli trafisz 3 takie same to wygrywasz podwojona kwote zakladu. Jezeli wylosuja sie 2 takie same to wychodzisz na zero")
        licznik1 = 0
        licznik2 = 0
        licznik3 = 0
        for i in range(3):
            x = randint(1,3)
            if x==1:
                licznik1+=1
            elif x==2:
                licznik2+=1
            else:
                licznik3+=1
        takie_same = 0

        print(f"wylosowano {licznik1} jedynek, {licznik2} dwojek i {licznik3} trojek")

        if licznik1==0:
            if licznik2 == 0 or licznik2 == 3:
                takie_same = 3
            else:
                takie_same = 2
        elif licznik1 == 3:
            takie_same = 3
        elif licznik1==1:
            if licznik2==1:
                takie_same=1
            else:
                takie_same=2
        else:
            takie_same=2
        
        if takie_same==3:
            print("wygrales!!!")
            self.pieniadze += x
        elif takie_same<2:
            print("przegrales")
            self.pieniadze -= x
        else:
            print("wychodzisz na zero")

        

    
    def zagraj(self):
        while 1:
            if self.pieniadze == 0:
                print("niestety nie masz pieniedzy zeby grac dalej i zostajesz wyrzucony z kasyna")
                return
            print("wybierz 1 zeby zagrac, wybierz 2 zeby opuscic kasyno")
            w_k = int(input("twoj wybor: "))
            while w_k!=1 and w_k!=2:
                print("Niepoprawny wybor")
                w_k = int(input("twoj wybor: "))
            if w_k==1:
                print("wybierz gre: 1-ruletka, 2 - maszyna")
                w = int(input("twoj wybor: "))
                while w!=1 and w!=2:
                    print("Niepoprawny wybor")
                    w = int(input("twoj wybor: "))
                if w==1:
                    self.ruletka()
                else:
                    self.maszyna()
            else:
                return