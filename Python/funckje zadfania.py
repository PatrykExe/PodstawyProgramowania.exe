#Zadanie 0.3.
#a)
def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]

wynik = suma_v(u, v)

print(wynik)

#Zadanie 2.1

def czy_anagramy(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
#return sorted(s1) == sorted(s2):

#Zadamie 2.2

def jaki_trojkat(a, b, c):
    if a + b + c > 2 * max([a, b, c]):
        if a ** 2 + b ** 2 == 2 * max([a, b, c]) ** 2:
            print('prostokątny')
        if a ** 2 + b ** 2 > 2 * max([a, b, c]) ** 2:
            print('ostrokątny')
        if a ** 2 + b ** 2 < 2 * max([a, b, c]) ** 2:
            print('rozwartokątny')
    else:
        print('nie jest trojkatem')


jaki_trojkat(7, 10, 16)


#Zadanie 2.3
def liczby_niezalezne(lista):
    wynik = []
    for f in lista:
        dzielniki = []
        for u in lista:
            if f % u == 0:
                dzielniki.append(u)
        if len(dzielniki) == 1:
            wynik.append(f)
    return wynik
print(liczby_niezalezne([12, 7, 3, 6, 21, 74]))


#2(4, 5, 6, 7, 8)


def ileLiter(tekst):
    slownik = dict()
    zbior = set(tekst)
    for x in zbior:
        ile = tekst.count(x)
        slownik[x] = ile
    return slownik

print(ileLiter('babcia'))
