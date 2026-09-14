#1. wprowadzanie danych przez użytkownika do programu
#  1. utworzenie zmiennej
#  2. na ekranie pojawia się komunikat z inputa
#  3. program się zatrzymuje i czeka na podanie danych i zatwierdzenie go ENTER'em
#  4. po wpisaniu i zatwierdzeniu ENTER'em to co wpiszemy trafia jako string do zmiennej
#  5. i program wykonuje się dalej

imie = input('Podaj swoje imie: ')

liczba = int(input('Podaj liczbę'))
print(type(liczba))

liczba_z_przecinkiem = float(input('Podaj liczbę z przecinkiem'))
print(type(liczba_z_przecinkiem))

cos = list(input('podaj coś: '))
print(cos)
