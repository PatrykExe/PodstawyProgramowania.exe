class Samochod:
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
        print("Właściciel:", self.wlasciciel)
        print("Ubezpieczenie:", self.ubezpieczenie)
        print("Adres:", self.adres)
    def PokazInfo(self):
        print(self.numer, self.miejsca, self.marka, self.bak,
              self.spalanie, self.przebieg, self.paliwo,
              self.wlasciciel, self.ubezpieczenie, self.adres)

Pojazd = Samochod('GD 6726 KI', 5, 'Nissan', 60, 6, 65720, 50,"Włodzimież Grzegrzółka", 'GAU781A37','Zamkowa 46, Choroszcz')

Pojazd.PokazInfo()
