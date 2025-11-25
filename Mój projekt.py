import random
print('WAŻNE!!! Waluta nie jest powiązana z prawdziwą walutą')
nagroda = [20, 25, 30, 50]
kara = [2, 3, 5]

saldo = 50
print("Twoje saldo to 50")
print("ryzyko niskie: Kwota wejściowa: 5zł")
print("ryzyko średnie: Kwota wejściowa: 10zł")
print("ryzyko wysokie: Kwota wejściowa: 15zł")

liczba_rund = int(input("Liczba rund: "))
ryzyko = input('Podaj poziom ryzyka (niskie, średnie, wysokie): ')
Wstep = input('Jeżeli wchodzisz, wpisz "tak", a jeżeli nie, wpisz "nie": ')

if ryzyko == "niskie":
    if Wstep == 'nie':
        print("Nie dołączyłeś do gry")

    elif Wstep == "tak":
        saldo = saldo -5
        while True:
             a = int(input('Podaj liczbę od 1 do 9: '))
             b = random.randint(1, 9)

             decyzja = input('Jesteś pewien co do liczby? (tak/nie): ').lower()

             if decyzja == "tak":

                if a == b:
                    if random.random() < 0.5: #50% szans
                        wygrana = random.choice(nagroda)
                        saldo = saldo + wygrana
                        print(f"Brawo, zgadłeś za pierwszym razem! Wygrałeś {wygrana} zł!")
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
                        print(f"Brawo, zgadłeś za pierwszym razem! Wygrałeś {wygrana} zł!")
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
    else:
        print('Odpowiedzi są tylko dwie: "tak" lub "nie".')

elif ryzyko == "średnie":
    saldo = saldo - 10

    if Wstep == 'nie':
        print("Nie dołączyłeś do gry")

    elif Wstep == "tak":
        saldo = saldo -5
        while True:
            a = int(input('Podaj liczbę od 1 do 9: '))
            b = random.randint(1, 9)

            decyzja = input('Jesteś pewien co do liczby? (tak/nie): ').lower()

            if decyzja == "tak":

                if a == b:
                    if random.random() < 0.5: #50% szans
                        wygrana = random.choice(nagroda)
                        saldo = saldo + wygrana
                        print(f"Brawo, zgadłeś za pierwszym razem! Wygrałeś {wygrana} zł!")
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
                        print(f"Brawo, zgadłeś za pierwszym razem! Wygrałeś {wygrana} zł!")
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
    else:
        print('Odpowiedzi są tylko dwie: "tak" lub "nie".')


elif ryzyko == "wysokie":
    saldo = saldo - 15

    if Wstep == 'nie':
        print("Nie dołączyłeś do gry")

    elif Wstep == "tak":
        saldo = saldo -5
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
                        print(f"Brawo! Wygrałeś {wygrana} zł!")
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
    else:
        print('Odpowiedzi są tylko dwie: "tak" lub "nie".')

else:
    print('Odpowiedzi są tylko dwie: "tak" lub "nie".')

for r in range(1, liczba_rund + 1):
    if saldo <= 0:
        print("\nSaldo wynosi 0 — koniec gry!")
        break

    print(f"\n===== RUNDA {r} =====")
    ryzyko = input("Wybierz poziom ryzyka (niskie/średnie/wysokie): ").lower()


print("\n       PODSUMOWANIE")
if saldo > 0:
    print(f"Zyskujesz: +{saldo} zł")
elif saldo < 0:
    print(f"tracisz: {saldo} zł")
elif saldo == 0:
    print("nic nie wygrałeś, ani nie przegrałeś.")
