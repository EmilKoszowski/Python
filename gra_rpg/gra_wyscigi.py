import random

class Auto:
    def __init__(self, nazwa, predkosc, przyspieszenie, wytrzymalosc, nitro, paliwo):
        self.nazwa = nazwa
        self.predkosc = predkosc
        self.przyspieszenie = przyspieszenie
        self.wytrzymalosc = wytrzymalosc
        self.nitro = nitro
        self.paliwo = paliwo

    def ulepsz_predkosc(self):
        self.predkosc += 10
        print(f"Prędkość {self.nazwa} została ulepszona do {self.predkosc}.")

    def ulepsz_przyspieszenie(self):
        self.przyspieszenie += 1
        print(f"Przyspieszenie {self.nazwa} zostało ulepszone do {self.przyspieszenie}.")

    def ulepsz_wytrzymalosc(self):
        self.wytrzymalosc += 5
        print(f"Wytrzymałość {self.nazwa} została ulepszona do {self.wytrzymalosc}.")

    def ulepsz_nitro(self):
        self.nitro += 1
        print(f"System nitro {self.nazwa} został ulepszony do poziomu {self.nitro}.")

    def zatankuj(self):
        self.paliwo = 100
        print(f"Paliwo {self.nazwa} zostało uzupełnione do pełna.")

    def napraw(self):
        self.wytrzymalosc = 100
        print(f"{self.nazwa} został naprawiony do pełnej wytrzymałości.")

    def scigaj_sie(self, przeciwnik):
        wynik = (self.predkosc * random.uniform(0.8, 1.2)) + (self.przyspieszenie * random.uniform(0.8, 1.2)) + (self.wytrzymalosc * random.uniform(0.8, 1.2)) + (self.nitro * random.uniform(0.8, 1.2))
        wynik_przeciwnika = (przeciwnik.predkosc * random.uniform(0.8, 1.2)) + (przeciwnik.przyspieszenie * random.uniform(0.8, 1.2)) + (przeciwnik.wytrzymalosc * random.uniform(0.8, 1.2)) + (przeciwnik.nitro * random.uniform(0.8, 1.2))
        
        print(f"{self.nazwa} uzyskał wynik {wynik:.2f}")
        print(f"{przeciwnik.nazwa} uzyskał wynik {wynik_przeciwnika:.2f}")
        
        if wynik > wynik_przeciwnika:
            print(f"{self.nazwa} wygrał wyścig!")
            return True
        else:
            print(f"{przeciwnik.nazwa} wygrał wyścig!")
            return False

        modyfikator_trasy = trasa.modyfikator(self)
        wynik = ((self.predkosc * random.uniform(0.8, 1.2)) +
                 (self.przyspieszenie * random.uniform(0.8, 1.2)) +
                 (self.wytrzymalosc * random.uniform(0.8, 1.2)) +
                 (self.nitro * random.uniform(0.8, 1.2))) * modyfikator_trasy

        wynik_przeciwnika = ((przeciwnik.predkosc * random.uniform(0.8, 1.2)) +
                             (przeciwnik.przyspieszenie * random.uniform(0.8, 1.2)) +
                             (przeciwnik.wytrzymalosc * random.uniform(0.8, 1.2)) +
                             (przeciwnik.nitro * random.uniform(0.8, 1.2)))

        print(f"{self.nazwa} uzyskał wynik {wynik:.2f}")
        print(f"{przeciwnik.nazwa} uzyskał wynik {wynik_przeciwnika:.2f}")
        
        if wynik > wynik_przeciwnika:
            print(f"{self.nazwa} wygrał wyścig!")
            return True
        else:
            print(f"{przeciwnik.nazwa} wygrał wyścig!")
            return False

class Trasa:
    def __init__(self, nazwa, typ):
        self.nazwa = nazwa
        self.typ = typ

    def modyfikator(self, auto):
        if self.typ == "Miasto":
            return 1.0 + (auto.przyspieszenie * 0.05)
        elif self.typ == "Autostrada":
            return 1.0 + (auto.predkosc * 0.05)
        elif self.typ == "Góry":
            return 1.0 + (auto.wytrzymalosc * 0.05)
        elif self.typ == "Pustynia":
            return 1.0 + (auto.nitro * 0.05)
        else:
            return 1.0

