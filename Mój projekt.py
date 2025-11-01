import random

nagroda = ['10zł', '20zł', '15 zł', '25zł', '30zł', '50zł' 'monster ultra white', 'monster ultra paradise']
kara = ['2zł', '3zł', '5zł', '10zł', 'cały maraton sprintem (udokumentowane)']

otrzymane_kary = []  #Lista od otrzymanych kar, które potem zostaną wyświetlone (skrypt od 40 linijki)

while True:  # Jest to pętla, która będzie aktywna do momentu zgadnięcia liczby przez użytkownika
    a = int(input('Podaj liczbę od 1 do 9: '))
    b = random.randrange(1, 10)

    decyzja = input('Jesteś pewien co do liczby? (tak/nie): ').lower()

    if decyzja == "tak":
        if a == b:
            print(f'Brawo, wygrałeś {random.choice(nagroda)}!')
            break  # kończy pętlę
        elif b == (a + 1) or b == (a - 1):
            print(f'No, blisko było, ale jednak żeś nie trafił: {random.choice(kara)}')
            print(f'Liczbą była cyfra {b}')
        else:
            print(f'Przegrałeś, a karą jest {random.choice(kara)}')
            print(f'Liczbą była cyfra {b}')

    elif decyzja == "nie":
        c = int(input('Podaj nową liczbę (następnej szansy nie ma!): '))
        if c == b:
            print(f'Brawo, wygrałeś {random.choice(nagroda)}!')
            break
        elif b == (c + 1) or b == (c - 1):
            print(f'No, blisko było, ale jednak żeś nie trafił: {random.choice(kara)}')
            print(f'Liczbą była cyfra {b}')
        else:
            print(f'Przegrałeś, a karą jest {random.choice(kara)}')
            print(f'Liczbą była cyfra {b}')

    else:
        print('Po Polskiemu nie rozumiesz? Odpowiedzi są dwie: "tak" lub "nie".')

if otrzymane_kary:
    print("\n Twoje kary: ")
    for idx, k in enumerate():
        print(f"{idx}. {k}")  #idx = index; k = poszczególna kara
        print(f"No cóż, otrzymałeś razem {otrzymane_kary} kar(y)")
else:
    print("\nSzacun, pierwsza próba!!")