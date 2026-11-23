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