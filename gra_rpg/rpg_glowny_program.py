from postac import *
from rycerz import *
from wiedzma import *
from superman import *
from kasyno import *
from lustrzaniec import *
from staruszek import *




def main():
    print("Wybierz postac 1 - Rycerz 2 - Superman")
    w_p = int(input("twoj wybor: "))
    while w_p != 1 and w_p != 2:
        print("Nie ma takiego wyboru")
        w_p = int(input("twoj wybor: "))
    if w_p == 1:
        print("Twoja postac to Rycerz")
        twoja_postac = Rycerz()
    else:
        print("Twoja postac to Superman")
        twoja_postac = Superman()
    
    
    runda = 1
    godzina = 9
    pokonani = 0
    while twoja_postac.hp > 0:
        losowanie = randint(0,2)
        if losowanie==0:
            twoj_przeciwnik = Wiedzma()
        elif losowanie==1:
            twoj_przeciwnik = Lustrzaniec()
        else:
            twoj_przeciwnik = Staruszek()
        kolej = 0

        print(f"Czy chcesz podjac sie nastepnej walki? 1 - tak 2 - nie, uciekaj za {twoj_przeciwnik.koszt_ucieczki} many")
        w_p = int(input("twoj wybor: "))
        while w_p != 1 and w_p != 2:
            print("Nie ma takiego wyboru")
            w_p = int(input("twoj wybor: "))
        if w_p == 2:
            if twoja_postac.mana < twoj_przeciwnik.koszt_ucieczki:
                print("Musisz walczyc")
            else:
                twoja_postac.mana -= twoj_przeciwnik.koszt_ucieczki
                print("kolejny przeciwnik")
                runda += 1
                godzina+=3
                godzina = godzina%24
                pokonani+=1
                continue


        while twoja_postac.hp > 0 and twoj_przeciwnik.hp > 0:

            print(f"Godzina: {godzina}")
            print("Ty:")
            print(twoja_postac) 
            print(f"Masz {twoja_postac.mana} many")
            print("Przeciwnik:")
            print(twoj_przeciwnik)
            print(f"runda {runda}")
            if kolej==0:
                print("W tej rundzie ty bedziesz atakowal\n\n")
            else:
                print("w tej rundzie bedzie atak przeciwnika\n\n")

            if len(twoja_postac.ekwipunek) > 0:
                print("wybierz czy chcesz uzyc cos ze swojego ekwipunku")
                print("0: nie chce nic uzywac")
                for i in range(len(twoja_postac.ekwipunek)):
                    print(f"{i+1}: " + twoja_postac.ekwipunek[i].opis)
                w_e = int(input("twoj wybor: "))
                while w_e < 0 or w_e > len(twoja_postac.ekwipunek):
                    print("Niepoprawny wybor")
                    w_e = int(input("twoj wybor: "))
                if w_e > 0:
                    twoja_postac.ekwipunek[w_e-1].uzyj(twoja_postac)
                    del twoja_postac.ekwipunek[w_e-1]

            if runda % 4 == 1 and twoja_postac.mana>0:
                print(f"Czy chcesz usc do kasyna zagrac o dodatkowa mane?: 1-tak, 2-nie")
                w_k = int(input("twoj wybor: "))
                while w_k!=1 and w_k!=2:
                    print("Niepoprawny wybor")
                    w_k = int(input("twoj wybor: "))
                if w_k==1:
                    k = Kasyno(twoja_postac.mana)
                    k.zagraj()
                    twoja_postac.mana = k.pieniadze


            

            if kolej == 0:
                print("twoj atak")
                twoja_postac.zaatakuj(twoj_przeciwnik)
                kolej = 1
            else:
                print("atak przeciwnika")
                if twoja_postac.blok == True:
                    print("Atak przeciwnika zablokowany")
                    twoja_postac.blok = False
                elif twoja_postac.laska == True:
                    la = randint(0,1)
                    if la==1:
                        print("Ogluszony laska przeciwnik cie nie trafia")
                    else:
                        print("Przeciwnik fartem atakuje cie mimo ogluszenia laska")
                        twoj_przeciwnik.zaatakuj(twoja_postac)
                    twoja_postac.laska = False
                else:
                    twoj_przeciwnik.zaatakuj(twoja_postac)
                kolej = 0

            runda += 1
            godzina+=3
            godzina = godzina%24
            twoj_przeciwnik.godzina = godzina

        if twoja_postac.hp > 0:
            print("Przeciwnik pokonany! Przygotuj sie na nastepnego")
            twoja_postac.mana += twoj_przeciwnik.nagroda
            print(f"Otrzymujesz {twoj_przeciwnik.nagroda} many za zwyciestwo. Teraz masz lacznie {twoja_postac.mana}")
            pokonani+=1
            twoja_postac.ekwipunek.extend(twoj_przeciwnik.ekwipunek)
        else:
            print( f"Niestety przeciwnik cie zabil. Koniec gry! Pokonales {pokonani} przeciwników")





