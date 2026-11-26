class CzlowiekRozumny:
    l_ludzi = 0
    def __init__(self, plec, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.plec = plec
        CzlowiekRozumny.l_ludzi += 1
    def PostarzSie(self, OIle):
        self.wiek += OIle
    def ZmienImie(self, NoweImie):
        imie = NoweImie
    def PokazInfo(self):
        print(self.imie, self.nazwisko, self.wiek, self.plec)

czlowiek1 = CzlowiekRozumny("Mężczyzna", "Włodzimież", 'Grzegrzółka', 57)
print(czlowiek1.imie, czlowiek1.nazwisko, czlowiek1.wiek)
czlowiek1.PokazInfo()
czlowiek1.PostarzSie(10)
czlowiek1.PokazInfo()




#------------------------------------------------
class wektor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    #def __str__(self):
    #    return f'[{self.x}, {self.y}, {self.z}]'
    def __str__(self):
        return str(list(vars(self).values()))
    def __add__(self, other):
        return wektor(self.x + other.x, self.y + other.y, self.z + other.z)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
w1 = wektor(2, 4, 7)
w2 = wektor(-3, 9, 1)
w3 = w1 + w2
print(w3)