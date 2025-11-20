import random

nagroda = [20, 25, 30, 50]
kara = [2, 3, 5]

saldo = 0

while True:
    a = int(input('Podaj liczbę od 1 do 9: '))
    b = random.randint(1, 9)

    decyzja = input('Jesteś pewien co do liczby? (tak/nie): ').lower()

    if decyzja == "tak":

        if a == b:
            if random.random() < 0.5: #50% szans
                wygrana = random.choice(nagroda)
                saldo = saldo + wygrana
                print(f"Brawo! Wygrałeś {wygrana} zł!")
            break

        else:
            wylosowana_kara = random.choice(kara)
            saldo = saldo - wylosowana_kara

            if b == a + 1 or b == a - 1:
                print(f"Blisko! Ale nie trafiłeś. Kara: {wylosowana_kara} zł")
            else:
                print(f"Przegrałeś: -{wylosowana_kara} zł")

            print(f"Prawidłowa liczba to {b}")
            continue

    elif decyzja == "nie":
        a = int(input("Podaj nową liczbę (ostatnia szansa!): "))

        if a == b:
            if random.random() < 0.5: #50% szans
                wygrana = random.choice(nagroda)
                saldo = saldo + wygrana
                print(f"Wygrałeś {wygrana} zł!")
            break

        else:
            wylosowana_kara = random.choice(kara)
            saldo = saldo - wylosowana_kara

            if b == a + 1 or b == a - 1:
                print(f"Blisko! Ale nie trafiłeś. Kara: {wylosowana_kara} zł")
            else:
                print(f"Źle! Twoja kara to {wylosowana_kara} zł")

            print(f"Prawidłowa liczba to {b}")
            continue
    else:
        print('Odpowiedzi są tylko dwie: "tak" lub "nie".')
        continue

print("\n       PODSUMOWANIE")
if saldo > 0:
    print(f"Zyskujesz: +{saldo} zł")
elif saldo < 0:
    print(f"tracisz {saldo} zł")
else:
    print("nic nie wygrałeś, ani nie przegrałeś.")