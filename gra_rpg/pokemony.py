from pokemon import *


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(60, "Elektryczny", "Pikachu", 100)


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__(60, "Wodny", "Squirtle", 100)

class Charmander(Pokemon):
    def __init__(self):
        super().__init__(60, "Ognisty", "Charmander", 100)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(60, "Trawiasty", "Bulbasaur", 100)


class Ekans(Pokemon):
    def __init__(self):
        super().__init__(100, "Trawiasty", "Ekans", 80)

class Mim(Pokemon):
    def __init__(self):
        super().__init__(100, "Basniowy", "Mim", 80)

class Vulpix(Pokemon):
    def __init__(self):
        super().__init__(140, "Ognisty", "Vulpix", 70)

class Psyduck(Pokemon):
    def __init__(self):
        super().__init__(140, "Wodny", "Psyduck", 70)

class Poliwag(Pokemon):
    def __init__(self):
        super().__init__(80, "Wodny", "Poliwag", "nie dotyczy")

class Rapidash(Pokemon):
    def __init__(self):
        super().__init__(120, "Ognisty", "Rapidash", "nie dotyczy")

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__(50, "Trawiasty", "Caterpie", "nie dotyczy")