from rpg_glowny_program import *
from pokemony_glowny_program import *
from gra_wyscigi import *


print("Witaj graczu! W jaka gre chcesz zagrac: 1 - RPG, 2 - Pokemony, 3 - Gra poboczna(Wyścigi)")
wyb = int(input("twoj wybor: "))
while wyb!=1 and wyb!=2 and wyb!=3:
    print("Nieprrawidlowy wybor")
    wyb = int(input("twoj wybor: "))

if wyb==1:
    main()
elif wyb==2:
    program()
elif wyb==3:
    wyscigi()