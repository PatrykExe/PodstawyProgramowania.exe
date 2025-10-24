from math import sqrt

a = float(input('Podaj liczbę a, która nie jest równa 0: '))
b = float(input('Podaj liczbę b: '))
c = float(input('Podaj liczbę c: '))
d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f'x1 = {x2}, x2 = {x2}')
elif d == 0:
    x = (-b) / (2 * a)
    print(f'x1 == x2 = {x}')
else:
    print('nie ma rozwiązania')
