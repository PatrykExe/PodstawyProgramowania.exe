#ZADANIE 13:

test_kompetencji_jezykowych = int(input('Podaj swój wynik z testu kompetencji. Wynik podaj w procentach: '))
ocena_ze_swiadectwa = int(input('Podaj swoją ocenę ze świadectwa: '))

if test_kompetencji_jezykowych > 90 or ocena_ze_swiadectwa >= 5:
    print('Dostałeś się do grupy zaawansowanej.')
elif not(test_kompetencji_jezykowych > 90 or ocena_ze_swiadectwa >= 5):
    print('Dostałeś się do grupy podstawowej')



#ZADANIE 14:
from math import sqrt
a = float(input('Podaj liczbę rzeczywistą, która nie jest równa 0: '))
b = float(input('Podaj następną liczbę rzeczywistą: '))
c = float(input('Podaj następną liczbę rzeczywistą: '))

d = b ** 2 - 4 * a * c
# d == delta (mój skrót myślowy)

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
    #rozbiłem na dwa print(), aby było czytelniejsze
elif d == 0:
    x = (-b) / (2 * a)
    print(f'x = {x}')
else:
    print('nie ma rozwiązań')


