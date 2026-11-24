class Samochod:
    def __init__(self, numer, miejsca, marka, bak, spalanie, przebieg, paliwo, wlasciciel, ubezpieczenie, adres):
        self.numer = numer #numer tablic rejestracyjnych
        self.miejsca = miejsca #ilość siedzeń
        self.marka = marka
        self.bak = bak #Pojemność baku
        self.spalanie = spalanie
        self.przebieg = przebieg
        self.paliwo = paliwo #Aktualny stan baku (ilość paliwa)
        self.wlasciciel = wlasciciel
        self.ubezpieczenie = ubezpieczenie #Numer ubezpieczenia
        self.adres = adres #Adres właściciela
    def PokazInfo(self):
        print(self.numer, self.miejsca, self.marka, self.bak, self.spalanie, self.przebieg, self.paliwo, self.wlasciciel, self.ubezpieczenie, self.adres)

Pojazd = Samochod('GD 6726 KI', 5, 'Nissan', 60, 6, 65720, 50, "Włodzimież Grzegrzółka", 'GAU781A37', 'Zamkowa 46, Choroszcz')
Pojazd.PokazInfo()