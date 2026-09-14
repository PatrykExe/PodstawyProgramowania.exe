#Rozwiązanie równania kwadratowego

# a = float(input("Podaj liczbę a, która nie jest 0: "))
# b = float(input("Podaj liczbę b: "))
# c = float(input("Podaj liczbę c: "))
#
# delta = b ** 2 - 4 * a * c
# if delta > 0:
#     x1 = (-b - delta ** 0.5) / (2 * a)
#     x2 = (-b + delta ** 0.5) / (2 * a)
#     print(f'x1 = {x1} v x2 = {x2},')
# elif delta == 0:
#     x = (-b) / (2 * a)
#     print('x1 = x2 = {}'.format(x))
# else:
#     print("nie ma rozwiązaniań")

#Zadanie 12

pisemny_polski = int(input('pisemny polski'))
pisemny_obcy = int(input('pisemny obcy'))
pisemny_dodatkowy = int(input('pisemny dodatkowy'))
ustny_polski = int(input('ustny polski'))
ustny_obcy = int(input('ustny obcy'))

if pisemny_polski >= 30 and pisemny_obcy >= 0 and pisemny_dodatkowy >= 30 and ustny_polski >= 30 \
    and ustny_polski >= 30:
    print('brawo, zdałeś to')
elif (pisemny_polski + pisemny_obcy + pisemny_dodatkowy + ustny_obcy + ustny_polski) / 5 >= 30:
    print('zdałeś to z amnezją')
else:
    print('nie zdałeś...')