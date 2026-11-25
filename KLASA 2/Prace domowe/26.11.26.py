class Samochod:
    LPojazdow = 0
    def __init__(self, numer, miejsca, marka, bak, spalanie, przebieg, paliwo, wlasciciel, ubezpieczenie, adres):
        self.numer = numer
        self.miejsca = miejsca
        self.marka = marka
        self.bak = bak
        self.spalanie = spalanie
        self.przebieg = przebieg
        self.paliwo = paliwo
        self.wlasciciel = wlasciciel
        self.ubezpieczenie = ubezpieczenie
        self.adres = adres
        Samochod.LPojazdow += 1
    def NadajWlasciciela(self, NWlasciciel, NAdres):
        self.wlasciciel = NWlasciciel
        self.adres = NAdres
    def Przejedz(self, PrzKilometry):
        zuzycie = self.spalanie * PrzKilometry / 100
        if zuzycie <= self.paliwo:
            self.paliwo -= zuzycie
            self.przebieg += PrzKilometry
        else:
            kilometry = self.paliwo * 100 / self.spalanie
            self.przebieg += kilometry
            self.paliwo = 0
    def UzupelnijPaliwo(self, IloscPaliwa):
        self.paliwo += IloscPaliwa
        if self.paliwo > self.bak:
            self.paliwo = self.bak
    def PrzypiszUbezpieczenie(self, NUbezpieczenie):
        self.ubezpieczenie = NUbezpieczenie
    def InformacjePodstawowe(self):
        print("Przebieg:", self.przebieg)
        print("Paliwo:", self.paliwo)
        print("Wlasciciel:", self.wlasciciel)
        print("Ubezpieczenie:", self.ubezpieczenie)
        print("Adres:", self.adres)
    def PokazInfo(self):
        print(self.numer, self.miejsca, self.marka, self.bak,
              self.spalanie, self.przebieg, self.paliwo,
              self.wlasciciel, self.ubezpieczenie, self.adres)

# ZADANIE 3
Auto1 = Samochod("GD 567 KR", 5, "BMW", 60, 7, 100000, 30,
                 "Jan Lotny", "ABC 123", "Choroszcz 1")
Auto2 = Samochod("GD456", 5, "Audi", 50, 6, 201060, 25,
                 "Adam Grzegrzółka", "DEF 456", "Jędrzejów 2")
Auto3 = Samochod("GD789", 7, "Jaecoo", 45, 5, 301308, 20,
                 "Piotr Przyłbicki", "XYZ 789", "Popielnik 3")
print("Liczba pojazdow:", Samochod.LPojazdow)

# ZADANIE 4
Pojazd = Samochod('GD 638 SZ', 6, "Audi", 9.6, 4.8, 20000.0,
                  7.5, "Mariusz Bak", "u04", "Kanarkowa 77")

# 1. Nadanie nowego wlasciciela
print("1. Nadanie wlasciciela:")
Pojazd.NadajWlasciciela("Bronislaw Kubek", "Papugowa 77")
Pojazd.InformacjePodstawowe()

# 2. Przypisanie ubezpieczenia
print("2. Przypisanie ubezpieczenia:")
Pojazd.PrzypiszUbezpieczenie("u05")
Pojazd.InformacjePodstawowe()

# 3. Proba przejechania 10000 km
print("3. Proba przejechania 10000 km:")
Pojazd.Przejedz(10000)
Pojazd.InformacjePodstawowe()

# 4. Proba uzupelnienia paliwa o 1000 litrow
print("4. Uzupelnienie paliwa o 1000 litrow:")
Pojazd.UzupelnijPaliwo(1000)
Pojazd.InformacjePodstawowe()

# 5. Przejechanie trasy 100 km
print("5. Przejechanie 100 km:")
Pojazd.Przejedz(100)
Pojazd.InformacjePodstawowe()


