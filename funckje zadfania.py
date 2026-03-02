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