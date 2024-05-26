class Team_R:
    def __init__(self,pokemon):
        self.pokemon = pokemon

    def walka(self, lista_pok):
        print("Spotykasz team R bedziesz musial z nimi walczyc")
        print("Wybierz swojego pokemona: ")
        for k in range(len(lista_pok)):
            print(f"{k}: {lista_pok[k]}")
        wp = int(input("twoj wybor: "))
        while (wp<0 or wp>=len(lista_pok)):
            print("Niepoprawny wybor")
            wp = int(input("twoj wybor: "))
        print("twoj pokemon: ")
        print(lista_pok[wp])
        lista_pok[wp].kondycja -= 20
        print("Ich pokemon : ")
        print(self.pokemon)
        if lista_pok[wp].cp > self.pokemon.cp:
            print("Wygrales! Zdobywasz ich pokemona")
            return True
        else:
            a = lista_pok[wp].cp // 5
            print(f"Przegrales! Twoj pokemon {lista_pok[wp].nazwa} traci {a} cp")
            lista_pok[wp].cp -= a
            return False