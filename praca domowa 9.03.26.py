import random
#                           ZADANIE 2.4
In = int(input("Podaj liczbę Rzeczywistą: "))
Out = int(input("Podaj liczbę Rzeczywistą: "))
def losuj_z_przedzialu():
    print(random.randint(In, Out))

losuj_z_przedzialu()

#                           ZADANIE 2.5

slownik = {'Data': '966 rok naszej ery',
           'Nazwa': 'Chrzest Polski',
           'Opis': 'Mieszko I przyjmuje chrzest, czym zapewnia'
                   ' Polsce bezpieczniejszą pozycję w ówczesnej'
                   ' Europie.'
}
def notatka():
    print(f'{slownik['Nazwa']} odbył się w {slownik['Data']}. Krótko mówiąc: {slownik['Opis']}')

notatka()

#                           ZADANIE 2.6
wybrane_liczby = set()
arg1 = [1, 2, 6, 4, 5]
arg2 = [8, 4, 5, 2]
def unikatowe_elementy():
    for x in arg1:
        for y in arg2:
            if x in y:
                wybrane_liczby.add(x)
            else:
                continue
print(wybrane_liczby)

#                           ZADANIE 2.7
liczba = int(input('Podaj liczbę całkowitą +'))
def suma_dzielników():
    suma_dzielniki = 0
    for x in range(1, liczba + 1):
        if liczba % x == 0:
            suma_dzielniki += x
    print(suma_dzielniki)
suma_dzielników()

#                           ZADANIE 2.8 w
a = int(input('Podaj dowolną dużą liczbę: '))

def liczba_liczb():
    for x in range(a):

