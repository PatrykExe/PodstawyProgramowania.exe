#Zadanie 1.1
lista = [4, 10, 12, 9, 5]
#Potęgi = [(4, 16, 64, 256), (10, 100, 1000, 10000), (), (), ()]
potęgi = [(x, x ** 2, x ** 3, x ** 4) for x in lista]

#Zadanie 1.2.
potęgi2 = list(map(lambda x: (x, x ** 2, x ** 3, x ** 4), lista))
print(potęgi2)

#Zadanie 1.3.
lista_dat = ['20241101', '20231223', '20220711', '20230503']

slownik_dat = list(map(lambda x: {'rok': int(x[:4]), 'miesiac': int(x[4:6]), 'dzien': int(x[6:]) }, lista_dat))
print(slownik_dat)

#Zadanie 2.
class Galeria:
    def __init__(self, kraj, miasto, lokale_handlowe):
        self.kraj = kraj
        self.miasto = miasto
        self.lokale_handlowe = lokale_handlowe

g1 = Galeria('PL', 'Gdańsk', [(4, 6), (6, 10), (11, 9)])

print(g1.kraj, g1.miasto, g1.lokale_handlowe[1][1])

#Zadanie 2.2
plik = open('galerie.txt')
dane = plik.readlines()
galerie = []

for x in dane:
    x = x.split()
    kraj = x[0]
    miasto = x[1]
    lokale_handlowe = [(int(d), int(s)) for d, s in zip(x[2::2], x[3::2])]
    galerie.append(Galeria(kraj, miasto, lokale_handlowe))

for g in galerie:
    print(g.kraj, g.miasto, g.lokale_handlowe)