def wybierz_auto():
    print("Wybierz swoje auto:")
    print("1. Ferrari (Predkosc: 200, Przyspieszenie: 5, Wytrzymałość: 50, Nitro: 1, Paliwo: 100)")
    print("2. Lamborghini (Predkosc: 210, Przyspieszenie: 4, Wytrzymałość: 55, Nitro: 2, Paliwo: 100)")
    print("3. Porsche (Predkosc: 220, Przyspieszenie: 6, Wytrzymałość: 45, Nitro: 3, Paliwo: 100)")
    print("4. McLaren (Predkosc: 230, Przyspieszenie: 5, Wytrzymałość: 60, Nitro: 2, Paliwo: 100)")
    print("5. Bugatti (Predkosc: 240, Przyspieszenie: 7, Wytrzymałość: 70, Nitro: 3, Paliwo: 100)")
    
    wybor = input("Podaj numer auta: ")
    
    if wybor == '1':
        return Auto("Ferrari", 200, 5, 50, 1, 100)
    elif wybor == '2':
        return Auto("Lamborghini", 210, 4, 55, 2, 100)
    elif wybor == '3':
        return Auto("Porsche", 220, 6, 45, 3, 100)
    elif wybor == '4':
        return Auto("McLaren", 230, 5, 60, 2, 100)
    elif wybor == '5':
        return Auto("Bugatti", 240, 7, 70, 3, 100)
    else:
        print("Nieprawidłowy wybór, domyślnie wybrano Ferrari.")
        return Auto("Ferrari", 200, 5, 50, 1, 100)

def menu_ulepszen(auto):
    while True:
        print("\nMenu ulepszeń:")
        print("1. Ulepsz prędkość")
        print("2. Ulepsz przyspieszenie")
        print("3. Ulepsz wytrzymałość")
        print("4. Ulepsz system nitro")
        print("5. Zatankuj paliwo")
        print("6. Napraw auto")
        print("7. Zakończ ulepszanie")
        wybor = input("Wybierz opcję: ")
        
        if wybor == '1':
            auto.ulepsz_predkosc()
        elif wybor == '2':
            auto.ulepsz_przyspieszenie()
        elif wybor == '3':
            auto.ulepsz_wytrzymalosc()
        elif wybor == '4':
            auto.ulepsz_nitro()
        elif wybor == '5':
            auto.zatankuj()
        elif wybor == '6':
            auto.napraw()
        elif wybor == '7':
            print("Zakończono ulepszanie.")
            break
        else:
            print("Nieprawidłowy wybór, brak ulepszeń.")

def powitanie():
    print("Witaj w grze wyścigowej!")
    print("Twoim celem jest pokonanie wszystkich przeciwników i ulepszanie swojego auta.")
    print("Powodzenia!\n")

def info_auto(auto):
    print(f"\nInformacje o aucie:")
    print(f"Nazwa: {auto.nazwa}")
    print(f"Prędkość: {auto.predkosc}")
    print(f"Przyspieszenie: {auto.przyspieszenie}")
    print(f"Wytrzymałość: {auto.wytrzymalosc}")
    print(f"Nitro: {auto.nitro}")
    print(f"Paliwo: {auto.paliwo}\n")

def losowy_event(auto):
    event = random.choice(["nic", "drobne uszkodzenie", "znaleziono ulepszenie", "strata paliwa", "bonus paliwa"])
    if event == "drobne uszkodzenie":
        auto.wytrzymalosc -= 5
        print("Twoje auto doznało drobnych uszkodzeń. Wytrzymałość zmniejszona o 5.")
    elif event == "znaleziono ulepszenie":
        auto.predkosc += 5
        auto.przyspieszenie += 1
        print("Znaleziono ulepszenie! Prędkość zwiększona o 5, przyspieszenie zwiększone o 1.")
    elif event == "strata paliwa":
        auto.paliwo -= 10
        print("Twoje auto straciło trochę paliwa. Paliwo zmniejszone o 10.")
    elif event == "bonus paliwa":
        auto.paliwo += 10

def wyscigi():
    powitanie()
    moje_auto = wybierz_auto()
    info_auto(moje_auto)
    przeciwnicy = [
        Auto("Tesla Roadster", 190, 3, 30, 1 ,100),
        Auto("Aston Martin", 200, 5, 35, 1, 100),
        Auto("Koenigsegg", 210, 6, 45, 2, 100),
        Auto("Pagani", 220, 7, 60, 2, 100),
        Auto("Bugatti Veyron", 230, 8, 70, 3, 100)
    ]

    for i, przeciwnik in enumerate(przeciwnicy, 1):
        print(f"\nWyścig {i} z {przeciwnik.nazwa}")
        losowy_event(moje_auto)
        
        if moje_auto.scigaj_sie(przeciwnik):
            if i < len(przeciwnicy):
                menu_ulepszen(moje_auto)
        else:
            print("Przegrałeś wyścig. Gra kończy się.")
            return
        info_auto(moje_auto)
    
    print("Gratulacje! Pokonałeś wszystkich przeciwników!")

if __name__ ==  "__wyscigi__":
    wyscigi()
    