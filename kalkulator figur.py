import math

def Pole_Kwadratu(a):
    return a**2

def Pole_Prostokąta(a, b): 
    return a * b 

def Pole_Trapezu(a, b, h):
    return [(a+b)*h]/2

def Pole_Trójkąta(a, h):
    return (a * h)/2

def Pole_Trójkąta_Równobocznego(a):
    return [((a**2)*3**(1/2))] / 4 

def Twierdzenie_Pitagorasa(a, b): 
    return (a**2 + b**2)**(1/2) 

def Pole_Koła(r):
    return (r**2) * 3,14 

def kalkulator():
    print("Witamy w kalkulatorze")
    while True:
        print("Opcje")
        print("1, Pole kwadratu")
        print("2, Pole prostokąta")
        print("3, Pole trapezu")
        print("4, Pole trójkąta")
        print("5, Pole trójkąta Równobocznego")
        print("6, Twierdzenie pitagorasa")
        print("7, Pole koła")
        print("8, Koniec")

wybor = input("wybierz opcje 1/2/3/4/5/6/7")

if wybor == '9':
    print("Dowidzenia")
    break 

if wybor == not in ('1', '2', '3', '4', '5', '6', '7', '8')
    print("Brak rozwiązania")
    continue

if wybor == '1':
    a = float(input("Podaj długość boku"))
    wynik = Pole_Kwadratu(a)
    print(f"Pole kwadratu wynosi: {wynik}")
elif wybor == '2':
    a = float(input("Podaj długość boku 1"))
    b = float(input("Podaj długość boku 2"))
    wynik = Pole_Prostokąta(a, b)
    print(f"Pole prostokąta wynosi: {wynik}")
elif wybor == '3':
    a = float(input("Podaj długość boku 1"))
    b = float(input("Podaj długość boku 2"))
    h = float(input("Podaj wysokość"))
    wynik = Pole_Trapezu(a, b, h)
    print(f"Pole trapezu wynosi: {wynik}")
elif wybor == '4':
    a = float(input("Podaj długość boku"))
    h = float(input("Podaj wysokość"))
    wynik = Pole_Trójkąta(a, h)
    print(f"Pole trójkąta wynosi: {wynik}")
elif wybor == '5':
    a = float(input("Podaj długość boku"))
    wynik = Pole_Trójkąta_Równobocznego(a)
    print(f"Pole trójkąta równobocznego wynosi: {wynik}")
elif wybor == '6':
    a = float(input("Podaj długość boku 1"))
    b = float(input("Podaj długość boku 2"))
    wynik = Twierdzenie_Pitagorasa(a, b)
    print(f"Twierdzenie pitagorasa wynosi: {wynik}")
elif wybor == '7':
    r = float(input("Podaj długość promienia"))
    wynik = Pole_Koła(r)
    print(f"Pole koła wynosi: {wynik}") 
if __name__ == "__main__": 
    kalkulator()