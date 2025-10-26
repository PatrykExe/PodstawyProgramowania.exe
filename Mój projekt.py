import random

a = int(input('Podaj liczbę od 1 do 9: '))
b = int(random.randrange(1, 10))

nagroda = ['rozgrzeszenie', 'spotify premium na rok']
kara = ['1v1 z niedzwiedziem', 'cały maraton sprintem (udokumentowane)', 'multiplą do okoła świata']

decyzja = input('Jesteś pewien co do liczby? (tak/nie): ')

if decyzja == "tak":
    if a == b:
        print(f'Brawo, wygrałeś {random.choice(nagroda)}')

    elif b == (a + 1):
        print(f'No, Blisko było ale jednak przewaliłeś, więc {random.choice(kara)}')
        print(f'Liczbą była cyfra {b}')

    elif b == (a - 1):
        print(f'No, Blisko było ale jednak przewaliłeś, więc {random.choice(kara)}')
        print(f'Liczbą była cyfra {b}')

    else:
        print(f'przegrałeś, a karą jest {random.choice(kara)}')
        print(f'Liczbą była cyfra {b}')

elif decyzja == "nie":
    c = int(input('Podaj liczbę, ale następnej szansy nie ma: '))

    if c == b:
        print(f'Brawo, wygrałeś {random.choice(nagroda)}')

    elif b == (c + 1):
        print(f'No, Blisko było ale jednak przewaliłeś, więc {random.choice(kara)}')
        print(f'Liczbą była cyfra {b}')

    elif b == (c - 1):
        print(f'No, Blisko było ale jednak przewaliłeś, więc {random.choice(kara)}')
        print(f'Liczbą była cyfra {b}')

    else:
        print(f'przegrałeś, a karą jest {random.choice(kara)}')
        print(f'Liczbą była cyfra {b}')

