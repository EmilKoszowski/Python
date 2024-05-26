from pokemon import *
from team_r import *
from pokemony import *
from item import *
from pokestop import *


def program():
    print("Jak masz na imie Trenerze?")
    imie = input("twoje imie: ")
    print(f"Witaj w swiecie Pokemon, {imie}")
    print("Czy chcesz rozpoczac przygode w lapaniu pokemonow? 1 - tak, 2- nie")
    w = int(input("twoj wybor: "))
    while w != 1 and  w!= 2:
        print("Nieprawidlowy wybor, wybierz jeszcze raz")
        w = int(input("twoj wybor: "))
    if w==2:
        return

    pozostale = [Pikachu(), Squirtle(), Charmander(), Bulbasaur(), Ekans(), Mim(), Vulpix(), Psyduck(), Team_R(Rapidash()), Team_R(Caterpie()), Team_R(Poliwag()), Pokestop(), Pokestop(), Pokestop(), Pokestop(), Pokestop()]
    zlapane = []
    kara = 0

    for i in range(12):
        print("Zlapane pokemony:")
        for j in zlapane:
            print(j)
        print("Wybierz kierunek: 1-gora, 2-dol, 3-lewo, 4-prawo")
        wk = int(input("twoj wybor: "))
        while wk != 1 and  wk!= 2 and wk!=3 and wk!=4:
            print("Nieprawidlowy wybor, wybierz jeszcze raz")
            wk = int(input("twoj wybor: "))
    
        indeks = randint(0, len(pozostale)-1)
        pok = pozostale[indeks]
        if type(pok) is Team_R:
            if len(zlapane) < 1:
                print("Trafiasz na Team R ale nie masz pokemona do obrony i Team R cie okrada. Dostajesz karne 100 punktow")
                kara+=100
                continue
            ww = pok.walka(zlapane)
            if ww==True:
                zlapane.append(pok.pokemon)
            del pozostale[indeks]
        elif type(pok) is Pokestop:
            print("Trafiles na pokestop. Zaraz wylosujesz specjalny item")
            pok.wybierz(zlapane)
            del pozostale[indeks]
        else:
            print("Znalazles pokemona: ")
            print(pok)
            print("Probujesz zlapac pokemona")
            if czy_pokeball==True:
                pok.procent = 100
                czy_pokeball = False
            wyn = pok.zlap()
            if wyn==True:
                zlapane.append(pok)
                del pozostale[indeks]
    print(f"Koniec gry! Zlapales {len(zlapane)} pokemonow")
    punkty = 0
    for p in zlapane:
        punkty += p.cp * p.kondycja // 100
    punkty -= kara
    print (f"Zdobyles {punkty} punktow")


