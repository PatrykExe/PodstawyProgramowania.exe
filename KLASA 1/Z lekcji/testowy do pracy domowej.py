from math import sqrt
a = float(input('Podaj liczbę rzeczywistą, która jest inna niż zero: '))
b = float(input('Podaj liczbę rzeczywistą: '))
c = float(input('Podaj liczbę rzeczywistą: '))

d = b ** 2 - 4 * a * c
if a == 0:
    print('czytać nie umisz?')

elif d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')

elif d == 0:
    x = (-b) / (2 * a)
    print(f'x1 = x2')
    print(f'x = {x}')

else:
    print('Rozwiązanie nie istnieje ty inwestycyjna wtopo twojej linii genetycznej')
