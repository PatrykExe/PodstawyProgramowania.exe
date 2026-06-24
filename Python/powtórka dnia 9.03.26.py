#               ZADANIE 2.1

def czy_anagramy(slowo1, slowo2):
    if sorted(slowo1) == sorted(slowo2):
        return True
    else:
        return False

print(czy_anagramy('ginger', 'nigger'))

#               ZADANIE 2.2
def jaki_Trojkat(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        print('Prostokątny')
    elif a ** 2 + b ** 2 > c ** 2:
        print('ostrokątny')
    elif a ** 2 + b ** 2 < c ** 2:
        print('rozwartokątny')

print(jaki_Trojkat(3, 4, 5))

#               ZADANIE 2.3
def liczby_niezalezne(lista):
    liczby = []
    for x in lista:


print(liczby_niezalezne([11, 3, 5, 13, 54, 67, 2137, 8, 6]))
